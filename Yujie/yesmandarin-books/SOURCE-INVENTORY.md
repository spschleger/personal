# YesMandarin books — source inventory

**Observed:** 24–25 August 2026

## Current conclusion

Xero is not yet complete books. The full supplied account `1913` statement range is imported and 79 of 253 lines are reconciled: 49 source-supported invoice-related receipts, nine Digital Pacific expenses and 21 Microsoft-related lines. The opening balance is posted. Six Microsoft lines, other expenses, transfers, Stripe-clearing items and ambiguous receipts remain unresolved. At the 1 September 2026 checkpoint Xero showed statement balance $31,016.85 and book balance $37,737.94, a $6,721.09 difference.

Use Xero as a historical invoice source during reconstruction. Treat complete bank statements as the cash source of truth. Xero will become the canonical books only after the source-backed reconstruction is verified.

## Xero organisation

- Organisation: YesMandarin.
- Xero organisation created 1 July 2025.
- Current plan: Ignite, AUD $37/month including GST.
- Cancellation is already scheduled for 12 September 2026.
- Financial year end: 30 June.
- GST accounting method: None.
- Xero Activity Statements are not set up.
- ABN Lookup verified on 26 August 2026 that ABN `63 198 083 103` is active, the entity is `CAO, YUJIE` (Individual/Sole Trader), the business name `YESMANDARIN` has been registered since 14 April 2025, and the entity is **not currently registered for GST**. Source: <https://abr.business.gov.au/ABN/View?abn=63198083103>.
- Expense reconstruction therefore uses Xero tax rate `BAS Excluded`; no GST or input-tax-credit amount is claimed.

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

## CBA Business Account ending `1913`

Canonical source exports and controls are under `sources/bank/`:

- `2025-07-01-to-2025-12-09-cba-business-account-1913.csv` — 54 rows; SHA-256 `94201191adaff86694395ddbe0eebd5f8cb8a844ee0318dd0df25cdbb5c19fcd`.
- `2025-12-09-to-2026-08-17-cba-business-account-1913.csv` — 200 rows; SHA-256 `35af754a3b78c9bb127807ec7b216d6a91fa42fc2e685a7cb21d3abd6264fbb0`.
- The exports overlap on one exact 9 December 2025 Microsoft debit. Removing that duplicate leaves 253 statement lines from 1 July 2025 through 17 August 2026.
- The source balance chain has no continuity breaks: opening balance $3,262.83 plus net movement $27,754.02 equals the 17 August 2026 closing balance of $31,016.85.
- Total credits are $44,572.45 and total debits are $16,818.43.
- Native Xero import file: `2025-07-01-to-2026-08-17-xero-bank-import.csv`; SHA-256 `a2170d4dbdb5bddb85379b3da2549825f944e4cb528e3e921fc23345655539a3`.
- Machine-readable controls: `2026-08-25-control-summary.json`. Rebuild with `scripts/prepare_cba_bank_import.py`.
- Native Xero import completed 25 August 2026: Xero reported 253 statement lines imported and zero duplicates. The reconciliation queue then showed 253 lines.
- Xero's post-import statement balance was $27,754.02, equal to imported net movement. Shane confirmed on 26 August 2026 that the $3,262.83 source opening balance was founder-contributed starting capital. It remains to be posted against capital introduced / owner's equity—not income—before the statement balance can agree to the $31,016.85 source closing balance. Treatment record: `workpapers/2026-08-26-opening-balance-treatment.json`.
- On 25 August 2026, 29 single-invoice candidates in the controlled worklist were reconciled individually, totalling $18,526.00. Each searched statement line disappeared and the queue fell exactly from 253 to 224; Xero then showed a $25,775.11 book balance.
- On 26 August 2026, the controlled review added 17 further single-invoice reconciliations totalling $10,342.00. Each searched line again disappeared and the queue fell exactly from 224 to 207. Cumulative invoice-payment reconciliations are 46 lines totalling $28,868.00. Xero then showed a $33,737.11 book balance against the unchanged $27,754.02 imported statement movement.
- Later on 26 August 2026, the $333 and $332 Jack Anderson receipts were each allocated as part payments to INV-0047. Together they settled the $665 invoice exactly; both searched lines disappeared and the queue fell from 207 to 205. Cumulative invoice-payment reconciliations are 48 lines totalling $29,533.00.
- The $449 M Janda receipt was then allocated as $448 to INV-0017 plus a $1 minor adjustment. The searched line disappeared and the queue fell from 205 to 204. Cumulative invoice-related receipt reconciliations are 49 lines totalling $29,982.00.
- The later $650 Daniel Lie row could not reuse INV-0066 after the explicitly referenced 13 May row consumed it. Shane confirmed on 3 September 2026 that the later receipt was a Term 3 Mandarin tuition sale agreed verbally. It was reconciled directly to `200 - Sales`, `BAS Excluded`, and visibly verified without creating a retrospective invoice. The audit is `workpapers/2026-08-26-unresolved-invoice-analysis.json`.

