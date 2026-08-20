# Personal finances — area map

This folder is Shane's personal-finance workspace. This file is a map: detailed conventions live with the thing that owns them — read down, don't duplicate up.

## What lives where

- **`strategy.md`** — the financial strategy (mining = bridge, side biz = replacement, EV play = wealth; liquidity > yield). The *why* behind everything else here.
- **`weekly-budget/`** — the zero-based budget app (Next.js + Neon) and the transaction-ingestion tooling. **Its `AGENTS.md` is canonical for anything budget/transaction related**, including the reconcile skill and DB conventions.
- **`raw/`** — immutable archive of bank exports (`nab-YYYY-MM-DD.csv/pdf`). Append-only: the reconciler files exports here itself; never edit or delete.
- **`Transactions.csv`** (when present) — a fresh NAB export awaiting ingestion. Transient: the reconciler consumes and archives it. The reconciler also auto-discovers fresh exports in `~/Downloads`, so this file may never appear.
- **`tax-return-FY2025-26/`** — current-year tax return working docs (IP rental schedule + deductions).
- **`FINANCES-TODO.md`** — running task list.
- **`docs/`** — inert reference paper: Wilson Mining EA + pay calculator, Zip contract, Medibank quote, super insurance cover. No tooling attached.

## Conventions

- Money tasks touching the budget → start from `weekly-budget/AGENTS.md`, not here.
- New bank exports are never hand-transcribed; they flow through `weekly-budget/scripts/reconcile.ts`.
- Dates in filenames are the export/document date, ISO format (`YYYY-MM-DD`).
