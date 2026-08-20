# The Schleger Line — research pass 2 (19 Aug 2026)

> **⚠ Corrections (19 Aug 2026, REPORT-yola-rose.md §5):** George Johnston's 1895 death is now PROVEN [A]; John Boland Johnstone was FJ's *nephew* (son of Elizabeth Ann Jane), not brother; the sisters' married names were swapped (Catherine Emily = Mrs Schmidt, Elizabeth Ann Jane = Mrs Bird then Mrs Boge); John Johnstone (b. 1919) died aged 3 in 1923; Harriett Curtis was born at Biscovey/St Blazey (Barratt, not Barrett); the Qld BDM API ignores parent-name filters, so the Rose Jackson counts quoted below were unfiltered (conclusions stand). Read that file alongside this one.


Supplement to `REPORT.md`. **New facts, corrections and documented dead ends only** — nothing already
in REPORT.md is restated except where this pass changes it. Grades follow REPORT.md:
**[A]** = primary record or contemporaneous print; **[B]** = strong secondary / researcher assertion;
**[C]** = inference.

Free sources only. No subscriptions, no certificates, no logins.

**New evidence files in `sources/`**
| file | what |
|---|---|
| `naa-pass2.txt` | full NAA RecordSearch result sets (Schleger, Johnstone) |
| `naa/*.jpg` | 45 digitised service-record pages (1 × WWI B2455, 4 × WWII B883/B884) |
| `qsa-pass2.txt` | full Qld State Archives result sets + immigration-register analysis |
| `qsa/*.pdf` | 4 free QSA digitised immigration registers (Scottish Hero, Highflyer) |
| `qld-bdm-pass2.txt` | all new Qld BDM index hits with registration numbers |
| `trove-hits-pass2.jsonl` | pass-2 Trove search hits |
| `trove-articles/nla.news-articleNNN.txt` | 31 new full article texts |
| `death-notices-pass2.md` | Ryerson / myTributes / Find a Grave / funeral-director sweep 1971–2024 |
| `austrian-origin-pass2.md` | Matricula / ANNO / Burgenland Bunch evidence |
| `qsa_search.py`, `trove_pass2.py` | reusable tooling (QSA ArchivesSearch API; Trove harvester) |

---

## Frank / Carl Schleger

**New**

- **The 1929 golden-wedding ship story does not check out against the actual passenger registers.** [A]
  QSA holds free digitised registers for both named ships:
  - *Scottish Hero*, 1,493 tons, Capt. Mowatt, **sailed London 14 Dec 1878, "Arrived Maryborough 5th
    April 1879"** — complete list read (Steerage / Assisted / Free / Remittance): **no SCHLEGER in any
    class or spelling.** (QSA DR39478, in ITM18478 = S13086 Register of passengers on immigrant ships
    arriving in Queensland No. 3; saved as `sources/qsa/QSA-DR39478_*.pdf`)
  - *Highflyer*, Capt. Hawkins, **London for Maryborough, sailed 2 Aug 1878**, 340 landed — complete
    list read: **no O'MEARA / O'MARA and no SCHLEGER.** (QSA DR38582, same series; `QSA-DR38582_*.pdf`)
  - Maryborough promissory-note registers for the same two arrivals list only 5 and 4 names
    respectively, none of them ours (DR39476, DR38585).
  - The only other *Scottish Hero* voyages in the window (1876, 1877) both **arrived Rockhampton**,
    not Maryborough (DR39474).
  → Interpretation [C]: these registers cover government (assisted / free / remittance / nominated)
  and steerage immigrants. Frank, a subject of Hungary, was **not eligible for assisted passage**, so a
  self-paid arrival would leave no entry. The negative is consistent with the article being right about
  the ship and wrong about the paperwork — or wrong about the ship. It is **not** evidence he did not
  arrive in 1878/79.
- Correction of detail: the article says both arrived "in 1878". Mary's ship sailed Aug 1878; the
  *Scottish Hero* Maryborough voyage landed **5 April 1879** — ten weeks before the June 1879 wedding. [A]
- **Full text of the golden-wedding article now captured** (`trove-articles/283753747.txt`,
  Bundaberg Daily News & Mail 24 Jul 1929, nla.news-article283753747). New detail not in REPORT.md: on
  arrival Frank "worked for Barbeler, the local baker" at Maryborough and **Mary conducted a night
  school**; the Gympie bakery was later bought by **Sam Weller**; the *Highflyer* voyage "took over 100
  days"; "eight children, of whom **one died by accident**, and 20 grandchildren" (1929). [A]
