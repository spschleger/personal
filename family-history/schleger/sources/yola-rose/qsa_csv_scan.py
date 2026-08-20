#!/usr/bin/env python3
"""Scan every downloaded QSA open-data index CSV (data.qld.gov.au) for a surname
(+ optional given-name regex).  Prints one line per hit with the file it came from,
so every hit is citable as <dataset CSV> / QSA Ref / Item ID / Digital Image ID.

usage:  qsa_csv_scan.py '<surname regex>' ['<given regex>']
"""
import csv, os, re, sys, glob

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qsa-csv")
LAST = ("last name", "lastname", "last_name", "surname", "family name", "name")
GIVEN = ("given names", "given name/s", "given name", "givennames", "first name",
         "given names/s", "other names", "first names")
DROP = ("item id source", "digital image id source", "index name", "description",
        "archivist notes", "responsible agency id", "responsible agency title",
        "series title", "record type", "item format")

def col(keys, cands):
    for k in keys:
        if k.strip().lower() in cands:
            return k
    return None

def scan(surname, given=None):
    sre = re.compile(surname, re.I)
    gre = re.compile(given, re.I) if given else None
    for fn in sorted(glob.glob(os.path.join(HERE, "*.csv"))):
        try:
            rows = list(csv.DictReader(open(fn, encoding="utf-8-sig", errors="replace")))
        except Exception as e:
            print(f"!! {os.path.basename(fn)}: {e}"); continue
        if not rows: continue
        keys = list(rows[0].keys())
        lc = col(keys, LAST); gc = col(keys, GIVEN)
        if not lc:
            continue
        for r in rows:
            l = (r.get(lc) or "").strip()
            g = (r.get(gc) or "").strip() if gc else ""
            if not sre.search(l):
                # some indexes put the whole name in one column
                if not (gc is None and sre.search(g)):
                    continue
            if gre and not gre.search(g):
                continue
            body = " | ".join(f"{k}={v.strip()}" for k, v in r.items()
                              if v and v.strip() and k.strip().lower() not in DROP)
            print(f"[{os.path.basename(fn)}] {body}")

if __name__ == "__main__":
    scan(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
