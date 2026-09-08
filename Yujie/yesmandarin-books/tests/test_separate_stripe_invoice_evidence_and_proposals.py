import csv
import json
import re
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "workpapers/2026-09-08-separate-stripe-invoice-readonly-evidence-and-proposed-entries.json"
PREDECESSOR_REVIEW = ROOT / "workpapers/2026-09-08-contractor-account-and-separate-stripe-review.json"
XERO_INVOICES = ROOT / "sources/xero/2026-08-24-sales-invoices.csv"

RAW_STRIPE_ID = re.compile(
    r"(?<![A-Za-z0-9])(?:ch|po|cus|in|py|txn|acct|ca)_[A-Za-z0-9]{12,}"
)


class SeparateStripeInvoiceEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = json.loads(AUDIT.read_text())
        cls.review = json.loads(PREDECESSOR_REVIEW.read_text())
        with XERO_INVOICES.open(newline="", encoding="utf-8-sig") as handle:
            cls.invoices = list(csv.DictReader(handle))

    def test_new_durable_files_do_not_propagate_raw_stripe_ids(self):
        for path in (AUDIT, PREDECESSOR_REVIEW, Path(__file__)):
            self.assertIsNone(RAW_STRIPE_ID.search(path.read_text()), path)
        self.assertEqual(
            self.audit["identifier_handling"]["identifier_values"], "[REDACTED]"
        )

    def test_later_chain_recomputes_and_remains_conditional(self):
        row = self.audit["three_invoice_relationships"][0]
        self.assertEqual(
            Decimal(row["gross"])
            - Decimal(row["processing_fee_including_gst"])
            - Decimal(row["invoicing_fee_including_gst"]),
            Decimal(row["net_payout"]),
        )
        self.assertEqual(row["service_period"], "Not available in preserved local sources.")
        self.assertIn(
            "Only after invoice detail proves",
            self.audit["proposed_entries_no_posting"]["later_charge_conditional"]["gate"],
        )

    def test_no_exact_xero_invoice_duplicate_for_later_charge(self):
        matches = [
            row
            for row in self.invoices
            if Decimal(row["Total"]) == Decimal("687.50")
        ]
        self.assertEqual(matches, [])
        ann = [row for row in self.invoices if row["ContactName"] == "Ann Panek"]
        self.assertEqual(
            sorted(Decimal(row["Total"]) for row in ann),
            [Decimal("855.00"), Decimal("870.00")],
        )

    def test_opening_bridge_and_no_current_income(self):
        opening = self.audit["opening_balance_control"]
        self.assertEqual(
            Decimal(opening["first_pre_period_net"])
            + Decimal(opening["second_pre_period_net"])
            + Decimal(opening["fee_adjustment_credits"]),
            Decimal(opening["opening_boundary_payout"]),
        )
        entries = " ".join(
            self.audit["proposed_entries_no_posting"]["opening_boundary_conditional"]["entries"]
        )
        self.assertIn("Do not credit current-period Sales", entries)
        self.assertIn("Owner A Drawings", entries)

    def test_invoice_line_items_are_honestly_blocked(self):
        retrieval = self.audit["invoice_detail_retrieval"]
        self.assertEqual(retrieval["requested_items"], 3)
        self.assertEqual(retrieval["retrieved_line_item_details"], 0)
        self.assertIn("0x0", retrieval["visible_browser_result"])
        self.assertIn("genuine UI-access blocker", retrieval["access_boundary"])

    def test_teaching_service_classification_rejects_semantic_misfit(self):
        proposal = self.audit["teaching_service_classification"]["proposal"]
        self.assertIn("Do not use 412", proposal)
        self.assertIn("dedicated Contractor teaching costs", proposal)
        self.assertIn("429", proposal)
        self.assertIn("Do not use 310", proposal)
        self.assertEqual(self.audit["teaching_service_classification"]["xero_writes"], 0)
        predecessor = self.review["contractor_teaching_service_review"]["account_proposal"]
        self.assertIn("Do not use 412", predecessor)

    def test_scope_is_read_only_and_reports_are_provisional(self):
        self.assertIn("No Stripe or Xero write", self.audit["scope"])
        self.assertEqual(self.audit["reports"]["status"], "provisional")
        self.assertEqual(self.audit["reports"]["tax_close"], "not complete")


if __name__ == "__main__":
    unittest.main()