- **QSA holds exactly 7 items for "Schleger" in all its holdings** (`qsa-pass2.txt`). Two are new:
  - **ITM3469712 — "Maryborough Leases – Bootharh Sawmill For Schleger Bros", 1911**, railway batch
    file, series S21280, ref CAT 374/3/12. First evidence of a **Schleger Bros sawmill** business. [A]
  - ITM2832237 — the will file, physical ref "**160**", confirming will 160/1931. [A]
- **NAA has no Schleger naturalisation, alien-registration or WWI enemy-alien file** — only 12 Schleger
  items nationally, all WWII service records or unrelated people. Consistent with Frank naturalising in
  Queensland in 1886, before Federation. [A]

---

## Children (Frank & Mary's eight)

**New / corrected**

- **Ignatius Loyola Schleger (1881–1915) — cause of death established, and it was not the war.** [A]
  He **took his own life at Burnett Heads on 4 August 1915, aged 32**, found hanging in a barn by a
  clothes-line wire; First-Class Constable Joyce took charge of the body; post-mortem next morning;
  buried Bundaberg Roman Catholic Cemetery, undertaker John Novakoski.
  (Brisbane Courier 5 Aug 1915 "Suicide at Burnett Heads", nla.news-article**20023652**; Bundaberg Mail
  5 Aug 1915 "SAD DEATH AT BURNETT HEADS", nla.news-article**216913781** — "had been in a weak state of
  mind for some years".) **No WWI service record exists for any Schleger** (NAA B2455 nil). [A]
- **Ignatius was a ward of the Public Curator from 1903.** [A] QSA **ITM1355052 — "SCHLEGER, Ignatius
  Loyola", 12 Mar 1903 – 9 Dec 1910, File – estates, mentally incapacitated persons**, series S334
  Protective Management Files (Public Curator Office), creating agency *Insolvency, Intestacy and
  Insanity Office, Brisbane*, agency file no. **75/1903**. Open Access, not digitised. He was 21 when
  the file opened. This is the documentary backing for "weak state of mind for some years" and for the
  family's "one died by accident".
- **Funeral notice 5 Aug 1915** (nla.news-article216913797) names the surviving siblings and their
  spouses as at 1915: Mr A. Schleger; Misses Mary & Clara; Mr & Mrs F. Hoffmann; Mr & Mrs J. Chalmers;
  Mr & Mrs F. M. Schleger; Mr & Mrs R. Schleger. [A]
- **Death registrations of all four daughters now located, each naming Frank and Mary as parents** [A]
  (see `qld-bdm-pass2.txt`):
  Catherine Theresa **Hoffmann** d. 8 Jul 1943 (C3040/1943) · Barbara Ellen **Chalmers** d. 22 Feb 1967
  (C97/1967) · Clara **Marshall** d. 27 Mar 1972 (B31149/1972) · Mary Bernadette **O'Leary** d. 18 Jul
  1976 (C3829/1976).
- **Correction:** child 7 is registered at birth as *Mary Anne* (C771/1891) but lived and died as
  **Mary Bernadette**; her husband's full name was **David Browne O'Leary** (from the 1983 death
  registration of their son Vincent Joseph Patrick O'Leary, b.1920, d. 8 Feb 1983, 51188/1983). [A]
- Marcia Josephine Schleger (b.1922, dau. of Raphael Emanuel) married surname = **FLANAGAN** —
  QSA teacher's staff card ITM3563689 "FLANAGAN, Marcia Josephine (nee SCHLEGER)". [A]
- Eileen May Catherine Schleger (b.1910, dau. of Francis Morgan) was a **schoolteacher**, staff card
  1928–1930, QSA ITM3567084. [A]

---

## Alphonso Leo's ten

**New**

- **Alphonso Leo's own obituary, death and funeral notices, 1964** — much richer than the 1951 set.
  (News-Mail Bundaberg 9 Sep 1964, nla.news-article**283376481** obituary + **283376455** notices;
  11 Sep 1964 funeral report **283378983**.) [A]
  - Died **8 September 1964**, Mater Misericordiae Hospital, West Bundaberg, **aged 78**; born
    Bundaberg, "the **fifth child** of Mr and Mrs F. C. Schleger, pioneer farmers at Burnett Heads";
    farmed Burnett Heads Road from young manhood until death; long-serving **secretary of the Burnett
    Heads School Committee**; **married in Brisbane** to Mary Ellen Napier.
  - **37 grandchildren** at Sept 1964.
  - Children with 1964 residences: Francis Charles (Sydney) · Valerie Mary — *Sister Mary Scholastica,
    **Barcaldine*** · Kevin (Bundaberg) · Terrence (Burnett Heads) · Olga — Mrs O. Hayes
    (**Toowoomba**) · Dalphine — Mrs E. Stitt (**Barolin**) · Alphonsus (**Rockhampton**) · Maureen —
    Mrs J. Moroney (Brisbane) · Regis — **Mrs K. Dennien** (Bundaberg) · Bernadine/Bernie (Brisbane).
  - Surviving siblings 1964: Raphael (Brisbane), Mrs B. Chalmers (Bundaberg), Mrs M. O'Leary
    (Bundaberg), Mrs C. Marshall (Brisbane).
  - Pallbearers: Frank, Kevin, Terry and Phonse Schleger, E. W. Stitt, J. Moroney.
  - Mass-card list gives grandchildren by household: **Terry & Olive — Wendy, Patricia**; **Kevin &
    Ellie — Sandra, Leonie, Paul, Bernice**; **Frank & Joy — Susanne and Frank (Sydney)**; "Phonse,
    Rose and family".
- **Mary Ellen Schleger's 1951 death notice** (Bundaberg News-Mail 3 Jul 1951,
  nla.news-article**283510756**) — died **2 July 1951 at the Mater Misericordiae Hospital, Bourbong
  Street, West Bundaberg**, aged 61y0m, of Burnett Heads; funeral from Holy Rosary Church, Barolin St.
  Same ten children, 1951 residences: Valerie was then at the **Convent, Rockhampton**; Delphine
  Mrs W. Stitt of **Sharon**; Olga Mrs T. Hayes of **Kolan**; Alphonsus in **Sydney**. [A]
- **Ambiguity to flag:** the 1964 obituary prints "Miss **Bernadine** Schleger (Brisbane)" while the
  funeral report the same week lists "five sons ... and **Bernie**". Qld BDM registers the death as
  **Bernard Emmanual Schleger, 11 Jun 1992** (5072/1992), parents Alphonso Leo / Mary Ellen Napier;
  Find a Grave indexes him as "**Bernadine Eamon** Schleger, 21 May 1933 – 11 Jun 1992", died at
  **Goodna**, buried Bundaberg Catholic Cemetery **Block 8 – P409, the same plot as Alphonso Leo**. The
  given name as actually registered needs the certificate to settle. [A record, C reconciliation]
- **WWII service — three of Alphonso's sons, all with digitised records** (NAA, `sources/naa/`) [A]:
  | | service no. | b. | enlisted | unit | out |
  |---|---|---|---|---|---|
  | **Francis Charles** | **Q71857** (B884, barcode 4457111) | 1 Feb 1917 Bundaberg | **7 Apr 1941, Childers** | L. of C. Units A.A.S.C. / **101 R.M.T.** | camp training Enoggera 16 Apr–12 Jul 1941; called up FTD 19 Dec 1941; RAAF Reserve 12 Jan 1942; **released 25 May 1942 as a reserved occupation**, discharged Redbank |
  | **Kevin Leo** | **QX43875** (B883, barcode 4918841) | 3 Jul 1919 Bundaberg | Bundaberg | **113 Aust. Gen. Transport Coy**, **L/Cpl** | CMF 19 Dec 1941 – 30 Nov 1942, **AIF 1 Dec 1942 – 7 Nov 1945**; 1,399 days effective, **1,283 days active service in Australia, NIL overseas**; discharged **7 Nov 1945 Redbank on occupational grounds — "cane farming"**; disch. cert. 230855 |
  | **Terrence Raphual** | **Q208478** (B884, barcode 4827472) | 4 Dec 1921 Bundaberg | 23 Dec 1941, Bundaberg | **10 Bn Volunteer Defence Corps**, Pte | taken on strength 3 May 1943 B'berg; placed on reserve 8 Jul 1944; **discharged 21 Oct 1945 on corps disbandment** |
  Next of kin on all three: **father Alphonso Leo Schleger, Burnett Heads, Bundaberg**.
  Occupations at enlistment: Francis Charles = **sugar chemist**; Terrence = **cane cutter**.
  Personal descriptions: Francis Charles hair fair / eyes grey; Kevin 5ft 5in, fair, blue eyes, brown
  hair; Terrence hair **black**, eyes blue. All R.C.
  Cousin **Lawrence Raphuel Schleger QX501472** (b. 17 Sep 1926, NOK father Raphuel) also served —
  B883 barcode 4464771. **Alphonsus Vincent and Bernard were too young; neither has a service record.** [A]
- **Francis Charles's civilian career**: holder of a **diploma in sugar chemistry**, past student of
  Bundaberg Christian Brothers' High School, and by 1952 **managing a vegetable-oils factory in
  Sydney**; flew Qantas to England, then West Germany, Holland, America and Fiji in 1952.
  (News-Mail 30 Jul 1952, nla.news-article**284068496**) [A]
- **Regis Margaret Schleger**: engagement announced 21 Apr 1953 — "**Regis Margaret**, youngest daughter
  of Mr and the late Mrs A. L. Schleger, Burnett Heads, to **Kevin Allan Dennien**, youngest son of Mr
  and Mrs K. Dennien, 2 May Street, South Bundaberg" (nla.news-article**283609352**). Born 22 Apr 1931,
  died 2009 at St Andrew's Hospital, Brisbane. [A / B]
- **Terence Raphael m. Olive Lillian Sutherland on 28 Aug 1943**; she died **12 Aug 2021 aged 98**
  (b. 30 Aug 1922) at Riverlea Aged Care, Bundaberg, and is buried in **the same grave** — Bundaberg
  General Lawn Cemetery **L2A/200**. Her notice names daughters **Wendy & Bevan Tanner** and **Tricia &
  Ian Green**, grandchildren Graham, Nicole, Kirsty, Mark, Chris & Trudie, Tamara & Kevin, and
  great-grandchildren Annika, Curtis, Oliver, Edith. An entire branch previously unrecorded.
  (Des Allen & Co notice via Internet Archive; see `death-notices-pass2.md` §3) [A]
- **Kevin Leo's widow Ellen Mary (Reilly/Riley) died 29 Feb 2016 aged 88.** [B]
- **Paul Kevin Schleger (1958–2024)** notice: "dearly loved son of **Kevin and Ellen** (both deceased);
  loved brother and brother-in-law of **Sandra, Leonie and Frank, Bernice**". **Correction to
  REPORT.md:** "Frank" is most likely **Leonie's husband**, not a fifth Schleger sibling — REPORT.md
  lists Kevin's children as "Sandra, Leonie, Frank, Paul Kevin, Bernice". Treat "Frank" as unconfirmed
  until a 1989 or 2016 notice is seen. [A notice / C reading]
- **Valerie Mary = Sister Mary Scholastica RSM**, professed with the **Rockhampton Sisters of Mercy on
  22 January 1950**, one of the group known as "The Nine"; at Barcaldine by 1964. [B]

---

## Phonse & Rose

**New**

- **Dean Michael Schleger — Shane's father — birth notice found.** [A]
  > "SCHLEGER. — At **Lady Goodwin**, on **December 8** [1952], to **Phonse and Rose (nee Johnstone)**,
  > a Son, **Dean Michael**."
  Morning Bulletin (Rockhampton) 11 Dec 1952, nla.news-article**57308947**; repeated in the Bundaberg
  News-Mail 13 Dec 1952, nla.news-article**283529814** ("at the Lady Goodwin Hospital, Rockhampton").
  This closes the Frank → Alphonso Leo → Phonse → **Dean (b. 8 Dec 1952, Rockhampton)** → Shane chain
  with a contemporaneous record at every generation.
- **Phonse's occupation:** he **resigned from the CSIRO** to contest Capricornia in 1963.
  (Telegraph, Brisbane, 13 Nov 1963, "KNOW YOUR ELECTORATE", nla.news-article**295380205**) [A]
- **1963 Capricornia result:** Gray (ALP) 19,673 · South (Lib.) 12,760 · **Schleger (DLP) 3,772**,
  informal 523, enrolment 39,860. (Toowoomba Chronicle 5 Dec 1963, nla.news-article**287657265**;
  progressive figures in Canberra Times 2 Dec 1963, nla.news-article**104280130**.) [A]
- **Engagement, Jan 1951** — full text now held [A]:
  > "The engagement is announced of **Yola Rose, youngest daughter of Mr and Mrs F. J. Johnstone, 140
  > Archer St, Rockhampton**, to **Alphonsus Vincent (Phonse) Schleger, Sydney**, fourth son of Mr and
  > Mrs A. L. Schleger, **Burnett Heads Road, Bundaberg**."
  (Morning Bulletin 6 Jan 1951, nla.news-article57064913; Bundaberg News-Mail 10 Jan 1951,
  nla.news-article283572776.) Phonse was living in **Sydney** in 1951, in **Rockhampton** by 1959.
- 1959: "Mr. A. V. Schleger and family returned to Rockhampton after spending a fortnight's holiday
  with his father, Mr A. L. Schleger, Burnett Heads." (News-Mail 29 Aug 1959,
  nla.news-article**284099083**) [A]
