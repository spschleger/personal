"""FreeBMD free index search (no login). curl_cffi to look like Chrome."""
import re, sys, json
import requests
S=requests.Session()
S.headers.update({"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"})
URL="https://www.freebmd.org.uk/cgi/search.pl"

def _tokens():
    t=S.get(URL,timeout=60).text
    d=dict(re.findall(r'<input[^>]*type="?hidden"?[^>]*name="?(\w+)"?[^>]*value="?([^">]*)',t))
    if not d:
        d=dict(re.findall(r'name="?(db|v|js)"?[^>]*value="?([^">]*)',t))
    return d

def search(surname, given="", type_="All", start=1837, end=1930, districtid="", countyid="",
           s_surname="", s_given="", sq="Mar", eq="Dec", exactgiven=False):
    tk=_tokens()
    fields=[("type",type_),("districtid",districtid),("surname",surname),("given",given),
            ("s_surname",s_surname),("s_given",s_given),("aad",""),("sq",sq),("start",str(start)),
            ("eq",eq),("end",str(end)),("vol",""),("pgno",""),("countyid",countyid),
            ("db",tk.get("db","")),("v",tk.get("v","")),("js","")]
    fields=[(k,v) for k,v in fields if not (k in ("districtid","countyid") and v=="")]
    if exactgiven: fields.append(("exactgiven","on"))
    fields.append(("find.x","1")); fields.append(("find.y","1"))
    files=[(k,(None,v)) for k,v in fields]
    r=S.post(URL,files=files,timeout=300,headers={"Referer":URL})
    return r.text

def parse(html):
    txt=re.sub(r'(?s)<script.*?</script>',' ',html)
    rows=[]
    for m in re.finditer(r'(?s)<tr[^>]*>(.*?)</tr>',txt):
        cells=[re.sub(r'\s+',' ',re.sub(r'(?s)<[^>]+>',' ',c)).replace('&nbsp;',' ').strip() for c in re.findall(r'(?s)<td[^>]*>(.*?)</td>',m.group(1))]
        cells=[c for c in cells if c!='']
        if len(cells)>=4: rows.append(cells)
    return rows

def summary(html):
    t=re.sub(r'(?s)<[^>]+>','\n',html)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
