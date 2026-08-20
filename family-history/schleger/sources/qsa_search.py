"""Queensland State Archives ArchivesSearch — free public index API.
POST /api/advanced_search  (multipart: query=<json>, page, sort)"""
import json, sys, time, requests
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
URL="https://www.archivessearch.qld.gov.au/api/advanced_search"
S=requests.Session(); S.headers["User-Agent"]=UA
def search(q, field="keywords", maxpages=10, sort="relevance"):
    out=[]; page=0
    while page<maxpages:
        body={"clauses":[{"field":field,"operator":"AND","query":q}],"filters":[],
              "filter_types":[],"filter_open_records_only":False,"filter_linked_digital_objects_only":False}
        r=S.post(URL, files={"query":(None,json.dumps(body)),"page":(None,str(page)),"sort":(None,sort)}, timeout=90)
        d=r.json(); out+=d.get("results",[])
        if len(out)>=d.get("total_count",0) or not d.get("results"): break
        page+=1; time.sleep(0.4)
    return out
def line(x):
    return " | ".join([x.get("qsa_id_prefixed",""), x.get("title","")[:120],
        x.get("dates_display_string","") or "", ";".join(x.get("terms") or [])[:80],
        (x.get("access_status") or ""), ";".join(x.get("previous_system_ids") or [])[:60],
        "ATSI:"+";".join(x.get("atsi_subjects") or [])[:60]])
if __name__=="__main__":
    for q in sys.argv[1:]:
        rs=search(q); print(f"=== {q}  ({len(rs)})")
        for x in rs: print("  ",line(x))
