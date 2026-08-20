# Yola Rose Johnstone — dedicated ancestry pass (19–20 Aug 2026)

A focused fourth pass on **Yola Rose Johnstone (c.1929 Rockhampton – 23 Nov 2019)**, Shane's paternal
grandmother, wife of Alphonsus Vincent "Phonse" Schleger. Supplements `REPORT.md` and
`REPORT-pass2.md`; **neither of those files has been edited**. New facts, corrections and documented
dead ends only.

Grades as before: **[A]** primary record or contemporaneous print · **[B]** strong secondary /
researcher assertion · **[C]** inference.

Free sources only — no subscriptions, no logins, no certificates purchased.

**New evidence in `sources/yola-rose/`**

| file / folder | what |
|---|---|
| `bdm/*.jsonl` | complete Qld BDM index sets pulled by surname (Jackson, Johnston, Johnstone, Curtis, Boge, Bird, Josefski, Jacksen, Jaxon) — 14,000+ index rows, filtered locally |
| `jackson-analysis.txt`, `jackson-analysis2.txt` | every Rose-Jackson-relevant cut of the Jackson sets, with the search space stated so the negatives are reproducible |
| `johnston-analysis.txt`, `johnston-analysis2.txt` | the same for Johnston / Johnstone / Curtis |
| `qsa-csv/` + `qsa-csv-manifest.txt` | 57 Queensland State Archives open-data index CSVs from data.qld.gov.au (the largest deleted after scanning; the manifest re-downloads them) |
| `qsa_csv_scan.py` | reusable scanner across every QSA index CSV at once |
| `qsa-jackson-robert.txt`, `qsa-jackson-rose-millie.txt`, `qsa-johnston.txt`, `qsa-johnston-curtis-targeted.txt`, `assi-jackson.txt` | the QSA index sweeps |
| `qsa-archivessearch.txt` | QSA ArchivesSearch API result sets |
| `qsa-images/` + its `README.txt` | four digitised QSA register pages, downloaded free via `archivessearch.qld.gov.au/api/download_file/{DID}` |
| `trove-*.txt`, `trove-hits-yola-rose.jsonl` | Trove sweeps with the exact queries |
| `../trove-articles/nla.news-articleNNN.txt` | full article texts (added to the existing pass-2 folder) |
| `curtis/` | Cornwall → South Australia → Maryborough evidence (FreeBMD / FreeCEN / OPC / SA) |
| `siblings/` | Ryerson / Find a Grave / cemetery / myTributes sweeps for Yola's siblings |
| `naa-yola-rose.txt` | 126 NAA RecordSearch result sets, each with its exact search term |
| `../naa/*.jpg` | 138 new digitised dossier pages: four Wide Bay JACKSON WWI files, plus the four missing pages (p13–p16) of Frederick Jason Johnstone's own dossier, which is now complete at 16 pp |
| `tq.py`, `trove_yr.py`, `qbdm_pull.py` | reusable tooling built this pass |

---

## 1. Rose Jackson — the record, the negatives, the leads

### 1a. What is now *record* [A]

| fact | citation |
|---|---|
| Rose Jackson m. Frederick Jason Johnstone **21 Aug 1919** | Qld BDM **C2254/1919** |
| She died **12 Nov 1974**, date of birth recorded as **1893**, parents recorded as **"Robert Jackson"** and **"Millie Jackson"** | Qld BDM **C7759/1974** |
| Their first child **John Johnstone b. 29 Dec 1919** (C13851/1919) **died 14 April 1923, aged 3** — parents on the death registration "Fredrick Jason Johnstone / Rose Jackson" | Qld BDM **C1214/1923** — *new this pass* |
| **Jacquiline Johnstone b. 10 Nov 1923**, parents Frederick Jason Johnstone / Rose Jackson | Qld BDM C12503/1923 |
| Rose was at the **Colosseum station house** (North Coast Line, near Miriam Vale) from at least 1934 to 1945, and gardened seriously: "Mrs R. Johnstone" of Colosseum placed **3rd 1934, 3rd 1935, 2nd 1937, 3rd 1945** in the Central Queensland **Railway Station Gardens Competition** | Morning Bulletin 27 Sep 1934 nla.news-article**55604485**; 11 Oct 1935 **54797316**; Queensland Times 19 Nov 1937 **124592159**; Morning Bulletin 26 Dec 1945 **56441628** — *all new this pass* |
| At her eldest daughter's wedding in Nov 1943, "the bride's mother chose a floral frock of American silk, with black accessories" | Bundaberg News-Mail 1 Dec 1943 nla.news-article**283143943** |

This is the first time Rose appears in print as a person rather than as a name on a registration. The
station-garden results are the only known contemporary trace of anything she did.

### 1b. Two positive sightings of a "Rose Jackson" in Maryborough, 1914–15 [A record, C identification]

Both are in the right town at the right age (our Rose would be 21–22), in the years immediately before
Frederick Jason Johnstone enlisted from Maryborough:

- **29 Aug 1914** — Women's Patriotic Meeting, Maryborough; the "B Section (Service in Australia)"
  list of Misses volunteering includes "**Rose Jackson**".
  (The Colonist, Maryborough, 29 Aug 1914, nla.news-article**293062885**)
- **1 Jun 1915** — 46th annual exhibition of the Wide Bay and Burnett Pastoral & Agricultural Society,
  needlework judging: "**Ribbon work: Florence E. Mowle 1, Rose Jackson 2**".
  (Queenslander News Budget, 5 Jun 1915, nla.news-article**291229410**)

