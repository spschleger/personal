# NAB CSV reconciliation audit — 2026-09-27

## Posted ingestion

- Source SHA-256: `7297f4f3778cb3ee07a0a305f46f6f3d342075abc19be0781a309a1bddf251cc`
- Account: `946410617`
- Reviewed digest: `0f75cc0183f4d0a57f0485e14aa34fd7e9d6774cc29ad404a8724de04c476adb`
- Applied: 120 inserts, 9 settles, 4 claims; 35 already ingested and 21 historical-overlap rows.
- Watermark advanced from `2026-09-10` to `2026-09-25`.
- Archive: `../raw/nab-2026-09-25.csv`, byte-identical to `source-original.csv`.
- Readback: all 189 posted source rows accounted for; 168 reconciled identities/aliases and 21 historical overlaps; unique fingerprints, aliases, and transaction IDs.
- Duplicate dry rerun from `source-original.csv`: 168 already ingested, 21 historical overlap, 0 settles, 0 claims, 0 inserts, 0 decisions.
- A first duplicate attempt supplied the now-stale answers and correctly failed closed (`Answer is outside the exact reviewed unresolved set`); the successful duplicate check omitted stale answers.
- Existing reconciled transaction `db#427` ($1 Paddle.net) was preserved. It remains a known historical source gap; no bank-equality claim is made.

## Pending cash reserve

The 24 pending rows were excluded from the posted ledger and total **$1,632.85**. Posted-derived bank cash is $13,070.91; reserving pending spending gives displayed/useful cash of **$11,438.06**. This is cash reporting only, not provisional ledger state.

## Funding applied

The reviewed sequential plan was applied through the deterministic CLI using explicit Thursday weeks:

- 2026-09-17: actual income/RTA $2,596.73; assignments $2,596.73; Savings received $338.26.
- 2026-09-24: actual income/RTA $1,109.61; assignments $1,109.61; Savings contributed $1,294.99 as the balancing assignment.
- Then $35.00 moved from Savings to Misc to cover the remaining posted Jetstar overage.
- Savings available moved from $5,952.47 to $4,960.74: net draw **$991.73**.
- Final readback: RTA $0; budget marker `2026-09-24`; transaction count unchanged at 550; all posted and actual envelope balances nonnegative; goals hash unchanged.
- The $1 Paddle.net row `db#427` remains preserved. The $1,632.85 pending reserve remains cash reporting only and is not assigned in the ledger.

Dry runs, apply output, move receipt, and exact final readback are in this directory (`fund-week-sep17-*`, `fund-week-sep24-*`, `savings-to-misc-sep24-move.json`, and `funding-final-readback.json`).
