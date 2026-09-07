import csv
import json
import unittest
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"
INVENTORY = ROOT / "workpapers/2026-09-08-fy2025-26-remaining-inventory-and-mapping-proposals.json"
EXPECTED_SOURCE_ROWS = [
    13, 24, 57, 58, 69, 71, 116, 125, 126, 133, 142, 156, 160, 163, 164,
    168, 169, 171, 172, 173, 174, 175, 178, 179, 183, 184, 192, 193, 196, 198,
]


class RemainingFyInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = json.loads(INVENTORY.read_text())
        with WORKLIST.open(newline="") as handle:
            cls.worklist = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_inventory_is_the_exact_30_row_checkpoint_population(self):
        rows = self.audit["transactions"]
        self.assertEqual(len(rows), 30)
        self.assertEqual([row["source_row"] for row in rows], EXPECTED_SOURCE_ROWS)
        self.assertEqual(len({row["source_row"] for row in rows}), 30)
        self.assertTrue(all(row["posting_status"] == "unreconciled_at_checkpoint_186" for row in rows))
        self.assertEqual(self.audit["checkpoint"]["reconciled"], 186)
        self.assertEqual(self.audit["checkpoint"]["remaining_fy2025_26"], 30)
        self.assertEqual(self.audit["checkpoint"]["remaining_post_2026_06_30"], 37)

    def test_every_inventory_row_agrees_exactly_to_the_source_worklist(self):
        for row in self.audit["transactions"]:
            source = self.worklist[row["source_row"]]
            self.assertLessEqual(datetime.strptime(source["date"], "%d/%m/%Y").date(), datetime(2026, 6, 30).date())
            self.assertEqual(datetime.strptime(source["date"], "%d/%m/%Y").strftime("%Y-%m-%d"), row["statement_date"])
            self.assertEqual(Decimal(source["amount"]), Decimal(row["amount"]))
            self.assertEqual(source["description"], row["bank_description"])
            self.assertEqual(source["kind"], row["kind"])

    def test_inventory_control_totals(self):
        rows = self.audit["transactions"]
        debits = [Decimal(row["amount"]) for row in rows if Decimal(row["amount"]) < 0]
        credits = [Decimal(row["amount"]) for row in rows if Decimal(row["amount"]) > 0]
        controls = self.audit["controls"]
        self.assertEqual(len(debits), 16)
        self.assertEqual(-sum(debits), Decimal("1176.74"))
        self.assertEqual(len(credits), 14)
        self.assertEqual(sum(credits), Decimal("9165.00"))
        self.assertEqual(sum(debits + credits), Decimal("7988.26"))
        self.assertEqual(Decimal(controls["debit_total"]), Decimal("1176.74"))
        self.assertEqual(Decimal(controls["credit_total"]), Decimal("9165.00"))
        self.assertEqual(Decimal(controls["net_movement"]), Decimal("7988.26"))

    def test_mapping_proposals_cover_every_remaining_row_once(self):
        proposals = self.audit["mapping_proposals"]
        proposed_rows = [source_row for proposal in proposals for source_row in proposal["source_rows"]]
        self.assertEqual(sorted(proposed_rows), sorted(EXPECTED_SOURCE_ROWS))
        self.assertEqual(len(proposed_rows), len(set(proposed_rows)))
        self.assertTrue(all(proposal["posting_status"].startswith("not_posted") for proposal in proposals))

    def test_taobao_item_nature_is_not_guessed_and_fees_are_separate(self):
        proposals = {proposal["group"]: proposal for proposal in self.audit["mapping_proposals"]}
        purchases = proposals["taobao_purchases_item_nature_unverified"]
        fees = proposals["international_transaction_fees"]
        self.assertIsNone(purchases["proposed_existing_account"])
        self.assertEqual(purchases["source_rows"], [24, 168, 172, 174])
        self.assertEqual(fees["source_rows"], [169, 173, 175])
        self.assertEqual(fees["proposed_existing_account"], "404 - Bank Fees")

    def test_no_xero_write_is_claimed(self):
        self.assertEqual(self.audit["status"], "read_only_preparation_complete_no_xero_writes")
        self.assertIn("No Xero transaction was posted or edited.", self.audit["guardrails"])


if __name__ == "__main__":
    unittest.main()