- **Correction to REPORT.md:** Yola Rose **died 23 November 2019**, not 14 December 2019 — 14 Dec is
  the Morning Bulletin *publication* date of the notice. Aged 90; late of Benevolent Living,
  Rockhampton, formerly Nerimbera; private service 9 Dec 2019; buried **Rockhampton Memorial Gardens,
  Lakes Creek — Pomegranate Grove C, 21**, the same plot as Phonse. [A]
- **Phonse died 29 July 2014, aged 87**, late of the Benevolent Home, Rockhampton, formerly Nerimbera
  (Ryerson Index; Find a Grave 206396254). Notice body not recoverable free — see dead ends. [B]
- **No marriage notice for Schleger–Johnstone 1951 exists in Trove.** Targeted searches
  ("Schleger Johnstone", "Yola Rose") return the two engagement notices and nothing else. The Qld BDM
  marriage index stops at 1949, so the 1951 marriage is not indexable online at all. [A negative]

---

## Johnstone / Jackson — and the Aboriginal-heritage question

This is where the pass changed the most. **REPORT.md's inference that the Johnstone family came from
outside Queensland (NSW?) is wrong.** They are a Maryborough / Apple Tree Creek (Childers) family; the
Qld BDM registers them as **JOHNSTON**, without the final *E*, which is why pass 1's searches missed them.

