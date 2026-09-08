import csv
import json
import unittest
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-final3-close-readiness-and-current-source-gap.json"
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"


class FinalThreeCloseReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(AUDIT.read_text())
        with WORKLIST.open(newline="") as handle:
            cls.source = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_read_only_status_and_checkpoint(self):
        self.assertIn("no_xero_writes", self.data["status"])
        live = self.data["fresh_live_verification"]["checkpoint"]
        self.assertEqual(live["unreconciled_statement_lines"], 40)
        self.assertEqual(live["fy2025_26_unreconciled_lines"], 3)
        self.assertEqual(live["post_2026_06_30_unreconciled_lines"], 37)
        self.assertEqual(Decimal(live["book_balance"]), Decimal("29739.75"))
        self.assertEqual(Decimal(live["statement_balance"]), Decimal("31016.85"))
        self.assertIn("not the 30 June", live["boundary"])

    def test_final_three_exact_source_and_proposals(self):
        items = self.data["final_three_parent_proposals"]
        self.assertEqual([row["source_row"] for row in items], [163, 160, 171])
        for item in items:
            source = self.source[item["source_row"]]
            self.assertEqual(
                datetime.strptime(source["date"], "%d/%m/%Y").strftime("%Y-%m-%d"),
                item["date"],
            )
            self.assertEqual(Decimal(source["amount"]), Decimal(item["amount"]))
            self.assertEqual(source["description"], item["bank_description"])
            self.assertIn("no_xero_write", item["decision_status"])
        courtney, mark, lunch = items
        self.assertEqual(courtney["proposal"]["account"], "200 - Sales")
        self.assertFalse(courtney["proposal"]["invoice_created"])
        self.assertIn("student", courtney["basis"].lower())
        self.assertIn("INV-0039", courtney["basis"])
        self.assertEqual(mark["proposal"]["account"], "420 - Entertainment")
        self.assertIn("client gift", mark["basis"].lower())
        self.assertIn("do not ask", mark["evidence_constraint"].lower())
        self.assertEqual(lunch["proposal"]["account"], "420 - Entertainment")
        self.assertIn("tax adjustment", lunch["tax_boundary"])
        for item in items:
            self.assertEqual(item["proposal"]["tax_rate"], "BAS Excluded")

    def test_chart_boundary_does_not_invent_gift_account(self):
        chart = self.data["live_chart_evidence"]
        self.assertIn("no account row", chart["gift_search"])
        accounts = {row["code"]: row for row in chart["existing_accounts"]}
        self.assertEqual(accounts["400"]["name"], "Advertising")
        self.assertEqual(accounts["420"]["name"], "Entertainment")
        self.assertIn("not source-supported", accounts["400"]["constraint"])
        self.assertEqual(accounts["420"]["default_tax"], "BAS Excluded")

    def test_year_end_target_recomputes(self):
        control = self.data["year_end_2026_control"]
        self.assertEqual(
            Decimal(control["source_opening_balance"]) + Decimal(control["source_bank_movement"]),
            Decimal("25086.17"),
        )
        self.assertEqual(Decimal(control["target_2026_06_30_bank_balance"]), Decimal("25086.17"))
        self.assertTrue(control["not_close_ready_because"])
        self.assertTrue(any("Stripe" in reason for reason in control["not_close_ready_because"]))

    def test_exact_37_later_rows_and_controls(self):
        inventory = self.data["post_2026_06_30_imported_remaining_inventory"]
        rows = inventory["transactions"]
        self.assertEqual(len(rows), 37)
        self.assertEqual([row["source_row"] for row in rows], [
            203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214,
            217, 218, 219, 220, 222, 223, 224, 226, 227, 229, 230, 232,
            233, 234, 235, 237, 238, 242, 243, 244, 245, 247, 248, 250, 251,
        ])
        for item in rows:
            source = self.source[item["source_row"]]
            self.assertEqual(source["date"], item["date"])
            self.assertEqual(Decimal(source["amount"]), Decimal(item["amount"]))
            self.assertEqual(source["description"], item["bank_description"])
        controls = inventory["controls"]
        credits = sum((Decimal(row["amount"]) for row in rows if Decimal(row["amount"]) > 0), Decimal("0"))
        debits = -sum((Decimal(row["amount"]) for row in rows if Decimal(row["amount"]) < 0), Decimal("0"))
        self.assertEqual(credits, Decimal(controls["credit_total"]))
        self.assertEqual(debits, Decimal(controls["debit_total"]))
        self.assertEqual(credits - debits, Decimal(controls["net_movement"]))
        self.assertEqual(credits - debits, Decimal("911.54"))

    def test_next_supported_batch_and_source_gap(self):
        batch = self.data["next_supported_later_period_batch"]
        self.assertEqual(batch["count"], 23)
        self.assertEqual(Decimal(batch["debit_total"]), Decimal("373.32"))
        self.assertEqual(sum(group["count"] for group in batch["groups"]), 23)
        self.assertEqual(
            sum((Decimal(group["total"]) for group in batch["groups"]), Decimal("0")),
            Decimal("373.32"),
        )
        coverage = self.data["current_source_coverage"]
        self.assertEqual(coverage["local_bank_source_end"], "2026-08-17")
        self.assertEqual(coverage["missing_statement_range"], {
            "from": "2026-08-18", "through": "2026-09-08", "calendar_days_inclusive": 22
        })
        self.assertIn("do not bring", coverage["constraint"].lower())

    def test_preserved_screenshots_exist(self):
        paths = [
            self.data["fresh_live_verification"]["jen_rollins_618"]["evidence"],
            self.data["fresh_live_verification"]["checkpoint"]["evidence"],
            self.data["live_chart_evidence"]["gift_search_evidence"],
            self.data["live_chart_evidence"]["accounts_evidence"],
            self.data["current_source_coverage"]["evidence"],
        ]
        for path in paths:
            self.assertTrue((ROOT / path).is_file(), path)


if __name__ == "__main__":
    unittest.main()
