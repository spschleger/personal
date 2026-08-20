#!/usr/bin/env python3
import requests, time, os, re
from bs4 import BeautifulSoup
D=os.path.dirname(os.path.abspath(__file__))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S=requests.Session(); S.headers.update({"User-Agent":UA,"Referer":"https://ryersonindex.org/search.php","Origin":"https://ryersonindex.org"})
Q=[("BARTLEM-any",{"search_sn":"BARTLEM"}),
   ("BARTLEM-Mafalda",{"search_sn":"BARTLEM","search_gn":"Mafalda"}),
   ("JOSEFSKI-Jacqueline",{"search_sn":"JOSEFSKI","search_gn":"Jacqueline","search_sx":"1"})]
for i,(lab,f) in enumerate(Q):
    fn=os.path.join(D,f"ryerson_{lab}.txt")
    if os.path.exists(fn) and os.path.getsize(fn)>200: print("SKIP",lab,flush=True); continue
    d=dict(f); d["search"]="Search Ryerson"
    delay=0
    for att in range(4):
        if delay: time.sleep(delay)
        try: r=S.post("https://ryersonindex.org/search.php",data=d,timeout=90)
        except Exception as e: print("ERR",lab,e,flush=True); delay=120; continue
        if r.status_code!=200: print("HTTP",r.status_code,lab,flush=True); delay=300; continue
        s=BeautifulSoup(r.text,"html.parser")
        rows=[" | ".join(x.get_text(" ",strip=True) for x in tr.find_all(["td","th"])) for tr in s.find_all("tr") if len(tr.find_all(["td","th"]))>=4]
        open(fn,"w").write(f"# Ryerson POST https://ryersonindex.org/search.php\n# query: {f}\n# accessed {time.strftime('%Y-%m-%d %H:%M %Z')}\n# HTTP {r.status_code}\n\n## table rows\n"+"\n".join(rows)+"\n")
        print("OK",lab,len(rows),flush=True)
        for x in rows[:60]: print("   ",x[:190],flush=True)
        break
    if i<len(Q)-1: time.sleep(60)