### The Johnston(e) family — now documented

- **Marriage: George Johnston = Harriett Ann Curtis, 7 Aug 1877 — Qld reg C677/1877.** [A]
- **Eight Qld births, father George Johnston, mother Harriett Ann Curtis** [A] (full list with
  registration numbers in `qld-bdm-pass2.txt`), including
  **Frederick Jason Johnston, born 28 December 1892 — C12224/1893.**
- **Harriett Ann Curtis's own origins** [A], from the 1940 obituary (Isis Recorder 23 Feb 1940,
  "APPLE TREE CREEK PIONEER", nla.news-article**287617188**) plus her death registration:
  - Born **St Austell, Cornwall, England**, c.1859/60; came to Australia **aged four, landing Adelaide
    in 1863**, with her parents **Thomas Curtis and Elizabeth Ann Barrett** (parents named on the death
    reg, **C856/1940**).
  - Her father **managed the Tee-bar Mines from 1865**, then took charge of the **Maryborough–Tinana
    river ferry**.
  - She and George Johnstone, **a road contractor**, "were among the **first settlers at Apple Tree
    Creek, Childers**".
  - She **married twice**; her second husband was **John Hughes of Maryborough** (marriage
    **C1530/1898**, 29 Sep 1898). She therefore **died as Harriet Ann HUGHES, at Maryborough on
    21 February 1940, aged 80**, and is buried from the Wesley Church, Maryborough (J. Kirk & Son).
    This is why no Johnstone death for her could be found. (Family notices: Maryborough Chronicle
    22 Feb 1940, nla.news-article**151359949**; Colonist 2 Mar 1940, nla.news-article**293680913**.)
  - Predeceased by "two sons and a daughter"; **11 grandchildren** in 1940.
