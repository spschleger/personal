# Low-dose hCG on TRT — E2 bump + PK/steady-state for draw timing

**Compiled:** 2026-07-13 · deep-research review (adversarially verified) · companion to `e2-lowering-options-research.md`, `hct-oxygen-thrombosis-research.md`, `current-plan.md`
**Question (Shane):** Adding **100 IU/day SubQ hCG** on top of established, dialed-in TRT (free T ~1034, E2 ~207 pmol/L, Hct 0.51, LH/FSH fully suppressed). (1) Expected E2 bump? (2) hCG half-life / steady state → earliest meaningful blood draw?

---

## BOTTOM LINE

1. **E2 bump — expect a real but modest rise; the exact number for *your* scenario has never been measured.** No study reports serum E2 on ~100 IU/day hCG added to *established* TRT. Mechanism is certain (hCG restarts intratesticular testosterone → local aromatase → E2 that a systemic AI can't fully reach), and the dose-response backbone says 100 IU/day meaningfully reactivates the testis. Best-grounded **inference: ~10–30% over your TRT-only E2** (so ballpark ~207 → ~230–270 pmol/L), with **very wide individual variance** — could be less, could be substantially more. This is an estimate, not a measured value.
2. **Draw timing — day ~10–14 of consistent daily dosing.** Serum hCG reaches steady state at ~**6–8 days** (daily SC); the downstream testicular T/E2 response **lags** the drug. Draw at **~2 weeks**, at a **consistent time ~24h after the prior injection** (trough-ish), fasted AM to match your other draws. Bundle **Hct + E2 + free T + SHBG**. A draw before ~day 7 undersamples (hCG still accumulating) and will mislead.

---

## QUESTION 1 — the E2 bump

### The honest gap
There is **no direct measurement** of serum E2 from ~100 IU/day hCG added to established TRT. Everyone asking this question is inferring from adjacent data. So the number is an estimate built from mechanism + dose-response, not a trial result. *(Confidence: this gap itself is high-confidence — the search found no such study.)*

### What the mechanism guarantees (high confidence)
- On TRT, LH/FSH are suppressed and the testis is quiescent. hCG is an **LH analog** → directly stimulates Leydig cells → restores **intratesticular testosterone (ITT)** → the testis's own **aromatase (located in Leydig cells)** converts it locally to E2. *(JCEM 2021, dgaa860; PNAS 1979 PMC411596 — hCG acutely stimulated Leydig aromatization 8-fold in 4h, even at saturating T.)*
- Intratesticular E2 runs **~2,779 pg/mL, ~81× serum**; ITT ~50–100× serum. *(Shiraishi/JCEM 2021, dgaa860.)* This is why the E2 hCG adds is **partly out of reach of a systemic AI** — it's made inside the testis. **→ if E2 sides appear, the lever is hCG dose-down, not adding an AI.** (Confirms your existing Dave-Lee note.)

### The dose-response backbone (high confidence, but measures ITT not serum E2)
- **Coviello 2005 (JCEM 90(5):2595):** 29 men on 200 mg TE/wk (TRT-like suppression) + hCG **125/250/500 IU every-other-day**, 3 wks. ITT vs baseline: placebo **−94%**, 125 IU **−25%**, 250 IU **−7%**, 500 IU **+26%**; linear with dose (P<0.001).
- **Roth 2010 (JCEM 95(8), PMC2913032):** gonadotropin-suppressed men, hCG **0/15/60/125 IU EOD**. ITT dose-dependent: **77 → 136 → 319 → 987 nmol/L**. Even 15 IU EOD moved it — the low end is **steep**, not flat.

**Dose-framing correction (this refutes the common "100 IU/day is a tiny sub-125 dose" claim):** 125 IU **EOD** ≈ 62.5 IU/day ≈ 438 IU/wk. **100 IU/day = 700 IU/wk.** So your dose sits **between the 125-EOD and 250-EOD Coviello arms** on weekly exposure — i.e. it lands ITT somewhere around **−10 to −15% of the natural pre-TRT baseline**, which is *substantial* testicular reactivation, not a token. More substrate for local aromatization than "microdose" framing implies. *(The literature's "response plateaus with repeated dosing" finding — Trinchard-Lugan 2002 — was refuted as applicable here: that plateau is Leydig **saturation at a ~3,250 IU dose**, 30× yours; at 100 IU/day you're on the rising part of the curve.)*

### The one on-TRT E2 data point — and why it's weak
- **Hsieh 2013 (J Urol, PMID 23260550):** 26 hypogonadal men, TRT + **500 IU IM EOD**. Reported E2 **2.2 → 3.7 pg/mL**. **Do not lean on this:** (a) the "before" was the *untreated* baseline, not established TRT, so it can't isolate hCG's marginal effect; (b) absolute values 2.2/3.7 pg/mL are **implausibly low** for adult male serum (normal ~20–40) — an assay anomaly; (c) 2.2→3.7 is a **~68% *relative*** rise (not "small"), but underpowered (p=0.11). **Direction (E2 up) is consistent; magnitude is unusable.**
- **Diagnostic-stim data (Wang 2005, PMID 16285473):** single hCG dose → E2 **+168% at 24h**. **Not applicable** — big diagnostic dose in low-baseline-E2 hypogonadal men (low baseline inflates the %). Useful only for *kinetics* (see Q2), not magnitude.

### Net for Q1
A real, modest incremental E2 rise on top of your already-high TRT E2, best-estimated at **~10–30%**, **highly individual** (Roth's 60 IU group spanned an IQR of 139–2,455 — Leydig responsiveness varies enormously). You tolerate ~207 asymptomatically, so this is a **watch, not a blocker** — and the right response to any E2 symptom is pulling hCG dose, not stacking an AI.

---

## QUESTION 2 — PK, steady state, draw timing

### hCG half-life (SubQ, relevant forms)
- **Recombinant (Ovidrel/choriogonadotropin alfa) FDA label:** terminal t½ **29 ± 6 h** SC; biphasic (distribution t½ ~4.5 h, terminal ~26.5 h IV). Tmax 12–24 h.
- **Highly-purified urinary hCG (Pregnyl/Choriomon-type — what's usually microdosed on TRT):** terminal t½ **~37–39 h** SC. *(PMC8930902.)*
- **SC vs IM:** SC delays peak and prolongs half-life vs IM, but **steroidogenic (T/LH/FSH) response is identical** — SC is as effective. *(Saal 1991, Fertil Steril.)*
- **Working number: terminal t½ ~30–37 h.** *(The "42–47h in men" figure floating around was refuted — it's from CG beta, a novel long-acting experimental variant you wouldn't use; standard hCG is ~29–37h.)*

### Steady state of serum hCG
- Daily SC dosing → **steady state ~6–8 days** (directly measured for a long-acting variant at 6–7/7–8 days; standard hCG likely ~5–7 days). Half-life math agrees: ~30–37 h × ~5 half-lives ≈ 6–8 days. Multi-dose **accumulation ~1.7×**. *(PMC8301557; Trinchard-Lugan 2002.)*

### The lag that matters — testicular response trails the drug
- After a dose, serum **T peaks at ~72–96 h**; **E2 peaks earlier, ~24 h** (E2 kinetics are faster than T). *(Choi/PMC8301557; Wang PMID 16285473.)*
- So even once serum hCG is at steady state (~day 7), the **Leydig steroidogenic output needs a few more days to plateau**. → the honest "this is my hCG effect" window is **~day 10–14**.

### Concrete draw protocol
- **Earliest meaningful draw: day ~10–14** of uninterrupted daily 100 IU. (Day 3–5 would catch a rising, not-yet-plateaued picture and under-read the effect.)
- **Time of day:** consistent, **~24 h after the previous injection** (trough-ish, mirrors your TRT-trough logic). With daily dosing + ~30 h half-life the peak–trough swing is smoothed by accumulation, so *consistency* matters more than chasing peak vs trough. Fasted AM to line up with your other panels.
- **Panel:** **Hct** (the safety gate — hCG adds erythropoietic drive on top of TRT; you start at 0.51), **E2**, **free T**, **SHBG**. Compare against your pre-hCG baseline (draw that baseline *before* the first injection).

---

## Evidence grading (as requested)
- **High / primary clinical:** the aromatization mechanism, ITT dose-response (Coviello 2005, Roth 2010), hCG PK/half-life (FDA labels, PMC8930902/8301557), the T-72–96h / E2-24h lag, SC≈IM steroidogenesis.
- **Weak / not usable for magnitude:** Hsieh 2013 on-TRT E2 numbers (assay anomaly + wrong comparison); stim-test 168% (wrong dose/population).
- **Inference (clearly flagged):** the ~10–30% serum-E2 estimate for 100 IU/day-on-TRT — no direct data exists; it's mechanism + dose-position + clinician/community consensus that "E2 climbs when hCG is added, sometimes enough to notice."
- **Anecdotal/community:** TRT-clinic and forum sources consistently report E2 rising on hCG-added-to-TRT and note systemic AIs blunt it incompletely — directionally consistent with the mechanism, not quantified.

## Key sources
- Coviello 2005, JCEM 90(5):2595 — ITT dose-response on TRT (125/250/500 IU EOD)
- Roth 2010, JCEM 95(8), PMC2913032 / PMID 20484472 — very-low-dose ITT (15/60/125 IU EOD)
- Hsieh 2013, J Urol, PMID 23260550 — hCG 500 IU EOD on TRT (E2 data weak)
- Wang/Kalicinski 2005, PMID 16285473 — E2 peaks 24h, T 72h post-hCG
- Shiraishi 2021, JCEM dgaa860 — intratesticular E2/T, Leydig aromatase
- PNAS 1979, PMC411596 — hCG acutely stimulates Leydig aromatization
- FDA Ovidrel label (DailyMed) — SC t½ 29±6h, biphasic
- PMC8930902 — SC urinary/recombinant hCG t½ ~37–39h
- PMC8301557 — daily SC steady state 6–8 days; T Tmax 72–96h
- Saal 1991, Fertil Steril — SC vs IM: PK differs, steroidogenesis identical
- Trinchard-Lugan 2002, RBMO — ~1.7× multi-dose accumulation
