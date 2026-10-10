import concurrent.futures
import unittest
from api.budget import process
from budget_app.errors import BudgetError


class WebAdapterTests(unittest.TestCase):
    def payload(self, **fields):
        return {"action": "view", "month": "2026-10", "state": {}, **fields}

    def add(self, state=None, **fields):
        return process(self.payload(action="add", state=state or {},
                       transaction_type="expense", transaction_date="2026-10-10",
                       category="food", amount=15000, **fields))

    def test_roundtrip_summary_budget_delete(self):
        first = self.add()
        read = process(self.payload(state=first["state"]))
        self.assertEqual(read["summary"]["expense"], 15000)
        self.assertEqual(read["transactions"], first["transactions"])
        budget = process(self.payload(action="budget", state=read["state"], amount=10000))
        self.assertEqual(budget["summary"]["budget"]["amount"], 10000)
        deleted = process(self.payload(action="delete", state=budget["state"],
                                      transaction_id=read["transactions"][0]["id"]))
        self.assertEqual(deleted["summary"]["expense"], 0)

    def test_invalid_input_keeps_original_state(self):
        state = self.add()["state"]
        before = repr(state)
        with self.assertRaises(BudgetError):
            process(self.payload(action="add", state=state, transaction_type="expense",
                                 transaction_date="2026-02-30", category="food", amount=10))
        self.assertEqual(repr(state), before)
        with self.assertRaises(BudgetError):
            process(self.payload(action="add", transaction_type="expense",
                                 transaction_date="2026-10-10", category="unknown", amount=10))

    def test_request_isolation(self):
        with concurrent.futures.ThreadPoolExecutor() as pool:
            results = list(pool.map(lambda _: self.add(), range(8)))
        self.assertTrue(all(len(result["transactions"]) == 1 for result in results))
        self.assertEqual(len({result["transactions"][0]["id"] for result in results}), 8)
        self.assertEqual(process(self.payload())["transactions"], [])

    def test_reject_noninteger_stored_amount(self):
        state = self.add()["state"]
        state["transactions"][0]["amount"] = True
        with self.assertRaises(ValueError):
            process(self.payload(state=state))


if __name__ == "__main__":
    unittest.main()
