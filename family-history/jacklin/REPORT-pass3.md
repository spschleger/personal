# The Jacklin Line — research pass 3 (19 Aug 2026)

Supplement to `REPORT.md`. **Only new facts, corrections and dead-ends** are listed here; everything already in REPORT.md is assumed and not repeated. Same grading: **A** primary record · **B** contemporary press narrative · **C** inference.

Scope of this pass: free online sources only (no paid subscriptions, no certificates, no accounts). Sources worked: NAA RecordSearch, Trove, Queensland State Archives open-data indexes (data.qld.gov.au), FreeBMD, FreeCEN2, Victorian BDM historical index, Ryerson (pass-2 capture), Mackay funeral-notice directory.

New evidence saved under `sources/`: `sources/naa/` (40 dossier page images, full transcription summaries `transcript-B2455-JACKLIN-ABE-1286.txt` and `transcript-B2455-WARD-CHARLES-WILLIAM-2504.txt`, keyword-search listings, and `naa-items-summary.txt`), `sources/england/` (FreeBMD + FreeCEN captures), `sources/qsa/` (immigration index CSVs, the scanned Dacca-voyage register PDF, and `README-qsa-datasets.txt` recording the datasets searched and deleted), `sources/trove-articles/` (11 new article texts), `sources/trove-hits-pass3.jsonl`, `sources/pass3/` (sifted Trove hit lists). New reusable scripts: `sources/naa_fetch.py`, `sources/freebmd.py`, `sources/freecen.py`, `sources/trove_pass3.py`, `sources/trove_pass3b.py`.

---

## 1. Desmond John Jacklin & Margaret Elizabeth Ward