For context, **F. J. Johnstone of Maryborough** appears on the district recruiting lists of 20 and
27 October 1915 (Maryborough Chronicle 20 Oct 1915 nla.news-article**150960055**; The Colonist 23 Oct
1915 **292960046**; Maryborough Chronicle 28 Oct 1915 **150957132** — "Messrs H. W. Jones and F. J.
Johnstone left by last night's train"; The Colonist 30 Oct 1915 **292963523**), matching his NAA
attestation of 30 Oct 1915.

**This does not identify her.** "Rose Jackson" is common and neither notice gives an address, an age
or a parent. But it is the first evidence putting *a* Rose Jackson of the right age in the Johnstone
family's own town, and it is the only positive placement anyone has yet found.

### 1c. A dramatic near-miss that must be excluded, not chased [A]

Anyone searching "Rose Jackson" + Queensland will hit this, so it is documented in full so that it is
never chased again.

**Maryborough Police Court, Wednesday 16 April 1902** (before E. Morey, P.M.): four children —
**Lizzie Jackson 11, Kate Jackson 10, George Jackson 7 and Rose Jackson 4** — were "proceeded against
as neglected children"; their mother **Mrs Mary Jackson** and eldest daughter **Mary, 17**, were
charged with vagrancy. The police evidence (Acting-Sergeant William Johnson, Newtown; Constable Hugh
Costello) describes a house in Walker Street, Newtown, then a vacant house next to the Hospital, two
bare rooms, no beds, no food. The P.M. sentenced the children to the **Industrial School at
Toowoomba** — Lizzie 4 years, Kate 5, Rose 7, George 7 — the mother to four months' hard labour in
Toowoomba gaol and the eldest daughter to two months.
(The Colonist, Maryborough, 19 Apr 1902, "VAGRANCY AND NEGLECTED CHILDREN",
nla.news-article**292775155** — full text at `sources/trove-articles/nla.news-article292775155.txt`)

The QSA records of that committal were traced and the register pages downloaded:

- **Toowoomba Girls Industrial School entrance book** (QSA A/4791, ITM212557, series S6594, digital
  image **DR56900**), reg. **284 Lizzie Jackson** — Queensland, C.E., age **11**; **285 Kate Jackson**
  — Queensland, C.E., age **10**; **286 Rose Jackson** — Queensland, C.E., age **4**. All three
  "slight", **complexion fair, hair fair, eyes blue**.
- **Toowoomba Girls Reformatory discharge register** (QSA REF4/1, ITM104862, series S16294, digital
  image **DR8818**), 17 May 1902: 284 Lizzie, 285 Kate, 286 Rose Jackson — "Transferred to the
  Orphanage at Sandgate, their sentences having been remitted".
- **Index to Queensland Orphanage Admissions** (QSA A/9990, ITM268111, series S6866, DR29904): Lizzie
  (Dept no. 3577, "Warwick"), Kate (3578), **Rose (3579)** admitted 14 May 1902; **George Jackson**
  (3582) 3 Jun 1902.

**Excluded** [A]: this Rose Jackson was **four** in 1902 (born c.1897/98, not 1893); her mother was
**Mary**, not Millie; no father appears anywhere in the case; and the register describes her as fair
of complexion, fair-haired and blue-eyed. She is not Shane's great-grandmother.

Also excluded: the **"Jackson Tragedy"** of March 1897 (a Maryborough/Newtown Mrs Jackson shot by her
husband at Brisbane Central Railway station, leaving a daughter Harriet Laura) — the couple are
**Henry Lithgow Jackson** and **Harriett Elizabeth Jackson**, both d. 2 Mar 1897 (Qld regs
B29569/1897 and B29568/1897), not Robert and Millie.
(Maryborough Chronicle 6 Mar 1897, nla.news-article**147683581**; The Colonist 13 Mar 1897,
**292728826**)

### 1d. One genuinely new lead that has NOT been excluded [A record, C identification]

The Qld BDM index contains:

> **B 10/08/1914 — Rose Jackson · father blank · mother "Rose Jackson" · reg B37002/1914**
> **D 11/08/1914 — Rose Jackson · father "–" · mother "Rose Jackson" · reg B19826/1914**

i.e. **an illegitimate daughter named Rose, born 10 August 1914 to a mother named Rose Jackson, who
died the next day.** No father was registered.

Our Rose was about 21 in August 1914. This is the only Queensland record of a *Rose Jackson as a
mother* in the whole index. It is **not proof** — the name is common and nothing in the index ties
the entry to Maryborough — but it is exactly the kind of event that leaves a woman's history
undocumented and that can generate an official file. Test it with the certificate, which will give
the mother's age, residence and occupation.

### 1e. Searched and NOT found — the negatives, stated precisely

All Queensland BDM figures below come from **complete** surname sets pulled this pass and filtered
locally (see §8 — the BDM search API silently ignores the father/mother/spouse parameters, so pass 2's
parameter-filtered searches were narrower than they appeared).

**Queensland BDM** (`bdm/jackson-*.jsonl`; **1,720 Jackson births, 2,666 deaths, 1,846 marriages** —
the entire indexed surname):

- **No Queensland birth registration for a Rose Jackson born c.1893 to a father Robert.** All seven
  Jackson births 1880–1910 with a given name containing "Ros" are listed in `jackson-analysis.txt` §9;
  the closest, Frances Rose Jackson (C5878/1893), has parents Thomas Jackson / Mary Ann Macartney.
  All 215 Jackson births 1890–96 were listed in full and read.
- **No Jackson birth 1880–1910 with a father named Robert and a mother named Millie / Milly / Amelia /
  Mildred / Millicent.** The Robert-Jackson fathers in that window are Robert Henry × Mary Yardley,
  Robert × Lilly/Lillas Forrest, Robert Alexander × Jessie Downs, Robert × Mary Jane Barr, Robert
  Leonard × Isabella Martin Adair Johnston, Robert O'Neil × Rachel Mary Mulligan and Robert ×
  Elizabeth Halkett — none of them a Millie.
- **No Jackson marriage, any year, of a Robert to a Millie/Milly/Amelia/Mildred/Millicent.**
- **No Jackson death, any year, whose mother is recorded as Millie or Milly** (100+ rows with a father
  Robert read individually), and **no Millie/Milly Jackson death in the index at all.**
- **Surname variants**: Jacksen — 0 births, 3 deaths, none relevant; Jaxon — 0 births, 1 death, not
  relevant; Jaxson / Jackston / Jacson — nil.
- **Given-name variants** Rosa, Rosie, Rosanna, Rose Ann, Rose Anna, Rosina, Rosetta among Jackson
  births 1885–1902 — nil relevant.
- **No Queensland marriage of a Rose Jackson other than the 1919 one.**

**Trove — the 1919 marriage notice does not exist in the digitised corpus.** Searched
`"Johnstone Jackson"` and `"Jackson Johnstone"` as exact phrases limited to 1919 (12 and 14 hits, all
read, all unrelated); `"JOHNSTONE-JACKSON"`; `"JACKSON-JOHNSTONE"`; `Johnstone Jackson marriage` and
`JOHNSTONE JACKSON marriage bride` limited to 1919 and 1920 and filtered to the Maryborough Chronicle,
The Colonist, The Alert, Isis Recorder, the Bundaberg papers, Gympie Times, Morning Bulletin and
Capricornian. **Nil.** The Maryborough Chronicle (1860–1947) and The Colonist (1884–1952) *are*
digitised for 1919, so this is a real absence, not a coverage gap — the marriage was simply not
announced in any paper Trove holds. (A `JACKSON—JOHNSTONE` wedding *does* exist in the Gympie Times of
20 Aug 1910, nla.news-article**187677433** / **187677537** — a different couple, St Andrew's Church,
Mt Pleasant, 2 Aug 1910.) Also nil: birth notices for John (1919) or Jacquiline (1923) Johnstone, and
any "nee Jackson" notice for Rose.

**Queensland State Archives open-data indexes** — 57 name-level index CSVs downloaded from
data.qld.gov.au and scanned in bulk (`qsa_csv_scan.py`; results in `qsa-jackson-robert.txt` and
`qsa-jackson-rose-millie.txt`):

- **Aboriginal War Census Returns 1915–1916** (QSA A/58922, ITM2043631, series S4354, DR25243; 6,810
  names): the only Jacksons are **Arthur** (St Lawrence, Rockhampton district), **Tommy** ×2
  (Ingham), **Peter** (Mt Carbine, Atherton) and three people whose *given* name was Jackson
  (Barambah Settlement, Cooktown, Townsville). **No Robert, no Millie, no Rose — and no Jackson at all
  in the Maryborough district**, which *is* covered by the census (120 people returned). A real
  negative for the Wide Bay, subject to the caveat that the census records people known to the
  Protector, not every Aboriginal person.
- **Australian South Sea Islanders 1867–1948** (71,440 rows): only **three** people surnamed Jackson —
  a court entry 1892, a prison entry 1895, and a 1905 arrival per *Sybil* from Guadalcanar ("or
  MENENA"). **No Robert, Millie or Rose.** Worth stating, because the Maryborough–Childers–Bundaberg
  belt was the heartland of the South Sea Islander population and an Islander-descended Jackson family
  there would have been a serious alternative explanation for the naming pattern. On this index it is
  not supported.
- Orphanages, Toowoomba Girls Industrial School and Reformatory, Dunwich Benevolent Asylum, indigence
  cases, outdoor relief, Brisbane and Mackay hospital registers, inquests, criminal depositions,
  prisoners, deed polls, divorces, wills, land selections, teachers, all the immigration registers,
  farm lads, pensions, consumptive patients: full result sets in the two files above. **Nothing places
  a Robert or Millie Jackson in the Wide Bay–Burnett.** Nearest misses: a "Rose Jackson, age 22"
  admitted twice to Mackay Hospital in Jul–Aug 1908 (ITM1001210, DR143701 — born c.1886, wrong age,
  wrong district), and the excluded Toowoomba/Maryborough case above.

**QSA ArchivesSearch** (`qsa-archivessearch.txt`): `"JACKSON, ROSE"` returns **four** items — two 1920s
immigrant files, one cross-reference, and **ITM732477** (the restricted Chief Protector's personal
file, SRS4429/1/12474, agency file **8R/119**). `"JOHNSTONE, ROSE"`, `"JOHNSTON, ROSE"`,
`"JACKSON, MILLIE"` and `"JACKSON, AMELIA"` return **nil**. `"JACKSON, ROBERT"` returns 54 items,
**none flagged Aboriginal and/or Torres Strait Islander** and none in the Wide Bay.

**National Archives of Australia** (126 searches, full result blocks in `naa-yola-rose.txt`):

- **"Jackson Millie" across the entire Commonwealth record returns two items, both the same NSW man
  from Parkes.** There is no Millie Jackson of Queensland anywhere in the NAA.
- "Jackson Amelia" (12 items) and "Jackson Rose" (49) likewise contain nothing from the Wide Bay.
- `B2455 "Jackson Robert"` = 52 items Australia-wide; `B2455 "Jackson QLD"` = 160, of which only 15
  touch the Wide Bay; "Jackson Maryborough" across all series = 43. The haystack is large but it has
  now been enumerated.
- Nil: "Jackson Isis", "Jackson Apple Tree Creek", "Jackson Robert Bundaberg", "Jackson Robert
  Gympie", "Jackson Rose Queensland", "Millie Jackson Queensland".

**The one NAA lead, and why it probably fails** [A record, C assessment]: **JACKSON Roland Alaric
Pryce, SN 3113, NAA B2455 barcode 7373024** (18 pages downloaded to `sources/naa/`) — attested
Brisbane 29 Jul 1915, aged 21y2m (**b. c. May 1894**), **born near Maryborough**, clerk, dark
complexion / brown eyes / black hair; **next of kin: father Mr R. L. Jackson, Indooroopilly,
Brisbane**. So a Robert Jackson *was* fathering children at Maryborough in the early 1890s, with Rose
(b. 1893) sitting immediately above Roland in the sibship. **But** the Queensland index identifies him
as **Robert Leonard Jackson**, a **schoolteacher** (QSA register of teachers ITM3686128, 1888–1932),
who married **Isabella Martin Adair Johnston** on 19 Dec 1892 (Qld reg C1433/1892) — his wife was
Isabella, not Millie, and his daughter born 18 Nov 1893 is registered as **Nora Katherine Sydnie**
(C7716/1894), not Rose. Recorded here so the lead is not re-found and over-read; the only way to
close it is Roland's or Nora's birth certificate.

Two other Wide Bay Jackson dossiers were downloaded and read, and both are ruled out:
**JACKSON Sydney Reid, SN 3499** (B2455/7372018) — born near Maryborough c. Jan 1896, motor mechanic,
NOK **father Mr L. Jackson, Tinana, Maryborough**, consent signed "**Lewis Jackson**" and annotated
"Mother Dead"; and **JACKSON Robert Nelson, SN 409** (B2455/7373020) — enlisted at **Childers** Feb
1915 but born parish of Buckingham near **Hobart**, NOK father Robert Jackson of 132 Liverpool Street,
Hobart. A fourth, **JACKSON Robert Samuel, SN 1975** (B2455/7373021), born parish of Bundaberg near
Childers c.1889, miner, NOK mother **Jane Jackson** of Woonona NSW, is collateral only.

### 1f. The Aboriginal-heritage question — where it actually stands

Handled as in pass 2: what the record shows, what was looked for and not found, what would settle it.
Nothing here is a conclusion.

**What the record shows.** Rose's 1974 death registration records her mother as "Millie Jackson" — a
single given name plus, apparently, the husband's surname rather than a maiden name — and no birth
registration for Rose exists in Queensland. That is the whole of it.

**What this pass added, and it cuts both ways.**

- The single QSA index entry that could be her — **ITM732477 "JACKSON, ROSE"**, Chief Protector's
  personal files, restricted until 2078 — is **still just a name in an index**. Nothing found this
  pass connects it to her, and nothing excludes it.
- Three Wide-Bay-specific negatives now lean *against* the hypothesis: she is absent from the
  **Aboriginal War Census 1915–16 Maryborough district**; the family is absent from the **South Sea
  Islander index**; and there is **no Millie Jackson of Queensland anywhere in the NAA**. None is
  decisive — the war census covers people under the Protector's administration, and a woman married
  into a white railway family in 1919 might never appear in any of the three.
- The mother-recorded-by-given-name-only pattern is now shown, from the same index, to be **common in
  Queensland regardless of ancestry**: 36 Jackson births in 1885–1905 alone were registered with a
  blank father and the mother given as "[given name] Jackson" (`jackson-analysis.txt` §11). It is a
  marker of illegitimacy and of itinerant or unregistered families at least as much as of anything
  else.
- The **geography correction from pass 2 is reinforced**: everything about this family is Wide
  Bay–Burnett (Maryborough, Apple Tree Creek/Childers, Dallarnil, Colosseum/Miriam Vale) until the
  move to Rockhampton in 1948. Any enquiry should be framed on Butchulla / Gooreng Gooreng / Gurang
  country, not Darumbal.

**Net position [C] — same direction as pass 2, sharper in shape:** the question is *open*, and the
free record has now been worked hard enough that it will not answer it. It turns entirely on documents
that cost money or require a written application — see §7.

### 1g. What would settle it

1. **Rose's death certificate, C7759/1974** — informant, birthplace, age, length of residence in
   Queensland, and how the informant described her parents.
2. **The marriage certificate, C2254/1919** — place of marriage, her age and birthplace, residence and
   occupation, her father's occupation, the witnesses, and — decisively — whether the marriage carried
   the **Protector's permission** endorsement required for a woman under the *Aboriginals Protection
   and Restriction of the Sale of Opium Act*. That endorsement, present or absent, settles it.
3. **A Community & Personal Histories family-history request** naming her exactly as recorded and
   citing **QSA ITM732477 / SRS4429/1/12474 / file 8R/119** directly. Free; needs a written
   application and proof of descent.
4. The birth certificate for **B37002/1914** (§1d) — cheap, and either connects Rose to a documented
   event or removes the lead.

---

## 2. Johnston origins — the 1895 identification is now PROVEN

Pass 2 offered "probable death of George Johnstone: 29 March 1895, Qld reg C2621/1895, parents William
Johnston & Elizabeth Vincent" as **[C — plausible but unproven]**. It is now **[A]**.

### 2a. George Johnston's death, 29 March 1895 — the chain

| evidence | citation |
|---|---|
| "…the circumstances connected with the death of **Mr George Johnston, who died rather suddenly at his residence in Ann Street on Friday night last**" — a magisterial inquiry was ordered. (2 April 1895 was a Tuesday; "Friday night last" = **29 March 1895**, exactly the date on C2621/1895.) | Maryborough Chronicle 2 Apr 1895, nla.news-article**146900288**; The Colonist 6 Apr 1895, **292743184** |
| The **widow gave evidence** at the inquiry before the Police Magistrate (Geo. L. Lukin), Senior Sergeant Gallagher attending: "**Harriet Ann Johnston** deposed: Am the widow of the deceased; he died on the 29th March last…" | Maryborough Chronicle 27 Apr 1895, nla.news-article**146904269**; The Colonist 4 May 1895, **292745136** |
| Intestacy advertisement: "In the LANDS and GOODS of **GEORGE JOHNSTON, late of Maryborough**, in the Colony of Queensland, **out of business**, deceased … Letters of Administration … may be GRANTED to **HARRIETT ANN JOHNSTON, of Maryborough, the lawful Widow** of the said deceased." Solicitor T. Morton, Wharf Street, Maryborough. | Telegraph (Brisbane) 13 Apr 1895, nla.news-article**173755765** |
| "Recent Wills — Letters of administration have been granted in the following estates: … **George Johnstone, of Maryborough. To Harriet Ann Johnstone; realty £260; personalty £1…**" | Telegraph 29 Jun 1895, nla.news-article**172674417** |
| "**Harriett Ann Johnston (administratrix of George Johnston, deceased) v. John M'Menamin**, money payable, £5 19s 10d" | Maryborough Chronicle 10 Oct 1895, nla.news-article**146900755**; The Colonist 12 Oct 1895, **292769388** |
| QSA holds the inquiry papers: **inquest JOHNSTON, George, file no. 132 of 1895, QSA ref JUS/N232, item PR2732958 (prev. ITM348831), series S36, microfilm Z91064** — Open Access, **not digitised** | QSA open data `inquests-1859-1905-non-digital.csv` |

→ **George Johnston, husband of Harriett Ann Curtis, died at his residence in Ann Street, Maryborough,
on Friday 29 March 1895**, and the Queensland index holds exactly one George Johnston death on that
date: **C2621/1895, parents William Johnston and Elizabeth Vincent**. Proven. [A]

**George Johnston's parents were therefore WILLIAM JOHNSTON and ELIZABETH VINCENT** — which also
explains the son christened **George Vincent** Johnston (b. 1888). A **brother** now appears:

> **Robert Johnston, d. 5 Aug 1880, Qld reg C1596/1880, parents William Johnston / Elizabeth Vincent.**

These are the *only two* Queensland registrations of any kind naming a parent "Elizabeth Vincent"
(`johnston-analysis.txt` §C). No Queensland birth or marriage exists for either George or Robert with
those parents, so **William Johnston and Elizabeth Vincent did not marry in Queensland and their sons
were not born there** — this is an immigrant family arriving as adults or as a household.

### 2b. What kind of man he was — the cause of death [A]

The widow's sworn evidence at the magisterial inquiry (full text in
`sources/trove-articles/nla.news-article146904269.txt`):

> "Am the widow of the deceased; he died on the 29th March last; **for the last ten months previous to
> his death he had been drinking very heavily, in fact he was only one week sober out of the ten
> months**; he had been suffering from bronchitis about a month before he died; **we lived in Ann
> street** … gave him another dose of the medicine [Dr Penny had prescribed] at 10 p.m.; about a
> quarter of an hour afterwards I heard him breathing strongly; spoke to him; he did not answer; was
> alarmed and ran to a neighbour's house (Mr Armstrong) … he looked at the deceased and said 'I think
> he is dead' … **he was suffering from drink; periodically for the past 17 years the deceased would
> drink to great excess, even of late having delirium tremens.**"

He was about 40–45. Harriett was 35, with eight living children; the youngest, Henry Albert Curtis,
had been born five months earlier.

### 2c. The farm, and how it was lost [A]

- **"Mr George Johnston, Fernhill Farm, Apple-tree Creek"** — the Isis Central Sugar Mill company had
  bought land from him and by Feb 1894 was buying more, "having found the land purchased from Mr
  George Johnston … is inadequate for their requirements".
  (Brisbane Courier 9 Feb 1894, nla.news-article**3574077**; The Queenslander 17 Feb 1894, **20713687**)
- **Childers Police Court, Wednesday 23 May 1894**, before Thos. Mowbray P.M.: "An action was brought
  by the **Colonial Sugar Refining Company Ltd against George Johnston** … the defendant agreed to
  **vacate the premises within 24 hours**." (Maryborough Chronicle 25 May 1894,
  nla.news-article**146969050**)
