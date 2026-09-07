import csv
import json
import unittest
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECOVERY = ROOT / "workpapers/2026-09-08-xero-merchant-expense-batch-3-recovery.json"
BLOCKED = ROOT / "workpapers/2026-09-07-xero-merchant-expense-batch-3-blocked.json"
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"
TRANSPORT_AUDITS = (
    ROOT / "workpapers/2026-09-07-xero-transport-expense-batch.json",
    ROOT / "workpapers/2026-09-07-xero-transport-expense-batch-2.json",
)


def load_json(path):
    with path.open() as handle:
        return json.load(handle)


class MerchantExpenseBatch3RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = load_json(RECOVERY)
        cls.blocked = load_json(BLOCKED)
        with WORKLIST.open(newline="") as handle:
            cls.worklist = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_recovery_is_the_exact_staged_source_population(self):
        staged = self.blocked["selection_control"]["transactions"]
        posted = self.audit["transactions"]
        self.assertEqual(len(posted), 17)
        self.assertEqual(
            [row["source_row"] for row in posted],
            [row["source_row"] for row in staged],
        )
        self.assertEqual(len({row["source_row"] for row in posted}), 17)
        self.assertTrue(all(row["posting_status"] == "posted_and_live_verified" for row in posted))

    def test_each_recovery_row_agrees_to_the_source_worklist(self):
        for row in self.audit["transactions"]:
            source = self.worklist[row["source_row"]]
            self.assertEqual(source["date"], datetime.strptime(row["statement_date"], "%Y-%m-%d").strftime("%d/%m/%Y"))
            self.assertEqual(Decimal(source["amount"]), Decimal(row["amount"]))
            self.assertEqual(source["description"], row["bank_description"])

    def test_batch_counts_category_totals_and_balance_arithmetic(self):
        rows = self.audit["transactions"]
        self.assertEqual(sum(-Decimal(row["amount"]) for row in rows), Decimal("428.25"))
        categories = {}
        for row in rows:
            categories.setdefault(row["account"], []).append(row)
        self.assertEqual(len(categories["453 - Office Expenses"]), 12)
        self.assertEqual(sum(-Decimal(row["amount"]) for row in categories["453 - Office Expenses"]), Decimal("271.83"))
        self.assertEqual(len(categories["485 - Subscriptions"]), 3)
        self.assertEqual(sum(-Decimal(row["amount"]) for row in categories["485 - Subscriptions"]), Decimal("36.42"))
        self.assertEqual(len(categories["493 - Travel - National"]), 2)
        self.assertEqual(sum(-Decimal(row["amount"]) for row in categories["493 - Travel - National"]), Decimal("120.00"))
        control = self.audit["queue_and_balance_control"]
        self.assertEqual(control["queue_before"] - control["queue_after"], 17)
        self.assertEqual(Decimal(control["book_balance_before"]) - Decimal(control["book_balance_after"]), Decimal("428.25"))
        self.assertEqual(control["source_statement_lines"] - control["queue_after"], control["total_lines_reconciled_to_date"])

    def test_exact_readback_queries_cover_all_17_without_batch_duplicates(self):
        queries = self.audit["post_write_exact_record_verification"]["queries"]
        new_counts = []
        for query in queries:
            if query["search"] == "60.00":
                new_counts.append(len(query["new_batch_dates"]))
                self.assertEqual(query["result_count"], 5)
                self.assertEqual(len(set(query["dates"])), 5)
            else:
                new_counts.append(query["result_count"])
        self.assertEqual(sum(new_counts), 17)
        self.assertEqual(self.audit["post_write_exact_record_verification"]["verified_new_record_count"], 17)

    def test_all_52_fy_transport_source_rows_are_now_audit_backed(self):
        source_transport = {
            source_row: Decimal(row["amount"])
            for source_row, row in self.worklist.items()
            if datetime.strptime(row["date"], "%d/%m/%Y").date() <= datetime(2026, 6, 30).date()
            and (row["proposed_account"] == "Travel" or "TRANSPORTFORNSW" in row["description"].replace(" ", "").upper())
        }
        audited = {}
        for path in TRANSPORT_AUDITS:
            for row in load_json(path)["transactions"]:
                audited[row["source_row"]] = Decimal(row["amount"])
        for row in self.audit["transactions"]:
            if row["source_row"] in (146, 154):
                audited[row["source_row"]] = Decimal(row["amount"])
        self.assertEqual(set(source_transport), set(audited))
        self.assertEqual(len(source_transport), 52)
        self.assertEqual(sum(-amount for amount in source_transport.values()), Decimal("862.85"))
        self.assertEqual(sum(-amount for amount in audited.values()), Decimal("862.85"))
        self.assertEqual(self.audit["transport_completion_control"]["source_minus_audited_rows"], [])


if __name__ == "__main__":
    unittest.main()
