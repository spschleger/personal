"""NAA RecordSearch fetcher (free guest session). curl_cffi (chrome impersonation) to pass Cloudflare."""
import re, sys, os, time, json
from curl_cffi import requests as creq
BASE="https://recordsearch.naa.gov.au"
S=creq.Session(impersonate="chrome")
HDR={"Origin":BASE,"Content-Type":"application/x-www-form-urlencoded"}

def _fields(html):
    d={}
    for m in re.finditer(r'<input[^>]*type="hidden"[^>]*>',html,re.I):
        tag=m.group(0)
        n=re.search(r'name="([^"]+)"',tag); v=re.search(r'value="([^"]*)"',tag)
        if n: d[n.group(1)]=v.group(1) if v else ""
    return d

def strip(h):
    t=re.sub(r'(?s)<(script|style).*?</\1>',' ',h)
    t=re.sub(r'(?s)<[^>]+>','\n',t)
    t=t.replace('&nbsp;',' ').replace('&amp;','&').replace('&#39;',"'").replace('&quot;','"')
    return re.sub(r'\n\s*\n+','\n',t).strip()

def _post(url, fields, ref):
    h=dict(HDR); h["Referer"]=ref
    return S.post(url,data=fields,timeout=120,headers=h)

def guest():
    r=S.get(f"{BASE}/SearchNRetrieve/Interface/SearchScreens/BasicSearch.aspx",timeout=60)
    if "SessionTimeout" in str(r.url) or "lbnGuest" in r.text:
        f=_fields(r.text); f["__EVENTTARGET"]="ctl00$ContentPlaceHolderSNR$lbnGuest"; f["__EVENTARGUMENT"]=""
        r=_post(str(r.url),f,str(r.url))
    return r

def basic_search(keyword, datefrom="", dateto="", per=200):
    url=f"{BASE}/SearchNRetrieve/Interface/SearchScreens/BasicSearch.aspx"
    r=S.get(url,timeout=60)
    if "SessionTimeout" in str(r.url):
        guest(); r=S.get(url,timeout=60)
    f=_fields(r.text)
    f["__EVENTTARGET"]=""; f["__EVENTARGUMENT"]=""
    f["ctl00$ContentPlaceHolderSNR$tbxKeyword"]=keyword
    f["ctl00$ContentPlaceHolderSNR$tbxDateFrom"]=datefrom
    f["ctl00$ContentPlaceHolderSNR$tbxDateTo"]=dateto
    f["ctl00$ContentPlaceHolderSNR$btnSearch"]="Search"
    r2=_post(url,f,url)
    if "PleaseWait" in str(r2.url) or "BasicSearch_Result" in r2.text:
        ru=f"{BASE}/SearchNRetrieve/Interface/SearchScreens/BasicSearch_Result.aspx"
        r2=_post(ru,_fields(r2.text),str(r2.url))
    h=r2.text
    if "ItemsListing" in str(r2.url) or "Items listing" in h:
        f2=_fields(h)
        f2["__EVENTTARGET"]="ctl00$ContentPlaceHolderSNR$ddlResultsPerPage"; f2["__EVENTARGUMENT"]=""
        f2["ctl00$ContentPlaceHolderSNR$ddlResultsPerPage"]=str(per)
        lu=f"{BASE}/SearchNRetrieve/Interface/ListingReports/ItemsListing.aspx"
        h=_post(lu,f2,lu).text
    return h

def rows(h):
    out=[]
    for m in re.finditer(r'(?s)<tr[^>]*>(.*?)</tr>',h):
        cells=re.findall(r'(?s)<t[dh][^>]*>(.*?)</t[dh]>',m.group(1))
        if len(cells)<7: continue
        c=[re.sub(r'\s+',' ',re.sub(r'(?s)<[^>]+>',' ',x)).replace('&amp;','&').strip() for x in cells]
        if c[1].lower().startswith('series'): continue
        out.append(c)
    return out

def item(barcode):
    return S.get(f"{BASE}/SearchNRetrieve/Interface/DetailsReports/ItemDetail.aspx?Barcode={barcode}",timeout=60).text

def npages(barcode):
    h=S.get(f"{BASE}/SearchNRetrieve/Interface/ViewImage.aspx?B={barcode}",timeout=60).text
    t=strip(h)
    m=re.search(r'-\s*Page\s+(\d+)\s+of\s+(\d+)\s*$',t) or re.search(r'Page\n(\d+)\nof\n(\d+)',t)
    return int(m.group(2)) if m else None

def pages(barcode, n, outdir, prefix):
    os.makedirs(outdir,exist_ok=True); got=0
    for s in range(1,n+1):
        fn=os.path.join(outdir,f"{prefix}-p{s:02d}.jpg")
        if os.path.exists(fn) and os.path.getsize(fn)>5000: got+=1; continue
        r=S.get(f"{BASE}/SearchNRetrieve/NAAMedia/ShowImage.aspx?B={barcode}&S={s}&T=P&R=0",timeout=180)
        if r.status_code==200 and r.headers.get("content-type","").startswith("image"):
            open(fn,"wb").write(r.content); got+=1
        else: print("  fail page",s,r.status_code)
        time.sleep(0.4)
    return got