- The selections themselves: **"George Johnston | Bundaberg [land office] | Childers [homestead area] |
  selection 1153 | 1876 [Act 40 Vic. No. 15] | 80 acres | consd purchased"**, with two continuation
  lines "do. **1158** … cancelled" and "do. **1260** … consd purchased".
  (QSA *Registers of Applications by Selectors 1868–1885*, LAN/P56, ITM23654, series S13961, digital
  image **DR106768**, register page 2744 — page image saved to `qsa-images/`.) Corroborated in print:
  "In the Land Court the following applications were accepted: — **George Johnston, 80 acres,
  Childers**" (Bundaberg Daily News & Mail 18 Dec 1926, "BYGONE BUNDABERG",
  nla.news-article**283745818**).

So the arc is: selector at Childers under the 1876 Act → "Fernhill Farm", Apple Tree Creek → land sold
to the sugar mill 1893 → evicted by CSR in May 1894 → living "out of business" in Ann Street,
Maryborough → dead of drink on 29 March 1895, intestate, leaving £260 realty and a widow with eight
children → Harriett remarried John Hughes in 1898.

### 2d. The eight children — consolidated, with registration numbers [A]

| # | child | born | reg | married | died |
|---|---|---|---|---|---|
| 1 | Thomas Robert Benjamin Johnston | 6 Aug 1880 | C4449/1880 (mother as "Courtis") | **Elizabeth Maria Schafer, 5 Apr 1915 — C1589/1915** | **1 Jul 1916 at Gayndah, aged 35y11m, "died suddenly"** — C3107/1916 |
| 2 | Harriet Alexander Johnston | 22 Aug 1883 | C458/1883 | — | 14 Dec 1883, infant (registered "Harriett Elizabeth") — C329/1883 |
| 3 | Elizabeth Ann Jane Johnston | 22 Dec 1884 | C9525/1885 | **(1) Joseph Bird, 19 Dec 1900 — C1678/1900; (2) Marcus Boge, 30 Apr 1924 — C1494/1924 (as "Elizabeth Anna Jane Bird")** | **24 Jan 1961 as Elizabeth Ann Jane BOGE — B42638/1961** |
| 4 | William John Johnston | 29 Jul 1886 | C10254/1886 | **Margaretha Henriette Nagel, 25 Sep 1913 — C2480/1913** | 6 Jun 1967 — C2569/1967 |
| 5 | George Vincent Johnston | 19 Aug 1888 | C11842/1888 | **Amanda Wilhelmine Pohlmann, 14 Sep 1912 — C2475/1912** | 20 Nov 1967 — C6140/1967 |
| 6 | Catherine Emily Johnston | 9 Oct 1890 | C12995/1890 | **Thomas Montgomery Schmidt, 10 Jun 1914 — C2370/1914** | (not in the index to 1994) |
| 7 | **Frederick Jason Johnston** | 28 Dec 1892 | C12224/1893 | Rose Jackson, 21 Aug 1919 — C2254/1919 | 25 Oct 1969 — C6787/1969 |
| 8 | Henry Albert Curtis Johnston | 25 Aug 1895 | C8499/1895 | **Elsie Daisy Strehlau, 27 Sep 1924 — C2427/1924** | 18 Jan 1928 — C677/1928 |

