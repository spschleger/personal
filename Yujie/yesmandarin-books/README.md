# YesMandarin books

Reconstruct Felicity's YesMandarin accounts from commencement and leave them tax-ready and maintainable.

Xero will be retained and become the canonical books after reconstruction. Existing invoices are source documents; existing payment status, bank entries, balances and reconciliation state are untrusted until rebuilt from complete bank and payment-processor evidence.

Current evidence, source hashes and reconstruction state: [`SOURCE-INVENTORY.md`](SOURCE-INVENTORY.md).

## Current state — 3 September 2026

- Xero invoice and manual-register evidence is preserved.
- Both Stripe accounts' payment, payout and balance ledgers are preserved and internally reconciled.
- Xero reconstruction is in progress. Of 253 imported account `1913` statement lines, 113 are reconciled and 140 remain (44.7% complete). Completed statement-line work comprises 51 source-supported invoice-related receipts, the $650 Daniel Lie and $618 Benjamin-Rashid Klaim verbal-agreement/direct tuition sales, nine Digital Pacific hosting expenses totalling $162.70, all 27 Microsoft-related lines, all nine Xero subscription debits totalling $315, all 13 office-rent debits totalling $9,750, the $2,000 transfer to account `9316` posted to `880 - Owner A Drawings`, and the source-matched $660.10 separate-account Stripe payout isolated to `092 - Stripe Clearing - Separate`.
- The Xero-linked Stripe chain is posted and verified in `Stripe Clearing`: six invoice receipts grossing $4,975.00, six processing fees totalling $105.89, and six payouts totalling $4,869.11 to Felicity's personal account ending `9316`. The payouts were posted to `880 - Owner A Drawings`; the verified clearing balance is $0.00. Audit: `workpapers/2026-09-02-xero-stripe-clearing-reconstruction.json`.
- Complete CBA transaction evidence for Business Account ending `1913` is preserved through 17 August 2026. All 253 unique statement lines were imported through Xero's native importer on 25 August 2026; Xero reported zero duplicates.
- Xero's imported statement movement is $27,754.02. Shane confirmed the source-backed $3,262.83 opening balance was founder-contributed starting capital. It was posted and verified in Xero's 30 June 2025 conversion balances as a $3,262.83 debit to `090 - Business Account` and credit to `881 - Owner A Funds Introduced`, with no income effect. This brings the source closing-balance control to $31,016.85.
- The 51 posted invoice-related receipt lines total $30,662.00. The first batch reconciled 29 lines totalling $18,526.00; the controlled review added 17 lines totalling $10,342.00; the two Jack Anderson receipts of $333 and $332 were split across INV-0047; the $449 M Janda receipt was allocated as $448 to INV-0017 plus a $1 minor adjustment; and the $68 plus $612 Take My Cans receipts were matched exactly to INV-0024.
- The $650 Daniel Lie receipt could not reuse INV-0066, which the verified 25 August audit tied to the explicitly referenced 13 May bank row. Shane confirmed on 3 September 2026 that the later receipt was sales for Term 3 Mandarin tuition agreed verbally. It was reconciled directly to `200 - Sales`, `BAS Excluded`, rather than against a fabricated retrospective invoice. The $618 Benjamin-Rashid Klaim receipt explicitly narrated as one term of student fees was likewise reconciled directly to `200 - Sales`, `BAS Excluded`, without creating an invoice. The other unmatched credits, unresolved debits and excluded $309.55 Shane receipt still require their own evidence or classification.
- Machine-readable posting audits: `workpapers/2026-08-25-xero-invoice-reconciliation-result.json`, `workpapers/2026-08-26-xero-additional-invoice-reconciliation-result.json`, `workpapers/2026-08-26-xero-expense-reconciliation-result.json`, `workpapers/2026-09-01-xero-microsoft-reconciliation-progress.json` and `workpapers/2026-09-03-xero-reconciliation-progress.json`. Opening-balance treatment: `workpapers/2026-08-26-opening-balance-treatment.json`.
- Three bank rules are saved and visibly confirmed in Xero: `Microsoft subscriptions` (bank text contains `Microsoft`; contact `Microsoft`; `485 - Subscriptions`; `BAS Excluded`), `Xero subscriptions` (description contains `XERO AU`; contact `Xero`; `485 - Subscriptions`; `BAS Excluded`), and `Office rent` (description contains `Rent`; contact `PTC Trust`; `469 - Rent`; `BAS Excluded`). The latest full balance checkpoint after Benjamin-Rashid Klaim showed statement balance $31,016.85 and book balance $22,663.14; subsequent invoice matches were verified by queue movement rather than a refreshed balance. The account remains unreconciled.
- Account `9316` will not be added as a Xero bank account. Stripe's payout exports are the source for the Xero-linked business receipts paid there, and the verified payouts clear to `880 - Owner A Drawings`. The separate Stripe account's $1,197.73 opening-boundary payout remains isolated and must not be recognised as current-period income. Any money returned from `9316` would appear as a business-account deposit; absent a matching unexplained deposit, it is treated as not returned.
- Immediate sequence: close FY2025–26 before later activity. The audit-backed projection is 103 unreconciled lines dated through 30 June 2026 (15 credits totalling $9,474.55 and 88 debits totalling $2,712.38), followed by 37 lines dated 1 July–17 August 2026. Resolve FY credits, classify FY withdrawals, close off-ledger Stripe/personal-paid items, prove Xero to the $25,086.17 source bank balance at 30 June, then produce the tax working pack. Critical path: `workpapers/2026-09-03-fy2025-26-tax-close-critical-path.md`.
- The non-Xero-linked Stripe account's $687.50 charge remains unattributed. Its source-matched $660.10 payout to account `1913` was reconciled on 3 September 2026 to the distinct current-asset account `092 - Stripe Clearing - Separate`, leaving a visible $660.10 credit balance and no revenue effect. The $24.37 processing fee and $3.03 invoicing fee remain unposted with the gross charge. The $1,197.73 opening-boundary payout remains isolated and outside current-period income. Audit: `workpapers/2026-09-02-separate-stripe-treatment-gates.json`.
- Shane must personally stop Xero's scheduled 12 September 2026 cancellation if the subscription is to continue.

## Done means

- Every relevant bank/card statement period is represented in the canonical books.
- Every statement line is reconciled or explicitly unresolved.
- Invoices and payments are correct.
- Other income, expenses, assets, drawings, contributions and transfers are correctly recorded.
- Bank closing balances agree by period.
- Missing evidence and tax-treatment questions are listed.
- GST turnover has been checked through time.
- Reports and source evidence are ready for Felicity or a registered tax agent.
- A small ongoing bookkeeping routine exists.

## Needed to start

- Felicity-approved access to YesMandarin Xero.
- Trading commencement date and entity details.
- Every bank account/card used for the business.
- Complete statements or exports from commencement.
- Current GST status and available receipts, supplier invoices, contractor records and asset records.

Use the smallest system that preserves reconciliation, evidence and auditability. Add tooling only when the work proves it is necessary.
