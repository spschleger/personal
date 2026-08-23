# AGENTS.md — YesMandarin Xero reconstruction

## Outcome

Get Felicity's YesMandarin books complete and functioning in Xero from the first day of trading. Xero is the accounting source of truth: invoices, bank reconciliation, chart of accounts, general ledger, reports and tax-accountant handoff.

The deliverable is correct books in Xero, not a bookkeeping app.

## Context

- YesMandarin is Felicity's Mandarin school and operates under her sole-trader position.
- Xero has been used to issue invoices only.
- Bank feeds/statements have not been reconciled, expenses have not been entered and the accounting ledger has not been maintained.
- The job is a back-reconstruction from commencement, followed by a simple ongoing process.
- Historical assumptions about GST status or turnover must be re-tested against the reconstructed numbers.

## System boundary

### Xero owns

- issued invoices and credits;
- contacts;
- chart of accounts;
- bank accounts and imported statement lines;
- reconciled invoice payments;
- spend/receive-money transactions;
- bills and attachments where appropriate;
- general ledger and financial reports.

### Supporting automation may own temporarily

- source-file inventory and checksums;
- parsing bank exports;
- deterministic match proposals;
- merchant/category suggestions;
- ambiguity queue;
- write/read-back verification logs.

Supporting code is disposable unless repeated operations prove a durable tool is necessary. Never create a parallel accounting ledger or app for its own sake.

## Reconstruction sequence

1. Establish commencement date, entity details, Xero organisation, financial year, accounting basis, bank accounts and current GST registration state.
2. Export/inspect all Xero invoices, credit notes, contacts and recorded payments from commencement.
3. Obtain complete statements/exports for every relevant bank account and card from commencement, with opening and closing balances.
4. Import missing statement periods into Xero using Xero's supported statement-import workflow.
5. Reconcile deposits against invoices: exact references first, then unique amount/customer/date evidence; review partial, combined, duplicated, refunded and ambiguous payments individually.
6. Explain all other deposits: other income, owner contribution, transfer, refund or unresolved.
7. Explain all withdrawals: business expense, asset, owner drawing, transfer, refund or unresolved. Attach source evidence where available.
8. Reconcile each statement period to the bank closing balance; do not declare a period complete merely because transactions were categorised.
9. Review unpaid/voided invoices, missing documents, mixed-use expenses, assets, contractors, cash, loans, GST turnover and prior-period consequences.
10. Produce Xero reports and a source-linked tax working pack. Felicity reviews and self-lodges or appoints a registered tax agent.
11. Define the smallest ongoing monthly process inside Xero.

## Matching and automation rules

- Begin read-only and dry-run.
- Bank statement date, amount and reference are bank-owned facts.
- Automatic matches require deterministic, unique evidence; same amount/date alone is not identity.
- Never automatically choose among same-value invoices, partial payments, combined payments or ambiguous customers.
- Never let a language model directly create accounting truth. It may explain or propose; deterministic code or an explicit human decision authorises a consequential write.
- Verify every Xero write by reading the resulting invoice/payment/transaction state back.
- Lock a merchant/category rule only after Shane or Felicity approves the rule and scope.
- Personal or mixed-use transactions are not silently treated as deductions.
- Corrections preserve an audit trail; do not erase settled history to make reports look clean.

## Tax boundary

This project prepares accurate books and tax working papers. It does not make declarations or lodge on Felicity's behalf. Tax treatment requiring professional judgement is isolated with facts and evidence for Felicity or a registered tax agent.

## Security

- Never store Xero credentials, OAuth tokens, bank credentials or TFNs in git.
- Use OAuth approval; never ask for or type Felicity's password.
- Keep source documents and financial data inside the personal estate.
- Do not send data to third parties without explicit approval.
