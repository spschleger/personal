# YesMandarin books — source inventory

**Observed:** 24 August 2026

## Current conclusion

Xero is not currently complete books. It is an invoice register plus 18 manually created payment/fee entries. No bank statement has ever been imported, all bank-register entries are unreconciled, and the displayed Xero bank balance does not represent a source bank statement.

Use Xero as a historical invoice source during reconstruction. Treat complete bank statements as the cash source of truth. Do not decide the permanent system of record until the bank reconstruction shows the real volume and complexity.

## Xero organisation

- Organisation: YesMandarin.
- Xero organisation created 1 July 2025.
- Current plan: Ignite, AUD $37/month including GST.
- Cancellation is already scheduled for 12 September 2026.
- Financial year end: 30 June.
- GST accounting method: None.
- Xero Activity Statements are not set up.
- GST status still requires confirmation against the entity record and reconstructed turnover; do not infer legal registration solely from Xero configuration.

## Sales invoices

Canonical export: `sources/xero/2026-08-24-sales-invoices.csv`

- SHA-256: `048c18babf80a1a05e914c2a2f29624d19d318ed192d4b36f54b3a23c9008bdf`
- 76 invoices across 35 contacts.
- Earliest invoice in export: INV-0003, dated 9 July 2025.
- Latest invoice: INV-0088, dated 14 August 2026.
- 13 marked Paid.
- 61 marked Awaiting Payment.
- 2 Draft.
- Total invoiced: $47,110.50.
- Marked paid: $8,419.00.
- Shown due: $38,691.50.
- Tax total across export: $0.00.
- Missing invoice numbers between INV-0002 and INV-0088: INV-0015, INV-0019, INV-0023, INV-0025, INV-0027, INV-0034, INV-0037, INV-0040, INV-0041, INV-0042, INV-0063. Determine whether each was deleted, voided, replaced or never issued.

The 61 overdue invoices are not evidence that customers owe $38,691.50. Xero has not been maintained against the bank; many are likely paid but unallocated.

## Xero bank register

Canonical extraction: `sources/xero/2026-08-24-xero-bank-register.csv`

- SHA-256: `f67a71c828fd5ce5d9736cd9aa1fd9c4701eb8822503f1bc4414eff2d60d2f1e`
- Account shown: Business Account ending 1913.
- No bank statement imported.
- Statement balance shown by Xero: $0.00.
- Balance from Xero-created entries: $8,313.11.
- 18 entries total: 12 payment entries and 6 transaction-fee entries.
- All 18 are Unreconciled.
- Entries span 10 July 2025 to 13 May 2026.

This register cannot establish bank cash or payment completeness. It is supporting evidence only.

## Required next sources

1. Complete transaction CSVs and statement closing balances for Business Account ending 1913 from 1 July 2025 through current date.
2. The same for every other bank account, card or payment account used for YesMandarin.
3. Confirmation of whether Stripe, Xero online payments, Square, PayID or another processor received customer money; export its payouts and fees if applicable.
4. Entity details and actual GST registration status.
5. Available expense receipts, supplier invoices, equipment/assets, contractor and payroll records.
6. Explanation or source history for the missing invoice numbers.

## First reconstruction pass

Once the complete bank export is available:

1. Prove each period opening balance + movements = closing balance.
2. Match deposits to invoice amounts using name/reference/date evidence; same date and amount alone are not identity.
3. Mark exact matches, candidate matches and unresolved deposits separately.
4. Explain withdrawals and processor fees.
5. Calculate rolling turnover independently of Xero invoice status.
6. Only then decide whether to repair Xero or migrate to a controlled cashbook.
