import requests, hashlib, json, sys, time, os
BASE="/Users/shane/personal/family-history/jacklin/sources"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S=requests.Session(); S.headers.update({"User-Agent":UA,"Accept":"application/json"})
S.get("https://trove.nla.gov.au/")
ctx=S.cookies.get("x-ctx"); key=hashlib.md5(("Wonder"+ctx).encode()).hexdigest().lstrip("0")
H={"apikey":key,"Referer":"https://trove.nla.gov.au/search"}
OUT=f"{BASE}/trove-hits-pass3.jsonl"
seen=set()
for l in open(OUT):
    try: seen.add(json.loads(l)["id"])
    except: pass
def q(terms, limits=None, maxn=300, tag=""):
    pos=0;n=0;tot=None;f=open(OUT,"a")
    while pos<maxn:
        p={"terms":terms,"pageSize":100,"startPos":pos}
        if limits: p["limits"]=json.dumps(limits)
        try: d=S.get("https://trove.nla.gov.au/api/search/137",params=p,headers=H,timeout=60).json()
        except Exception as e:
            print("err",e); break
        tot=d.get("totalRecords"); ws=d.get("works",[])
        for w in ws:
            if w["id"] in seen: continue
            seen.add(w["id"]); n+=1
            rec={k:w.get(k) for k in ("id","title","newspaper","date","page","snippets","wordCount","articleType")}
            rec["q"]=tag or terms
            f.write(json.dumps(rec,ensure_ascii=False)+"\n")
        f.flush()
        if not d.get("hasMoreResults") or not ws: break
        pos+=len(ws); time.sleep(0.4)
    f.close(); print(f"[{tag or terms}] total={tot} new={n}",flush=True); return tot
Y=lambda y:{"decade":[str(y)[:3]],"year":[str(y)]}
QS=[
 ('Ward Cunninghame',Y(1907),'Ward Cunninghame 1907'),
 ('Ward "Lake Tyers"',Y(1907),'Ward Lake Tyers 1907'),
 ('Ward Bairnsdale death',Y(1907),'Ward Bairnsdale death 1907'),
 ('Ward Cunninghame',Y(1908),'Ward Cunninghame 1908'),
 ('"Henry Ward" Dunolly',None,'Henry Ward Dunolly'),
 ('Ward Eddington obituary',None,'Ward Eddington obit'),
 ('Cunningham "Tambo River"',None,'Cunningham Tambo River'),
 ('"Thomas Cunningham" Bruthen',None,'Thomas Cunningham Bruthen'),
 ('Cunningham Johnsonville Bruthen',None,'Cunningham Johnsonville'),
 ('Jacklin "Louth Park"',None,'Jacklin Louth Park'),
 ('"T. Jacklin" Eton',None,'T Jacklin Eton'),
 ('Jacklin Mackay obituary 1931',None,'Jacklin obit 1931'),
 ('Holmes "North Eton" Jacklin',None,'Holmes North Eton'),
 ('"Jarvis Holmes"',None,'Jarvis Holmes'),
 ('"Mrs. Harvison" Woodford',None,'Mrs Harvison Woodford'),
 ('Jacklin Nudgee College',None,'Jacklin Nudgee College'),
 ('"Jacklin" Mackay hospital doctor',None,'Jacklin Mackay hospital'),
 ('Spunner Windsor death 1926',None,'Spunner Windsor 1926'),
 ('"W. H. Spunner"',None,'W H Spunner'),
 ('Corkhill Spunner',None,'Corkhill Spunner'),
]
for t,l,tag in QS:
    try: q(t,l,tag=tag)
    except Exception as e: print("FAIL",tag,e)
    time.sleep(0.5)
