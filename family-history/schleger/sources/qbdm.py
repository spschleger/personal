import sys, json, re, requests, csv
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S=requests.Session(); S.headers['User-Agent']=UA
h=S.get("https://www.familyhistory.bdm.qld.gov.au/").text
tok=re.search(r'name="_csrf" content="([^"]+)"',h).group(1)
def search(family, given="", rtype="births", dob=("01/01/1829","31/12/1924"), father="", mother="", spouse="", exactfam=True):
    out=[]; page=0
    while True:
        q={"count":"20","page":page,"subjectgivennames":given,"subjectfamilyname":family,
           "dobfrom":dob[0],"dobto":dob[1],"doefrom":"","doeto":"","fathersname":father,"mothersname":mother,
           "spousename":spouse,"regyear":"","regtype":"","regnum":"",
           "exactTermsGivennamesOnly":"false","exactTermsFamilynameOnly":"true" if exactfam else "false","recordtype":rtype}
        r=S.post("https://www.familyhistory.bdm.qld.gov.au/search",json=q,headers={"X-CSRF-TOKEN":tok,"Referer":"https://www.familyhistory.bdm.qld.gov.au/"})
        try: d=r.json()
        except Exception: print(r.status_code, r.text[:300]); return out
        if d.get("error"): print("ERR",d); return out
        out+=d.get("records",[])
        if len(out)>=d.get("found",0) or not d.get("records"): break
        page+=1
    return out
if __name__=="__main__":
    fam=sys.argv[1]; rtype=sys.argv[2]; given=sys.argv[3] if len(sys.argv)>3 else ""
    rng={"births":("01/01/1829","31/12/1924"),"marriages":("01/01/1829","31/12/1949"),"deaths":("01/01/1829","31/12/1994")}[rtype]
    exact = not (len(sys.argv)>4 and sys.argv[4]=="fuzzy")
    recs=search(fam,given,rtype,rng,exactfam=exact)
    print(json.dumps(recs,indent=1)[:200] if not recs else "", file=sys.stderr)
    for r in recs: print(json.dumps(r,ensure_ascii=False))

def search2(family, given="", rtype="deaths", doe=("01/01/1829","31/12/1994"), exactfam=True, **kw):
    out=[]; page=0
    while True:
        q={"count":"20","page":page,"subjectgivennames":given,"subjectfamilyname":family,"dobfrom":"","dobto":"","doefrom":doe[0],"doeto":doe[1],
           "fathersname":kw.get("father",""),"mothersname":kw.get("mother",""),"spousename":kw.get("spouse",""),"regyear":"","regtype":"","regnum":"",
           "exactTermsGivennamesOnly":"false","exactTermsFamilynameOnly":"true" if exactfam else "false","recordtype":rtype}
        r=S.post("https://www.familyhistory.bdm.qld.gov.au/search",json=q,headers={"X-CSRF-TOKEN":tok,"Referer":"https://www.familyhistory.bdm.qld.gov.au/"})
        d=r.json()
        if d.get("error"): print("ERR",d); return out
        out+=d.get("records",[])
        if len(out)>=d.get("found",0) or not d.get("records"): break
        page+=1
    return out
def line(r):
    t=r['recordtype'][0]
    s=f"{t} {r['subjectdoe']:>10} {r['subjectgivennames']} {r['subjectfamilyname']}"
    if t=='M': s+=f" = {r['othersubjectgivennames']} {r['othersubjectfamilyname']}"
    else: s+=f" | {r['parentfullname']} / {r['motherfullname']}" + (f" | dob {r['subjectdob']}" if t=='D' else "")
    return s+f"  [{r['regtype']}{r['regnum']}/{r['regyear']}]"