(All five marriages are new this pass.) Thomas Robert Benjamin's death notice reads: "**JOHNSTONE. —
At Gayndah, on July 1st, 1916, Thomas Robert Benjamin Johnstone, eldest son of Harriett Ann Johnstone,
Maryborough, and the late George Johnstone, and beloved husband of Elizabeth Johnstone, Gayndah, aged
35 years and 11 months. (Died suddenly.) (R.I.P.)**" (The Colonist 8 Jul 1916,
nla.news-article**292995079**) — the age matches the 6 Aug 1880 birth to the month.

The 1940 obituary's "predeceased by two sons and a daughter" is therefore Thomas Robert Benjamin
(1916), Henry Albert Curtis (1928) and the infant Harriet (1883).

### 2e. Frederick Jason Johnstone — new detail [A]

- His family nickname was **"Toby"** — "Frederick Jason (**'Toby'**) Johnstone (Colosseum,
  Bundaberg)". (Isis Recorder 23 Feb 1940, nla.news-article**287617188**; Maryborough Chronicle
  22 Feb 1940, **151359949**)
- In January 1928 he was living at **Dallarnil** (printed "Dappil"), between Biggenden and Childers —
  part of the gap between Maryborough (1915) and Colosseum (1937) is now filled.
  (The Colonist 28 Jan 1928, nla.news-article**293169820**)
- His enlistment is bracketed in print: on the Maryborough district recruiting list of 20 Oct 1915,
  and "left by last night's train" on 27 Oct 1915 — three days before the attestation date on his NAA
  file. (Maryborough Chronicle 20 Oct 1915 nla.news-article**150960055** and 28 Oct 1915 **150957132**;
  The Colonist 23 Oct 1915 **292960046** and 30 Oct 1915 **292963523**)
- **NAA confirms he is the only Johnston(e) of this family who served.** The B2455 series titles carry
  place of birth, place of enlistment and next of kin, so searching `B2455 + "Johnstone QLD"` (44
  hits) and `B2455 + "Johnston QLD"` (127 hits) enumerates every Queensland-connected WWI dossier under
  either spelling: **no dossier exists for Thomas Robert (Benjamin), William John, George Vincent,
  Henry Albert (Curtis) or John Boland.** `B2455 "Johnstone Harriet"` returns Frederick Jason only.
  (`naa-yola-rose.txt`)

### 2f. Where the Johnstons came from — still unanswered

The search space is now defined but not searched out. William Johnston × Elizabeth Vincent left no
Queensland marriage and no Queensland births for their sons George (b. c.1850s) and Robert (d. 1880).
QSA's assisted-immigration and shipping indexes hold no Johnston arrival that can be tied to them
(`qsa-johnston.txt`); NAA holds nothing (§2e). The surname is far too common for a blind search
without a birth year or birthplace — both of which are on **George's death certificate C2621/1895**
and on **Robert's, C1596/1880**. Those two certificates are the entire next step. Ulster and Scotland
are the obvious priors for a "Johnston", but **"Vincent"** as a maiden name is much more English than
either, so nothing should be assumed.

---

## 3. Curtis and Barrett — Cornwall → South Australia → Maryborough

### 3a. The Cornish origin is settled: ST BLAZEY / BISCOVEY, not St Austell town [A]

St Austell is only the **registration district**. The family's parish is **St Blazey**, and the hamlet
is **Biscovey**, in what became the parish of **Par** from 1849.

**1861 census — the whole household in one line**: Cornwall, census district St Austell, ED 16, civil
parish **St Blazey**, piece **RG9/1546**, page 13, dwelling 1010, schedule 74, address **"Biscovey"** —

> **Thomas CURTIS**, Head, married, **21**, **Tin Miner**, b. Cornwall, **St Blazey**
> **Elizabeth CURTIS**, Wife, married, **20**, b. Cornwall, **Tywardreath**
> **Harriet CURTIS**, Dau, **1**, b. Cornwall, **St Blazey**

(FreeCEN2 `search_records/610bc84cf493fd23e3ec71df`; saved as
`curtis/freecen-1861-household-curtis-stblazey.txt`.) "Tin Miner" at 21 is the direct antecedent of
"managed the Tee-bar Mines from 1865".

**Marriage**: **Thomas Curtis × Elizabeth Ann BARRATT, Dec quarter 1859, St Austell registration
district, GRO vol 5c page 260** — both halves confirmed by a volume/page cross-search. Note the
spelling: **the GRO index has BARRATT**; a Curtis × Barrett search returns nothing for all Cornwall
1837–1875. (FreeBMD; `curtis/freebmd-marr-curtis-barratt-cornwall.txt`) [A]

**Birth of Harriett Ann Curtis**: GRO index **Dec quarter 1859, St Austell district, vol 5c page 147**
— the only Harriet Ann Curtis in the district in that era. [A]

**Baptism**: **29 February 1860, parish of PAR (St Mary Biscovey)** — Harriet Ann CURTIS, father
Thomas, mother Elizabeth Ann, residence **Biscovey**. Cornwall OPC baptism record **id 7843046**, film
1596121, image 613. [A] Born late 1859, baptised Feb 1860 — consistent with "aged four" landing
Adelaide in 1863 and "aged 80" at death in Feb 1940. **She was the eldest child**: the marriage was
registered in the same quarter as her birth, and the full St Austell Curtis birth index 1850–1866
contains no other child attributable to the couple. The family therefore sailed in 1863 with, in all
likelihood, only Harriett.

### 3b. The generation back — WILLIAM CURTIS × JANE, and Jane was born in MALTA [A]

**1851 census**: Cornwall, census district Fowey, civil parish **St Blazey**, ecclesiastical parish
Par, piece **HO107/1906**, ED 4a, **folio 211, page 28, schedule 98**, address **"Biscovey"** — the
same house —

> **William CURTIS**, Head, 36, **Copper Miner**, b. Cornwall
> **Jane CURTIS**, Wife, 34, **birthplace MALTA** ("Born Overseas", nationality British)
> Emmery A. CURTIS, Dau, 12, b. St Blazey
> **Thomas CURTIS, Son, 11**, b. St Blazey

(FreeCEN2 `search_records/5a143549f4040b9d6e22b644`.) Corroborated by the baptism of their daughter
Elizabeth, 20 Apr 1842, St Blazey, father William, mother Jane, residence "Biscove" (Cornwall OPC
baptism id **5970931**).

**And NORMANTON is present at St Blazey** — Richard Normanton bapt. 1832 St Blazey, son of **Joseph**
and Elizabeth; Charles Normanton buried St Blazey 1851; Charles Normanton bapt. Par 1851, son of John
and Catherine; four further Normanton baptisms at Par in 1864. This independently corroborates the
Queensland death registration **C293/1898**, which names Thomas Curtis's mother as **Jane NORMANTON**,
and explains why the surname looks so un-Cornish: **[C]** Jane, born Malta c.1817, belongs to a
garrison or seafaring family that came back to a Cornish mining village. Normanton is otherwise
**functionally absent from Cornish civil registration** — no births and no marriages in the county
1837–1900, and a single 1995 death.

**Elizabeth Ann Barratt's own birth**: GRO index **Mar quarter 1841, St Austell district, vol 9 page
20** — the **only** Elizabeth Ann Barrett/Barratt birth registered in the district 1837–1850. Age 20
at the April 1861 census and ~69 at death on 24 Dec 1910 both fit. [B] Her father, per the Queensland
death registration **C4383/1911**, was **William Barratt/Barrett**; a Tywardreath baptism of 1844
(William Barrett, father **William**, mother **Harriet** — OPC id 1551137) is a plausible sibling and
would explain the naming of **Harriett** Ann Curtis. **[C]**, not proven.

### 3c. The Queensland end is now fully documented [A]

Pass 2 had Thomas Curtis only through his daughter's obituary. He is now a documented public official,
and his death is pinned.

| fact | citation |
|---|---|
| **Caretaker of the Maryborough bridge**, 1880 — "Thomas Curtis stated: Am caretaker of the Maryborough bridge" | Maryborough Chronicle 7 Aug 1880, nla.news-article**148731800** |
| Officer of the **Unity and Concord Lodge**, Maryborough, 1877 and 1879 | Maryborough Chronicle "Fifty Years Ago" 31 Dec 1927, nla.news-article**150979335**; The Colonist 5 Jan 1929, **293151199** |
| **Appointed "a ranger and bailiff of Crown lands, in the room of J. H. Pengelly, resigned"**, Government Gazette, April 1883 | Brisbane Courier 14 Apr 1883, nla.news-article**3416966**; The Queenslander 21 Apr 1883, **19790655**; Telegraph 14 Apr 1883, **174690804**; The Week 21 Apr 1883, **183698095** |
| **Crown Lands Ranger for the Gladstone and Bundaberg districts**; sued John Lamb of Bundaberg for defamation, Supreme Court Maryborough, May 1886 (verdict for the plaintiff, damages one farthing) | Toowoomba Chronicle 13 May 1886, nla.news-article**216253340**; Daily Observer 12 May 1886, **285381294**; The Week 22 May 1886, **183126121** |
| Prosecuted timber-cutting on Crown lands at Childers, 1894 and 1895 | Bundaberg Mail 12 Sep 1894, nla.news-article**216436472**; 10 Jul 1895, **216436792** |
| **"THE Crown Lands Ranger for the Gladstone and Bundaberg districts, Mr Thomas Curtis, is dead."** | Western Champion 1 Mar 1898, nla.news-article**76384191** |
| → his death registration is therefore **Qld C293/1898, d. 19 Feb 1898**, naming **his** parents as **WILLIAM CURTIS and JANE NORMANTON** | Qld BDM C293/1898 |
| **"DEATH. On December 24, 1910, at Townsville, Elizabeth Ann Curtis, relict of the late Thomas Curtis, formerly of Maryborough, and lately Crown Lands Ranger Bundaberg. Bundaberg papers please copy."** | Maryborough Chronicle 31 Dec 1910, nla.news-article**148945393**; The Colonist 7 Jan 1911, **292980819** |
| → her death registration is therefore **Qld C4383/1911**, naming her father as **WILLIAM BARRATT / BARRETT** | Qld BDM C4383/1911 |

