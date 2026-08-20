import requests, hashlib, json, sys, time, re, os
from bs4 import BeautifulSoup
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S=requests.Session(); S.headers.update({"User-Agent":UA,"Accept":"application/json"})
S.get("https://trove.nla.gov.au/")
ctx=S.cookies.get("x-ctx"); key=hashlib.md5(("Wonder"+ctx).encode()).hexdigest().lstrip("0")
H={"apikey":key,"Referer":"https://trove.nla.gov.au/search"}
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"trove-hits-pass2.jsonl")
TXT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"trove-articles")

def harvest(terms, limits=None, out=OUT, maxn=1000, tag=""):
    seen=set()
    if os.path.exists(out):
        for l in open(out):
            try: seen.add((json.loads(l).get("q"),json.loads(l)["id"]))
            except: pass
    pos=0; f=open(out,"a"); n=0; total=None
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
        total=d.get("totalRecords")
        ws=d.get("works",[])
        for w in ws:
            if (terms,w["id"]) in seen: continue
            seen.add((terms,w["id"])); n+=1
            rec={k:w.get(k) for k in ("id","title","newspaper","date","page","snippets","wordCount","articleType")}
            rec["q"]=terms; rec["tag"]=tag
            f.write(json.dumps(rec,ensure_ascii=False)+"\n")
        f.flush()
        if not d.get("hasMoreResults") or not ws: break
        pos+=len(ws); time.sleep(0.3)
    f.close()
    print(f"[{tag}] {terms!r} limits={limits} total={total} new={n}", file=sys.stderr)
    return n

def text(id):
    fn=f"{TXT}/nla.news-article{id}.txt"
    if os.path.exists(fn) and os.path.getsize(fn)>10: return open(fn).read()
    r=S.get(f"https://trove.nla.gov.au/newspaper/rendition/nla.news-article{id}.txt",headers=H,timeout=60)
    s=BeautifulSoup(r.text,"html.parser"); t=re.sub(r'\n\s*\n+','\n',s.get_text("\n")).strip()
    os.makedirs(TXT,exist_ok=True); open(fn,"w").write(t); return t
