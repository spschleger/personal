# SCHLEGER — Austrian/Hungarian origin, research pass 2 (raw evidence)

Research date: 2026-08-19. Method: free public web sources only. No logins, no payments.
Tools: curl (polite, 2s between requests), WebFetch, WebSearch.

Target person: Carl / Francis Charles "Frank" SCHLEGER, b. c.1851, baker.
- Naturalised Bundaberg, Queensland, 9 Sep 1886, aged 35, occupation baker, described as a
  "subject of the Kingdom of Hungary"; newspapers called him "a native of Austria".
- Parents per Qld death reg. C3513/1930: Carl SCHLEGER and Katharina FRANK.
- Arrived Maryborough, Qld 1878/79 (ship "Scottish Hero"); m. Mary O'Meara/O'Mara, Maryborough, Jun 1879.
- Implied birth window for register searching: c.1848–1854, searched widely as 1845–1860.

Origin hypotheses being tested:
- **H1 — Eisenstadt / Kismarton (Burgenland)** — per Bundaberg researcher Cathryn King (Burgenland Bunch).
- **H2 — Wolfsthal / Hainburg an der Donau, Bezirk Bruck an der Leitha (eastern Lower Austria)** —
  per present-day surname distribution, right on the old Hungarian border.
- **H3 (formulated during this pass, untested)** — one of the Hungarian-until-1921 border villages
  between the two: Kittsee/Köpcsény, Edelstal/Nemesvölgy, Deutsch Jahrndorf, Pama. These sit
  between Hainburg and Eisenstadt, were in the Kingdom of Hungary at the relevant date, and are
  within the modern Schleger surname cluster. H3 would satisfy *all three* of "subject of the
  Kingdom of Hungary", "a native of Austria", and the Wolfsthal/Hainburg distribution simultaneously.

TOP-LINE RESULT OF THIS PASS: two independent Burgenland Bunch researchers place SCHLEGER at
Eisenstadt→Australia in the 1870s, and one of them (Lynda Chalmers, Sydney) also lists the surname
**FRANK** — matching Katharina FRANK, the mother on the Qld death registration. That is a live,
free, human lead (Task 4c). Against that, BB's own transcribed record sets contain **no** Schleger
in the Eisenstadt district, and the 1857 Eisenstadt house lists contain none either (Task 4d).

---

## TASK 1 — MATRICULA ONLINE: parish register coverage

Root pages checked:
- https://data.matricula-online.eu/en/oesterreich/
- https://data.matricula-online.eu/en/ungarn/ → **HTTP 404, does not exist** (see 1f)
- https://data.matricula-online.eu/en/bestande/ (full country/fonds list)
- https://data.matricula-online.eu/en/suchen/ (place search)

### 1a. Diocese-level finding (critical)

Full list of Austrian holdings at https://data.matricula-online.eu/en/oesterreich/ , with parish counts:

| Slug | Label | Parishes |
|---|---|---|
| `burgenland` | Burgenland: Rk. Pfarren | **2** |
| `burgenland-ab-hb` | Burgenland: Ev. Kirchen A.B. und H.B. | 29 |
| `wien` | Wien/Niederösterreich (Osten): Rk. Erzdiözese Wien | **567** |
| `st-poelten` | Niederösterreich (Westen): Rk. Diözese St. Pölten | 410 |
| `daw` | Wien, Diözesanarchiv | 1 |
| `noela` | Niederösterreich: NÖ Landesarchiv | 2 |
| (others: Gurk, Linz, Salzburg, Graz-Seckau, Tirol, Vorarlberg, various evangelical) | | |