- **Probable death of George Johnstone: 29 March 1895, Qld reg C2621/1895, parents William Johnston &
  Elizabeth Vincent.** [C — plausible but unproven; supported by the son named George **Vincent**
  Johnston (b.1888) and by Harriett's remarriage in 1898.]
- **A brother not previously known:** the 1928 obituary of Henry Albert Curtis ("Gullie") Johnstone
  (Colonist, Maryborough, 28 Jan 1928, nla.news-article**293169820**) names **John Boland Johnstone
  (Brisbane)** as a fifth brother, and **two sisters, Mesdames Marcus Boge (Maryborough) and
  T. Schmidt (Brisbane)** — i.e. Catherine Emily and Elizabeth Ann Jane. Henry was born at Maryborough,
  a **painter** in the Railway Department, member of **Excelsior Lodge No. 1, P.A.F.S.O.A.**, died aged
  32y4m leaving a wife and two children, **Gilbert and Desmond**. [A]

### Frederick Jason Johnstone (1892–1969)

- **He enlisted in the AIF.** NAA **B2455, JOHNSTONE Frederick Jason, barcode 7369725, digitised
  (16 pp, downloaded to `sources/naa/`)**: [A]
  - Attested **30 October 1915 at Brisbane**, aged 23y10m; born Maryborough, Q.
  - Trade **hairdresser**; single; prior service **2 years 7 months Militia, Maryborough**.
  - Next of kin **mother, Harriet Johnstone, North St, Maryborough**.
  - Description: 5 ft 5¾ in, 130 lb, complexion **fair**, eyes **grey**, hair **dark brown**,
    religion **Methodist**; distinctive marks "D6–D6" and "**Hypospadias**".
  - The file is stamped **DEPOT** in red and carries no unit or service number — he was held at a
    depot battalion and **never embarked**. Almost certainly discharged medically.
- **Career** [A]: joined the Queensland Railways **1922**; fettler by 1934, promoted **ganger** soon
  after; at **Colosseum** (station house, North Coast Line, near Miriam Vale) 1937–1940; **ganger of
  No. 17 gang, Makowata, 1943**; transferred to the **Rockhampton workshops as a labourer in 1948**;
  working in the erecting shop and appealing (unsuccessfully) for the wagon-shop storeman's job in
  1950. In cross-examination in 1943 he admitted a conviction at the **Miriam Vale Court for assaulting
  a man named Ivan Edwards**. (Morning Bulletin 20 Apr 1943, nla.news-article**56144761**; 24 Mar 1950,
  nla.news-article**56937588**.)
- Died 25 Oct 1969 (C6787/1969). His siblings' deaths are now all indexed — see `qld-bdm-pass2.txt`.
- **Jacquiline Johnstone** appears in a 1937 pen-friends column as "**JACQUELINE JOHNSTONE, Station
  House, Colosseum, N.C. Line**", aged ~14, seeking a correspondent aged 12–16 (Truth, Brisbane,
  29 Aug 1937, nla.news-article**205734137**) — matching her 10 Nov 1923 birth and the family's
  Colosseum posting. [A] Her Rockhampton stage career is well documented in the Morning Bulletin
  1949–1953 as "**Jacqueline Johnstone (of Radio Fame)**", a **soprano** with the "Rockyettes" revue
  company (e.g. 14 Oct 1949 nla.news-article56919003; 14 Dec 1951 nla.news-article**57110662** —
  soprano solo "Star of Love"). [A]

