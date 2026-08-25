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
- Recorded customer payments: $8,419.00.
- Recorded transaction fees: $105.89.
- Net of those entries: $8,313.11, exactly matching Xero's displayed balance.
- All 18 are Unreconciled.
- Entries span 10 July 2025 to 13 May 2026.

This register cannot establish bank cash or payment completeness. It is supporting evidence only.

## Payment flow

- Most customers paid by bank transfer.
- A minority paid by Stripe/card.
- Reconstruct bank-transfer payments from the bank source. Reconstruct card payments from Stripe charge, fee and payout evidence, then tie the net payout to the bank.
- Do not infer payment merely from Xero's invoice status or manual payment entries.

## Stripe payment exports

Canonical evidence:

- `sources/stripe/2026-08-25-xero-linked-account-unified-payments.csv`
  - SHA-256: `995ebe89b9f9d757c6819c39eabf7ce4c4ac24837804a2259d73709d098c5a19`.
  - Six paid/captured AUD charges from 2 March to 13 May 2026.
  - Gross $4,975.00; refunds $0.00; fees $105.89; net $4,869.11.
  - All six payment IDs appear in the Xero bank register.
  - All six invoice-number metadata references appear in the Xero invoice export.
  - The $105.89 fee total exactly matches Xero's six manually entered fee rows.
- `sources/stripe/2026-08-25-separate-account-unified-payments.csv`
  - SHA-256: `67e1ceecadcf07ee0f0776f0a663db797949a7f60b942b019c0e188ca8f269ff`.
  - Eight paid/captured charges, two failed attempts requiring a payment method and two cancelled attempts.
  - Seven successful charges predate 1 July 2025: gross $3,725.10; fees $119.95; net $3,605.15. Keep them outside the YesMandarin reconstruction unless other evidence establishes relevance.
  - One successful charge falls after commencement: gross $687.50; fees $22.15; net $665.35. It has no direct payment-ID, invoice-ID, customer-email or exact invoice-total match in the current Xero exports and remains unattributed.
- Non-identifying machine-readable controls: `sources/stripe/2026-08-25-control-summary.json`.
- No payment IDs overlap across the two exports.

These Unified Payments exports prove payment attempts, successful charges and charge-level fees. They are not complete Stripe cash evidence: payout and balance-transaction exports are still required to connect net Stripe activity to deposits in the bank account.

## Required next sources

1. Complete transaction CSVs and statement closing balances for Business Account ending 1913 from 1 July 2025 through current date.
2. The same for every other bank account, card or payment account used for YesMandarin.
3. Payout and balance-transaction exports from both Stripe accounts, covering 1 July 2025 through current date; include payout IDs, arrival dates, gross charges, refunds, disputes, fees and net amounts.
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
