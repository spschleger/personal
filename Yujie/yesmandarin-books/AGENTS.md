# AGENTS.md — YesMandarin books

## Outcome

Get Felicity's YesMandarin books complete from the first day of trading and leave a simple, defensible system she can maintain.

The deliverable is correct, tax-ready books—not software. Xero is the chosen ongoing system of record, but becomes canonical only after the source-backed reconstruction is verified.

## Context

- YesMandarin is Felicity's sole-trader Mandarin school.
- Xero has been used to issue invoices but not maintain the books.
- Bank transactions, invoice payments, expenses and reconciliation need reconstruction from commencement.
- Historical GST assumptions must be checked against reconstructed turnover.

## System of record decision

**Decision — 24 August 2026:** retain Xero after 12 September 2026 and make it the canonical books only after a source-backed reconstruction.

- Treat existing Xero invoices as source documents.
- Treat all existing payment status, bank transactions, balances and reconciliation state as unverified; rebuild them from complete bank/payment-processor sources.
- Use deterministic local matching to prepare and verify the reconstruction.
- Import bank statement lines through Xero's native importer and perform reconciliation inside Xero. Browser automation may operate the UI under review. Add Xero API access only if the verified workload proves bulk payment/invoice writes earn the extra integration.
- Do not maintain a parallel custom ledger after Xero is rebuilt. Local artifacts are reconstruction evidence and control totals, not a second set of books.

## Reconstruction method

Use existing source systems and native features wherever they work:

1. Confirm commencement date, entity details, accounts and GST status.
2. Inventory invoices, credits and payments already in Xero.
3. Obtain complete bank/card statements from commencement. Use direct bank exports first; Redbark may supply posted transactions or fill gaps after Felicity authorises the relevant account.
4. Reconcile deposits to invoices and explain all other deposits in the chosen books.
5. Categorise withdrawals, attach available evidence and ask Shane or Felicity about genuinely ambiguous items.
6. Reconcile each period to its bank closing balance.
7. Review unpaid invoices, missing evidence, mixed-use expenses, assets, contractors and GST turnover.
8. Produce a short, source-linked tax working pack for Felicity or a registered tax agent.
9. Leave a small ongoing bookkeeping routine.

## Rules

- Do not treat Xero as canonical until the source-backed reconstruction is verified.
- Once chosen, keep one canonical ledger; do not maintain parallel books.
- Do not build an app, API integration or MCP workflow unless a demonstrated repetitive blocker cannot be handled safely in the chosen simple system.
- A small disposable conversion or matching script is acceptable when it saves work and its output is verified against bank and invoice sources.
- Bank date, amount and reference are bank-owned facts.
- Same date and amount alone do not prove transaction identity.
- Ambiguous, partial, combined or same-value invoice matches require review.
- Personal or mixed-use spending is not silently treated as deductible.
- Do not call a period reconciled until the ledger agrees to the source bank closing balance.
- Verify consequential writes and preserve an audit trail for corrections.

## Tax boundary

Prepare accurate books and tax working papers. Felicity makes declarations and self-lodges or appoints a registered tax agent. Isolate treatment questions requiring professional judgement.

## Security

- Never store credentials, OAuth tokens, bank credentials or TFNs in git.
- Never ask for Felicity's password; she approves account connections herself.
- Keep all financial material in the personal estate.
