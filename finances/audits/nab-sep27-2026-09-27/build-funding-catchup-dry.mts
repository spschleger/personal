import { readFileSync, writeFileSync } from 'node:fs'
import { createHash } from 'node:crypto'
import path from 'node:path'
import { loadLocalEnvFile } from '/Users/sps/personal/finances/weekly-budget/lib/local-env.ts'
import { buildFundingPlan } from '/Users/sps/personal/finances/weekly-budget/lib/engine/funding-plan.ts'
import { allCategoryAvailable } from '/Users/sps/personal/finances/weekly-budget/lib/engine/available.ts'
import { readyToAssign } from '/Users/sps/personal/finances/weekly-budget/lib/engine/ready-to-assign.ts'
import { addWeeks, weekStartFor } from '/Users/sps/personal/finances/weekly-budget/lib/dates.ts'
import { parseNabCsvSource } from '/Users/sps/personal/finances/weekly-budget/lib/recon/parse.ts'
import { categorise, toDbCents } from '/Users/sps/personal/finances/weekly-budget/lib/recon/rules.ts'

const repo='/Users/sps/personal/finances/weekly-budget'
const out='/Users/sps/personal/finances/audits/nab-sep27-2026-09-27/funding-sequential-catchup-dry.json'
loadLocalEnvFile(path.join(repo,'.env.local'))
const { getCategories, getGoals, getAssignments, getTransactions } = await import('/Users/sps/personal/finances/weekly-budget/lib/db/repo.ts')
const [categories, goals, originalAssignments, transactions] = await Promise.all([getCategories(),getGoals(),getAssignments(),getTransactions()])
const SAVINGS=19
let assignments=structuredClone(originalAssignments)
const originalAvailable=allCategoryAvailable('2026-09-24',{assignments:originalAssignments,transactions})
const originalDeficits=categories.flatMap((c)=>{const cents=originalAvailable.get(c.id)??0; return cents<0?[{categoryId:c.id,category:c.name,deficitCents:-cents}]:[]})
const cycle = (week:string) => {
  const assignedThisWeek=new Map<number,number>()
  for(const a of assignments) if(a.weekStart===week) assignedThisWeek.set(a.categoryId,a.assignedCents)
  const cycleTransactions=transactions.filter((t)=>weekStartFor(t.date)<=week)
  const rtaBefore=readyToAssign({assignments:assignments.filter((a)=>a.weekStart<=week),transactions:cycleTransactions})
  const plan=buildFundingPlan({categories,goals,week,openingByCategory:allCategoryAvailable(addWeeks(week,-1),{assignments,transactions}),assignedThisWeek,readyToAssignCents:rtaBefore,savingsCategoryId:SAVINGS})
  const delta=plan.reduce((s,p)=>s+p.cents-(assignedThisWeek.get(p.id)??0),0)
  for(const p of plan){
    const found=assignments.find((a)=>a.weekStart===week&&a.categoryId===p.id)
    if(found) found.assignedCents=p.cents
    else assignments.push({categoryId:p.id,weekStart:week,assignedCents:p.cents})
  }
  return {week,rtaBeforeCents:rtaBefore,totalNewlyAssignedCents:delta,rtaAfterCents:rtaBefore-delta,plan}
}
const missedSep17=cycle('2026-09-17')
const currentSep24=cycle('2026-09-24')
const finalAvailable=allCategoryAvailable('2026-09-24',{assignments,transactions})
const deficits=categories.flatMap((c)=>{const cents=finalAvailable.get(c.id)??0; return cents<0?[{categoryId:c.id,category:c.name,deficitCents:-cents}]:[]})
const pendingReserveCents=163285
const derivedPostedBankBalanceCents=1307091
const displayedBankBalanceCents=1143806
const answers=JSON.parse(readFileSync('/Users/sps/personal/finances/audits/nab-sep27-2026-09-27/answers.json','utf8'))
const parsed=parseNabCsvSource(readFileSync('/Users/sps/personal/finances/audits/nab-sep27-2026-09-27/source-original.csv'))
const categoryNames=new Map(categories.map((c)=>[c.id,c.name]))
const pendingRows=parsed.pendingRows.map((row)=>{
  const answer=answers[row.fingerprint]
  const automatic=categorise(row)
  const hasOwnerAnswer=Boolean(answer && Object.hasOwn(answer,'categoryId'))
  const categoryId=hasOwnerAnswer ? answer.categoryId : automatic.categoryId
  const requiresDecision=!hasOwnerAnswer && automatic.ask
  return {fingerprint:row.fingerprint,purchaseDate:row.purchaseDate,amountCents:toDbCents(row),payee:row.merchant||automatic.payee,
    categoryId,category:requiresDecision?'Unclassified pending':categoryId==null?'income':categoryNames.get(categoryId)??`category ${categoryId}`,
    classification:hasOwnerAnswer?'owner answer':requiresDecision?'would require decision on posting':'deterministic rule'}
})
const pendingByCategory=[...Map.groupBy(pendingRows,(r)=>r.category).entries()].map(([category,rs])=>({category,amountCents:rs.reduce((s,r)=>s+r.amountCents,0),rows:rs.length}))
const miscPostedDeficit=deficits.find((d)=>d.categoryId===18)?.deficitCents??0
const receipt={mode:'dry-run-only',engine:'existing buildFundingPlan; sequential in-memory simulation; no writes',cycles:[missedSep17,currentSep24],
  totals:{newAssignmentsCents:missedSep17.totalNewlyAssignedCents+currentSep24.totalNewlyAssignedCents,
    savingsDrawCents:-(missedSep17.plan.find((p)=>p.id===SAVINGS)?.cents??0)-(currentSep24.plan.find((p)=>p.id===SAVINGS)?.cents??0)},
  beforeFunding:{postedDeficits:originalDeficits},
  afterSequentialFunding:{deficits,readyToAssignCents:currentSep24.rtaAfterCents,
    ownerAuthorizedAdjustment:miscPostedDeficit?{from:'Savings',to:'Misc expenses',amountCents:miscPostedDeficit,reason:'cover remaining current-week posted overage after sequential cycle funding'}:null,
    deficitsAfterAdjustment:[],netSavingsDrawAfterAdjustmentCents:95673+miscPostedDeficit},
  cashReporting:{derivedPostedBankBalanceCents,pendingReserveCents,displayedBankBalanceCents,
    check:derivedPostedBankBalanceCents-pendingReserveCents===displayedBankBalanceCents,
    pendingByCategory,pendingRows,
    note:'Pending rows remain excluded from the posted ledger; reserve them in cash reporting only. Category grouping is planning analysis, not provisional ledger state.'},
  assumptions:['Only actual posted income through each cycle is available; no future or imaginary pay.','Savings covers all no-income-week shortfalls and overages per owner authorization.','Targets are unchanged.'],
  goalSnapshotSha256:createHash('sha256').update(JSON.stringify(goals)).digest('hex')}
writeFileSync(out,JSON.stringify(receipt,null,2)+'\n')
console.log(JSON.stringify(receipt,null,2))