These postings do not enter the decided opening-capital balance or resolve the remaining transaction classifications.

This proves the transaction sequence and balances for the supplied export range. It does not by itself categorise withdrawals or prove which deposits settle which invoices.

## Payment flow

- Most customers paid by bank transfer.
- A minority paid by Stripe/card.
- Reconstruct bank-transfer payments from the bank source. Reconstruct card payments from Stripe charge, fee and payout evidence, then tie the net payout to the bank.
- Do not infer payment merely from Xero's invoice status or manual payment entries.

## Stripe source evidence

Canonical evidence and non-identifying controls are listed in `sources/stripe/2026-08-25-control-summary.json`.

### Xero-linked Stripe account

- Payment attempts: `sources/stripe/2026-08-25-xero-linked-account-unified-payments.csv`.
- Payouts: `sources/stripe/2026-08-25-xero-linked-account-payouts.csv`.
- Balance transactions: `sources/stripe/2026-08-25-xero-linked-account-balance-transactions.csv`.
- Six paid/captured charges from 2 March to 13 May 2026: gross $4,975.00; processing fees $105.89; net $4,869.11.
- Six paid payouts total $4,869.11. All went to bank account ending `9316`.
- All six payment IDs appear in Xero's bank register, all six invoice metadata references appear in Xero's invoice export, and all six payout balance-transaction references resolve in the Stripe balance ledger.
- Charge net $4,869.11 less payouts $4,869.11 leaves zero Stripe movement. The $105.89 processing-fee total exactly matches Xero's six manually entered fee rows.
- Posted and freshly verified in Xero on 2 September 2026: the six invoice receipts, six processing fees and six payouts are in `Stripe Clearing`; the payouts to Felicity's personal account ending `9316` are allocated to `880 - Owner A Drawings`; the clearing balance is $0.00. Audit: `workpapers/2026-09-02-xero-stripe-clearing-reconstruction.json`.

### Non-Xero-linked Stripe account

The two Stripe accounts are available under the same Stripe login/account switcher. Stripe labels them `YesMandarin (Xero)` and `YesMandarin`. The exact underlying organisational relationship is not established by the exports, so keep their IDs, balances and payout chains account-scoped. Shane confirmed on 25 August 2026 that destination bank account ending `9316` is Felicity's personal account.

- Payment attempts: `sources/stripe/2026-08-25-separate-account-unified-payments.csv`.
- Raw full-history payouts: `sources/stripe/2026-08-25-separate-account-payouts-full-history.csv`.
- Raw full-history balance transactions: `sources/stripe/2026-08-25-separate-account-balance-transactions-full-history.csv`.
- Deterministic reconstruction-period extracts:
  - `sources/stripe/2026-08-25-separate-account-payouts-2025-07-01-to-2026-08-25.csv` — two rows.
  - `sources/stripe/2026-08-25-separate-account-balance-transactions-2025-07-01-to-2026-08-25.csv` — four rows.