### Rose Jackson — what the indexes actually show

Handled deliberately narrowly. What is **record**, and what is **not**:

- **Record [A]:** Rose Jackson m. Frederick Jason Johnstone 21 Aug 1919 (C2254/1919). She died
  12 Nov 1974 (C7759/1974) with **date of birth recorded as 1893** and parents recorded as
  "**Robert Jackson**" and "**Millie Jackson**".
- **Record [A] — searched, nothing found:** there is still **no Queensland birth registration** for a
  Rose Jackson b. c.1893 to a father Robert. Pass 2 checked (a) all Qld Jackson births 1885–1902 with a
  given name Rose — four, none with a father Robert; (b) all Qld Jackson births 1885–1902 with a father
  named Robert — 32, none named Rose and none with a mother named Millie/Amelia; (c) Qld Jackson deaths
  any year with a mother named Millie or Milly — none relevant. Full lists in `qld-bdm-pass2.txt`.
- **Record [A]:** the Queensland State Archives public index contains an item
  **ITM732477 — "JACKSON, ROSE"**, in series **S4429, *Personal Files – Office of the Chief Protector
  of Aboriginals***, item ref SRS4429/1/12474, agency file number **8R/119**, created under the
  Southern Protector of Aboriginals Office, **Restricted Access** (100-year RAP, opens 2078).
- **What that does *not* establish [C]:** the item's date range (1902–1978) is inherited from the
  series and is flagged "approximate" — it is not this person's dates. The public index gives **no
  place, no birth year, no parents, and no other identifier**. "Rose Jackson" is a common name and
  Queensland's Chief Protector's files run to 15,814 items. **This index entry is not evidence that the
  file relates to Shane's great-grandmother.** It is a lead, and the only way to test it is a
  Community & Personal Histories family-history request.
- **Record [A] — searched, nothing found:** no ATSI-flagged QSA item for "JOHNSTONE, Rose",
  "JACKSON, Millie" or "JACKSON, Amelia"; no ATSI-flagged item among 30 results for "JACKSON, Robert".
- **Standing inference, unchanged [C]:** a mother recorded by a single given name plus her husband's
  surname, with no birth registration for the daughter, is a pattern seen in Aboriginal families in
  1890s Queensland. It is also seen in remote, itinerant and unregistered non-Aboriginal families.
  **It remains suggestive, not probative.**
- **One geographic correction that matters [C]:** REPORT.md frames this as a Rockhampton/Darumbal
  question. The Johnstone family is **Maryborough / Childers / Colosseum**, and only moved to
  Rockhampton in **1948**. The 1919 marriage and Rose's own origins are far more likely to sit in the
  **Wide Bay–Burnett** (Butchulla, Gooreng Gooreng, Gurang) region than in Darumbal country. Any
  Community & Personal Histories request should say so.
- Frederick Jason's own AIF description ("complexion fair", Methodist, Cornish-English mother) speaks
  only to the **Johnstone** side and says nothing about Rose. [A]

---

## Austrian side

Full evidence: `sources/austrian-origin-pass2.md`. Headline results:

