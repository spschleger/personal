# YesMandarin books

Reconstruct Felicity's YesMandarin accounts from commencement and leave them tax-ready and maintainable.

Xero will be retained and become the canonical books after reconstruction. Existing invoices are source documents; existing payment status, bank entries, balances and reconciliation state are untrusted until rebuilt from complete bank and payment-processor evidence.

Current evidence, source hashes and reconstruction state: [`SOURCE-INVENTORY.md`](SOURCE-INVENTORY.md).

## Current state — 1 September 2026

- Xero invoice and manual-register evidence is preserved.
- Both Stripe accounts' payment, payout and balance ledgers are preserved and internally reconciled.
- Xero reconstruction is in progress. Of 253 imported account `1913` statement lines, 107 are reconciled and 146 remain (42.3% complete). Completed statement-line work comprises 49 source-supported invoice-related receipts, nine Digital Pacific hosting expenses totalling $162.70, all 27 Microsoft-related lines, all nine Xero subscription debits totalling $315, and all 13 office-rent debits totalling $9,750.
- Complete CBA transaction evidence for Business Account ending `1913` is preserved through 17 August 2026. All 253 unique statement lines were imported through Xero's native importer on 25 August 2026; Xero reported zero duplicates.
- Xero's imported statement movement is $27,754.02. Shane confirmed the source-backed $3,262.83 opening balance was founder-contributed starting capital. It was posted and verified in Xero's 30 June 2025 conversion balances as a $3,262.83 debit to `090 - Business Account` and credit to `881 - Owner A Funds Introduced`, with no income effect. This brings the source closing-balance control to $31,016.85.
- The 49 posted invoice-related receipt lines total $29,982.00. The first batch reconciled 29 lines totalling $18,526.00; the controlled review added 17 lines totalling $10,342.00; the two Jack Anderson receipts of $333 and $332 were split across INV-0047; and the $449 M Janda receipt was allocated as $448 to INV-0017 plus a $1 minor adjustment. Every searched line disappeared after posting and the queue fell one-for-one from 253 to 204.
- One invoice case remains unresolved: the $650 Daniel Lie receipt cannot reuse INV-0066, which the verified 25 August audit already tied to the explicitly referenced 13 May bank row. The other 25 unmatched credits, nine unresolved debits and excluded $309.55 Shane receipt still require their own evidence or classification.
- Machine-readable posting audits: `workpapers/2026-08-25-xero-invoice-reconciliation-result.json`, `workpapers/2026-08-26-xero-additional-invoice-reconciliation-result.json`, `workpapers/2026-08-26-xero-expense-reconciliation-result.json` and `workpapers/2026-09-01-xero-microsoft-reconciliation-progress.json`. Opening-balance treatment: `workpapers/2026-08-26-opening-balance-treatment.json`.
- Three bank rules are saved and visibly confirmed in Xero: `Microsoft subscriptions` (bank text contains `Microsoft`; contact `Microsoft`; `485 - Subscriptions`; `BAS Excluded`), `Xero subscriptions` (description contains `XERO AU`; contact `Xero`; `485 - Subscriptions`; `BAS Excluded`), and `Office rent` (description contains `Rent`; contact `PTC Trust`; `469 - Rent`; `BAS Excluded`). At the latest verified checkpoint, Xero showed statement balance $31,016.85, book balance $27,604.15 and a $3,412.70 difference, so the account is not reconciled.
- Immediate sequence: resolve the account `9316` / Stripe-clearing chain, including the $2,000 inter-account transfer, six Xero-linked Stripe payouts and the $1,197.73 opening-boundary payout; then classify the remaining unmatched credits, supplier debits, owner movements and ambiguous withdrawals.
- The remaining bank-source blocker is Felicity's personal account ending `9316`; its business-related movements must be isolated from the personal ledger before the Stripe chain and the $2,000 inter-account transfer can be completed.
- The non-Xero-linked Stripe account's $687.50 charge remains unattributed.
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