**>> The Roman Catholic Diözese Eisenstadt is NOT on Matricula Online.**
The `burgenland` collection (https://data.matricula-online.eu/en/oesterreich/burgenland/) contains
exactly **two** Roman Catholic parishes, and **neither is Eisenstadt**:
- https://data.matricula-online.eu/en/oesterreich/burgenland/kaisersteinbruch/ — Kaisersteinbruch
- https://data.matricula-online.eu/en/oesterreich/burgenland/moenchhof/ — Mönchhof

There is **no Eisenstadt / Kismarton parish on Matricula in any collection.**
H1 (Eisenstadt) therefore **cannot be tested on Matricula at all**. It requires either
Diözesanarchiv Eisenstadt directly, or FamilySearch's microfilm of the Hungarian RC registers
(login required — see Task 5).

### 1b. Archdiocese of Vienna (= eastern Lower Austria) — ALL H2 target parishes ARE online

All six border-district parishes exist as Matricula parishes:

- https://data.matricula-online.eu/en/oesterreich/wien/wolfsthal/ — Wolfsthal
- https://data.matricula-online.eu/en/oesterreich/wien/hainburg-an-der-donau/ — Hainburg an der Donau
- https://data.matricula-online.eu/en/oesterreich/wien/baddeutsch-altenburg/ — Bad Deutsch-Altenburg
- https://data.matricula-online.eu/en/oesterreich/wien/berg/ — Berg
- https://data.matricula-online.eu/en/oesterreich/wien/prellenkirchen/ — Prellenkirchen
- https://data.matricula-online.eu/en/oesterreich/wien/petronell-carnuntum/ — Petronell-Carnuntum (added as a neighbour)

Also present in the same district and available if the search needs widening:
Bruck an der Leitha, Höflein bei Bruck an der Leitha, Bergau, Schwechat.
(Full 567-parish list retrieved from `?page=1..6` of the `wien` collection.)

### 1c. COVERAGE — Taufbücher (baptism books) covering 1845–1860

**Every one of the six target parishes has continuous baptism coverage across the whole
1845–1860 window. There are no gaps.** Volumes to search:

**WOLFSTHAL**
- `01-03` Taufbuch **1827–1846** — https://data.matricula-online.eu/en/oesterreich/wien/wolfsthal/01-03/
- `01-04` Taufbuch **1846–1888** — https://data.matricula-online.eu/en/oesterreich/wien/wolfsthal/01-04/
  (one volume covers 1846–1888, i.e. the entire birth window in a single book)
- Supporting: `02-02` Trauungsbuch 1807–1850; `02-03` Trauungsbuch 1851–1898; `03-03` Sterbebuch 1836–1866

**HAINBURG AN DER DONAU** (best-granularity parish — 8-to-10-year volumes)
- `01-11` Taufbuch 1838–1844 — https://data.matricula-online.eu/en/oesterreich/wien/hainburg-an-der-donau/01-11/
- `01-12` Taufbuch **1845–1852** — https://data.matricula-online.eu/en/oesterreich/wien/hainburg-an-der-donau/01-12/  ← prime volume for b. c.1851
- `01-13` Taufbuch **1853–1863** — https://data.matricula-online.eu/en/oesterreich/wien/hainburg-an-der-donau/01-13/
- `01-14` Taufbuch 1864–1872 — https://data.matricula-online.eu/en/oesterreich/wien/hainburg-an-der-donau/01-14/
- Supporting: `02-09` Trauungsbuch 1830–1850 (parents' marriage); `02-10` Trauungsbuch 1851–1871; `03-09` Sterbebuch 1844–1865

**BAD DEUTSCH-ALTENBURG**
- `01-03` Taufbuch **1832–1854** — https://data.matricula-online.eu/en/oesterreich/wien/baddeutsch-altenburg/01-03/
- `01-04` Taufbuch **1855–1892** — https://data.matricula-online.eu/en/oesterreich/wien/baddeutsch-altenburg/01-04/
- Supporting: `02-02` Trauungsbuch 1768–1850; `02-03` Trauungsbuch 1851–1898; `03-03` Sterbebuch 1840–1876

**BERG**
- `01-03` Taufbuch **1829–1859** — https://data.matricula-online.eu/en/oesterreich/wien/berg/01-03/
- `01-04` Taufbuch **1859–1885** — https://data.matricula-online.eu/en/oesterreich/wien/berg/01-04/
- Supporting: `02-02` Trauungsbuch 1784–1845; `02-03` Trauungsbuch 1846–1898; `03-03` Sterbebuch 1834–1898

**PRELLENKIRCHEN**
- `01,2,3-05` Tauf-/Trauungs-/Sterbebuch 1815–1843 — https://data.matricula-online.eu/en/oesterreich/wien/prellenkirchen/01%252C2%252C3-05/
- `01-06` Taufbuch **1843–1874** — https://data.matricula-online.eu/en/oesterreich/wien/prellenkirchen/01-06/
  (single volume covers the entire birth window)
- Supporting: `02-06` Trauungsbuch 1844–1898; `03-06` Sterbebuch 1844–1888

**PETRONELL-CARNUNTUM**
- `01-07` Taufbuch **1841–1853** — https://data.matricula-online.eu/en/oesterreich/wien/petronell-carnuntum/01-07/
- `01-08` Taufbuch **1853–1871** — https://data.matricula-online.eu/en/oesterreich/wien/petronell-carnuntum/01-08/
- Supporting: `02-06` Trauungsbuch 1828–1871; `03-08` Sterbebuch 1840–1847; `03-09` Sterbebuch 1847–1860

### 1d. COVERAGE STATEMENT (summary)

> **COVERAGE:** For hypothesis H2 (Wolfsthal / Hainburg / Bad Deutsch-Altenburg / Berg /
> Prellenkirchen / Petronell-Carnuntum, all Archdiocese of Vienna), Matricula Online provides
> **complete, gap-free, freely-viewable Taufbuch scans across 1845–1860**, plus the matching
> Trauungsbücher (for the marriage of Carl SCHLEGER × Katharina FRANK, expected c.1840–1850)
> and Sterbebücher. Every volume needed is listed above with its exact URL. **All ten** of the
> relevant Taufbuch volumes carry a bound alphabetical **Index-Taufe** section (verified image-by-image,
> see 1e), so a surname lookup needs ~212 index images total, not thousands of register pages.
>
> For hypothesis H1 (Eisenstadt / Kismarton), Matricula Online has **ZERO coverage** — the
> Diözese Eisenstadt is not a Matricula partner and only two unrelated Burgenland RC parishes
> (Kaisersteinbruch, Mönchhof) are hosted. H1 cannot be progressed on Matricula.

Note: no OCR/scan reading was attempted, per scope. These are page-image registers.

### 1e. EVERY target volume carries a bound alphabetical baptism index — the search is cheap

Matricula exposes a per-volume image manifest (`labels` array in the volume page HTML). Checked
each 1845–1860 Taufbuch. All are **openly viewable, no login, no payment** (HTTP 200, plain
IIIF-style viewer, no auth wall), and **all ten have an `Index-Taufe` section**:

| Parish / volume | Years | Total images | Index images |
|---|---|---|---|
| hainburg-an-der-donau `01-12` | 1845–1852 | 385 | **25** |
| hainburg-an-der-donau `01-13` | 1853–1863 | 518 | **13** |
| wolfsthal `01-04` | 1846–1888 | 358 | **24** |
| berg `01-03` | 1829–1859 | 215 | **19** |
| berg `01-04` | 1859–1885 | 213 | **18** |
| prellenkirchen `01-06` | 1843–1874 | 364 | **30** |
| baddeutsch-altenburg `01-03` | 1832–1854 | 223 | **24** |
| baddeutsch-altenburg `01-04` | 1855–1892 | 312 | **24** |
| petronell-carnuntum `01-07` | 1841–1853 | 229 | **9** |
| petronell-carnuntum `01-08` | 1853–1871 | 260 | **26** |

**~212 index images in total cover the entire H2 hypothesis across all six parishes for 1845–1860.**
Looking up "Schleger" in the S-pages of those indexes is a couple of hours of eyeballing at most,
entirely free. This is the single cheapest decisive test available.

**Direct deep-links straight to the first index page** (the `?pg=N` parameter works — verified HTTP 200):

| Parish / volume | Years | Jump to index |
|---|---|---|
| hainburg-an-der-donau `01-12` | 1845–1852 | https://data.matricula-online.eu/en/oesterreich/wien/hainburg-an-der-donau/01-12/?pg=361 (imgs 361–385) |
| hainburg-an-der-donau `01-13` | 1853–1863 | https://data.matricula-online.eu/en/oesterreich/wien/hainburg-an-der-donau/01-13/?pg=506 (imgs 506–518) |
| wolfsthal `01-04` | 1846–1888 | https://data.matricula-online.eu/en/oesterreich/wien/wolfsthal/01-04/?pg=335 (imgs 335–358) |
| berg `01-03` | 1829–1859 | https://data.matricula-online.eu/en/oesterreich/wien/berg/01-03/?pg=197 (imgs 197–215) |
| berg `01-04` | 1859–1885 | https://data.matricula-online.eu/en/oesterreich/wien/berg/01-04/?pg=196 (imgs 196–213) |
| prellenkirchen `01-06` | 1843–1874 | https://data.matricula-online.eu/en/oesterreich/wien/prellenkirchen/01-06/?pg=335 (imgs 335–364) |
| baddeutsch-altenburg `01-03` | 1832–1854 | https://data.matricula-online.eu/en/oesterreich/wien/baddeutsch-altenburg/01-03/?pg=198 (imgs 198–223) |
| baddeutsch-altenburg `01-04` | 1855–1892 | https://data.matricula-online.eu/en/oesterreich/wien/baddeutsch-altenburg/01-04/?pg=289 (imgs 289–312) |
| petronell-carnuntum `01-07` | 1841–1853 | https://data.matricula-online.eu/en/oesterreich/wien/petronell-carnuntum/01-07/?pg=219 (imgs 219–229) |
| petronell-carnuntum `01-08` | 1853–1871 | https://data.matricula-online.eu/en/oesterreich/wien/petronell-carnuntum/01-08/?pg=235 (imgs 235–260) |

### 1f. Matricula Hungary — DOES NOT EXIST

`https://data.matricula-online.eu/en/ungarn/` returns **HTTP 404**. The authoritative fonds list at
https://data.matricula-online.eu/en/bestande/ shows Matricula hosts **only** these countries:

```
Deutschland  9095 parishes
Österreich   2857
Slovenia      660
Italien       106
Polen           5
Serbien         5
```

**There is no Hungary collection on Matricula at all.** So no Sopron/Ödenburg or Moson/Wieselburg
county register is on Matricula under any path.

Cross-checked with Matricula's own place search (https://data.matricula-online.eu/en/suchen/?place=X),
which correctly returns Hainburg an der Donau for `place=Hainburg`, but returns **zero results** for
every one of: `Eisenstadt`, `Kismarton`, `Kittsee`, `Edelstal`, `Jahrndorf`.

This also kills H3 (below) as a Matricula-testable hypothesis: the Hungarian-until-1921 border
villages (Kittsee/Köpcsény, Edelstal/Nemesvölgy, Deutsch Jahrndorf, Pama) are all Diözese Eisenstadt
parishes and are **not on Matricula either**.

---

## TASK 2 — ANNO (AustriaN Newspapers Online) full-text search

The ANNO search UI is an Angular SPA; the underlying free JSON API was located in the app bundle
`https://anno.onb.ac.at/anno-suche/main-6QGG4PKK.js` and is:

- `https://anno.onb.ac.at/anno-suche/rest/search/simple?query=<q>&from=0&facets=true`
- `https://anno.onb.ac.at/anno-suche/rest/search/complex?text=<q>&dateFrom=YYYY-MM-DD&dateTo=YYYY-MM-DD&place=<p>&title=<t>&from=0&facets=true`
- `https://anno.onb.ac.at/anno-suche/rest/search/snippet?documentId=<docId>&query=<q>`
- config (min/max date + full title list): `https://anno.onb.ac.at/anno-suche/rest/search/complex/config`

No key, no login. ANNO's indexed range is 1527-01-01 to 2025-12-31.

### 2a. Hit counts

| # | Query | Date range | totalHits |
|---|---|---|---|
| A | `"Schleger"` | 1840–1890 | 259 |
| — | `Schleger` (unquoted, all years) | all | 5285 |
| B | `"Schleger" AND "Eisenstadt"` | 1840–1890 | 21 |
| C | `"Schleger" AND "Kismarton"` | 1840–1890 | **0** |
| K | `"Schleger" AND "Kismarton"` | all years | 12 (earliest 1911) |
| D | `"Schleger" AND "Bäcker"` | 1840–1890 | 52 |
| E | `"Schleger" AND "Ödenburg"` | 1840–1890 | 72 |
| J | `"Schleger" AND "Bäcker" AND "Eisenstadt"` | 1840–1890 | 11 |
| F | `"Schleger"`, place=Eisenstadt | all years | 207 (all 1930+) |
| G | `"Schleger" AND "Hainburg"` | 1840–1890 | 28 |
| H | `"Schleger" AND "Wolfsthal"` | all years | 76 |
| I | `"Schleger" AND "Prellenkirchen"` | all years | 53 |
| L | `"Schleger" AND ("Queensland" OR "Australien")` | 1875–1935 | 98 |

**IMPORTANT CAVEAT:** ANNO's `AND` is *document-level*, not proximity. A hit means both terms appear
somewhere in the same issue — often on unrelated pages. Snippets were pulled to check each
promising 1840–1890 hit.

### 2b. Snippet verification of the 1840–1890 "Eisenstadt"/"Ödenburg" hits — ALL FALSE POSITIVES

Every pre-1890 co-occurrence checked turned out to be coincidental placement in hotel-arrival
lists (Fremdenlisten) or legacy/probate notices. None links a Schleger to Eisenstadt or Kismarton.

- **Fremden-Blatt, 4 Jul 1858, p.6** — http://data.onb.ac.at/ANNO/fdb18580704?query=%22Schleger%22&ref=anno-search&seite=6
  Text: `Schleger, Kfm, Wels.` and `Schleger, Prio, Waldh` — hotel arrivals list; the Schlegers
  are from **Wels (Upper Austria)** and Waidhofen, not Eisenstadt. Eisenstadt appears elsewhere on the page.
- **Wiener Zeitung, 17 Jän 1854, p.24** — http://data.onb.ac.at/ANNO/wrz18540117?query=%22Schleger%22&ref=anno-search&seite=24
  Text: `... Schleger, Hausknecht; Franz Koller, Zimmerputzer; Johann Rebell, Zimmerputzer ...`
  A list of servants/domestics (Vienna). No Eisenstadt link.
- **Wiener Zeitung, 7 Aug 1847, p.16** — http://data.onb.ac.at/ANNO/wrz18470807?query=%22Schleger%22&ref=anno-search&seite=16
  Text: `Schleger Barbara, Legat nach Aloysia Taucher und Katharina Dörflinger` /
  `Schleger Anna, Anna Holzer'sches Legat` — unclaimed-legacy list.
- **Wiener Zeitung, 17 Aug 1847, p.14** — http://data.onb.ac.at/ANNO/wrz18470817?query=%22Schleger%22&ref=anno-search&seite=14 — same legacy list, reprinted.
- **Fremden-Blatt, 4 Nov 1851, p.4** — http://data.onb.ac.at/ANNO/fdb18511104?query=%22Schleger%22&ref=anno-search&seite=4
  Text: `Schleger, k. k. Major, v. Preßburg.` then separately `Hr. Rosenberger, Handelsm., v. Oedenbg.`
  — the Ödenburg man is a different person on the next line. Note: a **Major from Pressburg
  (Bratislava)** — same border region as H2, ~15 km from Wolfsthal.
- **Fremden-Blatt, 17 Dez 1861, p.6** — http://data.onb.ac.at/ANNO/fdb18611217?query=%22Schleger%22&ref=anno-search&seite=6
  Text: `Schleger, Steyr.` — arrival from Steyr.

**Result: NO ANNO hit in 1840–1890 places a SCHLEGER in Eisenstadt or Kismarton.**
The earliest `Schleger` + `Kismarton` co-occurrence anywhere in ANNO is **1911**
(Deutsches Volksblatt 14 May 1911; Neues Wiener Tagblatt 19 May 1911), i.e. 60 years after the
birth in question and well after Frank had emigrated.

### 2c. POSITIVE SIGNAL — Schleger is a real, recurring surname in the Bruck an der Leitha / Hainburg district

Searching by newspaper title, the surname clusters heavily in the *local district press* of
exactly the Wolfsthal/Hainburg area (H2), not Eisenstadt:

- **Niederösterreichischer Grenzbote** (the Hainburg-district local paper) — `"Schleger"` = **30 hits**
  Search URL: https://anno.onb.ac.at/anno-suche/rest/search/complex?text=%22Schleger%22&title=Nieder%C3%B6sterreichischer+Grenzbote&from=0&facets=true&sort=date_asc
  Issues: 30 Sep 1917, 15 Feb 1920, 12 Feb 1928, 20 Jun 1937, 27 Jun 1937, 11 Jul 1937,
  25 Jul 1937, 21 Nov 1937, 19 Dez 1937, 20 Apr 1947, 28 Mär 1948, others.
  - Snippet, **NÖ Grenzbote 30 Sep 1917, p.4** — http://data.onb.ac.at/ANNO/non19170930?query=%22Schleger%22&ref=anno-search&seite=4
    `... Schleger, Marie Richl, Bartholomäus Hartl ...` and
    `... Schleger, Josef Kahler, Bartholomäus Burghart, Rosalia Berger, Katharina Sandriesser, Rosa Rein ...`
    (a local donors/subscribers list — i.e. resident villagers named Schleger)
- **Der Bezirksbote für den politischen Bezirk Bruck a.d. Leitha** — `"Schleger"` = 3 hits
  (15 Sep 1901, 4 Apr 1915, 26 Aug 1923)
  - Snippet, **Bezirksbote 15 Sep 1901, pp.2–3** — http://data.onb.ac.at/ANNO/beb19010915?query=%22Schleger%22&ref=anno-search&seite=2
    `... Schleger über das am Boden liegende Rad des Kainz stürzte und sich schwer verletzte ...` and
    `... Schleger stellte durch seinen Vertreter Ersatzansprüche und zwar: an Schmerzens[geld] ...`
    (a local court case — a resident Schleger suing over a bicycle collision)
- Combined-term counts reinforce this: `"Schleger" AND "Wolfsthal"` = 76, `"Schleger" AND
  "Prellenkirchen"` = 53 — and the top-ranked documents for both are **NÖ Grenzbote** and
  **Ostbahn-Bote** issues (1917, 1920, 1928, 1937, 1947, 1948), i.e. the Wolfsthal/Prellenkirchen
  local paper repeatedly carrying the name.

**ANNO DIGITISATION-WINDOW CAVEAT (important for interpreting the above):**
The district papers that would have named a Schleger family in 1845–1880 simply do not exist in
ANNO for that period. Measured directly:

| Newspaper | 1840–1899 issues in ANNO | 1900–1918 | 1919–1950 |
|---|---|---|---|
| Niederösterreichischer Grenzbote | **0** | 317 | 1604 |
| Der Bezirksbote (Bruck a.d. Leitha) | 24 | 985 | 903 |
| Burgenländische Freiheit (Eisenstadt) | **0** | **0** | 856 |

So the *absence* of 1845–1880 Wolfsthal/Hainburg Schleger newspaper hits is a coverage artefact,
not evidence of absence. The 1901–1948 local hits are the earliest the medium allows, and they
are consistent and repeated.

- **Burgenländische Freiheit** (Eisenstadt paper, ANNO run starts 1930) does carry Schleger
  (e.g. 3 Jän 1969, 25 Sep 1969, 10 Nov 1967, 29 Jän 1975, 30 Apr 1975) — but this is 20th-century
  and Burgenland-wide, and post-1921 Burgenland-Austrian; it does not localise to Eisenstadt town
  in the 1850s.

### 2d. Occupation- and given-name-targeted searches (all negative)

| Query | Range | totalHits | Verdict |
|---|---|---|---|
| `"Schleger" AND "Bäckermeister"` | 1850–1900 | 28 | All in Innsbruck / Klagenfurt / Linz / Mödling / Vienna theatre columns — no Burgenland or Bruck-district baker. |
| `"Schleger" AND "Bäcker" AND ("Hainburg" OR "Wolfsthal" OR "Bruck an der Leitha")` | 1850–1910 | 20 | Same Fremdenliste documents already shown false in 2b (Wiener Zeitung 17 Jän 1854, Fremden-Blatt 4 Jul 1858, Neues Fremden-Blatt 27 Jun 1867). |
| `("Carl Schleger" OR "Karl Schleger")` exact phrase | 1845–1890 | **1** | Single hit: Prager Tagblatt 8 May 1880 — http://data.onb.ac.at/ANNO/ptb18800508 . Prague, not the border region. |
| `"Schleger" AND "Frank" AND ("Eisenstadt" OR "Kismarton")` | 1840–1890 | 16 | Same hotel/legacy-list documents as 2b. No Schleger–Frank pairing. |

**The exact-phrase result matters:** across 45 years of the entire ANNO corpus, the name
"Carl Schleger"/"Karl Schleger" appears **once**, in Prague. There is no Austrian newspaper trace
of a Carl Schleger baker in either candidate region. This is consistent with an ordinary
village tradesman who would simply never appear in the press — it neither supports nor
undermines either hypothesis, but it closes the newspaper route for identifying the individual.

### 2e. ANNO conclusion

- No 1840–1890 ANNO evidence for a SCHLEGER at Eisenstadt / Kismarton. H1 gets **no support**.
- The surname is demonstrably resident in the **Bruck an der Leitha / Hainburg / Wolfsthal /
  Prellenkirchen** district from the earliest date the local press is digitised (1901). H2 gets
  **circumstantial support**, consistent with the modern surname distribution.
- Neither is proof. The register search (Task 1) is the decisive test.

---

## TASK 3 — Google Books

**BLOCKED — technical, not paywall.**

- API used: `https://www.googleapis.com/books/v1/volumes?q=...` (free, keyless).
- Queries attempted: `"Schleger" Eisenstadt`, `"Schleger" Kismarton`, `"Schleger" Ödenburg`,
  `"Schleger" Sopron`, `"Schleger" Bäcker`, plus a bare `Schleger` control, with and without `&country=US`.
- Every call returned **HTTP 429**:
  `Quota exceeded for quota metric 'Queries' and limit 'Queries per day' of service
  'books.googleapis.com' for consumer 'project_number:624717413613'`
  — i.e. the shared anonymous/keyless project quota is exhausted. Retried after delays, three times, same result.
- Fallback 1: HTML scrape of `https://www.google.com/search?q=%22Schleger%22+Eisenstadt&tbm=bks`
  → HTTP 200 but JS-only shell, zero rendered results; via WebFetch → consent/CAPTCHA interstitial.
- Fallback 2: HathiTrust full-text search
  `https://babel.hathitrust.org/cgi/ls?q1=%22Schleger%22%20Eisenstadt;a=srchls;anyall1=all;field1=ocr;lmt=ft`
  → **HTTP 403 Forbidden** (bot-blocked).
- Fallback 3: Internet Archive full-text API `https://ia-pub-fts-api.archive.org/search/v1/scrape`
  → connection failed (HTTP 000).

**NO Google Books result — positive or negative — was obtained. This task is NOT complete and
should be re-run later (the quota is daily and shared, so it may clear).** A free Google Books
API key would make this reliable.

---

## TASK 4 — The Burgenland Bunch (public pages only)

Site fully up; every URL below returned HTTP 200. No login used, no member-only area touched,
nothing submitted. (Legacy path `/surnames.htm` is a 404 — the site restructured to `/Surnames/surnames_*.html`.)

### 4a. SCHLEGER on the BB surname list — TWO hits, both Eisenstadt, both Australia

URL: **https://www.the-burgenland-bunch.org/Surnames/surnames_sc-sd.html** (page dated 29 Jun 2026)

Exact rows (Surname | Researcher | Village | Notes):

```
Schleger | Lynda Chalmers | Eisenstadt (Kis-Marton) | To Australia, 1870s before 1878.
Schleger | Cathryn King   | Eisenstadt (Kis-Marton) | Settled in Bundaberg, Australia, around the late 1870s.
```

These are the **only two SCHLEGER entries in the entire BB surname database**
(3,327 researchers / 9,590 surnames). Emails are JS-obfuscated on-page via `noSpam2(user,domain,tld,0)`;
decoded from raw HTML:
- Lynda Chalmers → `blotweed@hotmail.com`
- Cathryn King → `cjkin@queenslander.net`

### 4b. Cathryn King — public member entry (verbatim)

**https://www.the-burgenland-bunch.org/Members/BB-Members-IL.html** (Members I–L, updated 28 Jun 2026):

> "Cathryn King; Bundaberg, Queensland, Australia. SCHLEGER, Eisenstadt (Kismarton).
> Settled in Bundaberg around the late 1870s."

Also listed as a researcher on the Eisenstadt village page https://www.the-burgenland-bunch.org/Villages/E.htm.
No "Cathy King" / "C. King" pages exist. (Three unrelated Kings in the member list: Chris King, London;
Dianne (Pfeiler) King, PFEILER/Stadtschlaining; Julianna King, Bowdoinham ME.)

### 4c. >>> KEY NEW LEAD: Lynda Chalmers also lists FRANK <<<

**https://www.the-burgenland-bunch.org/Members/BB-Members-AD.html**:

> "Lynda Chalmers; Sydney, Australia. SCHLEGER, FRANK, Eisenstadt, to Australia probably 1870s
> but before 1878."

Email `blotweed@hotmail.com`.

*Both the Chalmers member entry and the two Schleger surname-table rows were re-fetched and
re-parsed first-hand during this pass — they are quoted verbatim from the live pages, not relayed.*

**This is the strongest single find of the pass.** Chalmers independently pairs the surname
SCHLEGER with the surname **FRANK** at Eisenstadt — and FRANK is exactly the mother's maiden name
on the Qld death registration (Katharina FRANK). Cathryn King does NOT list FRANK. That means
Chalmers is either working the same family from a different branch, or has the parents' generation
documented. She is in Sydney (same city as this researcher). **Contact Chalmers first, then King.**

### 4d. Negative evidence AGAINST Eisenstadt from BB's own record databases

The researcher claims are *claims*, not records. BB's actual transcribed data does not support them:

- **BB Combined Surnames List** (12,800+ surnames from 85,000+ families, built from the 1856–58
  house lists, Albert's Village Data and church birth records) —
  https://www.the-burgenland-bunch.org/HouseList/SurnamesListb.htm — contains exactly **one**
  SCHLEGER entry Burgenland-wide:
  ```
  1 | Schleger | JE | Zahling | 1693
  ```
  i.e. Zahling, Jennersdorf district (far south Burgenland), 1693. **No Schleger in the Eisenstadt
  district at all.**
- **Eisenstadt 1857 house list** — https://www.the-burgenland-bunch.org/HouseList/EU/Eisenstadt.htm
  ("Heads of house in: Eisenstadt 1857") and **Eisenstadt Berg 1857** —
  https://www.the-burgenland-bunch.org/HouseList/EU/EisenstadtBerg.htm
  → **zero Schleger / Schlegl / Schlögl** among heads of house. This is dead-centre in the 1845–1860
  window. Either the family were non-householding subtenants (BB explicitly notes such families
  "lived as subtenants in a farmhouse" and so are absent), or the Eisenstadt attribution is wrong.
- No BB-hosted transcription of Eisenstadt **Roman Catholic** registers exists for any period
  (https://www.the-burgenland-bunch.org/ChurchRecords/ChurchRecords.htm — Eisenstadt appears only
  under Jewish records, and those are marked "currently not available").

Other incidental SCHLEGER occurrences on BB (not Eisenstadt, likely unrelated):
- **Zahling** 1693 Urbarium Söllner list — https://www.the-burgenland-bunch.org/V_Histories/Zahling.htm
  (repeated in BB News No. 52, 28 Feb 1999 — https://www.the-burgenland-bunch.org/Newsletter/NL/Newsletter%20052.htm)
- **Szentpéterfa** 1787 birth, parents "Schleger, Joseph (Fr)" and "Schleger, Eve" —
  https://www.the-burgenland-bunch.org/ChurchRecords/Szentpeterfa/SzentpeterfaBirths2.htm

**Independently re-verified in this pass** (fetched https://www.the-burgenland-bunch.org/HouseList/SurnamesListb.htm
directly, 1.77 MB, and parsed every table row): the string `Schleger` occurs as a surname exactly
**once** in the entire file, and the row is:

```
1 | Schleger | JE | Zahling | 1693
```

All other near-matches in the file are genuinely different surnames — Schlegel, Schlegl, Schlagel,
Schlager, Schlögl, Schlögel, Schlogl — or village names containing "-schlag" (Redlschlag,
Holzschlag). **This is a free, positive negative result: across every Burgenland village house
list (1856–58) plus BB's church-birth data, there is no SCHLEGER in the Eisenstadt district and
none in the Kittsee / Edelstal / Deutsch Jahrndorf / Pama border strip (H3) either.**

*Caveat on that negative:* the BB combined list is built from house lists (heads of household only)
plus partial church records — it is not a complete transcription of the parish registers. A landless
or subtenant family, or a family that moved in after 1858, would be invisible to it. So this weakens
H1 and H3 but does not refute them.

Variants checked and **not found anywhere on BB**: SLEGER, SCHLÖGER.
Present but different families/villages: Schlegel (Fürstenfeld, Pilgersdorf, Deutsch Gerisdorf,
Lebenbrunn, Bubendorf); Schlagel/Schlögl/Schloegl (Burg, Steinbach, Girm, Deutschkreutz,
Piringsdorf, Hannersdorf, Lebenbrunn).

### 4e. Eisenstadt village + records pages

- **Village page:** https://www.the-burgenland-bunch.org/Villages/E.htm — "EISENSTADT (including
  Eisenstadt Schlossgrund = Kis-Marton-Váralja)"; Hungarian Kis-Marton, Croatian Željezno;
  parishes "Eisenstadt (RC, Jewish, civil) / Sopron, HU (LU until 1904)". Churches: Cathedral
  St. Martin and St. Rupert (Stadtpfarre), Haydnkirche, Johannes von Gottes Brüder, plus synagogues.
  32 named researchers incl. both King and Chalmers, plus Austria-based Eisenstadt researchers
  (Andrea Reiter `andrea.reiter1@chello.at`, Fabio Curman `genealogie@curman.at`, Oswald Held
  `o.held@hotmail.com`).
- **Thumbnail history:** https://www.the-burgenland-bunch.org/V_Histories/Eisenstadt.htm
- **>> The critical page for 1845–1860 RC records:**
  **https://www.the-burgenland-bunch.org/LDS/Eisenstadt.htm** ("BB Eisenstadt FamilySearch Films"):
  - Eisenstadt RC parish register start dates: Stadtpfarre 1624, St. Georgen 1658, Propstei 1680,
    Kleinhöflein 1710.
  - **Eisenstadt (Kis-Marton) RC B-M-D 1852–1860** — FHL film 700793, digital **004620339** →
    https://familysearch.org/search/film/004620339?cat=122648
    (then jumps to 1880–1895 on the same digital reel: Births i=84, Marriages i=247, Deaths i=350)
  - **Oberberg / Felső-Kismartonhegy RC B-M-D 1827–1870** — film 700771, digital **004675473** →
    https://familysearch.org/search/film/004675473?cat=112964 — **covers 1845–1860 continuously**
  - **Kleinhöflein / Kis-Höflény RC B-M-D 1827–1870** — film 700792, digital **004675486**
  - Jewish Eisenstadt B-M-D 1833–1895 — film 700794, digital 007952691
  - Military Eisenstadt B-M-D 1854–1871 — film 1454461 items 19–21, digital 007613321
  - BB states the pre-film originals "are now (or soon will be) online via Matriken.at, the records
    website of the Eisenstadt Diocese" — and https://www.the-burgenland-bunch.org/LDS/LDS.htm
    explicitly flags **Matriken.at as a PAY service**. So pre-1852 Eisenstadt Stadtpfarre originals
    are **not free**.
- **Village editor:** BB has no per-village editors. Surname & Villages Editor is **David Hofer**
  (per https://www.the-burgenland-bunch.org/Villages/Villages.htm and
  https://www.the-burgenland-bunch.org/Surnames/surnames.html). House lists/maps: **Klaus Gerger**.

### 4f. Public contact routes needing no membership

**Staff page:** https://www.the-burgenland-bunch.org/Staff/BB-Staff.html (emails in `(at)` form)
- President / Newsletter / DNA — **Tom Steichen**, Greencastle PA — `tj.steichen(at)comcast.net`
- Vice President / Houselists & Maps / Burgenland contact — **Klaus Gerger**, Vienna — `klaus.gerger(at)usa.net`
- Surname & Villages Editor — **David Hofer**, Alvarado TX — `david.hofer(at)sbcglobal.net`
- Membership Editor — Zac Stubits — `zac.stubits(at)the-burgenland-bunch.org`
- New Member Outreach — Patrick Kovacs, Vienna — `patrick.kovacs(at)the-burgenland-bunch.org`
- Research — Willi Schmidt, Allentown PA — `willischmidt(at)verizon.net`
- E-mail List Manager — Vanessa Sandu — `hooftyrn(at)msn.com`

Also free/open: public Facebook group https://www.facebook.com/groups/TheBurgenlandBunchOFFICIAL/ ;
the Ancestry Burgenland query board (linked from BB homepage); and the site-wide FreeFind search
`https://search.freefind.com/find.html?si=8480120&pid=r&query=<q>&mode=ALL` — indexes newsletters,
members, surnames, villages, houselists, no login.

**BB membership is itself free.** Homepage (https://www.the-burgenland-bunch.org/homepage.htm):
"The only requirement for membership is that you show a family connection to Burgenland;
membership is free (but nonetheless still valuable!)". Join form:
https://www.the-burgenland-bunch.org/MailOpen/new-member_vq.html — nothing was submitted in this pass.

---

## TASK 5 — Known login-gated dead ends (not attempted, per scope)

| Source | URL | Status |
|---|---|---|
| **GenTeam.at** | https://www.genteam.at | **Requires a free account.** Not attempted. This is the single highest-value blocked source: GenTeam hosts large Austrian/Burgenland index databases including Catholic parish indexes and Vienna-area name indexes. A free registration would very likely be the fastest test of both H1 and H2. |
| **FamilySearch** | https://www.familysearch.org | **Requires a free account.** Not attempted. Holds the microfilmed Hungarian RC registers for Sopron/Moson county incl. Kismarton (Eisenstadt) — i.e. the *only* practical way to test H1 remotely, since Matricula has zero Eisenstadt coverage. FamilySearch Full-Text Search (AI-transcribed) also now covers many Hungarian/Austrian registers. |

Both are free-to-register but require a login, which was out of scope for this pass.
**Recommendation: these two accounts are the obvious next step and cost nothing but an email address.**

### 5a. The exact FamilySearch reels to open the moment an account exists

Sourced free from BB's https://www.the-burgenland-bunch.org/LDS/Eisenstadt.htm — these are the
specific digitised reels that decide H1:

| Parish | Records | Years | FHL film | Digital / DGS | Direct link |
|---|---|---|---|---|---|
| **Eisenstadt (Kis-Marton)** RC | B-M-D | **1852–1860** | 700793 | **004620339** | https://familysearch.org/search/film/004620339?cat=122648 |
| **Oberberg / Felső-Kismartonhegy** RC | B-M-D | **1827–1870** | 700771 | **004675473** | https://familysearch.org/search/film/004675473?cat=112964 |
| **Kleinhöflein / Kis-Höflény** RC | B-M-D | 1827–1870 | 700792 | 004675486 | — |
| Eisenstadt Jewish | B-M-D | 1833–1895 | 700794 | 007952691 | — |
| Eisenstadt Military | B-M-D | 1854–1871 | 1454461 (items 19–21) | 007613321 | — |

Note the awkward fit: the main Eisenstadt town reel starts **1852**, one year *after* the c.1851
birth. **Oberberg (Felső-Kismartonhegy), 1827–1870, is the reel that actually covers the birth year
continuously** — and it is a suburb-parish of Eisenstadt. That is the single highest-value target.

### 5b. Matriken.at — PAYWALLED

https://www.the-burgenland-bunch.org/LDS/LDS.htm explicitly flags **Matriken.at** (the Diözese
Eisenstadt records website, which holds the pre-1852 Eisenstadt Stadtpfarre originals that predate
the FamilySearch filming) as a **pay service**. So the earliest Eisenstadt registers are behind
money, not just a login.

---

## TASK 6 — Hungarian free search surfaces (Hungaricana / MACSE / Arcanum / MNL / Radix)

No accounts created, no logins, no payments. Variants searched throughout: Schleger, Schléger,
Schlöger, Szleger, Sleger/Sléger.

### 6a. Paywall / login map (the headline)

| Source | Search | Counts + snippets | Full record / page | Verdict |
|---|---|---|---|---|
| **Hungaricana** library.hungaricana.hu | free | free (KWIC + page no.) | free page images | Fully open |
| **MNL** adatbazisokonline.mnl.gov.hu | free | free structured metadata | free datasheet + **full-res JPG** (2 MB, `/static/documents/1828/image/...`) | Fully open — richest free source |
| **Arcanum ADT** adt.arcanum.com | free | **free** — count, date, page, KWIC | Subscription (page/text/PDF; images 403) | Half-open; snippets alone are usable |
| **RadixIndex** radixindex.com | free | free surname→place counts | Subscription | Half-open |
| **RadixForum** radixforum.com | free | free | free | Open |
| **MACSE** macse.hu (NOT www.macse.hu — that domain is now a parked unrelated site) | free | **free** counts by locality/county | Login wall (`/db/ak/ak.php`) | Half-open |
| **FamilySearch full-text** | free account | — | — | Dead end without account |
| **GenTeam** genteam.at | free registration | — | — | Dead end without account. Site text: "Nach einer Registrierung und Anmeldung können Sie kostenfrei auf alle Datenbanken zugreifen." Two on-target DBs once registered: "Grabsteine Pannonien", "Jüdische Matriken im Burgenland". |

### 6b. Hungaricana (library.hungaricana.hu) — free, server-rendered

API pattern: `https://library.hungaricana.hu/hu/search/results/?list=<base64 of {"query":"..."}>` .
Accent-insensitive. Per-page OCR endpoints return 403; snippets are the free layer.

| Query | URL | Hits |
|---|---|---|
| Schleger | https://library.hungaricana.hu/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciJ9 | 417 |
| Schleger Sopron | https://library.hungaricana.hu/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciBTb3Byb24ifQ== | 21 |
| Schleger pék (baker) | https://library.hungaricana.hu/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciBwXHUwMGU5ayJ9 | 12 |
| Schleger Moson | https://library.hungaricana.hu/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciBNb3NvbiJ9 | 1 |
| Szleger | https://library.hungaricana.hu/hu/search/results/?list=eyJxdWVyeSI6ICJTemxlZ2VyIn0= | 3 |
| Schleger + Kismarton / Eisenstadt / Ödenburg / Wieselburg | (all four run) | **0 each** |

Genuine 18th–19th c. Schleger hits — all **Vas county / Szombathely diocese**, i.e. south of the target:
- Géfin, *A szombathelyi egyházmegye története III* (1935) p.357: "4135 Schleger György, sz. Csémben 1752 körül… 4136 Schleger József, sz. Csémben 1755 körül" —
  https://library.hungaricana.hu/hu/view/SZELT_SK_011/?query=Schleger&pg=360
- Tangl, *A Vasvár-Szombathelyi Székeskáptalan magánlevéltára* (2019) p.45: "Schleger József 1755–1834, **németlövői plébános**" (Németlövő = Deutsch Schützen, today southern Burgenland) —
  https://library.hungaricana.hu/hu/view/SZELT_SK_018/?query=Schleger&pg=150
- *Calendarium… elhunyt papjai 1777–2002* (2002): "SCHLEGER GYÖRGY, Csém 1752" (p.149); "1834 SCHLEGER JÓZSEF, Csém 1755, 79" (p.65) —
  https://library.hungaricana.hu/hu/view/SZELT_SK_019/?query=Schleger&pg=150
- *Magyarország iparosainak… cím- és lakjegyzéke* (1892) p.1467 "Schleger Vendel" — cross-checked on ADT: **Somogy county (Kaposvár)**, not Sopron. Not a lead.

**Negative: zero co-occurrence of Schleger with Kismarton, Eisenstadt, Ödenburg or Wieselburg anywhere in Hungaricana's full text.**

### 6c. MACSE (macse.hu) — aggregate counts free, records behind login

Free surname aggregate: `https://macse.hu/db/dbf.php?ln=Schleger&fn=&lang=hu&btnPolg=Kereses`
- Civil registers (1895+): births 14, marriages 31, deaths 70 — Budapest districts, Bicske (Fejér, 13),
  Békéscsaba, Szegvár, Debrecen, Salgótarján, Szombathely (Vas, 1), Pápa, Veszprém, Nagykanizsa, etc.
- Church registers: Dunabogdány, Hidegkút, Szarvas, Zsámbék, Jászárokszállás.
- **Sopron: 0. Moson: 0. Kismarton: 0.** Szleger: 0. Schlöger: 3 (Budapest).
- Structural reason: Kismarton left Hungary in 1921, so post-1895 Hungarian civil indexes never cover it.

### 6d. Arcanum ADT (adt.arcanum.com) — snippets free, pages paid

| Query | URL | Hits |
|---|---|---|
| Schleger | https://adt.arcanum.com/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciJ9 | 7,366 |
| Schleger Kismarton | https://adt.arcanum.com/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciBLaXNtYXJ0b24ifQ== | 20 |
| Schleger Eisenstadt | https://adt.arcanum.com/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciBFaXNlbnN0YWR0In0= | 571 |
| Schleger Bäcker | https://adt.arcanum.com/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciBCXHUwMGU0Y2tlciJ9 | 69 |
| "Schleger Károly" | https://adt.arcanum.com/hu/search/results/?list=eyJxdWVyeSI6ICJcIlNjaGxlZ2VyIEtcdTAwZTFyb2x5XCIifQ== | 31 |
| Schleger Ödenburg | https://adt.arcanum.com/hu/search/results/?list=eyJxdWVyeSI6ICJTY2hsZWdlciBcdTAwZDZkZW5idXJnIn0= | 2 |

Date filtering is not honoured via URL; restriction is by co-occurrence + reading snippet dates.

Disambiguation of the big numbers:
- The 571 "Schleger Eisenstadt" hits are almost entirely **1965–1989 Burgenländische Freiheit** football coverage of **Dr. Schleger, trainer of SC Eisenstadt**. Nothing 19th c.
- All 31 "Schleger Károly" (= Carl/Karl) hits, c.1911–1919, are one **Pápa (Veszprém)** family — Schleger Károly, day-labourer / MÁV railway worker, wife Bujcs Anna. Wrong man, wrong trade, wrong county.
- "Schleger Bäcker" hits are Vienna Wiener Zeitung lists (1746/1748/1831), coincidental.

**The one genuinely regional hit:** *Sopronvármegye* (Sopron), 25 Sep 1918, war-charity subscription
list: "…katonai rendőrség Herzl József 20, **Schleger Ferenc 10**, Rittsteuer Mátyás…" in the same
column as "Wolf Lipót sen. **Kismarton** 100" — Rittsteuer is a characteristic Kismarton-district surname.
https://adt.arcanum.com/hu/view/Sopronvarmegye_1918_09/?query=Schleger%20Kismarton&pg=113
This is a Schleger in the Sopron/Kismarton orbit in **1918** — 40 years after Frank emigrated. Weak but real.

**No baker (pék/Bäcker) named Schleger in Kismarton or Sopron appears in any free Hungarian full-text corpus.**

### 6e. MNL Adatbázisok Online (adatbazisokonline.mnl.gov.hu) — fully free, and the 1828 census "hit" REFUTED first-hand

API: `https://adatbazisokonline.mnl.gov.hu/search?term=<base64 of {"q":"Schleger","fq":{...},"sort":"score"}>`;
results embedded as `var searchResults = [...]` in the HTML. 1828-census facet filter:
`{"db_id":{"b83aac23b9528732c23cc7352950e880":"\"327\""}}`.

Full search (236 docs): https://adatbazisokonline.mnl.gov.hu/search?term=eyJxIjoiU2NobGVnZXIiLCJmcSI6W10sInNvcnQiOiJzY29yZSJ9
1828 Regnicolaris conscription hits (20 pages) include:
- **Sopron vármegye / Kis-Marton (109) – 28** — https://adatbazisokonline.mnl.gov.hu/adatbazis/az-1828-evi-orszagos-osszeiras/adatlap/1CC352A623804BEC33F7169A6B2C053F
- **Sopron vármegye / Kis-Marton (109) – 29** — https://adatbazisokonline.mnl.gov.hu/adatbazis/az-1828-evi-orszagos-osszeiras/adatlap/5F1E2D4F64014DB34F575E0E41B005FA
- Moson vármegye / Moson (30) – 3, – 4 ; Moson vármegye / Miklósfalu (29) – 17, – 18
- Others: Nyitra/Farkasd, Somogy/Endréd, Baranya/Mekényes, Heves/Gyöngyös-Oroszi, Pest & Buda suburbs, Károlyváros.

**The two Kis-Marton pages were downloaded at full resolution (3500×2587, ~2 MB each, no login;
`/static/documents/1828/image/HU_MNL_OL_W_21_31_N_26_ComSoproniensis/HU_MNL_OL_W_21_31_N_26_ComSoproniensis_109_Kis-Marton/E8D80BF9B391412FACA2D048EC4DFB8F.jpg` and
`.../D69B22768F0B4ECDC6D0DEE89B2AF2F1.jpg`) and read.**

Result: page 28 (left half) and page 29 (right half, Observationes) are the same spread, households
Nr. 261–280 of "Oppidum Kis Marton / Eisenstadt", Comitatus Soproniensis. **Every entry on the spread
is prefixed "Jud:" — this is the Jewish community section** (Nr. 276 is "Communitas Judaica";
Observatio to 272: "Habitat in Domo Communitatis in qua Synagoga est"). The name the MNL handwriting
recognition matched to "Schleger" is **Nr. 273 "Jud: Vid: Aaron Schlesinger"** — the widow of Aaron
SCHLESINGER. There is **no SCHLEGER on either page**. Neighbours for the record: Reichnitz, Reitlinger,
Fürst, Berner, Diring, Veis, Spitzer, Karpeles, Hirsch, Schönfeld, Wolf, Belz, Machalup, Unger,
Schneider, Mayer.

**So the MNL 1828 "Kis-Marton SCHLEGER" is a false positive (fuzzy HTR match on Schlesinger). The
1828 census does NOT place a Schleger household in Eisenstadt.** The Moson (30-3/4) and Miklósfalu
(29-17/18) hits were not image-checked and may be similar fuzzy matches; treat as unverified.

Also from MNL, unverified by image: SCHLÖGER in the 1828 census, Sopron county — Németh-Keresztur
(154)-20, Deretske (48)-2, Veingraben (220)-4, Sopronium city (60)-164
(https://adatbazisokonline.mnl.gov.hu/search?term=eyJxIjogIlNjaGxcdTAwZjZnZXIiLCAiZnEiOiBbXSwgInNvcnQiOiAic2NvcmUifQ==).
SZLEGER: 1 only (Fejér/Etyek). MNL HTR civil registers (153 Schleger hits): all Pest county
(Törökbálint, Torbágy, Budajenő, Budakeszi, Érd, Nagymaros).

### 6f. RadixIndex / RadixForum

- Free surname roll-up (POST `https://www.radixindex.com/cgi-bin/rixidxvn.cgi`, `act=searchsn&q=Schleger&lan=en`):
  1891 trade directory — Schléger: Kassa; Schleger: Bicske. RadixRef — Budapest, Nemesócsa, Szépliget,
  Temesvár, Újvidék, Bicske, Déva, Nagykanizsa. **WW1 Verlustliste — Schleger: Halbstadt, Kaunova (3),
  Kopitz, Törökbálint, Wien, and *Wolfsthal*.** No Sopron, Moson or Kismarton. Schlöger 0, Szleger 0.
  (The Wolfsthal WW1 casualty is one more small independent tick for the H2 surname cluster.)
- https://www.radixforum.com/surnames/schleger/ — 8-message board, all one **Veszprém county
  (Bakonyoszlop)** Schléger line (János d.1828 aged 52; Mátyás b.1842 Bakonyoszlop, to USA 1885–1900;
  Anton m.1900). Named researcher Bozsaky Dávid. Not the target line; useful only for exclusion.

### 6g. Task 6 conclusion

- **No free Hungarian index — Hungaricana, MACSE, ADT, MNL, Radix — places a SCHLEGER in Kismarton,
  Sopron or Moson county in 1840–1880.** The single apparent record hit (MNL 1828 Kis-Marton) was
  image-verified and is SCHLESINGER.
- Every documented 19th c. Hungarian SCHLEGER cluster is elsewhere: Vas/Szombathely (Csém priests,
  one at Deutsch Schützen), Veszprém (Bakonyoszlop, Pápa), Fejér (Bicske), Zala (Nagykanizsa),
  Somogy, Pest (Törökbálint etc.). Treat as exclusions.
- One weak regional trace: Schleger Ferenc, Sopron 1918.
- One more H2 tick: a WW1 casualty Schleger from Wolfsthal in the Verlustliste.
- Kismarton's own RC registers are held by Diözese Eisenstadt (not on Matricula; pre-1852 layer on
  paid Matriken.at; 1852+ on FamilySearch behind a free login). Diözese Eisenstadt contact per
  Matricula's own referral: +43 2682 777-234, museum@martinus.at.

---

## OVERALL ASSESSMENT AFTER PASS 2

### What actually moved

1. **A named human lead with the mother's surname.** Lynda Chalmers (Sydney,
   `blotweed@hotmail.com`) publicly researches **SCHLEGER *and* FRANK at Eisenstadt, "to Australia
   probably 1870s but before 1878"**. Katharina FRANK is the mother on the Qld death registration.
   Cathryn King (Bundaberg, `cjkin@queenslander.net`) has SCHLEGER/Eisenstadt/Bundaberg but *not*
   FRANK. Two independent researchers converging on Eisenstadt, one of them with the second
   surname right, is the most substantive thing found in this pass. **Both are contactable for free.**

2. **Matricula settles the method question, not the answer.** All H2 parishes are online,
   gap-free for 1845–1860, with bound alphabetical indexes — ~212 index images decide H2 for free.
   H1 (Eisenstadt) has *zero* Matricula coverage; Matricula has **no Hungary collection at all**.
   So H2 is testable right now at no cost; H1 needs FamilySearch (free account) and its pre-1852
   layer needs paid Matriken.at.

3. **ANNO gives no support to H1 and circumstantial support to H2.** No 1840–1890 Schleger/Eisenstadt
   or Schleger/Kismarton link exists — every apparent hit is a hotel-arrival or unclaimed-legacy
   list coincidence, verified snippet by snippet. Meanwhile Schleger is repeatedly a *resident*
   surname in the Bruck an der Leitha / Hainburg / Wolfsthal / Prellenkirchen district from 1901 —
   the earliest year the local press is digitised. **The pre-1900 silence there is a digitisation
   artefact, not evidence of absence** (measured: NÖ Grenzbote has 0 issues before 1900).

4. **A free negative against H1 and H3 from BB's own data.** Across every Burgenland village
   house list (1856–58) plus BB's church-birth data, SCHLEGER appears exactly once —
   *Zahling, 1693* — and the Eisenstadt 1857 house lists contain none. Independently re-verified.
   This does not refute H1 (subtenants and non-householders are invisible to house lists), but it
   does mean the Eisenstadt attribution currently rests on researcher assertion, not on any
   transcribed record anyone has published.

5. **The Hungarian free indexes are unanimous: no Schleger in Kismarton/Sopron/Moson 1840–1880**
   (Hungaricana, MACSE, Arcanum snippets, MNL, Radix — Task 6). The one apparent record, MNL's
   1828-census "Kis-Marton SCHLEGER", was pulled at full resolution and read: it is the widow of
   Aaron **SCHLESINGER** in the Jewish-community list — a handwriting-recognition fuzzy match. Two
   small H2 ticks fell out of the same sweep: a WW1 Verlustliste Schleger from **Wolfsthal**, and
   nothing at all for the surname in the Hungarian side of the border strip.

### Net position

**H1 (Eisenstadt) has the human testimony (two BB researchers, one with FRANK) but, after
this pass, still no record of any kind — Burgenland house lists, Hungarian census, Hungarian
full-text, Austrian newspapers all come up empty for the surname there.
H2 (Hainburg/Wolfsthal) has the surname distribution, repeated 20th-c. local-press residency,
a Wolfsthal WW1 casualty, and the free, complete, indexed registers — but no direct evidence yet.
Neither is established.** H3 (Hungarian border villages —
Kittsee, Edelstal, Deutsch Jahrndorf, Pama) remains attractive on paper because it reconciles
"subject of the Kingdom of Hungary" with "a native of Austria" and with the modern surname
cluster — but it is not on Matricula either, and BB's house lists show no Schleger there.

### Next actions, cheapest first

1. **Email Lynda Chalmers** (`blotweed@hotmail.com`) — she is in Sydney and lists both SCHLEGER
   and FRANK at Eisenstadt. Then Cathryn King (`cjkin@queenslander.net`). Ask each what the
   Eisenstadt attribution is actually *based on* — a record, or an inherited family story.
   Zero cost, highest expected value.
2. **Read the S-pages of the Matricula baptism indexes** for Hainburg `01-12` / `01-13` and
   Wolfsthal `01-04` (then Berg, Prellenkirchen, Bad Deutsch-Altenburg, Petronell). Free,
   immediate, and decisive for H2. Also check the Trauungsbücher for a Carl SCHLEGER × Katharina
   FRANK marriage c.1840–1850.
3. **Register free at FamilySearch**, then open digital reel **004675473** (Oberberg /
   Felső-Kismartonhegy RC, 1827–1870 — the only Eisenstadt-area reel that continuously covers the
   c.1851 birth year) and **004620339** (Eisenstadt town RC, 1852–1860). This is the direct test of H1.
4. **Register free at GenTeam.at** — its Austrian/Burgenland index databases would test H1, H2 and
   H3 at once.
5. **Re-run the Google Books queries** once the shared daily API quota resets (or with a free API key).
6. Consider joining the Burgenland Bunch (free) to add a SCHLEGER/Eisenstadt entry alongside King
   and Chalmers, and to email David Hofer (Surname & Villages Editor) or Klaus Gerger (Vienna-based,
   houselists/maps) — both listed publicly on the BB staff page.
