# AGENTS.md — YesMandarin books

## Outcome

Get Felicity's YesMandarin books complete from the first day of trading and leave a simple, defensible system she can maintain.

The deliverable is correct, tax-ready books—not Xero and not software. The ongoing system of record is an open decision until the real volume and complexity are inspected.

## Context

- YesMandarin is Felicity's sole-trader Mandarin school.
- Xero has been used to issue invoices but not maintain the books.
- Bank transactions, invoice payments, expenses and reconciliation need reconstruction from commencement.
- Historical GST assumptions must be checked against reconstructed turnover.

## First decision

Compare the smallest viable options after inventorying the business:

1. keep Xero on the cheapest plan that fits;
2. export Xero's invoice history and run a controlled cashbook/evidence system outside Xero;
3. use Xero only during reconstruction and migrate once the opening books are complete.

Choose on total operating effort and failure risk, not familiarity or sunk cost. Do not build a custom ledger until native spreadsheets plus deterministic scripts are shown to be insufficient.

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

- Do not declare Xero or a custom ledger canonical until the system-of-record decision is made.
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
