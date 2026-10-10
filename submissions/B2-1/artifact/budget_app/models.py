from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timezone
from typing import Any
from uuid import uuid4

from .errors import BudgetError


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:12].upper()}"


def parse_date(value: str) -> date:
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError) as error:
        raise BudgetError("날짜 형식이 올바르지 않습니다 (YYYY-MM-DD).", "예: 2026-09-30") from error
    if parsed.isoformat() != value:
        raise BudgetError("날짜 형식이 올바르지 않습니다 (YYYY-MM-DD).", "예: 2026-09-30")
    return parsed


def validate_month(value: str) -> str:
    try:
        parsed = datetime.strptime(value, "%Y-%m")
    except (TypeError, ValueError) as error:
        raise BudgetError("월 형식이 올바르지 않습니다 (YYYY-MM).", "예: 2026-09") from error
    if parsed.strftime("%Y-%m") != value:
        raise BudgetError("월 형식이 올바르지 않습니다 (YYYY-MM).", "예: 2026-09")
    return value


def parse_tags(value: str | list[str] | tuple[str, ...] | None) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        items = value.split(",")
    else:
        items = value
    return tuple(dict.fromkeys(tag.strip() for tag in items if tag.strip()))


@dataclass(frozen=True)
class Transaction:
    id: str
    type: str
    date: str
    amount: int
    category: str
    memo: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat(timespec="microseconds"))
    recurring_rule_id: str | None = None
    recurring_month: str | None = None

    def __post_init__(self) -> None:
        parse_date(self.date)
        if self.type not in {"income", "expense"}:
            raise BudgetError("타입은 income 또는 expense여야 합니다.", "타입 입력을 확인하세요.")
        if isinstance(self.amount, bool) or not isinstance(self.amount, int) or self.amount <= 0:
            raise BudgetError("금액은 양수 정수여야 합니다.", "예: 15000")
        if not self.category.strip():
            raise BudgetError("카테고리를 입력해야 합니다.", "category list로 등록된 항목을 확인하세요.")
        object.__setattr__(self, "tags", parse_tags(self.tags))

    @property
    def sort_key(self) -> tuple[str, str, str]:
        return self.date, self.created_at, self.id

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, row: dict[str, Any]) -> Transaction:
        return cls(
            id=str(row["id"]),
            type=str(row["type"]),
            date=str(row["date"]),
            amount=int(row["amount"]),
            category=str(row["category"]),
            memo=str(row.get("memo", "")),
            tags=parse_tags(row.get("tags")),
            created_at=str(row.get("created_at") or datetime.now(timezone.utc).isoformat(timespec="microseconds")),
            recurring_rule_id=row.get("recurring_rule_id"),
            recurring_month=row.get("recurring_month"),
        )


@dataclass(frozen=True)
class Budget:
    month: str
    amount: int

    def __post_init__(self) -> None:
        validate_month(self.month)
        if isinstance(self.amount, bool) or not isinstance(self.amount, int) or self.amount <= 0:
            raise BudgetError("예산은 양수 정수여야 합니다.", "예: --amount 500000")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class RecurringRule:
    id: str
    type: str
    day: int
    amount: int
    category: str
    memo: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.type not in {"income", "expense"}:
            raise BudgetError("타입은 income 또는 expense여야 합니다.", "--type income 또는 --type expense를 사용하세요.")
        if not 1 <= self.day <= 31:
            raise BudgetError("반복 날짜는 1에서 31 사이여야 합니다.", "--day 값은 1~31로 입력하세요.")
        if isinstance(self.amount, bool) or not isinstance(self.amount, int) or self.amount <= 0:
            raise BudgetError("금액은 양수 정수여야 합니다.", "예: --amount 15000")
        object.__setattr__(self, "tags", parse_tags(self.tags))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, row: dict[str, Any]) -> RecurringRule:
        return cls(
            id=str(row["id"]), type=str(row["type"]), day=int(row["day"]),
            amount=int(row["amount"]), category=str(row["category"]),
            memo=str(row.get("memo", "")), tags=parse_tags(row.get("tags")),
        )
