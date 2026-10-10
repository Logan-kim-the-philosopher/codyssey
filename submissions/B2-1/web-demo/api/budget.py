"""Stateless web adapter over the unchanged console service and JSONL store."""
import json
import sys
import tempfile
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from budget_app.errors import BudgetError
from budget_app.models import Budget, Transaction
from budget_app.service import BudgetService
from budget_app.storage import JsonlBudgetStore

MAX_BODY = 1_000_000


def process(payload):
    if not isinstance(payload, dict):
        raise ValueError("요청은 JSON 객체여야 합니다.")
    state = payload.get("state", {})
    if not isinstance(state, dict):
        raise ValueError("저장 데이터 형식이 올바르지 않습니다.")
    transactions, budgets = state.get("transactions", []), state.get("budgets", [])
    if not isinstance(transactions, list) or not isinstance(budgets, list):
        raise ValueError("거래와 예산은 목록이어야 합니다.")
    if len(transactions) > 2000 or len(budgets) > 120:
        raise ValueError("체험용 저장 한도를 초과했습니다 (거래 2,000건, 예산 120개).")
    for row in transactions:
        if not isinstance(row, dict) or type(row.get("amount")) is not int:
            raise ValueError("거래 금액은 정수여야 합니다.")
    for row in budgets:
        if not isinstance(row, dict) or type(row.get("amount")) is not int:
            raise ValueError("예산 금액은 정수여야 합니다.")
    with tempfile.TemporaryDirectory(prefix="budget-demo-") as directory:
        store = JsonlBudgetStore(Path(directory))
        store.ensure_files()
        store.replace_transactions(Transaction.from_dict(row) for row in transactions)
        store.write_budgets(Budget(**row) for row in budgets)
        service = BudgetService(store)
        action = payload.get("action", "view")
        if action == "add":
            if len(transactions) >= 2000:
                raise ValueError("거래는 최대 2,000건까지 저장할 수 있습니다.")
            service.add_transaction(**{key: payload[key] for key in (
                "transaction_type", "transaction_date", "category", "amount", "memo", "tags"
            ) if key in payload})
        elif action == "delete":
            service.delete_transaction(payload["transaction_id"])
        elif action == "budget":
            service.set_budget(payload["month"], payload["amount"])
        elif action != "view":
            raise ValueError("지원하지 않는 작업입니다.")
        rows = [item.to_dict() for item in service.iter_transactions()]
        saved_budgets = [item.to_dict() for item in store.iter_budgets()]
        summary = service.summary(payload["month"])
        if summary["budget"] is not None:
            summary["budget"] = asdict(summary["budget"])
        return {"state": {"transactions": rows, "budgets": saved_budgets},
                "transactions": rows, "categories": service.categories(), "summary": summary}


class handler(BaseHTTPRequestHandler):
    def respond(self, status, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_BODY:
                self.respond(413, {"error": "요청 데이터는 1MB 이하여야 합니다."})
                return
            payload = json.loads(self.rfile.read(length))
            self.respond(200, process(payload))
        except BudgetError as error:
            self.respond(400, {"error": str(error), "hint": error.hint})
        except (ValueError, TypeError, KeyError, AttributeError) as error:
            self.respond(400, {"error": "입력 데이터가 올바르지 않습니다.", "hint": str(error)})
        except OSError:
            self.respond(500, {"error": "거래를 처리하지 못했습니다. 잠시 후 다시 시도하세요."})

    def do_GET(self):
        self.respond(200, {"status": "ok", "engine": "budget_app"})
