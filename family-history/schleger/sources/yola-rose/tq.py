#!/usr/bin/env python3
"""Trove phrase-query helper for pass 4. Prints hits (optionally filtered to a
newspaper-name regex) and appends everything to trove-hits-yola-rose.jsonl."""
import json, re, sys, os, time
import trove_yr as T

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trove-hits-yola-rose.jsonl")

def q(terms, limits=None, n=40, paper=None, show=True, tag=""):
    p = {"terms": terms, "pageSize": min(n, 100), "startPos": 0}
    if limits: p["limits"] = json.dumps(limits)
    for att in range(4):
        try:
            d = T.S.get("https://trove.nla.gov.au/api/search/137", params=p,
                        headers=T.H, timeout=60).json(); break
        except Exception:
            time.sleep(3 * (att + 1)); d = {}
    ws = d.get("works", [])
    pre = re.compile(paper, re.I) if paper else None
    out = []
    f = open(OUT, "a")
    for w in ws:
        if pre and not pre.search(w.get("newspaper") or ""): continue
        out.append(w)
        rec = {k: w.get(k) for k in ("id", "title", "newspaper", "date", "page",
                                     "snippets", "wordCount", "articleType")}
        rec["q"] = terms; rec["tag"] = tag
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    f.close()
    if show:
        print(f"--- {terms!r} limits={limits} total={d.get('totalRecords')} shown={len(out)}")
        for w in out:
            sn = " // ".join(re.sub(r"</?em>", "", s) for s in (w.get("snippets") or []))[:260]
            print(f"  [{w['id']}] {w.get('date')} | {(w.get('newspaper') or '')[:44]} | {w.get('title','')[:50]}")
            print(f"        {sn}")
    return out

if __name__ == "__main__":
    q(sys.argv[1], paper=sys.argv[2] if len(sys.argv) > 2 else None)
