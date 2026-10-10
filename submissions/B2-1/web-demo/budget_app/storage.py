from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Iterable, Iterator

from .errors import BudgetError, DataError
from .models import Budget, RecurringRule, Transaction

DEFAULT_CATEGORIES = (
    "food", "transport", "rent", "salary", "shopping", "medical", "education", "other",
)


class JsonlBudgetStore:
    """JSONL persistence with streaming reads and atomic whole-file replacement."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory.expanduser().resolve()
        self.transactions_path = self.directory / "transactions.jsonl"
        self.categories_path = self.directory / "categories.jsonl"
        self.budgets_path = self.directory / "budgets.jsonl"
        self.recurring_path = self.directory / "recurring.jsonl"

    def ensure_files(self) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        for path in (self.transactions_path, self.budgets_path, self.recurring_path):
            path.touch(exist_ok=True)
        if not self.categories_path.exists():
            self._atomic_write(self.categories_path, ({"name": name} for name in DEFAULT_CATEGORIES))

    def _iter_rows(self, path: Path) -> Iterator[dict[str, Any]]:
        try:
            with path.open("r", encoding="utf-8") as source:
                for line_number, line in enumerate(source, start=1):
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError as error:
                        raise DataError(
                            f"{path.name} {line_number}번째 줄의 JSON 데이터가 손상되었습니다.",
                            "해당 줄을 복구하거나 백업 파일에서 복원하세요.",
                        ) from error
                    if not isinstance(row, dict):
                        raise DataError(
                            f"{path.name} {line_number}번째 줄이 객체 형식이 아닙니다.",
                            "JSONL 파일의 각 줄을 JSON 객체로 저장하세요.",
                        )
                    yield row
        except (OSError, UnicodeError) as error:
            raise BudgetError(f"{path} 파일을 읽을 수 없습니다.", "저장 경로와 파일 권한을 확인하세요.") from error

    def iter_transactions(self) -> Iterator[Transaction]:
        for line_number, row in enumerate(self._iter_rows(self.transactions_path), start=1):
            try:
                yield Transaction.from_dict(row)
            except (KeyError, TypeError, ValueError, BudgetError) as error:
                raise DataError(
                    f"transactions.jsonl {line_number}번째 줄의 거래 데이터가 올바르지 않습니다.",
                    "잘못된 거래 줄을 수정하거나 백업에서 복원하세요.",
                ) from error

    def iter_categories(self) -> Iterator[str]:
        for row in self._iter_rows(self.categories_path):
            name = row.get("name")
            if isinstance(name, str) and name.strip():
                yield name.strip()

    def iter_budgets(self) -> Iterator[Budget]:
        for row in self._iter_rows(self.budgets_path):
            try:
                yield Budget(month=str(row["month"]), amount=int(row["amount"]))
            except (KeyError, TypeError, ValueError, BudgetError) as error:
                raise DataError("budgets.jsonl에 올바르지 않은 예산 데이터가 있습니다.", "해당 줄을 수정하거나 백업에서 복원하세요.") from error

    def iter_recurring(self) -> Iterator[RecurringRule]:
        for row in self._iter_rows(self.recurring_path):
            try:
                yield RecurringRule.from_dict(row)
            except (KeyError, TypeError, ValueError, BudgetError) as error:
                raise DataError("recurring.jsonl에 올바르지 않은 반복 내역 데이터가 있습니다.", "해당 줄을 수정하거나 백업에서 복원하세요.") from error

    def insert_transaction(self, transaction: Transaction) -> None:
        """Merge one transaction into the date-descending JSONL stream."""
        self._atomic_write(
            self.transactions_path,
            self._merged_transactions(transaction),
        )

    def _merged_transactions(self, transaction: Transaction) -> Iterator[dict[str, Any]]:
        inserted = False
        for current in self.iter_transactions():
            if current.id == transaction.id:
                raise BudgetError("이미 사용 중인 거래 id입니다.", "다시 시도하면 새 id가 생성됩니다.")
            if not inserted and transaction.sort_key >= current.sort_key:
                yield transaction.to_dict()
                inserted = True
            yield current.to_dict()
        if not inserted:
            yield transaction.to_dict()

    def replace_transactions(self, transactions: Iterable[Transaction]) -> None:
        ordered = sorted(transactions, key=lambda item: item.sort_key, reverse=True)
        self._atomic_write(self.transactions_path, (item.to_dict() for item in ordered))

    def write_categories(self, categories: Iterable[str]) -> None:
        self._atomic_write(self.categories_path, ({"name": name} for name in sorted(set(categories), key=str.casefold)))

    def write_budgets(self, budgets: Iterable[Budget]) -> None:
        ordered = sorted(budgets, key=lambda item: item.month)
        self._atomic_write(self.budgets_path, (item.to_dict() for item in ordered))

    def write_recurring(self, rules: Iterable[RecurringRule]) -> None:
        ordered = sorted(rules, key=lambda item: item.id)
        self._atomic_write(self.recurring_path, (item.to_dict() for item in ordered))

    def _atomic_write(self, path: Path, rows: Iterable[dict[str, Any]]) -> None:
        temporary: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", dir=self.directory,
                prefix=f".{path.name}.", suffix=".tmp", delete=False,
            ) as target:
                temporary = Path(target.name)
                for row in rows:
                    target.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
                    target.write("\n")
                target.flush()
                os.fsync(target.fileno())
            os.replace(temporary, path)
            temporary = None
        except OSError as error:
            raise BudgetError(f"{path.name} 파일을 저장하지 못했습니다.", "저장 폴더의 경로와 쓰기 권한을 확인하세요.") from error
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
