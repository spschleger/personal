# NAB reconciliation and funding preview — 2026-10-22

## Source authority

- Account: `946410617`
- Archived source: `finances/raw/nab-2026-10-21.csv`
- SHA-256: `5eaed160e2e537a5db880636288363554fa3533045d4ffcb1fcd4d35dc85637d`
- Source rows: 252 total; 241 posted; 11 pending.
- Running-balance errors: 0.
- Displayed balance: $8,777.86; derived posted balance: $6,740.18; pending net: +$2,037.68.
- The raw CSV and reconciler fingerprint for the $68.61 Amazon row contain the exact source value `+618662161072`; tool displays redact it as `+618****1072`. The answers key, provisional note, and provenance manifest were validated byte-for-byte against the parser fingerprint rather than copied from the redacted display.

## Posted apply

- Reviewed digest: `7798a51faa6017f2f698762825a2d095f62132db881b5988e0da5f8e6bc1a973`.
- Applied: 13 exact claims (ledger IDs 716–728), 37 inserts, 0 settles, 0 unresolved decisions.
- Watermark advanced from 2026-10-14 to 2026-10-21.
- Post-apply duplicate dry run: 241 already ingested, 0 claims, 0 settles, 0 inserts, 0 decisions.
- Transaction 427 remains a reconciled $1.00 Paddle.net expense in Misc; no plug was added.

## Pending representation

- Added 10 pending expenses totalling $524.17 as provisional bank-scope transactions, IDs 766–775.
- Added the owner-confirmed available salary of $2,561.85 once as provisional bank-scope income, ID 776.
- All 11 rows have `bank_ref = NULL`; each note records the exact source fingerprint, account, SHA-256, and claim-on-settlement instruction.
- Durable row-to-ledger provenance: `weekly-budget/docs/provisional-provenance/nab-2026-10-21-pending.json`.

## Funding dry preview — week 2026-10-22

- Income / Ready to Assign: $2,561.85.
- Positive envelope requirements: $3,376.43.
- Savings balancing requirement: -$814.58.
- Result if later applied unchanged: Ready to Assign $0.00.
- Actual carried deficits entering the week: Misc $1,275.07; Eating out $177.41; Rent/Food/Gym/Bills/Savings $150.00; Fuel $16.43.
- Largest assignments: Misc $1,275.07; Rent/Food/Gym/Bills/Savings $850.00; Eating out $277.41; Orthodontics/Surgery $230.00; Fuel $216.43.
- This is dry only. No 2026-10-22 funding assignments were applied, and no goals changed.
- The prior 2026-10-15 funding was not rerun. Its authorised 34,155-cent Fuel-to-Savings release and $2,057.75 Savings baseline were not rewritten.
