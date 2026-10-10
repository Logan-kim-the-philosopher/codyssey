from __future__ import annotations

import calendar
import csv
import os
import shutil
import tempfile
from dataclasses import replace
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterator

from .decorators import logged_and_timed
from .errors import BudgetError
from .models import Budget, RecurringRule, Transaction, new_id, parse_date, parse_tags, validate_month
from .storage import JsonlBudgetStore

CSV_COLUMNS = ("date", "type", "category", "amount", "memo", "tags")


class BudgetService:
    def __init__(self, store: JsonlBudgetStore) -> None:
        self.store = store

    def categories(self) -> list[str]:
        return sorted(set(self.store.iter_categories()), key=str.casefold)

    def _require_category(self, category: str) -> None:
        if category not in set(self.store.iter_categories()):
            raise BudgetError(
                f"등록되지 않은 카테고리입니다: {category}",
                "category list로 확인하거나 category add로 먼저 등록하세요.",
            )

    @logged_and_timed
    def add_transaction(
        self,
        transaction_type: str,
        transaction_date: str,
        category: str,
        amount: int,
        memo: str = "",
        tags: str | tuple[str, ...] = "",
    ) -> Transaction:
        self._require_category(category)
        transaction = Transaction(
            id=new_id("TX"), type=transaction_type, date=transaction_date,
            amount=amount, category=category, memo=memo, tags=parse_tags(tags),
        )
        self.store.insert_transaction(transaction)
        return transaction

    def iter_transactions(self) -> Iterator[Transaction]:
        yield from self.store.iter_transactions()

    def search(
        self,
        from_date: str | None = None,
        to_date: str | None = None,
        category: str | None = None,
        transaction_type: str | None = None,
        query: str | None = None,
        tag: str | None = None,
    ) -> Iterator[Transaction]:
        if from_date:
            parse_date(from_date)
        if to_date:
            parse_date(to_date)
        if from_date and to_date and from_date > to_date:
            raise BudgetError("검색 시작일이 종료일보다 늦습니다.", "--from 날짜를 --to 날짜보다 앞서게 입력하세요.")
        if transaction_type and transaction_type not in {"income", "expense"}:
            raise BudgetError("타입은 income 또는 expense여야 합니다.", "--type income 또는 --type expense를 사용하세요.")
        folded_query = query.casefold() if query else None
        for transaction in self.store.iter_transactions():
            if from_date and transaction.date < from_date:
                continue
            if to_date and transaction.date > to_date:
                continue
            if category and transaction.category != category:
                continue
            if transaction_type and transaction.type != transaction_type:
                continue
            if folded_query and folded_query not in transaction.memo.casefold():
                continue
            if tag and tag not in transaction.tags:
                continue
            yield transaction

    def update_transaction(
        self,
        transaction_id: str,
        *,
        transaction_date: str | None = None,
        transaction_type: str | None = None,
        category: str | None = None,
        amount: int | None = None,
        memo: str | None = None,
        tags: str | None = None,
    ) -> Transaction:
        changes = {
            key: value for key, value in {
                "transaction_date": transaction_date,
                "transaction_type": transaction_type,
                "category": category,
                "amount": amount,
                "memo": memo,
                "tags": tags,
            }.items() if value is not None
        }
        if not changes:
            raise BudgetError("수정할 필드를 하나 이상 지정하세요.", "update --help에서 수정 옵션을 확인하세요.")
        transactions = list(self.store.iter_transactions())
        current = next((item for item in transactions if item.id == transaction_id), None)
        if current is None:
            raise BudgetError(f"거래 id를 찾을 수 없습니다: {transaction_id}", "list로 거래 id를 확인하세요.")
        if category is not None:
            self._require_category(category)
        updated = replace(
            current,
            date=transaction_date if transaction_date is not None else current.date,
            type=transaction_type if transaction_type is not None else current.type,
            category=category if category is not None else current.category,
            amount=amount if amount is not None else current.amount,
            memo=memo if memo is not None else current.memo,
            tags=parse_tags(tags) if tags is not None else current.tags,
        )
        self.store.replace_transactions(updated if item.id == current.id else item for item in transactions)
        return updated

    def delete_transaction(self, transaction_id: str) -> None:
        transactions = list(self.store.iter_transactions())
        remaining = [item for item in transactions if item.id != transaction_id]
        if len(remaining) == len(transactions):
            raise BudgetError(f"거래 id를 찾을 수 없습니다: {transaction_id}", "list로 거래 id를 확인하세요.")
        self.store.replace_transactions(remaining)

    def summary(self, month: str) -> dict[str, Any]:
        validate_month(month)
        income = 0
        expense = 0
        category_totals: dict[str, int] = {}
        count = 0
        for transaction in self.store.iter_transactions():
            if transaction.date[:7] != month:
                continue
            count += 1
            if transaction.type == "income":
                income += transaction.amount
            else:
                expense += transaction.amount
                category_totals[transaction.category] = category_totals.get(transaction.category, 0) + transaction.amount
        budget = next((item for item in self.store.iter_budgets() if item.month == month), None)
        return {
            "month": month,
            "count": count,
            "income": income,
            "expense": expense,
            "balance": income - expense,
            "category_totals": sorted(category_totals.items(), key=lambda pair: (-pair[1], pair[0].casefold())),
            "budget": budget,
        }

    def set_budget(self, month: str, amount: int) -> Budget:
        budget = Budget(month=month, amount=amount)
        budgets = [item for item in self.store.iter_budgets() if item.month != month]
        budgets.append(budget)
        self.store.write_budgets(budgets)
        return budget

    def remove_category(self, category: str) -> None:
        categories = self.categories()
        if category not in categories:
            raise BudgetError(f"카테고리를 찾을 수 없습니다: {category}", "category list로 등록된 카테고리를 확인하세요.")
        if any(item.category == category for item in self.store.iter_transactions()):
            raise BudgetError(f"거래에서 사용 중인 카테고리는 삭제할 수 없습니다: {category}", "해당 거래의 카테고리를 먼저 변경하세요.")
        if any(item.category == category for item in self.store.iter_recurring()):
            raise BudgetError(f"반복 내역에서 사용 중인 카테고리는 삭제할 수 없습니다: {category}", "반복 규칙을 먼저 제거하거나 다른 카테고리로 변경하세요.")
        self.store.write_categories(name for name in categories if name != category)

    @logged_and_timed
    def import_csv(self, source: Path) -> tuple[int, int, list[str]]:
        categories = set(self.store.iter_categories())
        imported = 0
        skipped = 0
        errors: list[str] = []
        try:
            with source.open("r", encoding="utf-8-sig", newline="") as csv_file:
                reader = csv.DictReader(csv_file)
                headers = set(reader.fieldnames or [])
                missing = {"date", "type", "category", "amount"} - headers
                if missing:
                    raise BudgetError(
                        f"CSV 필수 열이 없습니다: {', '.join(sorted(missing))}",
                        "date,type,category,amount 헤더를 포함해 UTF-8 CSV로 저장하세요.",
                    )
                for line_number, row in enumerate(reader, start=2):
                    try:
                        category = (row.get("category") or "").strip()
                        if category not in categories:
                            raise BudgetError(f"등록되지 않은 카테고리: {category}", "먼저 category add로 등록하세요.")
                        raw_amount = (row.get("amount") or "").strip()
                        if not raw_amount.isdecimal():
                            raise BudgetError("금액은 양수 정수여야 합니다.", "amount 열에 0보다 큰 정수를 입력하세요.")
                        transaction = Transaction(
                            id=new_id("TX"),
                            type=(row.get("type") or "").strip(),
                            date=(row.get("date") or "").strip(),
                            amount=int(raw_amount),
                            category=category,
                            memo=(row.get("memo") or "").strip(),
                            tags=parse_tags(row.get("tags") or ""),
                        )
                        self.store.insert_transaction(transaction)
                        imported += 1
                    except BudgetError as error:
                        skipped += 1
                        errors.append(f"{line_number}행: {error}")
        except (OSError, UnicodeError, csv.Error) as error:
            raise BudgetError(f"CSV 파일을 읽지 못했습니다: {source}", "파일 경로와 UTF-8 인코딩을 확인하세요.") from error
        return imported, skipped, errors

    @logged_and_timed
    def export_csv(
        self,
        destination: Path,
        *,
        month: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> int:
        if month:
            validate_month(month)
        if from_date:
            parse_date(from_date)
        if to_date:
            parse_date(to_date)
        if not month and not (from_date and to_date):
            raise BudgetError("내보내기 조건이 필요합니다.", "--month 또는 --from과 --to를 함께 지정하세요.")
        if from_date and to_date and from_date > to_date:
            raise BudgetError("시작일이 종료일보다 늦습니다.", "--from 날짜를 --to 날짜보다 앞서게 입력하세요.")
        destination = destination.expanduser().resolve()
        protected_paths = {
            self.store.transactions_path.resolve(),
            self.store.categories_path.resolve(),
            self.store.budgets_path.resolve(),
            self.store.recurring_path.resolve(),
        }
        if destination in protected_paths:
            raise BudgetError("내보내기 경로가 내부 저장 파일과 겹칩니다.", "데이터 폴더 밖의 CSV 경로를 지정하세요.")
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary: Path | None = None
        count = 0
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", newline="", dir=destination.parent,
                prefix=f".{destination.name}.", suffix=".tmp", delete=False,
            ) as output:
                temporary = Path(output.name)
                writer = csv.DictWriter(output, fieldnames=CSV_COLUMNS)
                writer.writeheader()
                for transaction in self.store.iter_transactions():
                    if month and transaction.date[:7] != month:
                        continue
                    if from_date and transaction.date < from_date:
                        continue
                    if to_date and transaction.date > to_date:
                        continue
                    writer.writerow({
                        "date": transaction.date,
                        "type": transaction.type,
                        "category": transaction.category,
                        "amount": transaction.amount,
                        "memo": transaction.memo,
                        "tags": ",".join(transaction.tags),
                    })
                    count += 1
                output.flush()
                os.fsync(output.fileno())
            os.replace(temporary, destination)
            temporary = None
        except OSError as error:
            raise BudgetError(f"CSV 파일을 저장하지 못했습니다: {destination}", "출력 폴더의 경로와 쓰기 권한을 확인하세요.") from error
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return count

    def add_recurring(
        self,
        transaction_type: str,
        day: int,
        amount: int,
        category: str,
        memo: str = "",
        tags: str = "",
    ) -> RecurringRule:
        self._require_category(category)
        rule = RecurringRule(
            id=new_id("RR"), type=transaction_type, day=day, amount=amount,
            category=category, memo=memo, tags=parse_tags(tags),
        )
        self.store.write_recurring([*self.store.iter_recurring(), rule])
        return rule

    def generate_recurring(self, month: str) -> int:
        validate_month(month)
        already_created = {
            (item.recurring_rule_id, item.recurring_month)
            for item in self.store.iter_transactions()
            if item.recurring_rule_id is not None
        }
        last_day = calendar.monthrange(int(month[:4]), int(month[5:7]))[1]
        created = 0
        for rule in self.store.iter_recurring():
            if (rule.id, month) in already_created:
                continue
            transaction = Transaction(
                id=new_id("TX"), type=rule.type,
                date=date(int(month[:4]), int(month[5:7]), min(rule.day, last_day)).isoformat(),
                amount=rule.amount, category=rule.category, memo=rule.memo,
                tags=rule.tags, recurring_rule_id=rule.id, recurring_month=month,
            )
            self.store.insert_transaction(transaction)
            created += 1
        return created

    def backup(self) -> Path:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        destination = self.store.directory / "backups" / f"backup-{stamp}"
        try:
            destination.mkdir(parents=True, exist_ok=False)
            for source in (
                self.store.transactions_path,
                self.store.categories_path,
                self.store.budgets_path,
                self.store.recurring_path,
            ):
                shutil.copy2(source, destination / source.name)
        except OSError as error:
            raise BudgetError("백업 파일을 생성하지 못했습니다.", "저장 폴더의 여유 공간과 쓰기 권한을 확인하세요.") from error
        return destination