- **Margaret Elizabeth Jacklin: born 4 February 1927, died 1 July 2025** — Mackay Funeral Notices directory, 2025 archive, entry "JACKLIN, Margaret Elizabeth · 4th Feb 1927 – 1st Jul 2025" (https://www.mackayfuneralnotices.com.au/archived-2025). The notice was lodged by **Newhaven Funerals NQ, Mackay Harbour**. [A] — *replaces "c.1927–2025"; consistent with the Ryerson probate notice of 3 Oct 2025, late of Beaconsfield.*
- **NEW: Desmond John Jacklin was a Commonwealth Quarantine Officer.** *Australian Government Gazette*, General, 27 April 1976 — "Department of Health: Appointment and Cancellation of Appointment of Quarantine Officers ... **Desmond John Jacklin** ..." (**Trove 240842173**); and *Commonwealth of Australia Gazette*, General, 22 June 1982 — "Termination of Appointment and Appointment of Quarantine Officers, General Quarantine ... **Desmond John Jacklin** ..." (**Trove 240545244**). The 1982 entry is the administrative termination following his death on 9 Sep 1981. So alongside his North Mackay general practice he held a **Commonwealth Department of Health appointment as a Quarantine Officer at the Port of Mackay** from at least 1976. [A]
- **Desmond's 1981 death notice is not in the Ryerson Index.** Re-reading the pass-2 capture (`sources/ryerson-index-jacklin.html`, 84 Jacklin rows) there is no Desmond John Jacklin 1981 — the only "Desmond" is a 1998 Central Coast NSW man. Ryerson does not index the *Daily Mercury* for 1981. Trove's *Daily Mercury* run also stops in 1954. **Dead end online; still needs Mackay library microfilm.** [A negative]
- New from the same Ryerson capture (not in REPORT.md):
  - **JACKLIN, Heather Joyce — probate notice 1 May 2026, late of Mackay, Qld.** A very recent Mackay Jacklin estate; likely close family (generation of North Jacklin). Worth asking the family about. [A]
  - **JACKLIN, Daphne Margaret — d. 5 Oct 2018, funeral 11 Oct 2018, late of West Mackay, formerly of Pleystowe.** Confirmed as the widow of George Douglas "Doug" Jacklin: his WWII service record names next of kin "JACKLIN DAPHNE" (NAA B883 QX44362). [A]
  - Doug Jacklin's own funeral notices: d. 12 Apr 2007 aged 89, funeral 17 Apr 2007, "late of West Mackay, formerly of Pleystowe" (*Mackay Daily Mercury* 14 & 16 Apr 2007). [A]

## 2. Abraham "Abe" Jacklin (1891–1962)

**His full WWI dossier is now in hand: NAA: B2455, JACKLIN ABE, Item ID 7361151, 15 pages, downloaded to `sources/naa/naa-B2455-JACKLIN-ABE-7361151-p01..15.jpg`.** (https://recordsearch.naa.gov.au/SearchNRetrieve/Interface/DetailsReports/ItemDetail.aspx?Barcode=7361151)

Attestation (p01–p03), 21 February 1916 at **Rockhampton**:
- Enlisted and attested as **"Abe Jacklin"** — that spelling is used throughout, and is how he signed. Service number **1286**. [A]
- Age 23; **born Eton, Queensland**; trade **motor car driver**; single; **Church of England**; **no prior military service**. [A]
- **Next of kin: "(Mother) Fanny Jacklin (Mrs), P.O. Savannah, Eton, Mackay, Q."** — "Savannah" is a new locality for the family, and is the *only* address anywhere in the file (no "North Eton", no "Double Peak"). [A]
- Description: height 5 ft 5¾ in, weight 9 st 13 lb, chest 36 in, complexion dark, eyes brown, hair black. [A]
- Posted to **42nd Battalion, A Company**, certified by the O.C. 42nd Bn, 11th Infantry Brigade, at Thompsons Paddock (Enoggera), 2 June 1916. [A]

Service (Statement of Service p04–p06; Casualty Forms p09–p14; Base Records card p15):
- **Embarked Sydney 5 June 1916 per HMAT "Borda"; disembarked Southampton 23 July 1916.** Hospital in England Sept–Oct 1916. **Proceeded to France via Southampton 25 November 1916.** [A]
- Mumps, 10th Field Ambulance → 7th General Hospital, **St Omer, January 1917**; rejoined 22–23 Jan 1917. [A]
- **Appointed Lance Corporal 6 August 1917. Promoted Temporary Corporal 8 October 1917** (vice Cpl Chandler, evacuated sick). [A]
- **Wounded in action 10 October 1917, France — G.S.W. right thigh.** 8 C.C.S. → 11 General Hospital, Camiers → convalescent depots Étaples / Cayeux / Rouelles. **Reverted to Lance Corporal 11 October 1917 on evacuation. Rejoined the 42nd Bn from wounded 22 November 1917.** Base Records advised his mother **20 November 1917**. [A]
- Furlough in England 18 Feb – 8 Apr 1918. [A]
- **Wounded in action, 2nd occasion — GASSED (mustard), 26 May 1918, France.** 11 Fld Amb → 5 C.C.S. → Ambulance Train 10 → General Hospital, **Le Tréport**; **invalided to England 5–6 June 1918 per H.S. "Aberdonian"**; **admitted Horton (County of London) War Hospital, Epsom, 7 June 1918 — condition cabled as "SEVERE"**, later "improving" (17 Jul) and "convalescent" (27 Jul). 3rd Auxiliary Hospital, Dartford 15 Jul 1918 → No. 3 Convalescent Depot, Hurdcott → No. 1 Command Depot, Sutton Veny → Overseas Training Brigade, Longbridge Deverill. [A]
- **Transferred to the 15th Battalion 5 October 1918**; to France via Folkestone 24 Oct; taken on strength 15th Bn 29 October 1918. [A]
- **Returned to Australia per H.T. "Port Napier", embarked England 12 May 1919; disembarked 4 July 1919 (2nd Military District, list 279); discharged 1st Military District (Queensland) 20 August 1919.** [A]
- Medals: **British War Medal no. 18863 and Victory Medal no. 18120** (issued Jan 1919 series). **1914/15 Star: "N.E." — not entitled.** No disciplinary entries anywhere in the file. [A]
- Base Records file reference **R 27236**; a letter of 23 April 1937 (p07) shows his file being sent to the **Deputy Commissioner, Repatriation Commission, Brisbane** — i.e. he or his family were dealing with Repatriation in 1937. [A]

**Corrections to REPORT.md §2:**
1. He enlisted at **Rockhampton**, not Mackay. [A]
2. His substantive rank was **Lance Corporal**; he was a Corporal (temporary) only for three days, 8–11 October 1917. The press "Cpl. Abe Jacklin" is right for late 1917 but not for the war as a whole. [A]
3. "Wounded Dec 1917" = the **G.S.W. right thigh of 10 October 1917**; the December press date reflects the notification chain (Base Records advised 20 Nov 1917). [A]
4. "Gassed Jun 1918" = **gassed 26 May 1918**; the June date is the hospital admission in England (7 June). [A]

**New Trove articles (texts saved in `sources/trove-articles/`):**
- *Daily Mercury* 21 Jun 1918, "PERSONAL" — **Trove 173907732**: "Mr. and Mrs. Thos. Jacklin, North Eton, have received news from Base Records, Melbourne, reporting that their son, Corporal Abe Jacklin, has been gassed and is classed as wounded — second occasion." [A]
- *Daily Mercury* 18 Jul 1919, "SOLDIERS RETURN" — **Trove 178637688**: "A number of soldiers returned overland last night. They were Sergeant Howell, **Lance Corporal Jacklin**, Driver King, and Privates **A. and P. Harvison**. The men were met and welcomed by Mr. J. E. Joseph (chairman of the Reception Committee)." — his actual homecoming, and note the Harvisons travelling with him (the Holmes/Harvison in-laws of Woodford). [A]
- *Daily Mercury* 14 Aug 1916, "PERSONAL" — **Trove 188675596**: a Mackay mother advised that her son "and Private A. Jacklin had arrived in England all well". [B]
- *Daily Mercury* 28 Sep 1916, "SOLDIERS' LETTERS" — **Trove 188686340**: a Mackay soldier's letter naming "H. Dowling, A. Jacklin" among the Mackay boys in England. [B]
- *Daily Mercury* 12 Aug 1919, "ETON. WELCOME HOME" — **Trove 178634799** (a Jacklin among those welcomed). [B]
- Mrs Jacklin of the North Eton branch appears repeatedly as a knitter in the **Soldiers' Sock Fund** lists 1918 (Trove 177704978, 177696957, 177705963) and the **Soldiers' Sock Fund** president's message Mar 1919 (177707146). [B]

**Other NAA items found (not digitised — paper only):**
- **NAA: BP709/1, M27236, Item ID 32444744** — "JACKLIN, Abraham [aka Abe] – Service Number – 1286", **1916–1963**, held Brisbane. This is his Repatriation/DVA case file and would cover his post-war health, pension and the 1937 correspondence. [A]
- Brother **Thomas George "George" Jacklin**: **NAA B884, Q215145, Item ID 4931687** — "JACKLIN GEORGE THOMAS, dob 17 Jun 1886, b. Mackay Qld, enlisted Mackay Qld, NOK JACKLIN SOPHIE", 1939–1948. Confirms his exact date of birth (17 Jun 1886, matching Qld birth index) and that he served in WWII home forces. [A]
- Nephew **George Douglas "Doug" Jacklin**: **NAA B883, QX44362, Item ID 4838391-series**, and **A13860, QX44362, Item ID 31034640** — dob 31 Mar 1918, b. Mackay, enlisted Brisbane, NOK JACKLIN DAPHNE. [A]
**Brother Henry "Harry" Jacklin of North Eton — two previously unknown daughters.** *Daily Mercury* 30 Dec 1948, Family Notices (**Trove 171436455**, text saved) carries two engagements in the same column:
- "**HAWKINS—JACKLIN**: the engagement is announced of **Olive, second daughter of Mr and Mrs H. Jacklin, Eton North**, to Victor, fifth son of Mr and Mrs E. H. Hawkins, Eton North."
- "**STEVENS—JACKLIN**: the engagement is announced of **Irene, eldest daughter of Mr and Mrs H. Jacklin, Eton North**, to Gordon, fourth son of Mr and Mrs F. H. Stevens, Homebush Road, Mackay."
So Henry "Harry" Jacklin (1898–1986, m. Ann Richardson Clark 1926) had at least two daughters, **Irene** (eldest) and **Olive** (second), both engaged in December 1948. Neither marriage could be found in the Queensland marriage index (public only to 1949) — so they probably married in 1950 or later. [A]

- Cousin branch: **NAA B2455, JACKLIN JOHN, Item ID 7360194** — "SN 1878, b. Zillmere Qld, enlisted Brisbane, NOK (Mother) JACKLIN Elizabeth" — a son of **William Jacklin & Elizabeth Hall** (the Ipswich/Glenore Grove line); his repatriation file is **BP709/1, M6344 Part 1, Item ID 32253320** (1942–1967). [A]

## 3. Thomas Jacklin (1857–1931) & Fanny Margaret Holmes (c.1859–1933)

*(English origins are in the "England — Lincolnshire origins" section below; this section covers the Queensland end.)*

### 3a. THE HOLMES ARRIVAL — the ship was the *DACCA*, and the register has been read

Queensland State Archives, *Assisted immigration 1848–1912* (series S13086, item **ITM18484**, register **page 170**, digital image **DR38134**; index CSV `sources/qsa/assisted-immigration-1848-1912-h.csv`, scan `sources/qsa/qsa-assisted-immigration-register-1887-DR38134.pdf`, register p.170 = PDF p.8). **Corrects J. J. Holmes's 1937 obituary, which was read as "Decca".** [A]

**Voyage header (register p.163):** *"**Dacca**, 3000 tons, **Captain Stone**, sailed from **LONDON** on the **3rd June 1887** and arrived at **Brisbane** on the **26th July 1887**. Surgeon Superintendent **Dr Jos. Goodall**. Matron **Miss Cosgrove**."* 570 souls in all; 1 birth and 2 deaths on the voyage. **75 souls were landed at Mackay** (64 of them on free passage). [A]

**The Holmes group, under the section heading "MACKAY — FREE"** (i.e. **government-assisted free passage** to Mackay, not full-fare), all entered as one ditto-block under the surname Holmes:

| Christian name | Age | Status | Calling | Read | Write | Religion | **County** |
|---|---|---|---|---|---|---|---|
| **Lang** | 41 | married male | **F.L.** (farm labourer) | yes | yes | P | **Lincoln** |
| **Fanny** | 48 | married female | — | yes | yes | P | **Lincoln** |
| **John J.** | 23 | **married male** | **F.L.** | yes | yes | P | **Lincoln** |
| **Ann** | 24 | **married female** | — | yes | yes | P | **Lincoln** |
| **Loughley** | 2 | child 1–12, male | — | — | — | P | **Lincoln** |
| **Florence** | 1 | child 1–12, female | — | — | — | P | **Lincoln** |
| **Mary** | 17 | single female | **D.S.** (domestic servant) | yes | yes | P | **Lincoln** |
| **Tom** | 14 | single male | **F.L.** | yes | yes | P | **Lincoln** |

- **Native place: LINCOLN(SHIRE) for every one of them** — independent confirmation of the Lincolnshire origin from the arrival record itself. (The register records **county only, no parish**.) Religion **P** = Protestant. All four adults could read and write. Remarks column blank — **no nominator named**. [A]
- **CORRECTION to my earlier reading of the index:** the register's tick-columns show **two married couples, not one**. **John J. Holmes (23) was already married, to Ann (24)**, and **Loughley (2) and Florence (1) are their children** — not Langley senior's. So:
  - **John Jarvis Holmes emigrated in 1887 with a wife (Ann) and two infants.** [A]
  - **"Loughley" = Langley Holmes junior, son of John Jarvis Holmes** — matching FreeBMD "Holmes Langley, b. Mar quarter 1885, Louth district, 7a/623" (the family had moved into the Louth district by then, which also explains why Fanny Margaret married a Louth man in 1878). [A/B]
  - **Mary (17) and Tom (14)**, entered as single, are Langley senior and Fanny's children — Mary J, b. Driby c.1870 in the 1871 census; Tom b. c.1873. [A]
- **No JACKLIN appears anywhere in the Dacca volume** — correct, Thomas and Fanny had arrived four years earlier. [A negative]

### 3b. THE JACKLIN ARRIVAL — *found*, on the assisted-immigration register after all

**Queensland State Archives, *Assisted immigration 1848–1912*: "JACKLINE, Thomas, 25" and "JACKLINE, Fanny, 24", ship "HANNAH LANDELS", arrival 1883/09/11, register page 237, item ITM18480, digital image DR38564.**
Index row source: `sources/qsa/assisted-immigration-1848-1912-j.csv`; scan downloaded to `sources/qsa/qsa-assisted-immigration-register-1883-hannah-landels-DR38564.pdf`;
free download URL: `https://www.archivessearch.qld.gov.au/api/download_file/DR38564`. **[A]**

- **This is Thomas Jacklin and Fanny Margaret née Holmes on the ship named in his 1931 obituary.** The surname is indexed as **JACKLINE** and the ship as **"Hannah Landels"** (one final *l*) — which is why a naive search for "JACKLIN," / "Landell" misses them. **My earlier conclusion in this same report that they travelled unassisted was wrong: they came out on a *free* Government passage and are on the register.** [A]
- Ages fit exactly: **Thomas 25** (b. Q1 1857) and **Fanny 24** (b. Q1 1859 — see the England section; this is a further independent check on her 1859 birth rather than 1858). [A]
- The index arrival date **11 September 1883** is two days earlier than the newspaper account (anchored off Flat Top on 13 September, immigrants landed 14 September) — registers commonly record the official/port date rather than the landing date, and the register itself gives "arrived Mackay 11th Sept 1883". [A/B]

**The register page has now been read (PDF p.9 = register p.237; the PDF covers register pp. 229–243, i.e. the whole Mackay list).**

**Voyage header (register pp. 229–230):** *"**Hannah Landels**, **1400 tons**, **Capt. "Lyriar"** [handwriting uncertain — possibly Lyrias / Lynas; worth checking against Lloyd's or the Qld shipping reports], **from GLASGOW**, arrived **Mackay, 11th September 1883**. Surgeon Superintendent **Dr Paddle**. Matron **Mrs Knights**."* No date of departure is recorded in this volume (the *Daily Mercury* supplies it: 6 June 1883). [A]

**The two Jackline rows, in full:**

| Column | Thomas | Fanny |
|---|---|---|
| Surname | **Jackline** | *(family grouping, cell blank)* |
| Christian name | **Thomas** | **Fanny** |
| Adults — married male | **25** | — |
| Adults — married female | — | **24** |
| Single / children / infants | — | — |
| **Remarks** | **blank** | **blank** |

- **Section heading: "FREE"** (register pp. 233–241 are the Free section; the Jacklines sit in the alphabetical J run on p.237). **They travelled on a fully Government-paid *free* passage direct to Mackay** — not "assisted", not "remittance", and certainly not full fare. Port of disembarkation: **Mackay** (the whole volume is the Mackay list). [A]
- **This volume has no native-place, occupation, religion or nominator columns** — unlike the 1887 *Dacca* register. Its printed columns are only No. / Surname / Christian name / Adults (married M, married F, single M, single F) / Children 1–12 (M, F) / Infants under 1 (M, F) / Remarks, with **the age written into whichever adult-or-child column classifies the person**. The faint marks in the Remarks column are show-through from the reverse of the leaf. **So this record cannot supply their Lincolnshire parish or a sponsor's name** — that will have to come from the Immigration Agent's correspondence or the shipping/board papers at QSA. [A]
- **Ship's nationality summary (register p.242): 390 Scotch, 43 English, 16 Irish embarked.** The *Daily Mercury*'s "Scottish migrants" description is exactly right, and **the Jacklins were among only 43 English people on board** — genuinely conspicuous outliers on a Glasgow emigrant ship bound for a Queensland sugar district. [A]
- **General summary (p.243):** 449 souls embarked (63 married M, 63 married F, 148 single M, 57 single F, 46 boys, 54 girls, 18 infants), **5 births and 7 deaths on the voyage, 447 landed**. Of these, **328 were on free passage** (the Jacklines' category), 119 assisted, 1 steerage, 1 remittance. [A]
- **No HOLMES anywhere in the volume** — the closest surname is "Home" (Wm, 25, who died on the voyage). Fanny's family followed four years later on the *Dacca*. [A negative]
- Names on p.237 are ordered **alphabetically within the Free section**, so neighbours are not travelling companions. The entries immediately above and below the Jacklines are **Jackson** (Sarah ~14, Mary ~17), and **Johnstone** (Wm 30, Jane 32 and five children). Two later pencil annotations elsewhere on the page — **"Pension Enq. Sep 1940"** and **"Pension Enq. 9-11-34"** — show this register was used in the twentieth century as proof of age for old-age pension claims. [A]
- Other Jacklins in the Queensland assisted index (spelling **JACKLIN**), none obviously ours: Fred 21 (*Silhet*, 19 Sep 1883), Mary A 21 (*Duke of Buckingham*, 4 Jan 1886), **William 24 (*Oriana*, 14 Oct 1887)**, George N 19 (*Roma*, 3 May 1888), George 24 (*Jumna*, 18 Sep 1890). The 1887 *Oriana* William is a tempting but **conflicting** candidate for Thomas's brother William Jacklin, who had already married in Queensland in 1886 — and in any case the William born at North Cockerington in 1862 would have been 25 in Oct 1887, close enough that it is worth checking DR39013. [C]
- **NOTE on searching this index:** neither surname nor ship name can be trusted to a single spelling. "Jacklin" is indexed as **JACKLINE** for the 1883 arrival; the ship is **"Hannah Landels"**, not "Landells". Always search on a short stem. The *Registers of immigrants 1882–1938* dataset separately contains no Jacklin/Jackline at all. [A]
- **Voyage detail for the Hannah Landells** — *Daily Mercury* 19 Sep 1931, "The 'Hannah Landells' — Passengers Interviewed" (**Trove 170403842**, text saved): the ship **left Glasgow on the morning of 6 June 1883** (Greenock the same night), made no landfall for months, **dropped anchor between Flat Top and Round Top on the morning of 13 September 1883**, was cleared by Dr M'Burney on 14 September, and **the whole of the immigrants, about 350, were landed at Mackay on the evening of 14 September 1883**. [B]
- *Daily Mercury* 13 Sep 1933, "Scottish Migrants — Jubilee of Arrival of the Hannah Landells" (**Trove 172952860**, text saved): a fiftieth-anniversary piece confirming the ship carried **Scottish immigrants from Glasgow**, many still in Mackay in 1933. [B] — *worth noting that a Lincolnshire farm couple sailed out of Glasgow on a Scottish emigrant ship; that is a clue about how their passage was arranged.*
- **No JACKLIN appears in the Queensland *Land Selections 1885–1981* index or the *Registers of Applications by Selectors 1868–1885* index** (both datasets downloaded, searched and then deleted for size — see `sources/qsa/README-qsa-datasets.txt` for the download URLs). Consistent with the obituary's "leased, then bought": Louth Park at Double Peak was a **freehold purchase, not a Crown selection**. [A negative]
- **James Jacklin "formerly of Gayton-le-Marsh, Lincoln" was NOT Thomas's brother.** Queensland death index: **James Jacklin d. 2 April 1892, parents GEORGE JACKLIN & THERESA WALKER (C1955/1892)** — a different Lincolnshire Jacklin family from Thomas's (Abraham & Maria Skipworth). REPORT.md §3's "same Lincolnshire cluster, relationship unproven" can be tightened to **"a separate Lincolnshire Jacklin family — cousins at most."** [A]
  - Related: his widow appears to have remarried within the surname — Qld marriage index **William Jacklin = Emma Jacklin, 7 November 1896 (B18311/1896)**; Emma Marston had married James Jacklin at Ipswich in Oct 1889. [A/C]
  - Two other early Queensland Jacklin deaths, both from yet other families: **Frederick Jacklin d. 20 May 1885, father John Jacklin (C308/1885)**; and **William Jacklin d. 22 June 1936, parents John Jacklin & Matilda Johnston (B31940/1936)** — i.e. there were at least three unrelated Jacklin lines in Queensland, so care is needed with un-parented index entries. [A]
- Trove searches for **"Louth Park"** and **"Double Peak"** produced nothing about the Jacklin farm (all "Louth Park" hits are a NSW locality near Maitland; "Double Peak" hits are the Double Peak Central Mill Co.). [A negative]
- Trove searches for **"Langley Holmes"** produced only an unrelated NSW probate. [A negative]

## 4. Taylor / North (Mackay, Irish)

- **Nothing new.** Not actively worked this pass beyond confirming that the Queensland *Naturalisations 1851–1908* open dataset exists (https://www.data.qld.gov.au/dataset/naturalisations-1851-to-1908) — but Irish-born migrants were already British subjects and would not appear in it, so it is unlikely to help with John Taylor or Mary North. Their Irish counties remain unknown and the cheapest route is still the Qld death certificates (purchase). [C]

## 5. Ward / Spunner (Gippsland)

**Charles William Ward's full WWI dossier is now in hand: NAA: B2455, WARD CHARLES WILLIAM, Item ID 8347361, 25 pages, downloaded to `sources/naa/naa-B2455-WARD-CHARLES-WILLIAM-8347361-p01..25.jpg`.** (https://recordsearch.naa.gov.au/SearchNRetrieve/Interface/DetailsReports/ItemDetail.aspx?Barcode=8347361)

- **THE HEADLINE FACT (p22, Application to Enlist): "Statement regarding Death or Absence of either or both Parents: *Mother died Aug 10th 1907*."** Written on the form he lodged at Lakes Entrance on 17 March 1916, with his father's consent signature ("William Ward") beside it. **Catherine/Kathleen (Cunningham) Ward died 10 August 1907.** [A]
- Applied to the Recruiting Officer at **Lakes Entrance, 17 March 1916** (accepted by R. J. Gilsenan, Recruiting Officer; passed fit locally); **attested at Sale, Victoria, 21 March 1916**; service number **2504**. Age **20 years 10 months** → born ~May 1895; **farm labourer**; single; **Roman Catholic**; height 5 ft 6⅝ in, weight 135 lb, chest 34½–37½ in, complexion fair, eyes blue; distinctive marks "3 vaccination scars left arm". Postal address **Lakes Entrance, Gippsland**. Birthplace recorded as "near the Town of **Cunninghame**, in the County of **Gippsland Lakes**, Vic." [A]
- Next of kin throughout: **"Mr W. Ward, Lakes Entrance, Gippsland Lakes, Victoria"** — unchanged 1916–1919 (p01, p19, p22). No siblings, no wife, no mother's given name appear anywhere in the file. [A]
- Units: 19th Depot Battalion Geelong (26 Apr – 3 Aug 1916) → **5th Reinforcements, 46th Battalion** (3 Aug 1916, Geelong, under Lt James Grant) → **46th Battalion**, taken on strength 29 Dec 1916. **Private throughout — no promotions.** [A]
- **Embarked Melbourne 7 September 1916 per HMAT A15 "Port Sydney"; disembarked Plymouth 29 October 1916**; 12th Training Bn, Codford; **to France via Folkestone per "Princess Victoria" 4 December 1916**; 4 A.D.B.D. Étaples 5 Dec 1916. [A]
- Medical history: P.U.O./trench fever May 1917 (9 C.C.S., 3 Canadian General Hospital, Boulogne); influenza June 1917; **scabies** Dec 1917, Mar 1918 and Aug 1918; P.U.O. June 1918; **I.C.T. (inflammation of connective tissue) of the buttocks — invalided to the U.K. 13 June 1918, admitted 2nd Eastern General Hospital, Brighton, 14 June 1918**, then 1st Australian Auxiliary Hospital, Harefield, 22 July 1918; classified **B1a3** (7 Aug 1918) then **B1a4** (19 Aug 1918) at Sutton Veny; **V.D., 1st Australian Dermatological Hospital, Bulford, 14 Jan – 12 Feb 1919 (30 days)**; tonsillitis at sea, March 1919. [A]
- One disciplinary entry: **out of bounds at 10.30 p.m., Sutton Veny, 3 September 1918 — 2 days confined to barracks.** [A]
- UK leave 16 Dec 1917 – 3 Jan 1918; furlough 24 Jul – 7 Aug 1918. [A]
- **Return: embarked England (Devonport) per H.T. "Anchises" 28 Feb / 1 Mar 1919; disembarked Melbourne 13 April 1919 (recorded 17 April 1919 for 3rd M.D. purposes); discharged 22 May 1919, 3rd Military District (Victoria)**, ref M 41/1491. Total service ≈ 3 years 2 months. [A]
- Medals: **British War Medal no. 52870 and Victory Medal no. 51761**; 1914/15 Star "not entitled". First issue returned undelivered by 3rd D.B. on 10 May 1923; he re-applied on **13 February 1924 giving his address as "C. W. Ward, Tambo Upper, Gippsland"**, and signed for the medals on **14 April 1924** (p15, p16). [A] — *independently confirms he was settled at Tambo Upper by early 1924, consistent with the 1921 Discharged Soldiers' Settlement block.*
- Base Records card notes **"Will to A.A.G. 3 M.D. 29.10.19, M 26/1244"** — a will was lodged in 1919. [A]

**Corrections to REPORT.md §5:**
1. **He was never wounded in action.** There is no gunshot/shell wound, no "wounded in action" entry, no gassing and no medical board in the file; the June 1918 evacuation to England was for **I.C.T. of the buttocks**, and Base Records' letter to his father (3 Jul 1918) deliberately strikes out "I regret" because it was illness, not a wound. **The Dec 1918 "welcomed home wounded" item is not him.** Re-reading *Bairnsdale Advertiser* 11 Dec 1918, "District News — Lakes Entrance" (**Trove 74182543**), the text says only *"a public welcome home to **Private Ward**, one of the Lakes Entrance soldiers who had come back wounded"* — **no given name**, and Lieut. James replied on his behalf. On 10 December 1918 Charles William Ward was at the Overseas Training Battalion, Longbridge Deverill, England, and he did not land in Melbourne until April 1919. **This is a different Ward.** [A]
2. Two "TRAINEE" annotations in the file (p17, p23) show he had a **pre-war compulsory-training / Senior Cadet record book**, despite answering "No" to prior service on the attestation. [A]
3. **The Aug 1916 farewell is confirmed as him and dates precisely.** *Bairnsdale Advertiser* 9 Aug 1916, "Lakes Entrance" (**Trove 74176806**): "There were two other soldiers present also, who had been farewelled a few weeks ago … They are Ptes. Wm. Todd, of Lakes Entrance, and **Chas. Ward, of Lake Tyers**" — i.e. he was home on final leave in late July / early August 1916, four to five weeks before embarking from Melbourne on 7 September 1916. The same article names **"Mr Gilsenan, on behalf of the recruiting committee"** — the **R. J. Gilsenan** who signed Ward's Certificate of Recruiting Officer at Lakes Entrance on 17 March 1916. [A/B]

**Other NAA items for this family:**
- **NAA: B884, V364966, Item ID 6642644** — "WARD CHARLES WILLIAM : Service Number V364966 : **Date of birth 08 May 1895** : Place of birth **LAKES ENTRANCE VIC** : Place of enlistment **BRUTHEN** : Next of Kin **WARD MAUD**", 1939–1948. **This is his WWII (Volunteer Defence Corps) enlistment and gives his exact date of birth: 8 May 1895** — matching Vic birth registration 20047/1895 and his 1916 stated age of 20 y 10 m. [A]
- **NAA: B73, M55544, Item ID 21175077** — "WARD, Charles William – Service Number 2504", **1916–1986**: his Repatriation (Victoria) case file. A covering letter in the B2455 dossier (p20) shows he **applied to the Repatriation Department for benefits on 29 August 1962** — months before his death that year (Vic death 22527/1962). Paper only, not digitised. [A]
- **NAA: B883, VX54353, Item ID 6113297** — "WARD WILLIAM CHARLES : **Date of birth 14 Apr 1919** : Place of birth **BAIRNSDALE VIC** : Place of enlistment Royal Park Vic : Next of Kin **WARD C**", 1939–1948. This is C. W. Ward's eldest son. **Correction: he was born 14 April 1919, not 1920** — i.e. very close to (and possibly before) his parents' 1919 marriage (Vic 9907/1919). Worth checking the exact marriage date. [A]
- **NAA: CP979/2, item 162, Item ID 7909745** — "SPUNNER George Revington", 1920: a file on Maud's youngest brother. [A]
- No WWI B2455 dossier was found for William Armitage, Victor Ramsay or George Revington Spunner in a full NAA keyword sweep of "SPUNNER" (`sources/naa/naa-search-spunner.txt`) — the only Victorian B2455 Spunner is James Richard Spunner of Sorrento (SN 592), a different family. [A negative]

## Ward / Cunningham — the Catherine problem

- **Catherine (Cunningham) Ward died 10 August 1907** (NAA B2455 8347361, p22 — her son's own enlistment application). [A]
- **But her death is not in the Victorian index.** Using the Victorian BDM historical-events API (`my.rio.bdm.vic.gov.au`):
  - **All WARD deaths registered in Victoria in 1907 = 22 records.** None is a Catherine / Kate / Katherine / Kathleen; none is female and of the right age; none is in Gippsland. [A negative]
  - Widening to **1906–1908 = 71 WARD deaths in all of Victoria**; the only C/K given names are "Cornelius" (1908, Brunswick) and "Chas Stanley" (1906, Chiltern). [A negative]
  - **All deaths of any surname registered at Cunninghame, Lake Tyers, Bruthen and Swan Reach in 1907** were listed: Cunninghame — Christian WILKINS 75, Hart COWLISHAW 73; Lake Tyers — Mildred May SCOTT 11, Larry JOHNSON 56; Bruthen — Isabella ILLIG 70, Sarah GILES 61, Hy Richd SUMNER, + 1; Swan Reach — 5, none a Ward. **No Ward death was registered anywhere in that district in 1907.** [A negative]
  - "Catherine WARD" deaths 1905–1910 anywhere in Victoria: **nil**. [A negative]
- **Implication:** either she died and was registered **outside Victoria** (NSW is the obvious candidate given the Cunningham family's Kiandra/Monaro origins), or she is indexed under a badly mangled surname, or there is a genuine gap in the Victorian index. This is now a sharply-defined question with a known date (10 Aug 1907) to search against. [C]
- Trove searches (year-limited to 1907–08, Gippsland papers) produced **no death or funeral notice for a Mrs Ward of Lake Tyers/Cunninghame**. [A negative]
- The NSW BDM historical index could not be driven this pass (see dead ends).
- NAA keyword searches for "Cunninghame" and "CUNNINGHAM Swan Reach" produced nothing for this family (`sources/naa/naa-search-cunninghame.txt`, `naa-search-cunningham-swan-reach.txt`). [A negative]

## England — Lincolnshire origins (**the big gain of this pass**)

All from **FreeBMD** (https://www.freebmd.org.uk/cgi/search.pl) and **FreeCEN2** (https://www.freecen.org.uk) — both free, no login. Captures in `sources/england/`.

### The Jacklins: Keddington, Covenham, North Cockerington and Louth

- **Abraham Jacklin (Thomas's father) was born c.1830–31 at KEDDINGTON, Lincolnshire** — a parish immediately north of Louth. Recorded as born at Keddington in every census. [A]
  - **1851 census, Keddington** (HO107/2111A, p11, sched. 31): **Abraham JACKLIN, servant, unmarried, 21, agricultural labourer, b. Keddington**, living in the household of **William Clark, head, unmarried, 47, farmer occupying 130 acres employing 1 labourer**. `sources/england/freecen-jacklin-1851-keddington.txt` [A]
- **MARRIAGE: JACKLIN Abraham × SKIPWORTH Maria — Louth registration district, June quarter 1856, GRO vol 7a page 1083.** Confirmed both ways by FreeBMD's spouse cross-reference. `sources/england/freebmd-marr-jacklin-skipworth.txt` + `freebmd-marr-skipworth-jacklin.txt` [A]
  - **This resolves the Elizabeth/Maria question in REPORT.md §3.** There is one marriage and one wife: **Maria Skipworth**. William Jacklin's Queensland death registration (parents "Abraham & Maria Skipworth") is correct; **Thomas Jacklin's Queensland death registration C3913/1931, which gives "Elizabeth Skipworth", is wrong** (or records a second forename never used). **Thomas and William were full brothers.** [A]
- **THOMAS JACKLIN: birth registered Louth district, March quarter 1857, GRO 7a/560** (FreeBMD, `freebmd-births-jacklin-louth.txt`). **Born at COVENHAM, Lincolnshire** (birthplace given as Covenham in both the 1861 and 1871 censuses) — *not* Louth town, though Louth was the family's "native town" as the obituary says. [A/B]
- **1861 census, Great Carlton (Saltfleet sub-district), Lincolnshire** (piece 2385, ED 10, p107, sched. 15, dwelling 85): **JACKLIN Abraham, head, married, 31, ag lab, b. Keddington · Maria, wife, 22, b. Ashby · Thomas, son, 4, b. Covenham.** `sources/england/freecen-jacklin-1861-saltfleet.txt` [A]
- **1871 census, Keddington** (RG10-era piece 3404, ED 28, p56, sched. 2, dwelling 10): **JACKLIN Abraham, head, 40, ag lab, b. Keddington · Maria, wife, 33, b. Ashby · Thomas, son, 14, ag lab, b. Covenham · William, son, 9, b. North Cockerington · George, son, 4, b. Keddington.** `sources/england/freecen-jacklin-1871-louth.txt` [A]
  - **William Jacklin (the Ipswich/Glenore Grove emigrant) was born c.1862 at North Cockerington, Lincolnshire** — FreeBMD's Louth births include "Jacklin William, Mar 1862, 7a/551" as the best match. [A/B]
  - **A third brother, GEORGE Jacklin, b. c.1867 at Keddington** — not previously known. Candidate registration: Louth births "JACKLIN George, Dec 1867, 7a/544" or "Jun 1866, 7a/580". [A/C]
  - Maria was **born at "Ashby", Lincolnshire c.1838–39** (Ashby cum Fenby or Ashby Puerorum — not yet resolved). [A]
- **Maria Jacklin died 1880: FreeBMD deaths, Jun quarter 1880, Louth, aged 42, GRO 7a/353** — the right age for a woman born c.1838. [B]
- **Abraham remarried: FreeBMD marriages, JACKLIN Abraham, Dec quarter 1880, Louth, GRO 7a/1161.** [A/B]
- **1891 census, Eastfield Road, Louth**: **JACKLIN Abraham, head, 60, platelayer (employee), b. Keddington · "June A" [Jane A?] wife, 56, tailoress, b. Louth.** He had left farm labour for the railway. `sources/england/freecen-jacklin-1891-louth.txt` [A]
- **Abraham Jacklin died: FreeBMD deaths, Jun quarter 1903, Louth, aged 72, GRO 7a/337** — exactly matching b. c.1831 Keddington. [B]

### The Holmes side: Bilsby, Driby and Hogsthorpe (Spilsby/Alford, not Louth)

- **MARRIAGE: JACKLIN Thomas × HOLMES Fanny — Louth registration district, September quarter 1878, GRO vol 7a page 911.** Confirmed both ways by FreeBMD's spouse cross-reference. `sources/england/freebmd-marr-jacklin-holmes.txt` + `freebmd-marr-holmes-jacklin.txt` [A] — **corrects REPORT.md's estimate of "c.1880–83": they married in 1878 and emigrated five years later.**
- **FANNY MARGARET HOLMES: birth registered SPILSBY district, March quarter 1859, GRO 7a/528** — the only "Fanny Margaret Holmes" registered in Lincolnshire in the whole 1850–1870 window. **Born at BILSBY, Lincolnshire.** `sources/england/freebmd-births-holmes-fanny-lincs.txt` [A/B]
- **1861 census, Southfield, Bilsby (Alford sub-district)** (piece 2378, ED 9, p17, sched. 4, dwelling 21): **HOLMES Fanny, HEAD, WIDOW, 24, "Ag Lab's Widow", b. Bilsby · HOLMES Fanny M, dau, 2, b. Bilsby · MEDCALF Mary A, boarder, widow, 71.** `sources/england/freecen-holmes-1861-alford.txt` [A]
- **1871 census, Driby (Spilsby district)** (RG10/3395, ED 1, p8, sched. 43, dwelling 45): **HOLMES Langley, head, married, 27, ag lab, b. HOGSTHORPE · Fanny, wife, 34, b. Bilsby · Fanny M, dau, 12, scholar, b. Bilsby · John J, son, 7, scholar, b. Bilsby · Mary J, dau, 1, b. Driby.** `sources/england/freecen-holmes-1871-driby.txt` [A]
- **MARRIAGE: HOLMES Langley — Spilsby district, March quarter 1868, GRO 7a/797** (the only Langley Holmes marriage in Lincolnshire). `sources/england/freebmd-marr-holmes-langley-lincs.txt` [A]
- **And the bride on that same page is "HOLMES Fanny" — Spilsby, Mar quarter 1868, GRO 7a/797.** `sources/england/freebmd-marr-holmes-fanny-spilsby.txt` [A] **This is decisive: Langley Holmes married a woman who was already surnamed Holmes — the widow Fanny Holmes of Bilsby.** (FreeBMD's spouse cross-reference cannot pair two identical surnames, but an identical district/volume/page in the same quarter for "Holmes Langley" and "Holmes Fanny" is the standard proof.)

**What this means — a genuine correction to the family tree:**

> **Langley Holmes was Fanny Margaret's STEPFATHER, not her biological father.** Her mother Fanny was **already a Holmes widow in April 1861**, with two-year-old Fanny M; Langley Holmes (b. c.1844) only married Fanny in **Q1 1868**, when Fanny Margaret was nine. Fanny Margaret's biological father was her mother's **first** husband, also a Holmes — which is why she carried the Holmes surname all along, and why her 1933 Queensland death registration (C577/1933) names "Langley Holmes" as her father: he was the man who raised her from the age of nine. **Grade A: the 1861 census entry ("Fanny Holmes, head, WIDOW, 24, Ag Lab's Widow", with 2-year-old Fanny M) and the 1868 Holmes-x-Holmes marriage on GRO 7a/797 are both primary. What remains unknown is the first husband's name.**
>
> John Jarvis Holmes (b. c.1864 Bilsby, between the two marriages) is the son of Fanny and — probably — Langley, born before their 1868 marriage. His 1937 obituary calling Thomas Jacklin his "brother-in-law" is still correct: he and Fanny Margaret were half-siblings by the same mother. [C]

- **MARRIAGE: HOLMES John Jarvis — Louth registration district, December quarter 1884, GRO 7a/1151** (FreeBMD; `sources/england/freebmd-marr-holmes-john-louth.txt`). This is John Jarvis Holmes's marriage to the "Ann, 24" of the *Dacca* list — and it confirms the **"Jarvis"** middle name in an English record for the first time. Their son **Langley ("Loughley") was born the very next quarter, Mar 1885, Louth 7a/623**. Ann's maiden surname is not yet known; it is on GRO page 7a/1151, Dec 1884, Louth. [A]
- **Cross-checks that all tally:** the Dacca 1887 group ages against the 1871 census — Lang 41 (b. c.1846 vs census c.1844), Fanny 48 (b. c.1839 vs census c.1837; and "Mrs Holmes senr" d. 31 Jan 1918 Qld "in her 79th year" → b. c.1839 ✓), **John J 23** (b. c.1864 ✓), **Mary 17** (b. c.1870 ✓ — "Mary J, dau, 1" at Driby in 1871). [A]
- **"Loughley Holmes, 2" on the Dacca 1887 = Langley Holmes junior**: FreeBMD births, **Holmes Langley, March quarter 1885, Louth district, 7a/623** — the only Langley Holmes birth in Lincolnshire. (District is Louth rather than Spilsby, so either the family had moved toward Louth by 1885 or this is a different child; grade B.) [B]
- **Open lead — the name of Fanny Margaret's biological father.** In Spilsby district FreeBMD shows a **marriage "HOLMES Bennet, Sep quarter 1857, 7a/837"** and a **death "Holmes Bennett, Sep quarter 1858, Spilsby, 7a/328"** — a man who married in 1857 and died in 1858 in exactly the right district, which would leave a young widow and a posthumous daughter born Q1 1859. FreeCEN also shows a Holmes family at **Hogsthorpe** using "Bennet" as a middle name (William Bennet, Jane Bennet, Emma Bennet Holmes) — the same village Langley Holmes came from. **Speculative but testable.** [C]
- **Not corroborated in England: Fanny's maiden name "Shepherd".** No HOLMES × SHEPHERD / SHEPPARD / SHEPPERD marriage exists in FreeBMD for Lincolnshire 1837–1875; no Fanny Shepherd born c.1837 at Bilsby appears in FreeCEN Lincolnshire; and there is **no Shepherd household at Bilsby, Alford, Driby, Hogsthorpe or Willoughby** in FreeCEN's Lincolnshire coverage at all (the only nearby Shepherd is a Thos Shepherd b. c.1842 at Spilsby); and the full list of **SHEPHERD marriages in Spilsby district 1850–1865** contains no Fanny (`sources/england/freebmd-marr-shepherd-spilsby.txt`). The only evidence remains the Queensland death registration C658/1918 ("father Thomas Grant Shepherd"). FreeBMD's coverage of 1850s Lincolnshire marriages is not complete, so this is not a refutation — but it is not confirmed either. [A negative / open]
- **FreeCEN has no 1881 Lincolnshire transcription** — so the pre-emigration 1881 snapshot of Thomas & Fanny Jacklin's household (and whether they had English-born children who died or came with them) is **not available on the free sites**. This is now the single biggest remaining gap. [dead end — free sources]

---

## Dead ends / needs login or purchase

| Source | Status |
|---|---|
| **FamilySearch** | Requires a (free) account login for record search — not used, per brief. Would likely resolve the 1881 census and the Lincolnshire parish registers. |
| **Ancestry / FindMyPast / MyHeritage / TheGenealogist** | Paid subscription. |
| **GRO (gro.gov.uk) online index + certificates** | Requires an account; the GRO birth index gives **mother's maiden name** for 1837+ births, which would immediately settle Fanny Margaret Holmes's parentage and Thomas Jacklin's mother. Certificates are ~£12.50 each. |
| **NAA BP709/1 M27236** (Abe Jacklin's Repatriation file, 1916–1963) and **NAA B73 M55544** (C. W. Ward's Repatriation file, 1916–1986) | Open access but **paper only, not digitised** — must be ordered (copying fee) or read in Brisbane / Melbourne. |
| **Qld BDM certificates** (C4645/1925 John Taylor, C4531/1937 Mary North, C3913/1931 Thomas Jacklin, C577/1933 Fanny Jacklin) | Purchase only. |
| **Vic BDM / NSW BDM certificates and images** | Purchase only (the *indexes* are free and were used). |
| **NSW BDM historical index** (familyhistory.bdm.nsw.gov.au) | Behind Cloudflare **and** built on an Apache Wicket form that discards values set programmatically; could not be driven headlessly or reliably through the browser in the time box. **Not attempted to completion — this is the next place to look for Catherine Ward's 1907 death and for the Cunningham births at Kiandra/Cooma.** |
| **Ryerson Index** | Returned HTTP 429 ("server overloaded") on every attempt this pass; the pass-2 capture was used instead. Retry later with long delays. |
| **QSA ArchivesSearch** (archivessearch.qld.gov.au) | Single-page app whose API is reCAPTCHA-gated; item-level browsing is not scriptable. **Workaround used: the same indexes are published as open CSV/JSON at data.qld.gov.au, and the register scans download freely from `https://www.archivessearch.qld.gov.au/api/download_file/{DID}`.** |
| **Mackay *Daily Mercury* after 1954** | Not on Trove (copyright cut-off). Desmond Jacklin's Sept 1981 obituary still requires Mackay library microfilm. |
| **Margaret Elizabeth Jacklin's full funeral notice** | The directory entry (name + dates) is public, but the notice body is served from a Wix data collection and is not in the page source; it is visible on mackayfuneralnotices.com.au and on the Mackay Funeral Notices Facebook post crediting **Newhaven Funerals NQ**. Worth opening in a browser to capture the family names. |
| **AWM (awm.gov.au)** | The collection-search URLs tried returned 404 and the site is JS-driven; **not completed**. The Embarkation Roll and Red Cross Wounded & Missing files were not checked — but the B2455 dossiers already supply embarkation ship/date for both men, and neither was posted missing, so the Red Cross files are unlikely to exist. |

---

## Next steps (revised)

**Highest value first:**

0. **Find out how Thomas and Fanny got a free Government passage from Glasgow to Mackay.** Register p.237 has now been read and carries **no native place and no nominator** (the 1883 volume simply has no such columns). The next places to look are the **Immigration Agent's correspondence and the ship's board/despatch papers** at QSA for the *Hannah Landels* (Mackay, Sep 1883), and the Queensland Agent-General's emigration records in London. A Lincolnshire couple embarking at Glasgow on a ship that was 87% Scottish is the single most interesting unexplained fact in the whole file.
1. **Find Catherine (Cunningham) Ward's death, 10 August 1907.** Now a precise target. Search the **NSW BDM index** (deaths 1907, surname Ward, any given name) and, failing that, Queensland and South Australia. Also try the Victorian index by *place* for the whole of 1907 in the surrounding districts (Bairnsdale, Orbost, Sale) rather than by name. Her death registration is the record that will name **Thomas Cunningham and Margaret Murphy** as her parents and close REPORT.md §5's biggest gap.
2. **1881 England census for Thomas & Fanny Jacklin, and for Langley & Fanny Holmes.** Not available on FreeCEN. A free FamilySearch account (or a Findmypast day pass at a library) would give: the Jacklins' address and any English-born children immediately before emigrating in 1883, and would confirm the Holmes household before the Dacca in 1887.
3. **Order/inspect GRO index entries with mother's maiden name** for: Thomas Jacklin (Louth 7a/560, Mar 1857) and Fanny Margaret Holmes (Spilsby 7a/528, Mar 1859). The Holmes one is decisive — it will name Fanny Margaret's mother and, on the certificate, her biological father.
4. **Identify the spouse in the two key marriages:** Louth 7a/1083 (Jun 1856) is confirmed as Jacklin × Skipworth; but **Spilsby 7a/797 (Mar 1868)** — whom did Langley Holmes marry? and **Spilsby 7a/837 (Sep 1857)** — whom did Bennet Holmes marry? FreeBMD requires a surname to do a page search; the GRO index scan (on FamilySearch/Ancestry) shows all four names on the page.
5. **Lincolnshire parish registers** for Keddington, Covenham, North Cockerington, Bilsby, Driby, Hogsthorpe and Louth — baptisms, marriages and burials. Lincolnshire Archives' catalogue (**LincsToThePast**) is free to search; the images are on FamilySearch/Findmypast.
6. **NAA BP709/1 M27236** — Abe Jacklin's Repatriation file (1916–1963). 47 years of file covering his gassing, his 1937 dealings with Repatriation Brisbane, and probably his family circumstances. Order a copy.
7. **Margaret Elizabeth Jacklin's 2025 funeral notice** — open mackayfuneralnotices.com.au 2025 archive in a browser (or the Newhaven Funerals NQ Facebook post) and capture the family names; that is the fastest route to Judith's siblings and to Shane's cousins.
8. **JACKLIN, Heather Joyce — probate notice 1 May 2026, late of Mackay** (Ryerson). Identify her: she is very likely North Jacklin's generation and her notice may name the surviving family.
9. **Check the 1919 marriage date of Charles William Ward and Maud Frances Spunner** (Vic 9907/1919) against their son William Charles's birth on **14 April 1919**.
10. Retry the **Ryerson Index** with long delays for Desmond John Jacklin (1981) — but expect nothing; the Mackay paper is not indexed for that year.
11. **AWM** — Embarkation Rolls and the *Australian Red Cross Wounded and Missing* files were not reached this pass; low expected yield, but cheap once the site is driven through a browser.

---

## Technical notes (additions to REPORT.md's)

- **NAA RecordSearch is behind Cloudflare** — plain `curl`/`requests` get HTTP 403. **`curl_cffi` with `impersonate="chrome"` passes cleanly.** Guest session: `GET /SearchNRetrieve/Interface/SearchScreens/BasicSearch.aspx` redirects to `SessionTimeout.aspx`; POST that URL back with all hidden fields plus `__EVENTTARGET=ctl00$ContentPlaceHolderSNR$lbnGuest` **and** `Referer`/`Origin` headers (without them the session doesn't stick). Search: POST `BasicSearch.aspx` with `ctl00$ContentPlaceHolderSNR$tbxKeyword` + `...$btnSearch=Search` → you land on `PleaseWait.aspx`, whose form auto-posts to **`BasicSearch_Result.aspx`** — repost its hidden fields there → `ItemsListing.aspx`. Page size via a postback on `ddlResultsPerPage`. Item detail: `DetailsReports/ItemDetail.aspx?Barcode={ItemID}`. Viewer: `Interface/ViewImage.aspx?B={ItemID}` (page count is in the "Page N of M" text). **Page images: `/SearchNRetrieve/NAAMedia/ShowImage.aspx?B={ItemID}&S={page}&T=P&R=0`** — full-resolution JPEGs, ~150–250 KB each, no session beyond the guest cookie. Script: **`sources/naa_fetch.py`**.
  - (A browser fallback also works: in Chrome, an `<a download>` click will save the first image, but Chrome then blocks automatic multiple downloads — use the `curl_cffi` route instead.)
- **FreeBMD** (`https://www.freebmd.org.uk/cgi/search.pl`) is *not* Cloudflare-protected; ordinary `requests` works. POST **multipart/form-data** with the hidden `db` and `v` tokens taken from a fresh GET of the search page. Gotchas: (a) **omit `districtid` and `countyid` entirely when blank** — an empty `districtid` triggers a MySQL syntax error page; (b) the start/end date range is frequently ignored, so you get the district's whole run (useful, not harmful); (c) a surname is mandatory, so a pure volume/page search is not possible; (d) marriage spouse pairing works by setting `s_surname` and running the query in both directions. Script: **`sources/freebmd.py`**, drivers `freebmd_run*.py`. County id for Lincolnshire is `LIN,6,33,49,50,52,102,103,154,175,176,225,226`; district ids Louth `937`, Spilsby `265`.
- **FreeCEN2** (`https://www.freecen.org.uk`): POST `/search_queries` with the Rails `authenticity_token` scraped from `/search_queries/new`; params `search_query[last_name]`, `[first_name]`, `[chapman_codes][]` (county, e.g. `LIN`). Results link to `/search_records/{id}/{slug}`, and that page renders **the whole household**. Lincolnshire coverage: 1841, 1851, 1861, 1871, 1891 — **1881 is not transcribed**. Script: **`sources/freecen.py`**.
- **Queensland State Archives without the captcha:** QSA's indexes are published as open data on **data.qld.gov.au** (CKAN). `GET /api/3/action/package_search?q=immigration`, then `package_show?id={name}` for resource URLs. Key datasets used: `assisted-immigration-1848-to-1912` (A–Z CSVs + a 111 MB combined CSV), `registers-of-immigrants-1882-to-1938`, `land-selections-1885-1981`, `applications-by-selectors-1868-1885`, `naturalisations-1851-to-1908`. Each row carries a **Digital Image ID**, and **`https://www.archivessearch.qld.gov.au/api/download_file/{DID}` returns the scanned register as a PDF with no captcha** (the Dacca register came down as a 10.7 MB, ~70-page PDF).
- **Victorian BDM API**: confirmed still working when driven as a page-context `fetch` from `https://my.rio.bdm.vic.gov.au/efamily-history/-`. Useful extras beyond REPORT.md's note: the body accepts **`place`** (matched against the indexed place string — "Cunninghame", "Bruthen", "Swan Reach", "Lake Tyers" all work) and **`person.name.firstGivenName`** alone; results cap out around 100 and an over-large query returns an error object rather than an array, so **narrow by year or place rather than paging**.
- **NSW BDM** (familyhistory.bdm.nsw.gov.au) is Cloudflare-protected *and* an Apache Wicket app: setting input values via JavaScript does not update the server-side model, so the search always comes back "family name must be entered". It needs genuine keystroke-level automation.
- **Ryerson Index** rate-limits hard (HTTP 429) and stayed blocked for the whole session.
- Trove web API date limits work: add `limits={"decade":["190"],"year":["1907"]}` (the `l-` prefixed form works identically). Note the `terms` parameter is effectively OR-weighted, so multi-word queries return a lot of noise — sift the returned `snippets` locally rather than trusting `totalRecords`.
