import requests, hashlib, json, sys, time, re, os
from bs4 import BeautifulSoup
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S=requests.Session(); S.headers.update({"User-Agent":UA,"Accept":"application/json"})
S.get("https://trove.nla.gov.au/")
ctx=S.cookies.get("x-ctx"); key=hashlib.md5(("Wonder"+ctx).encode()).hexdigest().lstrip("0")
H={"apikey":key,"Referer":"https://trove.nla.gov.au/search"}
def harvest(terms, limits=None, out="hits.jsonl", maxn=5000):
    seen=set()
    if os.path.exists(out):
        for l in open(out): seen.add(json.loads(l)["id"])
    pos=0; f=open(out,"a"); n=0
    while pos<maxn:
        p={"terms":terms,"pageSize":100,"startPos":pos}
        if limits: p["limits"]=json.dumps(limits)
        for att in range(4):
            try:
                r=S.get("https://trove.nla.gov.au/api/search/137",params=p,headers=H,timeout=60); d=r.json(); break
            except Exception as e:
                time.sleep(3*(att+1)); d=None
        if not d: break
        ws=d.get("works",[])
        for w in ws:
            if w["id"] in seen: continue
            seen.add(w["id"]); n+=1
            f.write(json.dumps({k:w.get(k) for k in ("id","title","newspaper","date","page","snippets","abstrct","wordCount","articleType")},ensure_ascii=False)+"\n")
        f.flush()
        print(terms, pos, d.get("totalRecords"), file=sys.stderr)
        if not d.get("hasMoreResults") or not ws: break
        pos+=len(ws)
    f.close(); return n
def text(id):
    fn=f"trove-text/{id}.txt"
    if os.path.exists(fn): return open(fn).read()
    r=S.get(f"https://trove.nla.gov.au/newspaper/rendition/nla.news-article{id}.txt",headers=H,timeout=60)
    s=BeautifulSoup(r.text,"html.parser"); t=re.sub(r'\n\s*\n+','\n',s.get_text("\n")).strip()
    os.makedirs("trove-text",exist_ok=True); open(fn,"w").write(t); return t
if __name__=="__main__":
    harvest("Jacklin",{"state":["Queensland"]},"hits-jacklin-qld.jsonl")
    harvest('"Jacklin" Mackay',None,"hits-jacklin-mackay.jsonl")
    harvest('Jackling',{"state":["Queensland"]},"hits-jackling-qld.jsonl")
    ids=set()
    for fn in ["hits-jacklin-qld.jsonl","hits-jacklin-mackay.jsonl","hits-jackling-qld.jsonl"]:
        for l in open(fn): ids.add(json.loads(l)["id"])
    print("fetching text for",len(ids),file=sys.stderr)
    for i,id in enumerate(sorted(ids)):
        try: text(id)
        except Exception as e: print("fail",id,e,file=sys.stderr)
        if i%50==0: print("text",i,file=sys.stderr)
        time.sleep(0.15)
