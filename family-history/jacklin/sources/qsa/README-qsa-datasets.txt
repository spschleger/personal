QSA indexes used in pass 3 (all free open data from https://www.data.qld.gov.au — CKAN API)

KEPT HERE:
  assisted-immigration-1848-1912-h.csv  (Holmes family, Dacca 1887 - the key hit)
  assisted-immigration-1848-1912-j.csv  (all Jacklin entries in the assisted index)
  qsa-assisted-immigration-register-1883-hannah-landels-DR38564.pdf
        = the register volume containing the "Hannah Landels" list (arrival 11 Sep 1883),
          register page 237, item ITM18480, digital image DR38564 -- the page carrying
          JACKLINE Thomas (25) and JACKLINE Fanny (24), i.e. Thomas Jacklin and Fanny Margaret
          nee Holmes. https://www.archivessearch.qld.gov.au/api/download_file/DR38564
  qsa-assisted-immigration-register-1887-DR38134.pdf
        = the scanned register volume containing the Dacca (26 Jul 1887) passenger list,
          QSA series S13086, item ITM18484, register page 170, digital image DR38134.
          Downloaded free from https://www.archivessearch.qld.gov.au/api/download_file/DR38134

WARNING ON SPELLINGS: the 1883 Jacklin arrival is indexed under the surname JACKLINE and the
ship is spelled "Hannah Landels" (one final l). Search on short stems, e.g. grep -i "jacklin" and
grep -i "landel".

SEARCHED AND DELETED (all returned NIL for JACKLIN / HOLMES-of-Mackay; re-download if needed):
  registers-of-immigrants-1882-1938.csv  (20 MB)
      https://www.data.qld.gov.au/dataset/3b20c3ba-a9a9-4f39-b35a-9edb642fe6be/resource/92549282-330f-49ea-bf20-4ecef54e7ec2/download/register-of-immigrants-1882-1938.csv
      -> no JACKLIN/JACKLINE at all in this dataset.
  land-selections-1885-1981.csv  (20 MB)
      https://www.data.qld.gov.au/dataset/03e462ee-9ad3-4974-a770-e536cf827bd0/resource/54cbd1ea-03a8-4b59-b478-526001663226/download/land-selections-1885-1981.csv
      -> no JACKLIN. (One HOLMES, David Henry, selection 149, Mackay, 28 Jul 1890, LAN/P324, ITM23910 - relationship unknown.)
  registers-of-applications-by-selectors-1868-1885.csv  (17 MB)
      https://www.data.qld.gov.au/dataset/c56272b9-9159-4f84-8a4a-2eaabd5c7923/resource/95e39f44-f522-4f94-97a2-f21b2589446d/download/registers-of-applications-by-selectors-1868-1885.csv
      -> no JACKLIN.

Also noted but not downloaded: naturalisations-1851-to-1908 (Irish-born were already British subjects,
so John Taylor / Mary North would not appear).