- **Two independent Burgenland Bunch researchers, both public, both contactable free** [A as quoted
  from the live pages; B as genealogy]:
  - `surnames_sc-sd.html`: "Schleger | **Cathryn King** | Eisenstadt (Kis-Marton) | Settled in
    Bundaberg, Australia, around the late 1870s." — `cjkin@queenslander.net`
  - Same page: "Schleger | **Lynda Chalmers** | Eisenstadt (Kis-Marton) | To Australia, 1870s before
    1878." Her member entry reads "**SCHLEGER, FRANK**, Eisenstadt, to Australia probably 1870s but
    before 1878" — `blotweed@hotmail.com`, **Sydney**.
  - **This is the pass's best Austrian lead**: Chalmers independently pairs SCHLEGER with **FRANK**,
    which is exactly Katharina **Frank**, the mother on the 1930 Qld death registration. King does not.
- **Matricula coverage — the answer to REPORT.md next-step 3** [A]:
  - **Diözese Eisenstadt is NOT on Matricula at all, and Matricula has no Hungary collection.** The
    Eisenstadt hypothesis cannot be tested there.
  - **Every Wolfsthal/Hainburg-cluster parish IS online, gap-free for 1845–1860, with bound
    alphabetical indexes**: Wolfsthal, Hainburg an der Donau, Bad Deutsch-Altenburg, Berg,
    Prellenkirchen, Petronell-Carnuntum (Archdiocese of Vienna). ~212 index images decide that
    hypothesis for free. Exact volume URLs and deep links are in `austrian-origin-pass2.md` §1c–1e.
- **ANNO** [A]: every apparent 1840–1890 "Schleger + Eisenstadt/Kismarton" hit was checked snippet by
  snippet and **all are false positives** (hotel-arrival lists, unclaimed-legacy notices). Conversely
  Schleger recurs as a resident surname in the **Hainburg / Bruck an der Leitha** district press from
  1901 — but that paper has **no digitised issues before 1900**, so the pre-1900 silence is a
  digitisation artefact, not evidence.
- **Burgenland Bunch's own transcribed data argues against Eisenstadt** [A]: across the 1856–58
  Burgenland house lists and BB's church-birth data, SCHLEGER appears **once**, at *Zahling, 1693*
  (Jennersdorf district). The **Eisenstadt 1857 house lists contain no Schleger at all.** House lists
  record heads of house only, so this does not refute the attribution — but it does mean the Eisenstadt
  origin currently rests on **researcher assertion, not on any published record**.
- **Hungarian free indexes are unanimously negative** [A]: Hungaricana, MACSE, Arcanum snippet search,
  MNL and RadixIndex show **no Schleger in Kismarton / Sopron / Moson 1840–1880**. One apparent
  MNL 1828-census hit ("Kis-Marton SCHLEGER") was downloaded at full resolution and read — it is
  **"Jud: Vid: Aaron Schlesinger"** in the Jewish community list, an HTR mis-match. Refuted.
- **One more tick for the Wolfsthal cluster** [B]: a WWI *Verlustliste* entry for a SCHLEGER from
  **Wolfsthal**. And exact-phrase "Carl/Karl Schleger" across the whole ANNO corpus 1845–1890 returns
  **one** hit, in Prague — the name is genuinely rare in the Austrian press.
- **Net position [C]:** Eisenstadt has the human testimony and no record; Wolfsthal/Hainburg has the
  surname distribution and free, complete, indexed registers and no direct evidence. Neither is
  established. A third possibility — the Hungarian-until-1921 border villages (Kittsee, Edelstal,
  Deutsch Jahrndorf, Pama), which would reconcile "subject of Hungary" with "native of Austria" and
  with the modern surname cluster — is untested and not on Matricula either.

---

## Dead ends / needs login or purchase

