from __future__ import annotations

import argparse
import logging
import sys
from functools import wraps
from pathlib import Path
from typing import Any, Callable, TypeVar

from .errors import BudgetError
from .models import Transaction
from .service import BudgetService
from .storage import JsonlBudgetStore

F = TypeVar("F", bound=Callable[..., int])


class FriendlyArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["add_help"] = False
        super().__init__(*args, **kwargs)
        self.add_argument("--help", action="help", help="사용 방법 표시")

    def error(self, message: str) -> None:
        raise BudgetError(f"명령 인자가 올바르지 않습니다: {message}", "해당 명령에 --help를 붙여 사용법을 확인하세요.")


def friendly_errors(function: F) -> F:
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> int:
        try:
            return function(*args, **kwargs)
        except BudgetError as error:
            print(f"[오류] {error}", file=sys.stderr)
            print(f"[힌트] {error.hint}", file=sys.stderr)
            return 2
        except OSError as error:
            print(f"[오류] 파일 작업을 완료하지 못했습니다: {error}", file=sys.stderr)
            print("[힌트] 파일 경로와 권한을 확인하세요.", file=sys.stderr)
            return 2
        except EOFError as error:
            print("[오류] 입력이 중단되었습니다.", file=sys.stderr)
            print("[힌트] add 명령의 입력을 끝까지 완료하세요.", file=sys.stderr)
            return 2

    return wrapper  # type: ignore[return-value]


