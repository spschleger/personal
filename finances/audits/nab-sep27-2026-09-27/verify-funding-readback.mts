import { createHash } from 'node:crypto'
import { writeFileSync } from 'node:fs'
import path from 'node:path'
import { loadLocalEnvFile } from '/Users/sps/personal/finances/weekly-budget/lib/local-env.ts'
import { allCategoryAvailable } from '/Users/sps/personal/finances/weekly-budget/lib/engine/available.ts'
import { readyToAssign } from '/Users/sps/personal/finances/weekly-budget/lib/engine/ready-to-assign.ts'

const repo = '/Users/sps/personal/finances/weekly-budget'
const out = '/Users/sps/personal/finances/audits/nab-sep27-2026-09-27/funding-final-readback.json'
loadLocalEnvFile(path.join(repo, '.env.local'))

const { getCategories, getGoals, getAssignments, getTransactions } = await import('/Users/sps/personal/finances/weekly-budget/lib/db/repo.ts')
const { db } = await import('/Users/sps/personal/finances/weekly-budget/lib/db/client.ts')
const { settings } = await import('/Users/sps/personal/finances/weekly-budget/lib/db/schema.ts')
const [categories, goals, assignments, transactions, settingsRows] = await Promise.all([
  getCategories(), getGoals(), getAssignments(), getTransactions(), db.select().from(settings),
])
const week = '2026-09-24'
const available = allCategoryAvailable(week, { assignments, transactions })
const postedAvailable = allCategoryAvailable(week, { assignments, transactions: transactions.filter((transaction) => transaction.bankRef !== null) })
const balances = categories.map((category) => ({
  categoryId: category.id,
  category: category.name,
  availableCents: available.get(category.id) ?? 0,
  postedAvailableCents: postedAvailable.get(category.id) ?? 0,
}))
const savingsBeforeCents = 595247
const savingsAfterCents = available.get(19) ?? 0
const receipt = {
  generatedAt: new Date().toISOString(),
  week,
  assignments: assignments
    .filter((assignment) => assignment.weekStart === '2026-09-17' || assignment.weekStart === week)
    .sort((a, b) => a.weekStart.localeCompare(b.weekStart) || a.categoryId - b.categoryId),
  transactionCount: transactions.length,
  lastExportAt: settingsRows[0]?.lastExportAt ?? null,
  lastBudgetCycleCompletedWeek: settingsRows[0]?.lastBudgetCycleCompletedWeek ?? null,
  readyToAssignCents: readyToAssign({ assignments, transactions }),
  balances,
  allEnvelopeBalancesNonnegative: balances.every((balance) => balance.availableCents >= 0),
  allPostedEnvelopeBalancesNonnegative: balances.every((balance) => balance.postedAvailableCents >= 0),
  savings: {
    beforeCents: savingsBeforeCents,
    afterCents: savingsAfterCents,
    changeCents: savingsAfterCents - savingsBeforeCents,
  },
  preservedPaddleTransaction: transactions.find((transaction) => transaction.id === 427) ?? null,
  pendingReserveReportingOnlyCents: 163285,
  goalSnapshotSha256: createHash('sha256').update(JSON.stringify(goals)).digest('hex'),
}
writeFileSync(out, `${JSON.stringify(receipt, null, 2)}\n`)
console.log(JSON.stringify(receipt, null, 2))
