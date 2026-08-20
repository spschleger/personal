import requests, hashlib, json, sys, time, re, os
from bs4 import BeautifulSoup
BASE="/Users/shane/personal/family-history/jacklin/sources"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S=requests.Session(); S.headers.update({"User-Agent":UA,"Accept":"application/json"})
S.get("https://trove.nla.gov.au/")
ctx=S.cookies.get("x-ctx"); key=hashlib.md5(("Wonder"+ctx).encode()).hexdigest().lstrip("0")
H={"apikey":key,"Referer":"https://trove.nla.gov.au/search"}
OUT=f"{BASE}/trove-hits-pass3.jsonl"
seen=set()
if os.path.exists(OUT):
    for l in open(OUT):
        try: seen.add(json.loads(l)["id"])
        except: pass

def harvest(terms, limits=None, maxn=600, tag=""):
    pos=0; n=0; f=open(OUT,"a"); tot=None
    while pos<maxn:
        p={"terms":terms,"pageSize":100,"startPos":pos}
        if limits: p["limits"]=json.dumps(limits)
        d=None
        for att in range(4):
            try:
                r=S.get("https://trove.nla.gov.au/api/search/137",params=p,headers=H,timeout=60); d=r.json(); break
            except Exception as e:
                time.sleep(3*(att+1))
        if not d: break
        tot=d.get("totalRecords")
        ws=d.get("works",[])
        for w in ws:
            if w["id"] in seen: continue
            seen.add(w["id"]); n+=1
            rec={k:w.get(k) for k in ("id","title","newspaper","date","page","snippets","wordCount","articleType")}
            rec["q"]=tag or terms
            f.write(json.dumps(rec,ensure_ascii=False)+"\n")
        f.flush()
        if not d.get("hasMoreResults") or not ws: break
        pos+=len(ws)
        time.sleep(0.4)
    f.close()
    print(f"[{tag or terms}] total={tot} new={n}", flush=True)
    return n

def text(id):
    fn=f"{BASE}/trove-articles/nla.news-article{id}.txt"
    if os.path.exists(fn): return open(fn).read()
    r=S.get(f"https://trove.nla.gov.au/newspaper/rendition/nla.news-article{id}.txt",headers=H,timeout=60)
    s=BeautifulSoup(r.text,"html.parser"); t=re.sub(r'\n\s*\n+','\n',s.get_text("\n")).strip()
    open(fn,"w").write(t); return t

QUERIES=[
 ('"Hannah Landells"',None),
 ('"Louth Park" Mackay',None),
 ('"Double Peak" Mackay',None),
 ('"Langley Holmes"',None),
 ('Skipworth Mackay',None),
 ('Skipworth Jacklin',None),
 ('Jacklin "North Eton"',None),
 ('Jacklin rifle Mackay',None),
 ('"Decca" Mackay 1887',None),
 ('Holmes Woodford Mackay Harvison',None),
 ('Harvison Woodford',None),
 ('Jacklin Nudgee',None),
 ('"Jacklin" welcome home Mackay',None),
 ('Jacklin Mackay 1919',None),
 ('"Dr. Jacklin" Mackay',None),
 ('"Desmond Jacklin"',None),
 ('"D. J. Jacklin"',None),
 ('"North Jacklin"',None),
 ('Spunner Creswick',None),
 ('Spunner',None),
 ('Ward Eddington Dunolly',None),
 ('"Henry Ward" Eddington',None),
 ('Cunningham "Swan Reach"',None),
 ('Cunningham Kiandra',None),
 ('"Margaret Murphy" Cunningham Tambo',None),
 ('"Catherine Ward" Lake Tyers',None),
 ('"Mrs. Ward" "Lake Tyers"',None),
 ('"Chas. Ward" "Lake Tyers"',None),
 ('Jacklin Ipswich Gatton',None),
 ('"William Jacklin" Queensland',None),
 ('"James Jacklin" Gayton',None),
 ('"Gayton-le-Marsh"',None),
]
if __name__=="__main__":
    for q,lim in QUERIES:
        try: harvest(q,lim,tag=q)
        except Exception as e: print("FAIL",q,e,flush=True)
        time.sleep(0.6)