def _add_data_dir(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--data-dir", default=argparse.SUPPRESS, help="데이터 폴더 (기본값: ./data)")


def build_parser() -> FriendlyArgumentParser:
    parser = FriendlyArgumentParser(
        prog="python -m budget_app",
        description="JSONL 파일 기반 콘솔 용돈 기입장",
    )
    parser.add_argument("--data-dir", default="./data", help="데이터 폴더 (기본값: ./data)")
    commands = parser.add_subparsers(dest="command", required=True, parser_class=FriendlyArgumentParser)

    add = commands.add_parser("add", help="대화형으로 거래 추가")
    _add_data_dir(add)

    listing = commands.add_parser("list", help="최신 거래 목록")
    _add_data_dir(listing)
    listing.add_argument("--limit", type=int, default=20, help="표시할 최대 거래 수 (기본값: 20)")

    search = commands.add_parser("search", help="조건에 맞는 거래 검색")
    _add_data_dir(search)
    search.add_argument("--from", dest="from_date", help="시작일 YYYY-MM-DD")
    search.add_argument("--to", dest="to_date", help="종료일 YYYY-MM-DD")
    search.add_argument("--category", help="카테고리")
    search.add_argument("--type", dest="transaction_type", choices=("income", "expense"), help="income 또는 expense")
    search.add_argument("--q", help="메모 키워드")
    search.add_argument("--tag", help="태그")
    search.add_argument("--limit", type=int, default=100, help="표시할 최대 거래 수 (기본값: 100)")

    summary = commands.add_parser("summary", help="월별 수입·지출 요약")
    _add_data_dir(summary)
    summary.add_argument("--month", required=True, help="요약할 월 YYYY-MM")
    summary.add_argument("--top", type=int, default=5, help="지출 카테고리 표시 개수 (기본값: 5)")

    budget = commands.add_parser("budget", help="월 예산 설정과 조회")
    budget_commands = budget.add_subparsers(dest="budget_command", required=True, parser_class=FriendlyArgumentParser)
    budget_set = budget_commands.add_parser("set", help="월 예산 설정")
    _add_data_dir(budget_set)
    budget_set.add_argument("--month", required=True, help="예산 월 YYYY-MM")
    budget_set.add_argument("--amount", required=True, type=int, help="양수 정수 금액")
    budget_show = budget_commands.add_parser("show", help="월 예산 조회")
    _add_data_dir(budget_show)
    budget_show.add_argument("--month", required=True, help="조회할 월 YYYY-MM")
    budget_list = budget_commands.add_parser("list", help="전체 예산 조회")
    _add_data_dir(budget_list)

    category = commands.add_parser("category", help="카테고리 관리")
    category_commands = category.add_subparsers(dest="category_command", required=True, parser_class=FriendlyArgumentParser)
    for name, help_text in (("add", "카테고리 추가"), ("list", "카테고리 목록"), ("remove", "카테고리 삭제")):
        subcommand = category_commands.add_parser(name, help=help_text)
        _add_data_dir(subcommand)
        if name in {"add", "remove"}:
            subcommand.add_argument("--name", help="카테고리명")

    update = commands.add_parser("update", help="옵션 방식으로 거래 수정")
    _add_data_dir(update)
    update.add_argument("--id", required=True, help="거래 id")
    update.add_argument("--date", dest="transaction_date", help="날짜 YYYY-MM-DD")
    update.add_argument("--type", dest="transaction_type", choices=("income", "expense"), help="income 또는 expense")
    update.add_argument("--category", help="카테고리")
    update.add_argument("--amount", type=int, help="양수 정수 금액")
    update.add_argument("--memo", help="메모 (빈 문자열이면 비움)")
    update.add_argument("--tags", help="쉼표로 구분한 태그")

    delete = commands.add_parser("delete", help="거래 삭제")
    _add_data_dir(delete)
    delete.add_argument("--id", required=True, help="삭제할 거래 id")

    import_parser = commands.add_parser("import", help="CSV 거래 가져오기")
    _add_data_dir(import_parser)
    import_parser.add_argument("--from", dest="source", required=True, help="가져올 CSV 경로")

    export = commands.add_parser("export", help="조건에 맞는 거래를 CSV로 내보내기")
    _add_data_dir(export)
    export.add_argument("--out", required=True, help="출력 CSV 경로")
    export.add_argument("--month", help="월 YYYY-MM")
    export.add_argument("--from", dest="from_date", help="시작일 YYYY-MM-DD")
    export.add_argument("--to", dest="to_date", help="종료일 YYYY-MM-DD")

    backup = commands.add_parser("backup", help="저장 데이터를 타임스탬프 백업")
    _add_data_dir(backup)

    recurring = commands.add_parser("recurring", help="반복 거래 규칙 관리")
    recurring_commands = recurring.add_subparsers(dest="recurring_command", required=True, parser_class=FriendlyArgumentParser)
    recurring_add = recurring_commands.add_parser("add", help="반복 규칙 추가")
    _add_data_dir(recurring_add)
    recurring_add.add_argument("--type", dest="transaction_type", required=True, choices=("income", "expense"))
    recurring_add.add_argument("--day", required=True, type=int, help="매월 실행일 1~31")
    recurring_add.add_argument("--amount", required=True, type=int, help="양수 정수 금액")
    recurring_add.add_argument("--category", required=True, help="등록된 카테고리")
    recurring_add.add_argument("--memo", default="", help="메모")
    recurring_add.add_argument("--tags", default="", help="쉼표로 구분한 태그")
    recurring_list = recurring_commands.add_parser("list", help="반복 규칙 목록")
    _add_data_dir(recurring_list)
    recurring_generate = recurring_commands.add_parser("generate", help="특정 월의 반복 거래 생성")
    _add_data_dir(recurring_generate)
    recurring_generate.add_argument("--month", required=True, help="생성할 월 YYYY-MM")

    return parser


def _prompt(label: str, optional: bool = False) -> str:
    suffix = " (선택)" if optional else ""
    return input(f"{label}{suffix}: ").strip()


def _positive_limit(value: int, option: str) -> None:
    if value <= 0:
        raise BudgetError(f"{option}은 1 이상의 정수여야 합니다.", f"{option} 값을 1 이상으로 입력하세요.")


def _table(headers: list[str], rows: list[list[str]]) -> None:
    if not rows:
        print("데이터 없음")
        return
    widths = [max(len(headers[index]), *(len(row[index]) for row in rows)) for index in range(len(headers))]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def _transaction_row(item: Transaction) -> list[str]:
    return [item.id, item.date, item.type, item.category, f"{item.amount:,}", item.memo, ",".join(item.tags)]


def _print_transactions(items: list[Transaction]) -> None:
    _table(["ID", "DATE", "TYPE", "CATEGORY", "AMOUNT", "MEMO", "TAGS"], [_transaction_row(item) for item in items])


def _category_name(args: argparse.Namespace) -> str:
    name = args.name.strip() if args.name is not None else _prompt("카테고리명")
    if not name:
        raise BudgetError("카테고리명을 입력하세요.", "예: food")
    return name


def _execute(args: argparse.Namespace, service: BudgetService, store: JsonlBudgetStore) -> int:
    if args.command == "add":
        transaction_date = _prompt("날짜(YYYY-MM-DD)")
        transaction_type = _prompt("타입(income/expense)")
        category_name = _prompt("카테고리")
        amount_text = _prompt("금액(양수 정수)")
        if not amount_text.isdecimal():
            raise BudgetError("금액은 양수 정수여야 합니다.", "예: 15000")
        memo = _prompt("메모", optional=True)
        tags = _prompt("태그(쉼표로 구분)", optional=True)
        transaction = service.add_transaction(transaction_type, transaction_date, category_name, int(amount_text), memo, tags)
        print(f"[저장 완료] id={transaction.id}")
    elif args.command == "list":
        _positive_limit(args.limit, "--limit")
        from itertools import islice
        _print_transactions(list(islice(service.iter_transactions(), args.limit)))
    elif args.command == "search":
        _positive_limit(args.limit, "--limit")
        from itertools import islice
        matches = service.search(args.from_date, args.to_date, args.category, args.transaction_type, args.q, args.tag)
        _print_transactions(list(islice(matches, args.limit)))
    elif args.command == "summary":
        _positive_limit(args.top, "--top")
        result = service.summary(args.month)
        if result["count"] == 0:
            print(f"데이터 없음 ({result['month']})")
        print(f"총 수입: {result['income']:,}원")
        print(f"총 지출: {result['expense']:,}원")
        print(f"잔액: {result['balance']:,}원")
        budget = result["budget"]
        if budget:
            ratio = result["expense"] / budget.amount * 100
            print(f"예산: {budget.amount:,}원 (사용률 {ratio:.1f}%)")
            if result["expense"] > budget.amount:
                print("[경고] 월 예산을 초과했습니다.")
        print(f"\n지출 TOP {args.top}")
        for position, (category_name, amount) in enumerate(result["category_totals"][:args.top], start=1):
            print(f"{position}) {category_name} {amount:,}원")
        if not result["category_totals"]:
            print("지출 내역 없음")
    elif args.command == "budget":
        if args.budget_command == "set":
            budget = service.set_budget(args.month, args.amount)
            print(f"[저장 완료] {budget.month} 예산 {budget.amount:,}원")
        elif args.budget_command == "show":
            budget = next((item for item in store.iter_budgets() if item.month == args.month), None)
            if budget is None:
                raise BudgetError(f"{args.month} 예산이 없습니다.", "budget set으로 월 예산을 먼저 등록하세요.")
            print(f"{budget.month} 예산: {budget.amount:,}원")
        else:
            rows = [[item.month, f"{item.amount:,}원"] for item in sorted(store.iter_budgets(), key=lambda value: value.month)]
            _table(["MONTH", "BUDGET"], rows)
    elif args.command == "category":
        if args.category_command == "list":
            _table(["CATEGORY"], [[name] for name in service.categories()])
        elif args.category_command == "add":
            name = _category_name(args)
            if name in service.categories():
                raise BudgetError(f"이미 등록된 카테고리입니다: {name}", "category list로 기존 목록을 확인하세요.")
            store.write_categories([*service.categories(), name])
            print(f"[저장 완료] category={name}")
        else:
            name = _category_name(args)
            service.remove_category(name)
            print(f"[삭제 완료] category={name}")
    elif args.command == "update":
        transaction = service.update_transaction(
            args.id, transaction_date=args.transaction_date,
            transaction_type=args.transaction_type, category=args.category,
            amount=args.amount, memo=args.memo, tags=args.tags,
        )
        print(f"[수정 완료] id={transaction.id}")
    elif args.command == "delete":
        service.delete_transaction(args.id)
        print(f"[삭제 완료] id={args.id}")
    elif args.command == "import":
        imported, skipped, errors = service.import_csv(Path(args.source))
        print(f"[완료] imported={imported}, skipped={skipped}")
        for error in errors[:10]:
            print(f"[건너뜀] {error}", file=sys.stderr)
        if len(errors) > 10:
            print(f"[안내] 나머지 {len(errors) - 10}건의 오류는 표시하지 않았습니다.", file=sys.stderr)
    elif args.command == "export":
        count = service.export_csv(Path(args.out), month=args.month, from_date=args.from_date, to_date=args.to_date)
        print(f"[완료] {Path(args.out)} ({count} records)")
    elif args.command == "backup":
        destination = service.backup()
        print(f"[백업 완료] {destination}")
    elif args.command == "recurring":
        if args.recurring_command == "add":
            rule = service.add_recurring(args.transaction_type, args.day, args.amount, args.category, args.memo, args.tags)
            print(f"[저장 완료] recurring_id={rule.id}")
        elif args.recurring_command == "list":
            rules = sorted(store.iter_recurring(), key=lambda value: (value.day, value.id))
            rows = [[rule.id, rule.type, str(rule.day), rule.category, f"{rule.amount:,}", rule.memo, ",".join(rule.tags)] for rule in rules]
            _table(["ID", "TYPE", "DAY", "CATEGORY", "AMOUNT", "MEMO", "TAGS"], rows)
        else:
            created = service.generate_recurring(args.month)
            print(f"[완료] {args.month} generated={created}")
    return 0


@friendly_errors
def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    store = JsonlBudgetStore(Path(args.data_dir))
    store.ensure_files()
    logging.basicConfig(
        filename=str(store.directory / "budget.log"),
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    return _execute(args, BudgetService(store), store)