### 3d. Elizabeth Ann Curtis's own old-age pension claim, 1908 [A]

QSA *Index to Pensions 1908–1909* (COL/A4774, ITM212540, series S6578, digital image **DR56521**),
register page 82, claim **1636**, registered **15 August 1908**:

> **CURTIS, Elizabeth Ann · "Eng" · age 68 · years in Queensland: 36 · present place of residence:
> Maryborough · 10/- per week recommended · certificate 1237, payable at Maryborough, from 1 July.**

(Page image at `qsa-images/DR56521_p85_pension-register-p82_ELIZABETH-ANN-CURTIS-1636.png`.)

Nationality **English**, corroborating the Cornish birth, and age 68 in Aug 1908 → born **c.1839/40**,
matching the Mar-1841 GRO birth registration. But note the tension: **"36 years in Queensland" implies
arrival about 1872**, whereas the 1940 obituary has Thomas Curtis managing the Teebar Mines "in 1865".
The "Other States" column is blank for everyone on that page, so this cannot be pushed hard — but if
the 36 is right, the family spent roughly nine years in South Australia (1863–1872) before coming
north, which is a materially different search and changes where their middle children were born.

### 3e. Harriett's siblings [A]

All with father Thomas Curtis and mother Elizabeth Ann Barrett:

| sibling | born | died |
|---|---|---|
| John Curtis | 4 Apr 1877 — C3620/1877 | 5 Apr 1877, one day old — C1614/1877 (mother spelt "Barnett") |
| Frederick Thomas Curtis | (no Qld birth) | 28 Jul 1879 — C1705/1879 |
| **Frederick Britton Curtis** | 10 Sep 1881 — C4368/1881 | 1 Feb 1925 — B44954/1925 |
| William Curtis | (no Qld birth) | 5 Apr 1931 — B13740/1931 |

Frederick Britton Curtis married **Elizabeth Ellen Matthews, 27 Sep 1905 (C2392/1905)**. Note the
shape of that list — Queensland births only from 1877, and two sons who died in Queensland with no
Queensland birth. Consistent with older children born in South Australia, and so with the pension
register's 1872 rather than the obituary's 1865.

**"Britton" is not a Cornish family surname.** Searched and not found: no Britton baptism, marriage or
burial at St Blazey in the Cornwall OPC; no Curtis × Britton marriage in Cornwall 1837–1890; Britton
births in the St Austell district begin only in 1903. The name must have been acquired in Queensland —
a godparent, employer or lodge brother — or comes from the Barrett side.

### 3f. South Australia, 1863 — one candidate, no confirmation

**[C]** SAGHS free birth index: **CURTIS, Jane, female, father Thomas CURTIS, Adelaide district,
book/page 27/221, 1863** — the only 1863 Adelaide-district Curtis birth with a father Thomas, and
"Jane" matches Thomas's own mother's name. The mother's name is behind the SAGHS paywall, so it is
unconfirmed. If it is theirs, it proves the family was in Adelaide in 1863 and dates the move north.

**Searched and not found**: the SAGHS *Ship Passenger Arrivals in South Australia* index holds **no
Thomas, Elizabeth or Harriett Curtis arriving 1860–1866** (the only Curtis arrivals in the window are
Anne 1865, Martha 1860, Hargrave 1862) — but this is a **weak** negative, because the whole index
holds only 165 Curtis records across 1836–1952 and is far from complete for unassisted arrivals. No
Barrett arrivals 1860–66 either. No SA Curtis death 1862–68 and no SA Curtis marriage 1862–68
attributable to the family.

---

## 4. Yola's siblings and their families

### 4a. The four children of Frederick Jason Johnstone and Rose Jackson

| # | child | born | fate |
|---|---|---|---|
| 1 | **John Johnstone** | 29 Dec 1919 — C13851/1919 | **died 14 Apr 1923, aged 3** — C1214/1923 (*new this pass*) |
| 2 | **Jacquiline / Jacqueline Johnstone** | 10 Nov 1923 — C12503/1923 | m. **Lawrence Aubrey Josefski** 20 Nov 1943; **divorced 1949**; soprano, Rockhampton 1949–53 |
| 3 | **Mafalda Johnstone** | 9 Oct 1926 | see §4c |
| 4 | **Yola Rose Johnstone** | c.1929 | m. Alphonsus Vincent Schleger 1951; d. 23 Nov 2019 |

Yola grew up with two sisters, not a brother and two sisters — John died before she was born.

### 4b. Jacqueline Johnstone → Josefski: married, divorced, and one child [A]

**The marriage.** "JOSEFSKI—JOHNSTONE. The marriage of **Miss Jacqueline Johnstone, eldest daughter of
Mr and Mrs F. J. Johnstone, Colosseum**, to **Lance-Corporal Laurence A. Josefski, of Bundaberg**,
took place at the **Lutheran Church, South Bundaberg, on November 20 [1943]**. Pastor Reuther
officiated. It was a typical quiet war-time wedding. The bride looked charming in a simply styled
street-length frock of dusty pink crepe. **The two bridesmaids, sisters of the bride**, wore
street-length frocks of pink and green taffeta. **The bride's mother chose a floral frock of American
silk, with black accessories.** … The groom was attended by his two brothers. **Miss Eunice Josefski,
sister of the groom**, decorated the church with white gardenias and bridal fern."
(Bundaberg News-Mail 1 Dec 1943, nla.news-article**283143943**)

The two bridesmaids are Mafalda (then 17) and **Yola Rose (then 14)** — the earliest known appearance
of Shane's grandmother anywhere.

Registered as **Lawrence Aubrey Josefski = Jacqueline Johnstone, 20 Nov 1943, Qld reg C3965/1943.**

**The husband.** **Lawrence Aubrey Josefski, b. 16 Jun 1920 (C3947/1920)**, son of **August Josefski**
and **Johanna Marie Henriette Scholz** (married 8 Jul 1918, C1976/1918); he died **10 Sep 1974
(C4813/1974)**. His sister **Eunice Constance Josefski, b. 6 Oct 1918 (C12212/1918)**, married Joseph
Mervyn Magee on 8 Jan 1944 (C43/1944). The Josefskis were a **Miriam Vale / Colosseum** family before
they were a Bundaberg one — an "A. Josefski" ran a Miriam Vale Shire road gang at the Colosseum Creek
crossing in 1929 (Bundaberg Daily News & Mail 7 Jun 1929 nla.news-article**283755461**, 9 Aug 1929
**283752945**, 17 Sep 1929 **283761546**, 6 Dec 1929 **283772968**). The two families were neighbours
at Colosseum before they were in-laws.

**The divorce**, Supreme Court, Rockhampton, November 1949, reported at length [A]:

> "**DESERTION.** **Jacqueline Josefski, of Rockhampton**, sought dissolution of her marriage with
> **Lawrence Aubery Josefski, of Imbil, Queensland**, on the grounds of desertion. The action was
> undefended. Mr E. R. Larcombe (instructed by the firm of D. P. Carey, town agents for Mr G.
> Finemore, Bundaberg) appeared for the plaintiff. Evidence was given by the plaintiff that she and
> the defendant were **married at Bundaberg on November 20, 1943, according to the rites of the
> Lutheran Church. They lived at Colosseum, near Gladstone, and at Bundaberg. There was one child of
> the marriage.** At the time of the marriage her husband was serving with the AMF. He saw her on
> leave and their married life was happy until **December 1945, when he told her he preferred his girl
> friend in Brisbane**… The defendant was discharged in March 1946 but he did not come to see her. He
> came to Bundaberg in June 1946 and they lived together for six days. When he left he promised to
> make a home for her… The defendant came to Bundaberg where witness was working in a cafe, in January
> 1947, but failed to keep an appointment with her to discuss their marriage. She took proceedings
> against him for maintenance and he consented to an order being made. His Honour granted an order nisi
> returnable after three months and **gave the plaintiff custody of the child**, with costs against the
> defendant."
> (Morning Bulletin, Rockhampton, 19 Nov 1949, "Driven Away By Husband's Conduct",
> nla.news-article**56924082**)

**So Yola Rose had a niece or nephew** — one child of Jacqueline and Lawrence Josefski, born between
1944 and 1947 and raised by Jacqueline. That child is a first cousin of Shane's father, and is not yet
named (the Queensland birth index stops at 1924).

This also explains the stage name: from 1949 Jacqueline performed in Rockhampton under her **maiden**
name, as "Jacqueline Johnstone (of Radio Fame)" — she had just resumed it, and her parents had moved
to Rockhampton the year before.

Lawrence Aubrey Josefski afterwards: a son **Rodney August Josefski** died 20 Dec 1949 (C4556/1949),
parents recorded "Lawrence Aubrey / **Violet Thelma Zillmann**"; and **Lawrence Aubrey Josefski married
Erin Ursula Heathwood, 18 Aug 1951 (B33409/1951)**. [A for the registrations; **[C]** for the
reconstruction that these are all the same man — the Queensland index contains only one Lawrence
Aubrey Josefski birth.]

### 4c. Mafalda Maria Johnstone → Mrs Edward Lewis BARTLEM — **solved** [A]

**As a child at Colosseum** she appears four times in print:

- Miriam Vale school sports, Dec 1937: "girls' race, Jean Craig 1, Gwen Cox 2, **Mafalda Johnstone**
  3" (Bundaberg Daily News & Mail 18 Dec 1937, nla.news-article**284824088**)
- Truth (Brisbane) crossword competition winner, 13 Nov 1938 — "**MAFALDA JOHNSTONE, Station House,
  Colosseum**" (nla.news-article**203912036**)
