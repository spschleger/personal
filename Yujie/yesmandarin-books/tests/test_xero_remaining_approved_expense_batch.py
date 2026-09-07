import json
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-xero-remaining-approved-expense-batch.json"


class RemainingApprovedExpenseBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())
        cls.rows = cls.data["transactions"]

    def test_batch_controls(self):
        data, rows = self.data, self.rows
        self.assertEqual(data["status"], "posted_and_live_verified")
        self.assertEqual(len(rows), 8)
        self.assertEqual({r["source_row"] for r in rows}, {13, 57, 58, 116, 169, 173, 175, 179})
        self.assertEqual(sum(-Decimal(r["amount"]) for r in rows), Decimal("500.48"))
        self.assertEqual(data["controls"]["queue_before"] - data["controls"]["queue_after"], 8)
        self.assertEqual(Decimal(data["controls"]["book_balance_before"]) - Decimal(data["controls"]["book_balance_after"]), Decimal("500.48"))
        self.assertTrue(all(r["tax_rate"] == "BAS Excluded" for r in rows))
        self.assertEqual(data["controls"]["new_accounts_created"], 0)

    def test_accounts_and_scope_are_bounded(self):
        data = self.data
        by_row = {r["source_row"]: r for r in self.rows}
        self.assertEqual({by_row[i]["account"] for i in (13, 179)}, {"453 - Office Expenses"})
        self.assertEqual({by_row[i]["account"] for i in (169, 173, 175)}, {"404 - Bank Fees"})
        self.assertEqual({by_row[i]["account"] for i in (57, 58, 116)}, {"445 - Light, Power, Heating"})
        self.assertTrue(all(r["date"] <= "2026-06-30" for r in self.rows))
        self.assertEqual(data["remaining_checkpoint"], {
            "all_unreconciled_statement_lines": 59,
            "fy2025_26_unreconciled_lines": 22,
            "post_2026_06_30_unreconciled_lines": 37,
            "later_covau_row": {"date": "2026-07-02", "amount": "-239.67", "status": "not_posted_outside_fy_scope"},
        })


if __name__ == "__main__":
    unittest.main()
