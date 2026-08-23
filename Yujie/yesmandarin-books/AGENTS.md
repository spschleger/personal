# AGENTS.md — YesMandarin books

## Outcome

Get Felicity's YesMandarin books complete and functioning in Xero from the first day of trading. Xero is the only accounting source of truth.

The deliverable is correct, tax-ready books—not software.

## Context

- YesMandarin is Felicity's sole-trader Mandarin school.
- Xero has been used to issue invoices but not maintain the books.
- Bank transactions, invoice payments, expenses and reconciliation need reconstruction from commencement.
- Historical GST assumptions must be checked against reconstructed turnover.

## Method

Use Xero's native features wherever they work:

1. Confirm commencement date, entity details, accounts and GST status.
2. Inventory invoices, credits and payments already in Xero.
3. Obtain complete bank/card statements from commencement. Use direct bank exports first; Redbark may supply posted transactions or fill gaps after Felicity authorises the relevant account.
4. Import missing statement periods into Xero.
5. Reconcile deposits to invoices and explain all other deposits.
6. Categorise withdrawals, attach available evidence and ask Shane or Felicity about genuinely ambiguous items.
7. Reconcile each period to its bank closing balance.
8. Review unpaid invoices, missing evidence, mixed-use expenses, assets, contractors and GST turnover.
9. Produce Xero reports and a short tax working pack for Felicity or a registered tax agent.
10. Leave a small ongoing Xero routine.

## Rules

- Xero owns invoices, statement lines, payments, expenses, accounts, reconciliation and reports.
- Do not create a parallel ledger.
- Do not build an app, API integration or MCP workflow unless a demonstrated repetitive blocker cannot be handled safely in Xero.
- A small disposable conversion or matching script is acceptable when it saves work and its output is verified in Xero.
- Bank date, amount and reference are bank-owned facts.
- Same date and amount alone do not prove transaction identity.
- Ambiguous, partial, combined or same-value invoice matches require review.
- Personal or mixed-use spending is not silently treated as deductible.
- Do not call a period reconciled until Xero agrees to the source bank closing balance.
- Verify consequential writes and preserve an audit trail for corrections.

## Tax boundary

Prepare accurate books and tax working papers. Felicity makes declarations and self-lodges or appoints a registered tax agent. Isolate treatment questions requiring professional judgement.

## Security

- Never store credentials, OAuth tokens, bank credentials or TFNs in git.
- Never ask for Felicity's password; she approves account connections herself.
- Keep all financial material in the personal estate.
