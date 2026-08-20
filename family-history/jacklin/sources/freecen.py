"""FreeCEN2 free census search (no login)."""
import re,time
from curl_cffi import requests as creq
S=creq.Session(impersonate="chrome")
BASE="https://www.freecen.org.uk"
def _tok():
    t=S.get(BASE+"/search_queries/new",timeout=60).text
    return re.search(r'name="authenticity_token" value="([^"]+)"',t).group(1)
def search(last,first="",county="LIN",start="",end="",fuzzy=False):
    d={"utf8":"✓","authenticity_token":_tok(),
       "search_query[last_name]":last,"search_query[first_name]":first,
       "search_query[start_year]":str(start),"search_query[end_year]":str(end),
       "search_query[chapman_codes][]":county,"commit":"Search"}
    if fuzzy: d["search_query[fuzzy]"]="1"
    r=S.post(BASE+"/search_queries",data=d,timeout=240,headers={"Referer":BASE+"/search_queries/new"})
    return r.text
def hits(h):
    out=[]
    m=re.search(r'(?s)<table.*?</table>',h)
    if not m: return out
    for rw in re.findall(r'(?s)<tr[^>]*>(.*?)</tr>',m.group(0)):
        a=re.search(r'href="(/search_records/[^"]+)"',rw)
        cells=[re.sub(r'\s+',' ',re.sub(r'(?s)<[^>]+>',' ',c)).strip() for c in re.findall(r'(?s)<t[dh][^>]*>(.*?)</t[dh]>',rw)]
        if a: out.append((a.group(1),' | '.join(cells[1:])))
    return out
def household(path):
    h=S.get(BASE+path,timeout=120).text
    t=re.sub(r'(?s)<script.*?</script>',' ',h); t=re.sub(r'(?s)<style.*?</style>',' ',t)
    out=[]
    for tb in re.findall(r'(?s)<table.*?</table>',t):
        for rw in re.findall(r'(?s)<tr[^>]*>(.*?)</tr>',tb):
            cells=[re.sub(r'\s+',' ',re.sub(r'(?s)<[^>]+>',' ',c)).replace('&nbsp;',' ').strip() for c in re.findall(r'(?s)<t[dh][^>]*>(.*?)</t[dh]>',rw)]
            if any(cells): out.append(' | '.join(cells))
    return '\n'.join(out)
