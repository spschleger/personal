import { readFileSync, writeFileSync } from 'node:fs'
import path from 'node:path'
import { neon } from '/Users/sps/personal/finances/weekly-budget/node_modules/@neondatabase/serverless/index.mjs'
import { loadLocalEnvFile } from '/Users/sps/personal/finances/weekly-budget/lib/local-env.ts'

const repo = '/Users/sps/personal/finances/weekly-budget'
const base = '/Users/sps/personal/finances/audits/nab-sep27-2026-09-27'
loadLocalEnvFile(path.join(repo, '.env.local'))
if (!process.env.DATABASE_URL) throw new Error('DATABASE_URL not found')
const sql = neon(process.env.DATABASE_URL)
const review = JSON.parse(readFileSync(path.join(base, 'review-pre-apply.json'), 'utf8'))
const dry = readFileSync(path.join(base, 'reconcile-dry-pre-apply.txt'), 'utf8')
const settleIds = new Set([...dry.matchAll(/^SETTLE db#(\d+)/gm)].map((m) => Number(m[1])))
const claimIds = new Set([...dry.matchAll(/^CLAIM  db#(\d+)/gm)].map((m) => Number(m[1])))
const facts = review.snapshot.sourceFacts
const refs = facts.map((f: {fingerprint: string}) => f.fingerprint)
const identities = await sql`SELECT canonical_ref, post_date::text, purchase_date::text, amount_cents, description, disposition, transaction_id, reason FROM bank_identities WHERE canonical_ref = ANY(${refs})`
const aliases = await sql`SELECT alias_ref, canonical_ref, provider, account_ref, post_date::text, purchase_date::text, amount_cents, description FROM bank_identity_aliases WHERE alias_ref = ANY(${refs})`
const canonicalRefs = [...new Set([...identities.map((x) => String(x.canonical_ref)), ...aliases.map((x) => String(x.canonical_ref))])]
const allIdentities = await sql`SELECT canonical_ref, post_date::text, purchase_date::text, amount_cents, description, disposition, transaction_id, reason FROM bank_identities WHERE canonical_ref = ANY(${canonicalRefs})`
const directTxns = await sql`SELECT id, date::text, payee, amount_cents, category_id, note, bank_ref, reconciliation_scope, tags FROM transactions WHERE bank_ref = ANY(${refs})`
const ids = [...new Set([...allIdentities.flatMap((x) => x.transaction_id == null ? [] : [Number(x.transaction_id)]), ...directTxns.map((x) => Number(x.id))])]
const txns = await sql`SELECT id, date::text, payee, amount_cents, category_id, note, bank_ref, reconciliation_scope, tags FROM transactions WHERE id = ANY(${ids})`
const byAlias = new Map(aliases.map((x) => [String(x.alias_ref), x]))
const byCanonical = new Map(allIdentities.map((x) => [String(x.canonical_ref), x]))
const byTxn = new Map(txns.map((x) => [Number(x.id), x]))
const byDirectRef = new Map(directTxns.map((x) => [String(x.bank_ref), x]))
const rows = facts.map((fact: {fingerprint: string, postDate: string, purchaseDate: string, amountCents: number, description: string}) => {
  const alias = byAlias.get(fact.fingerprint)
  const canonicalRef = alias ? String(alias.canonical_ref) : fact.fingerprint
  const identity = byCanonical.get(canonicalRef)
  const direct = byDirectRef.get(fact.fingerprint)
  const transactionId = identity?.transaction_id != null ? Number(identity.transaction_id) : direct?.id != null ? Number(direct.id) : null
  const transaction = transactionId == null ? null : byTxn.get(transactionId)
  const kind = transactionId != null && fact.postDate <= review.snapshot.watermark ? 'already'
    : transactionId != null && settleIds.has(transactionId) ? 'settle'
    : transactionId != null && claimIds.has(transactionId) ? 'claim'
    : alias ? 'insert' : 'already'
  return { source: fact, kind, alias: alias ?? null, identity: identity ?? null, transaction: transaction ?? null,
    status: transaction?.bank_ref ? 'reconciled' : fact.postDate <= review.snapshot.watermark ? 'historical-overlap-ignored' : 'ERROR' }
})
for (const row of rows) if (row.status === 'historical-overlap-ignored') row.kind = 'historical-overlap'
const counts = Object.fromEntries(['already','settle','claim','insert','historical-overlap'].map((kind) => [kind, rows.filter((x) => x.kind === kind).length]))
const watermark = await sql`SELECT last_export_at::text, last_budget_cycle_completed_week::text FROM settings WHERE id=1`
const duplicateTransactionIds = [...new Set(rows.map((x) => x.transaction?.id).filter((id, i, a) => id != null && a.indexOf(id) !== i))]
const receipt = { generatedAt: new Date().toISOString(), selectedAccount: '946410617', reviewDigest: review.digest,
  summary: { sourceRows: rows.length, counts, allExpectedRowsAccountedFor: rows.every((x) => x.status === 'reconciled' || x.status === 'historical-overlap-ignored'),
    sourceFingerprintsUnique: new Set(rows.map((x) => x.source.fingerprint)).size === rows.length,
    transactionIdsUnique: duplicateTransactionIds.length === 0, duplicateTransactionIds,
    aliasRows: rows.filter((x) => x.alias).length, aliasRefsUnique: new Set(rows.flatMap((x) => x.alias ? [x.alias.alias_ref] : [])).size === rows.filter((x) => x.alias).length,
    watermark: watermark[0] }, rows }
writeFileSync(path.join(base, 'ledger-readback-exact.json'), JSON.stringify(receipt, null, 2) + '\n')
console.log(JSON.stringify(receipt.summary, null, 2))
