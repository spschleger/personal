import csv
import json
import unittest
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POSTING = ROOT / "workpapers/2026-09-08-xero-maria-john-august-direct-receipt.json"
REVIEW = ROOT / "workpapers/2026-09-08-contractor-account-and-separate-stripe-review.json"
WORKLIST = ROOT / "workpapers/2026-08-25-account-1913-reconciliation-worklist.csv"


class MariaContractorAndStripeReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.posting = json.loads(POSTING.read_text())
        cls.review = json.loads(REVIEW.read_text())
        with WORKLIST.open(newline="", encoding="utf-8-sig") as handle:
            cls.source = {int(row["source_row"]): row for row in csv.DictReader(handle)}

    def test_maria_source_and_posting_are_exact(self):
        source = self.source[235]
        posted = self.posting["xero_posting"]
        self.assertEqual(posted["date"], datetime.strptime(source["date"], "%d/%m/%Y").date().isoformat())
        self.assertEqual(Decimal(posted["total"]), Decimal(source["amount"]))
        self.assertEqual(posted["description"], source["description"])
        self.assertEqual(posted["contact"], "Maria John")
        self.assertEqual(posted["account_code"], "200")
        self.assertEqual(posted["account_name"], "Sales")
        self.assertEqual(posted["tax_rate"], "BAS Excluded")
        self.assertEqual(posted["transaction_type"], "Receive Money")
        self.assertEqual(posted["reconciliation_state"], "Reconciled")

    def test_single_write_checkpoint_control(self):
        before = self.posting["checkpoint"]["before"]
        after = self.posting["checkpoint"]["after"]
        self.assertEqual(before["unreconciled_count"] - after["unreconciled_count"], 1)
        self.assertEqual(Decimal(after["book_balance"]) - Decimal(before["book_balance"]), Decimal("345.00"))
        self.assertEqual(Decimal(after["statement_balance"]), Decimal(before["statement_balance"]))
        self.assertEqual(
            Decimal(after["statement_balance"]) - Decimal(after["book_balance"]),
            Decimal(after["remaining_difference"]),
        )
        self.assertEqual(self.posting["scope_controls"]["xero_writes"], 1)
        self.assertEqual(self.posting["scope_controls"]["other_xero_writes"], 0)

    def test_duplicate_and_zero_invoice_controls_are_preserved(self):
        controls = self.posting["pre_write_controls"]
        self.assertEqual(controls["distinct_prior_receipt"]["date"], "2026-06-16")
        self.assertEqual(controls["distinct_prior_receipt"]["amount"], "345.00")
        self.assertIn("no matching transaction", controls["live_find_and_match"].lower())
        self.assertEqual(Decimal(controls["invoice_control"]["total"]), Decimal("0.00"))
        self.assertIn("cannot absorb", controls["invoice_control"]["conclusion"])

    def test_posting_evidence_exists_and_contains_exact_details(self):
        for relative in self.posting["evidence"]:
            self.assertTrue((ROOT / relative).is_file(), relative)
        ax = json.loads((ROOT / self.posting["evidence"][0]).read_text())
        labels = [str(element.get("label", "")) for element in ax["elements"]]
        for expected in (
            "Maria John",
            "5 Aug 2026",
            "Fast Transfer From MARIA JOHN From Maria John (Suguru)",
            "Sales",
            "BAS Excluded",
            "345.00",
            "Reconciled",
        ):
            self.assertIn(expected, labels)

    def test_contractor_rows_and_existing_account_are_exact(self):
        contractor = self.review["contractor_teaching_service_review"]
        for row in contractor["source_rows"]:
            source = self.source[row["logical_source_row"]]
            self.assertEqual(row["date"], datetime.strptime(source["date"], "%d/%m/%Y").date().isoformat())
            self.assertEqual(Decimal(row["amount"]), Decimal(source["amount"]))
            self.assertEqual(row["bank_description"], source["description"])
            self.assertIn("Teaching service payment", row["bank_description"])
        account = contractor["verified_existing_account"]
        self.assertEqual(account["code"], "412")
        self.assertEqual(account["name"], "Consulting & Accounting")
        self.assertEqual(account["type"], "Expense")
        self.assertEqual(account["default_tax_rate"], "BAS Excluded")
        self.assertEqual(account["live_search_result_count"], 1)
        for relative in account["evidence"]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_separate_stripe_bridges_recompute(self):
        stripe = self.review["separate_stripe_local_review"]
        later = stripe["later_chain"]
        self.assertEqual(
            Decimal(later["gross"])
            - Decimal(later["processing_fee_including_gst"])
            - Decimal(later["invoicing_fee_including_gst"]),
            Decimal(later["payout_amount"]),
        )
        opening = stripe["opening_boundary_chain"]
        parts = opening["composition_proved_by_full_balance_ledger"]
        self.assertEqual(
            Decimal(parts[0]["net_contribution"])
            + Decimal(parts[1]["net_contribution"])
            + Decimal(parts[2]["net_fee_adjustment_credits"]),
            Decimal(opening["payout_amount"]),
        )

    def test_review_remains_read_only_and_provisional(self):
        self.assertEqual(self.review["xero_writes"], 0)
        self.assertEqual(self.review["reports"]["status"], "provisional")
        self.assertEqual(self.review["reports"]["tax_close"], "not complete")
        prohibited = " ".join(self.review["separate_stripe_local_review"]["do_not_do"])
        self.assertIn("Do not force", prohibited)
        self.assertIn("Do not post", prohibited)


if __name__ == "__main__":
    unittest.main()