| what | status |
|---|---|
| **DVA WWII Nominal Roll** (`nominal-rolls.dva.gov.au`) | The site's `searchAdvancedJSON.json` endpoint returns a server error for every parameter combination tried; results load only via that AJAX call. `ww2roll.gov.au` does not resolve. **Not a paywall — the site is broken.** Everything it would have given (service number, DOB, place of birth, place of enlistment, NOK, unit) was obtained instead from the NAA B883/B884 records themselves. |
| **Qld BDM certificates** | Still the only way to get birthplaces, informants and Protector's-permission endorsements. Priority: Rose Johnstone née Jackson **death 1974 (C7759/1974)** and **marriage 1919 (C2254/1919)**; Frank Schleger **marriage 1879 (C741/1879)** and **death 1930 (C3513/1930)**. Purchase required. |
| **QSA ITM732477 (JACKSON, ROSE — Chief Protector's personal file)** | Restricted until 2078. Access only via a **Community & Personal Histories** family-history request (free, but needs a written application and proof of descent). |
| **QSA ITM1355052 (Ignatius Loyola, Public Curator file 75/1903)** | Open Access but **not digitised** — needs a reading-room visit or a paid copy order. |
| **QSA Registers of Removals** (ITM337006, ITM337007, SRS4973) | Restricted Access. Index to register of removals 1942–1964 (ITM337123) is Open Access but not digitised. |
| **FamilySearch** | Free account required. The two decisive Eisenstadt reels are identified: digital **004675473** (Oberberg/Felső-Kismartonhegy RC B-M-D 1827–1870 — covers c.1851 continuously) and **004620339** (Eisenstadt town RC 1852–1860). |
| **GenTeam.at** | Free account required; would test all three Austrian hypotheses at once. |
| **Matriken.at** (Diocese of Eisenstadt originals) | **Pay service.** Pre-1852 Eisenstadt Stadtpfarre registers are behind it. |
| **Google Books API** | Blocked by shared daily quota during this pass — **not attempted successfully**. Task incomplete, re-run later. |
| **Hungaricana / Arcanum** | Arcanum full text is paywalled; no free Sopron/Moson surface found. |
| **Sydney Morning Herald 1988 / 2003 notices** (Francis Charles, Joyce Lillian) | Fairfax/Nine archive paywall. |
| **News Corp regional archives** (Bundaberg News-Mail 2016 Ellen Mary; News-Mail + Courier-Mail 2009 Regis) | Paywall + coverage gap. |
| **1971 / 1980 / 1989 / 1992 notices** (Terence, Valerie, Kevin Leo, Bernard) | **Coverage gaps, not paywalls** — Ryerson's Morning Bulletin and News-Mail indexing does not reach back that far, and no funeral-home archive covers those years. Only cemetery data exists. |
| **Phonse's 2014 notice body** | myTributes' archive starts ~2019; `tributes.themorningbulletin.com.au` is decommissioned and not archived at notice level. Coverage gap. |
| **Trove pre-1891 Maryborough/Gympie** | Searched exhaustively including OCR variants (Schlegher, Sehleger, Schlegar, fuzzy). **Zero pre-1891 Queensland hits for Schleger in any spelling.** The bakery years (1879–1890) leave no newspaper trace that Trove has digitised. |

---

## Next steps (revised)

1. **Email Lynda Chalmers** (`blotweed@hotmail.com`, Sydney — she lists SCHLEGER *and* FRANK at
   Eisenstadt), then **Cathryn King** (`cjkin@queenslander.net`, Bundaberg). Ask each what the
   Eisenstadt attribution is based on: a record, or an inherited story. Zero cost, highest value.
2. **Read the "S" pages of the Matricula baptism indexes** for Hainburg, Wolfsthal, Berg,
   Prellenkirchen, Bad Deutsch-Altenburg and Petronell, 1845–1860 — and the Trauungsbücher for a
   **Carl Schleger × Katharina Frank** marriage c.1840–1850. Free, immediate, decisive either way.
   Deep links in `austrian-origin-pass2.md` §1e.
3. **Free FamilySearch account** → digital reels **004675473** and **004620339** (the direct test of
   the Eisenstadt hypothesis). Also free **GenTeam.at**.
4. **Qld Community & Personal Histories family-history request** — name **Rose Jackson / Rose Johnstone
   (b. c.1893, d. 12 Nov 1974, C7759/1974)**, her parents as recorded (**Robert Jackson**, **Millie
   Jackson**), the marriage **C2254/1919**, and cite **QSA ITM732477 / SRS4429/1/12474 / file 8R/119**
   directly. Frame the search around **Wide Bay–Burnett / Maryborough–Childers–Miriam Vale**, not
   Rockhampton. Ask whether CPH can confirm or exclude the identification.
5. **Buy two certificates first** (not four): Rose's 1974 death and the 1919 marriage. Between them
   they should give her birthplace, her age, her parents as stated by the informant, and — if it was
   required — the Protector's permission for the marriage, which would settle the question outright.
6. **Order a copy of QSA ITM1355052** (Public Curator file 75/1903, Ignatius Loyola) — it is Open
   Access and will contain medical and family correspondence from 1903–1910.
7. **Ask Carmel Schleger** (Phonse & Rose's daughter, an Indigenous consultant) what the family
   holds — with the corrected geography (Maryborough/Childers, not Rockhampton) and the corrected
   Johnstone spelling in hand.
8. Re-run the **Google Books** queries when the quota resets; and re-check **myTributes** periodically
   for the older Rockhampton notices as its archive is backfilled.
9. Minor: settle whether Alphonso Leo's youngest son was registered **Bernard Emmanual** or
   **Bernadine Eamon**; and whether Kevin Leo had a son **Frank** or whether "Frank" is Leonie's
   husband.