- Truth "Penfriends' Nook", 11 Dec 1938 — "**MAFALDA JOHNSTONE, of Station House, Colosseum, N.C.
  Line**, is wanting a…" (nla.news-article**203914779**)
- Truth "The Chief's Mail Bag", 1 Oct 1939 — "Sorry, you will have to choose another pen-name,
  **Mafalda Johnstone, of Colosseum**" (nla.news-article**206301265**)

Her elder sister Jacquiline had used the same pen-friends column two years earlier from the same
address (Truth 29 Aug 1937, nla.news-article205734137).

**Then, in 1947–48:**

- Full name **Mafalda Maria**, "**second daughter**". Engagement, Bundaberg News-Mail 14 Oct 1947:
  "BARTLEM—JOHNSTONE. — The engagement is announced of **Mafalda Maria, second daughter of Mr and Mrs
  F. J. Johnstone, Burnett Street, Bundaberg**, to Edward Lewis, third son of Mr and Mrs Bartlem."
  (nla.news-article**283849360**) — *this also fills another residence gap: the family was at Burnett
  Street, Bundaberg in 1947, between Makowata (1943) and Rockhampton (1948).*
- **Marriage: Edward Lewis Bartlem = Mafalda Johnstone, 26 Jun 1948, Qld reg C1382/1948.**
- **Death: 10 September 2022, aged 95.** North Rockhampton Cemetery burial index (Rockhampton Regional
  Council, free PDF): "BARTLEM MAFALDA MARIA (ASHES) 95 F — died 10 September 2022 — interred 10
  November 2022 — Sec H Row D Grave 5 — RC". Corroborated by Find a Grave memorial **251233434**
  ("Mafalda Maria Bartlem, 9 Oct 1926 – 10 Sep 2022"), whose birth date matches her registered one
  exactly.
- **Her husband**: **Edward Lewis Bartlem, b. 19 Nov 1924** (C12578/1924), son of Arthur Lewis Bartlem
  and Ethel Alberta Barnes; **d. 17 Dec 1982** (50137/1983); buried in the same grave. His headstone
  (Find a Grave memorial **160442332**) reads: "**79950 Leading Aircraftman Edward L. Bartlem, Royal
  Australian Air Force, 17th December 1982 Age 58. Dearly loved by wife Mafalda, Jason, Devon, Adrian,
  Shaun and Edwina.**"
- **So Yola Rose had five Bartlem nieces and nephews: Jason, Devon, Adrian, Shaun and Edwina.** The
  eldest carries her father's middle name — internal confirmation of the identification.
- Mafalda passed the **State Scholarship examination, Gladstone centre**, results published 22 Jan 1941
  (Morning Bulletin, nla.news-article**56192446**).

### 4d. Both sisters on stage together, 1948 [A]

Before the divorce, Jacqueline performed under her **married** name and beside her sister:
Bundaberg News-Mail, 28 Jan 1948, "'FREE & EASY' Revue Pleases Large Audience" —
"**Jacqueline Josefski** in her classical contributions reached a high standard in articulation and
vocalism… A spirited 'Boogie' number greatly pleased as contributed by **Mafalda Maria**."
(nla.news-article**283358169**) After the November 1949 divorce she is billed only as **Jacqueline
Johnstone**: Rockyettes revues, Morning Bulletin 14 Oct 1949 (nla.news-article**56919003**), 28 Apr
1951 (**57075590**), 16 Oct 1951 (**57123291**), 14 Dec 1951 (**57110662** — soprano solo "Star of
Love").

### 4e. Burials — Frederick Jason and Rose [A]

Rockhampton Regional Council, **North Rockhampton Cemetery** burial index (free PDF):

- **JOHNSTONE, FREDERICK JASON**, 76, M — died **25 October 1969**, buried **27 October 1969** —
  **Section E, Row C, Grave 20 — Presbyterian**
- **JOHNSTONE, ROSE**, 81, F — died **12 November 1974**, buried **14 November 1974** —
  **Section E, Row C, Grave 22 — Roman Catholic**

Adjacent graves, not the same one. Note also the **denominational split** — Frederick Presbyterian
(his AIF file gave Methodist), Rose Roman Catholic. Find a Grave memorials **160453306** (Frederick
Jason) and **160453309** (Rose Jackson Johnstone); their infant son John is memorial **173711829**.

**A footnote worth flagging [C]:** Rose is credited by name with the Colosseum station garden in the
Central Queensland competition, and the family's address is repeatedly given as "**Station House**,
Colosseum". In that competition the credited person is usually the station master or **station
mistress** (e.g. "Tryphenia (station mistress Mrs G. Pearce)", Morning Bulletin 26 Dec 1945). Frederick
Jason was a **ganger**, not a station master. It is therefore possible — not established — that Rose
herself held the position of station mistress at Colosseum. A Queensland Railways staff record would
settle it.

### 4f. Henry Albert Curtis "Gullie" Johnstone's family — solved [A]

- **Death notice**, The Colonist (Maryborough) 28 Jan 1928, nla.news-article**293169834**: "JOHNSTONE.
  — On January 18, 1928, at his residence, **Richmond-Lane, Maryborough**, Henry Albert Curtis
  ('**Gullie**'), beloved husband of **Elsie Daisy Johnstone**, and beloved father of **Gilbert and
  Desmond Johnstone**; aged 34 years and 4 months." (The stated age is wrong — born 25 Aug 1895, he
  was 32y5m. Notice error.)
- **Elsie Daisy Johnstone née Strehlau did not remarry.** She was still "Mrs E. D. Johnstone, 22
  Richmond-lane" in 1940 (Maryborough Chronicle 5 Oct 1940, nla.news-article**152066192**, at her
  mother's funeral) and in 1951 (Maryborough Chronicle 25 Jun 1951, **148961653**). Her parents were
  **Henry Carl Strehlau** and **Clara Strehlau** of Thinoomba (Clara born Germany, arrived Maryborough
  aged 10, d. 4 Oct 1940). **Elsie died 14–15 Aug 1973, aged 72**, at Demaine Hospital, Maryborough
  (Ryerson Index, Fraser Coast Chronicle 15 and 16 Aug 1973), and is buried **in the same plot as
  Gullie — Maryborough Monumental Cemetery, monumental K 141** (Australian Cemeteries Index
  inscriptions 15624508 and 15624509).
- **Gilbert Henry Johnstone**, b. c.1925, a **locomotive driver** of Nathan Street, Brighton, Brisbane
  — named in a 1964 rail-crash report as "the driver was Gilbert Henry Johnstone, 39" (Telegraph
  31 Jul 1964, nla.news-article**296171865**), an ALP plebiscite candidate 1965, and as a boy Inner
  Guard of the P.A.F.S.O.A. juvenile lodge "Excelsior's Pride No. 31", Maryborough, 1938 (Maryborough
  Chronicle 13 Sep 1938, nla.news-article**152162941**). **Died 10 Oct 2002, aged 77**, late of
  Brighton (Ryerson: Courier-Mail and Fraser Coast Chronicle notices). [B]
- **Desmond Robert Johnstone**, b. c.1926/27; married **Thelma Catherine West, 21 Apr 1951 (Qld reg
  C2389/1951)**; **died 4 Feb 2015, aged 88**, at Chelsea, Maryborough (Ryerson, Fraser Coast Chronicle
  7 Feb 2015). [B]
  Neither son appears in the Queensland birth index because it closes at 1924 and both were born after
  their parents' September 1924 marriage.

### 4g. Searched and not found, with the coverage swept

- **Jacqueline's death, and any remarriage, are genuinely not found.** Swept: Ryerson JOHNSTONE +
  Jacqueline (sounds-like, 20 rows Australia-wide, none Central Queensland), + Jacquiline (0);
  **Ryerson holds no JOSEFSKI notices at all** (0 rows for the whole surname); Qld BDM deaths
  1829–1994 across the complete JOHNSTONE (791), JOHNSTON (2,329) and JOSEFSKI (32) sets; Find a
  Grave under both surnames; all three Rockhampton council burial indexes; myTributes. **The
  structural reason:** the Queensland marriage index closes at **1949**, so a remarriage after her
  November 1949 divorce cannot be indexed at all, and a death after 1994 under a third surname is out
  of reach of every free source.
- **The child of Jacqueline and Lawrence Josefski (b. c.1944–46) is not identified.** The Queensland
  birth index closes at 1924.
- **Mafalda's death notice is not published anywhere reachable** — and the reason is exact:
  **Ryerson's Rockhampton Morning Bulletin death-notice indexing runs 1 Feb 1989 – 27 Jun 2020 only.**
  She died 10 Sep 2022, two years past the end. Her death is nonetheless firmly established from the
  council burial index and Find a Grave. The same coverage limit is why **Frederick's 1969 and Rose's
  1974 notices are out of Ryerson's scope rather than absent** — whereas the **Fraser Coast Chronicle
  (= Maryborough Chronicle) is indexed 26 Dec 1860 – 18 Jul 2020**, which is exactly why the
  Maryborough branch (Elsie 1973, Gilbert 2002, Desmond 2015) came out cleanly. **Record this
  asymmetry — it is the single most useful thing to know about Ryerson for this family.**
- A **Ryerson given-name-only sweep for "Mafalda" across all surnames Australia-wide** returned 164
  rows, of which only ten have any Queensland connection and none is ours — confirming her notice is
  not in Ryerson under any married surname.
- **Trove caution:** `"Jacqueline Johnstone"` returns 116 hits, the great majority of them an
  **unrelated Sydney model and dancer** of Hurstville and Pitt Street. Do not conflate.
- **Yola Rose's own 2019 myTributes notice names no siblings**, so that route to Mafalda and
  Jacqueline was closed.
- **Fraser Coast Regional Council "Cemeteries Online"** could not be searched at all — the old Liferay
  query URL now 403s and the current page is an ASP.NET postback form needing a live browser session.
  A blocker, not a null result; it would give the Maryborough register entries for Gullie, Elsie
  Daisy, and possibly Gilbert and Desmond.

