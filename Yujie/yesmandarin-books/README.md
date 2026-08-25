# YesMandarin books

Reconstruct Felicity's YesMandarin accounts from commencement and leave them tax-ready and maintainable.

Xero will be retained and become the canonical books after reconstruction. Existing invoices are source documents; existing payment status, bank entries, balances and reconciliation state are untrusted until rebuilt from complete bank and payment-processor evidence.

Current evidence, source hashes and reconstruction state: [`SOURCE-INVENTORY.md`](SOURCE-INVENTORY.md).

## Current state — 25 August 2026

- Xero invoice and manual-register evidence is preserved.
- Both Stripe accounts' payment, payout and balance ledgers are preserved and internally reconciled.
- Xero reconstruction is in progress. The complete account `1913` statement range is imported and the first 29 source-supported invoice payments are reconciled; expenses, transfers, Stripe-clearing items, opening balance and ambiguous receipts remain unresolved.
- Complete CBA transaction evidence for Business Account ending `1913` is preserved through 17 August 2026. All 253 unique statement lines were imported through Xero's native importer on 25 August 2026; Xero reported zero duplicates.
- Xero currently shows a $27,754.02 statement balance because the import contains movement only. The source-backed $3,262.83 opening balance still needs to be represented before the account can agree to its $31,016.85 closing balance.
- A deterministic first-pass worklist for account `1913` is under `workpapers/`: all 29 bank lines with one invoice candidate supported by reference or payer-name evidence were reconciled in Xero on 25 August 2026, totalling $18,526.00. The Xero queue fell from 253 to 224 lines. Another 20 invoice-payment lines need review, 25 credits have no defensible invoice candidate, and nine debits remain unresolved.
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
