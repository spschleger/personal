#!/usr/bin/env python3
"""Pass 4 — pull COMPLETE Qld BDM index sets for a surname and cache as JSONL.

IMPORTANT (correction to pass 2's method): the familyhistory.bdm.qld.gov.au /search
endpoint appears to IGNORE the fathersname / mothersname / spousename parameters —
sending them returns the unfiltered surname set. So: pull the whole surname set once
and filter locally.  A blank subjectfamilyname returns the whole index (capped 10000)
and must never be used.
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import qbdm

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = {"births": ("01/01/1829", "31/12/1924"),
       "marriages": ("01/01/1829", "31/12/1949"),
       "deaths": ("01/01/1829", "31/12/1994")}

def pull(fam, rtype, exact=True, given=""):
    tag = f"{fam.lower()}-{rtype}" + (f"-{given.lower()}" if given else "") + ("" if exact else "-fuzzy")
    fn = os.path.join(HERE, "bdm", tag + ".jsonl")
    os.makedirs(os.path.join(HERE, "bdm"), exist_ok=True)
    if os.path.exists(fn) and os.path.getsize(fn) > 0:
        return [json.loads(l) for l in open(fn)]
    if rtype == "deaths":
        recs = qbdm.search2(fam, given, rtype, RNG[rtype], exactfam=exact)
    else:
        recs = qbdm.search(fam, given, rtype, RNG[rtype], exactfam=exact)
    with open(fn, "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{tag}: {len(recs)}", file=sys.stderr)
    time.sleep(0.5)
    return recs

if __name__ == "__main__":
    for spec in sys.argv[1:]:
        parts = spec.split(":")
        fam, rtype = parts[0], parts[1]
        exact = not (len(parts) > 2 and parts[2] == "fuzzy")
        r = pull(fam, rtype, exact)
        print(f"{spec} -> {len(r)}")