---

## 5. Corrections to the earlier reports

`REPORT.md` and `REPORT-pass2.md` have **not** been edited; the corrections are recorded here.

1. **`REPORT-pass2.md`, "A brother not previously known" — John Boland Johnstone was NOT a brother.**
   The Queensland index registers **John Boland Johnston, born 7 August 1899 (C7839/1899), father
   blank, mother "Elizabeth Ann Jane Johnston"** — the illegitimate son of Frederick Jason's sister
   Elizabeth Ann Jane (b. 22 Dec 1884), who was fourteen. He was registered under the Johnston
   surname and raised in the household, which is why the 1928 obituary of Henry Albert Curtis
   Johnstone lists him among the brothers. He married **Ursie May Doss, 22 Nov 1922 (C3229/1922)** and
   died **28 Nov 1971 (B28414/1971)**, his mother still recorded as Elizabeth Ann Jane Johnston. He is
   Frederick Jason's **nephew**. [A for the registrations; [B] for the reading, which rests on there
   being only one Elizabeth Ann Jane Johnston in the whole Queensland index.]
2. **`REPORT-pass2.md`, the two sisters — the married names are the wrong way round.**
   **Catherine Emily Johnstone** married **Thomas Montgomery Schmidt** (10 Jun 1914, C2370/1914) =
   "Mrs T. M. Schmidt". **Elizabeth Ann Jane Johnston** married **Joseph Bird** (19 Dec 1900,
   C1678/1900), then **Marcus Boge** (30 Apr 1924, C1494/1924, as "Elizabeth Anna Jane Bird") = "Mrs
   Marcus Boge"; she died 24 Jan 1961 as **Elizabeth Ann Jane Boge** (B42638/1961), parents George
   Johnston / Harriet Ann Curtis. Pass 2 had Catherine Emily = Mrs Boge and Elizabeth Ann Jane =
   Mrs Schmidt. [A]
3. **`REPORT-pass2.md`, "Mesdames Marcus Boge (Maryborough) and T. Schmidt (Brisbane)"** — by February
   1940 Mrs T. M. Schmidt was at **Gympie**, not Brisbane (Maryborough Chronicle 22 Feb 1940,
   nla.news-article**151359890**). The 1928 obituary's "Brisbane" was twelve years earlier. [A]
4. **`REPORT-pass2.md`, "probable death of George Johnstone … [C — plausible but unproven]"** — now
   **proven [A]**; see §2a.
5. **`REPORT.md` and `REPORT-pass2.md`, the sibling list** — **John Johnstone (b. 29 Dec 1919) died as
   an infant on 14 April 1923** (C1214/1923). [A]
6. **`REPORT-pass2.md`, the Rose Jackson negatives — right conclusions, wrong method.** Pass 2's
   statements ("all Qld Jackson births 1885–1902 with a father named Robert — 32", etc.) were produced
   by passing `fathersname` / `mothersname` to the BDM search API. **That API ignores those
   parameters** — verified this pass, the same query with and without them returns the identical
   unfiltered surname set. The conclusions happen to be right, but the numbers quoted were not what
   the searches actually did. All figures in §1e come from local filtering of the complete surname
   sets. [A]
7. **`REPORT-pass2.md`, Frederick Jason's whereabouts** — the gap between Maryborough (1915) and
   Colosseum (1937) is partly filled: he was at **Dallarnil** in January 1928. [A]
8. **`REPORT.md`, "Harriett Ann Curtis … b. c.1859 St Austell, Cornwall"** — St Austell is the
   **registration district**. She was born at **Biscovey, in the parish of St Blazey**, and baptised
   at **Par** on 29 Feb 1860. Her mother's surname is spelt **BARRATT** in the English records, not
   Barrett. [A]
9. Minor: the Queensland index spells the mother of Thomas Robert Benjamin Johnston (C4449/1880) as
   "**Courtis**", which is why a `Curtis` regex misses that one birth. The count of eight Queensland
   births to George and Harriett is confirmed — all eight are tabulated in §2d. [A]

---

## 6. Dead ends — needs a login, a payment, or a reading room

| what | status |
|---|---|
| **Qld BDM certificates** | Still the only way to answer the Rose Jackson question. Priority: **Rose's death C7759/1974**, the **marriage C2254/1919**, the **1914 birth B37002/1914**, then **George Johnston's death C2621/1895** and **Robert Johnston's C1596/1880** (Johnston origin), and **Thomas Curtis's C293/1898** and **Elizabeth Ann Curtis's C4383/1911** (the Cornish generation). Purchase required. |
| **QSA ITM732477 — "JACKSON, ROSE", Chief Protector's personal file, SRS4429/1/12474, file 8R/119** | Restricted Access, 100-year RAP, opens 2078. Only route is a free **Community & Personal Histories** family-history request — written application plus proof of descent. |
| **QSA inquest file JUS/N232 no. 132/1895 (George Johnston)**, item PR2732958, series S36, microfilm Z91064 | **Open Access but not digitised.** Reading-room visit or paid copy order. Contains the full depositions of which only a newspaper précis survives. |
| **GRO marriage certificate, Curtis × Barratt, Dec qtr 1859, St Austell, vol 5c p 260** | **Login + fee** at gro.gov.uk. The single highest-value document left on the Cornish side: church or chapel, both ages, both occupations, **both fathers' names and occupations**, and the witnesses. |
| **1841 census, Biscovey / St Blazey (Fowey district)** | **FreeCEN has no 1841 Fowey coverage.** Needs FamilySearch (free account) or a paid site. Would resolve the William-Curtis-×-Elizabeth (1834 baptism) vs William-×-Jane (1842 baptism) ambiguity and show Jane's "Foreign Parts" birth marker. |
| **Tywardreath 1841 / 1851 (the William Barrett household)** | **FreeCEN has no Tywardreath coverage for 1841 or 1851.** FamilySearch or paid. |
| **Passengers in History** (SA Maritime Museum) — the best free tool for a 1863 Port Adelaide arrival | **Decommissioned.** `passengersinhistory.sa.gov.au` 301-redirects to the museum's research page and the tool is gone. |
| **genealogysa.org.au record details** | Index rows are free; **"View Details" is paywalled** and mothers' names show as "(members only)". Confirming SA birth 27/221 (Jane Curtis, Adelaide 1863) needs SAGHS membership or a purchase. |
| **State Records SA passenger lists 1845–1940** | Images are free but there is **no free name index** — you must already know the ship and date. Not searchable by surname. |
| **TheShipsList** (`theshipslist.com`) | **DNS failure — host does not resolve.** Technical, not a paywall. |
| **familyhistorysa.info shipping index** | **TLS certificate mismatch**, could not fetch. |
| **Bound for South Australia** | Free, but covers **1836–1851 only** — useless for 1863. |
| **Queensland electoral rolls and Post Office directories** | On Ancestry / Findmypast — **paid**. The cheapest way to find where a Robert or Millie Jackson lived in the Wide Bay 1900–1919, and to place Rose before 1919. Not attempted. |
| **NSW BDM historical index** | Cloudflare **and** an Apache Wicket app: setting inputs via JavaScript does not update the server-side model, so the search always returns "family name must be entered". Re-confirmed this pass. NSW has **not** published its historical index as open data (data.nsw.gov.au carries only statistical BDM datasets). If Rose was born outside Queensland, this is the blocker. |
| **Rockhampton Morning Bulletin after 1954** | Frederick Jason's 1969 and Rose's 1974 death and funeral notices sit past Trove's digitisation boundary. Not a paywall. |
| **Queensland school admission registers** | The QSA open-data set `school-admissions-registers-1878-2001` is an **item-level list of registers, not a name index** — it cannot be searched for a child, and the registers are not digitised. A Wide Bay register for c.1899–1905 is the natural place to find Rose Jackson as a schoolgirl with a parent's name and address. Reading room only. |
| **Fraser Coast Regional Council "Cemeteries Online"** | The old Liferay query URL (`burialAdmin_WAR_cemeteries`) now **403s**, and the current page is an ASP.NET postback form (`ctl06$txtSearch` + `__SEAMLESSVIEWSTATE`) that needs a live browser session. **Could not be searched at all** — a blocker, not a null result. Would give the Maryborough Cemetery register entries for "Gullie" Johnstone and Elsie Daisy (plot K 141) and possibly Gilbert (2002) and Desmond (2015). One browser-driven pass would clear it. |
| **Ryerson Index coverage, Rockhampton Morning Bulletin** | Death notices indexed **1 Feb 1989 – 27 Jun 2020 only** (ryersonindex.org/rmbdths1.htm). Frederick Jason (1969), Rose (1974) and Mafalda (2022) all fall **outside** that window — they are out of scope, not absent. By contrast the **Fraser Coast Chronicle (= Maryborough Chronicle) is indexed 26 Dec 1860 – 18 Jul 2020**, which is why the Maryborough branch came out cleanly. Not a paywall — a coverage boundary. |
| **NAA B883 for JOSEFSKI, Lawrence Aubrey, Q138061** (Australian Army, enlisted Gladstone, discharged 14 Mar 1946, L/Cpl, 127 General Transport Company) | Free if digitised; **not fetched this pass**. NOK addresses 1943–46 would fix where Jacqueline was living and may name their child. |
| **FamilySearch / GenTeam** | Free but require an account; excluded by the brief. |
| Everything in `REPORT-pass2.md`'s dead-ends table | unchanged |

---

## 7. Next steps, in order of value per dollar

1. **Buy two certificates: Rose Johnstone's death (C7759/1974) and the 1919 marriage (C2254/1919).**
   Between them they should give her birthplace, her age, her parents as stated by an informant who
   knew her, her residence and occupation in 1919, the place of marriage, the witnesses, and — if it
   was required — the **Protector's permission** endorsement, which settles the heritage question in
   either direction. Nothing else comes close in value.