- The full ledger has 23 rows and reconciles internally to zero: charges/payments $4,412.60 less $156.33 processing fees and $19.42 Stripe service fees equals $4,236.85 of payouts.
- The payment-only export's `Fee` column excludes GST; the balance ledger's fee and net fields are authoritative. The earlier $22.15 post-commencement fee becomes $24.37 including GST.
- Reconstruction-period bridge:
  - an opening Stripe balance of $1,197.73 was paid to bank account ending `9316` at the period boundary;
  - one later charge grossed $687.50, incurred $24.37 processing fee and $3.03 invoicing fee, and produced a $660.10 payout to bank account ending `1913`;
  - that later charge still has no direct Xero payment-ID, invoice-ID, customer-email or exact invoice-total match and remains unattributed.
- All four full-history payout balance-transaction references resolve in Stripe. No payment IDs overlap between the two Stripe accounts.

### Consequence

Stripe evidence is complete for the Xero-linked chain, which is posted and closed to zero. The separate account remains account-scoped. On 3 September 2026 its source-matched $660.10 payout to business account `1913` was reconciled to the distinct current-asset account `092 - Stripe Clearing - Separate`; this leaves a controlled $660.10 credit balance and does not recognise revenue. The upstream $687.50 charge, $24.37 processing fee and $3.03 invoicing fee remain unposted pending attribution. The $1,197.73 opening-boundary payout to personal account `9316` remains isolated and outside current-period income.

## Required next sources

1. Treatment evidence for the separate Stripe account's unattributed $687.50 charge and the $1,197.73 opening-boundary balance. Do not classify either payout as revenue.
2. Any transaction evidence after 17 August 2026 for Business Account ending `1913` when it becomes available.
3. The same for every other bank account, card or payment account used for YesMandarin.
4. Entity details and actual GST registration status.
5. Available expense receipts, supplier invoices, equipment/assets, contractor and payroll records.
6. Explanation or source history for the missing invoice numbers.

## First reconstruction pass

Account `1913` deterministic workpapers were generated on 25 August 2026:

- `workpapers/2026-08-25-account-1913-reconciliation-worklist.csv`
- `workpapers/2026-08-25-account-1913-reconciliation-summary.json`
- `workpapers/2026-08-25-xero-invoice-reconciliation-result.json` — posted-result audit record for the 29 verified Xero invoice reconciliations.
- `workpapers/2026-08-26-unresolved-invoice-analysis.json` — follow-up evidence for the remaining invoice exceptions and the verified posting of Jack Anderson's two-part settlement of INV-0047.
- `workpapers/2026-08-26-opening-balance-treatment.json` — owner-confirmed treatment of the $3,262.83 opening bank balance as capital introduced / owner's equity, not income; the Xero conversion-balance posting is verified.
- Rebuild with `scripts/prepare_1913_reconciliation_worklist.py`; matching behaviour is covered by `tests/test_prepare_1913_reconciliation_worklist.py`.
- The 253-row control totals remain exact: $44,572.45 credits, $16,818.43 debits and $27,754.02 net movement.
- All 29 statement lines with one invoice candidate supported by an explicit invoice reference or payer-name evidence plus amount and date bounds were reconciled in Xero on 25 August 2026. Another 20 invoice-payment lines remain review items; 25 credits have no defensible invoice candidate.
- Expense proposals are worklist aids, not tax conclusions: 67 are straightforward merchant/reference candidates, 97 require business-use or account review, and nine debits remain unresolved.
- The `9316` transfer stays blocked until the other side is supplied. The $660.10 Stripe payout is isolated to Stripe clearing rather than revenue, and Shane's $309.55 reimbursement is isolated from invoice income.

Once the complete bank export is available:

1. Prove each period opening balance + movements = closing balance.
2. Match deposits to invoice amounts using name/reference/date evidence; same date and amount alone are not identity.
3. Mark exact matches, candidate matches and unresolved deposits separately.
4. Explain withdrawals and processor fees.
5. Calculate rolling turnover independently of Xero invoice status.
6. Repair and reconcile Xero from the verified reconstruction; do not maintain a parallel custom ledger.