2. **Lodge the Community & Personal Histories family-history request.** Free. Name her exactly as
   recorded (Rose Jackson / Rose Johnstone, b. c.1893, d. 12 Nov 1974, C7759/1974), give the parents as
   recorded (Robert Jackson, Millie Jackson), cite the marriage C2254/1919, cite **ITM732477 /
   SRS4429/1/12474 / file 8R/119** directly, and **frame the enquiry on the Wide Bay–Burnett —
   Maryborough, Childers/Isis, Dallarnil, Miriam Vale/Colosseum — not Rockhampton.** Ask them to
   confirm or exclude.
3. **Buy George Johnston's death certificate (C2621/1895).** Now that the identification is proven,
   this is the one document that will say where he was born and how long he had been in the colony,
   and it unlocks the whole Johnston line. Cross-check against Robert Johnston's (C1596/1880).
4. **Order the GRO marriage certificate for Curtis × Barratt, Dec qtr 1859, St Austell, 5c/260** —
   confirms or kills "William Curtis" and "William Barratt" in one page, and names the witnesses.
5. **Buy Thomas Curtis's (C293/1898) and Elizabeth Ann Curtis's (C4383/1911) Queensland death
   certificates** — birthplaces, ages, years in the colonies, and the years-in-South-Australia figure
   that would resolve the 1863-vs-1872 tension in §3d.
6. **Test the 1914 lead**: birth B37002/1914 and death B19826/1914. Cheap, and it either connects Rose
   to a documented event or removes it.
7. **Find Jacqueline's child.** The 1949 divorce report says there was one child and that Jacqueline
   had custody. A Queensland birth search 1944–47 for a Josefski born to Jacqueline would name Shane's
   father's first cousin. Also identify and order the QSA Supreme Court matrimonial-cause file for
   *Josefski v Josefski*, Rockhampton 1949.
8. **Jacqueline's second marriage** is the biggest remaining gap in the forward tree. Best free
   levers: Trove 1950–54 Morning Bulletin for a JOSEFSKI or JOHNSTONE engagement/marriage notice at
   Rockhampton; the Rockhampton electoral rolls; and a Ryerson given-name search on "Jacqueline"
   restricted by location. Her Rockyettes career ends in the digitised record in 1953 — a marriage
   around then is the likeliest explanation.
8a. **Fetch NAA B883 for JOSEFSKI Lawrence Aubrey Q138061** — free, and its next-of-kin entries
   1943–46 may name the child.
8b. **Contact the Find a Grave contributor who created Mafalda's memorial** (member 49949980,
   memorial 251233434, created March 2023) — almost certainly a Rockhampton local holding the family
   notice.
8c. **Cross-check the Rockhampton BARTLEM notices** (Ryerson shows several 2015–2025) against
   Mafalda's five children — **Jason, Devon, Adrian, Shaun and Edwina Bartlem** — to complete that
   branch.
9. **Free FamilySearch account** would unblock three things at once: the 1841 Biscovey census, the
   Tywardreath Barrett household, and the Wesleyan/Methodist registers for St Blazey and Par (Thomas
   Curtis's baptism is missing from the Anglican register — near-universal for Cornish miners).
10. **Chase Joseph Normanton at St Blazey** (Richard Normanton bapt. 1832, son of Joseph and
    Elizabeth). If Jane, born Malta c.1817, is Joseph's daughter, the British Army / Royal Navy Malta
    garrison chaplains' returns (TNA RG32–33, free-indexed on FamilySearch) should hold her baptism —
    the clean primary proof of "Jane Normanton".
11. **Trove the South Australian shipping columns for 1863** (South Australian Register, South
    Australian Advertiser) for a Curtis arrival. With Passengers in History decommissioned this is the
    only remaining free route to the 1863 landing.
12. **Ask Carmel Schleger** (Phonse and Rose's daughter, an Indigenous consultant) what the family
    holds — now with the corrected geography (Maryborough / Childers / Dallarnil / Colosseum), the
    corrected registration spelling (JOHNSTON), the "Toby" nickname, the Josefski marriage and divorce,
    and Rose's station-garden prizes as conversation openers.
13. **When a paid subscription is acceptable**, the Queensland electoral rolls 1903–1919 on Ancestry
    are the highest-yield paid source for Robert and Millie Jackson.
14. **Order QSA inquest file 132/1895** (George Johnston) — Open Access, cheap copy order.

---

## 8. Technical notes (additions to the earlier reports')

- **The Queensland BDM search API silently ignores `fathersname`, `mothersname` and `spousename`.**
  `POST https://www.familyhistory.bdm.qld.gov.au/search` with those fields set returns *exactly* the
  same count as with them blank (e.g. "Jackson births with father Robert" = 1,720 = all Jackson
  births). A blank `subjectfamilyname` returns the whole index capped at 10,000 rows and will silently
  eat a session. **Method that works: pull the complete set for a surname once, cache it as JSONL, and
  filter locally.** Script: `sources/yola-rose/qbdm_pull.py`, wrapping the pass-2 `sources/qbdm.py`.
  Index cut-offs unchanged: births to 1924, marriages to 1949, deaths to 1994. The `regtype` letter
  (B / C / F) is a register series, not a district, and must not be read as a place.
- **Queensland State Archives name indexes are open data and can be scanned in bulk, with no captcha.**
  `GET https://www.data.qld.gov.au/api/3/action/package_search?q=organization:queensland-state-archives&rows=200`
  lists **128 datasets**; `package_show?id={name}` gives the resource URLs. 57 are name-level CSVs —
  inquests, wills, orphanages, reformatories, hospitals, gaols, immigration, land selections, teachers,
  pensions, indigence, outdoor relief, deed polls, divorces, the **Aboriginal War Census 1915–16** and
  the **Australian South Sea Islanders 1867–1948** index among them. Downloading the lot is ~450 MB.
  `sources/yola-rose/qsa_csv_scan.py` scans every CSV at once for a surname regex plus an optional
  given-name regex, normalising the wildly inconsistent headers ("Last name" / "LAST Name" /
  "LAST NAME" / "Last Name"; "Given names" / "Given name/s" / "Given Names"). Far faster and far more
  complete than the ArchivesSearch UI.
- **Downloading a digitised QSA register page.** Every CSV row carries a **Digital Image ID**;
  `https://www.archivessearch.qld.gov.au/api/download_file/{DID}` returns the whole scanned volume as a
  PDF (or a single JPEG for small items), with no captcha and no session. Volumes run 25–75 MB and
  100–160 pages. Where the CSV has a "PDF page" column, use it; where it gives only a register "Page",
  **calibrate** — render one page, read the printed folio number, and interpolate. Two worked examples
  from this pass: *Applications by Selectors* LAN/P56 is **two register pages per PDF page** (register
  2744 = PDF page 22); the 1908–09 pension register is **PDF page = register page + 3**. Render with
  `pdftoppm -r 150 -f N -l N -png file.pdf out` — note pdftoppm zero-pads the page number in the
  output filename (`out-085.png`, not `out-85.png`).
- **Trove's undocumented web API does honour quoted exact phrases** in `terms`, contrary to what pass
  3's note implies: `"Yola Rose"` returns 14, `Yola Rose` returns 2,877. Relevance ranking degrades to
  near-matches after the exact hits, so always read the returned `snippets` rather than trusting
  `totalRecords`. Multi-word *unquoted* queries remain OR-weighted and are only usable with a
  newspaper filter applied locally. `limits={"decade":["191"],"year":["1919"]}` works. Helper:
  `sources/yola-rose/tq.py` — prints hits with snippets, filters by a newspaper-name regex, and appends
  everything to `trove-hits-yola-rose.jsonl`; article text via `trove_yr.text(id)`.
- **Trove newspaper coverage that matters for this family**: Maryborough Chronicle 1860–1947, The
  Colonist (Maryborough) 1884–1952, The Alert (Maryborough) 1899–1939, Isis Recorder (Childers) from
  1931, Bundaberg Mail & Burnett Advertiser, Bundaberg Daily News & Mail 1925–1942 → Bundaberg
  News-Mail 1942–1961, Gympie Times, Morning Bulletin (Rockhampton) 1878–1965. The Isis Recorder
  starts only in 1931, which is why the Apple Tree Creek years are thin.
- **FreeBMD**: Cornwall county id is `CON,59,61`; **St Austell district id is 118**. A volume/page
  cross-search (set vol and page, no spouse) is the reliable way to confirm both halves of a marriage.
  Watch the **Barratt / Barrett** split — the GRO index has this family under BARRATT.
- **FreeCEN2 Cornwall coverage**: 1841, 1851, 1861, 1871, 1881, 1891 and a partial 1901. **No 1911.**
  And two specific holes that matter here: **no 1841 coverage for the Fowey district (St Blazey)**, and
  **no Tywardreath for 1841 or 1851**.
- **Cornwall OPC** (`opc-cornwall.org` / `cornwall-opc-database.org`): parish names invert — use
  `"Blazey, St."` and `"Austell, St."`; **Par is a separate parish from 1849**. Coverage is uneven —
  the St Blazey Curtis baptism set 1820–1850 holds only three records, so absence there is not
  evidence of absence (Wesleyan registers are the likely explanation for Cornish miners).
- **genealogySA** (`genealogysa.org.au`): the free index table renders only if `page_no` is set to
  `1` — leaving it blank returns an empty page.
- **NAA RecordSearch**: the `B2455` series titles embed place of birth, place of enlistment and next of
  kin, so a keyword search of the form `B2455 "<surname> QLD"` **enumerates** every
  Queensland-connected WWI dossier under that spelling. That turns "is there a service record for
  brother X?" from an open-ended question into a closed one. Same `curl_cffi` mechanics as pass 3.
- **`requests` / `beautifulsoup4` / `curl_cffi` are not installed system-wide on this machine** and the
  Homebrew Python is PEP-668 externally-managed. Build a throwaway venv:
  `python3.13 -m venv venv && ./venv/bin/pip install requests beautifulsoup4 curl_cffi lxml`.
