import sys,re,os,time
sys.path.insert(0,'/Users/shane/personal/family-history/jacklin/sources')
import freebmd as F
OUT='/Users/shane/personal/family-history/jacklin/sources/england'
LOUTH="937"; LINCS="LIN,6,33,49,50,52,102,103,154,175,176,225,226"
def clean(h):
    t=re.sub(r'(?s)<script.*?</script>',' ',h); t=re.sub(r'(?s)<style.*?</style>',' ',t)
    t=re.sub(r'(?s)<[^>]+>','\n',t); t=re.sub(r'&nbsp;?',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    i=t.find('Surname \n'); j=t.find('Space for Advertisement')
    if i<0: return "NO RESULTS / ERROR\n"+t[:800]
    if j<0: j=len(t)
    return t[i:j].strip()
JOBS=[
 ("marr-skipworth-jacklin", dict(surname="Skipworth",s_surname="Jacklin",type_="Marriages",start=1837,end=1900)),
 ("marr-jacklin-holmes",    dict(surname="Jacklin",s_surname="Holmes",type_="Marriages",start=1837,end=1900)),
 ("marr-holmes-jacklin",    dict(surname="Holmes",s_surname="Jacklin",type_="Marriages",start=1837,end=1900)),
 ("marr-holmes-shepherd",   dict(surname="Holmes",s_surname="Shepherd",type_="Marriages",start=1837,end=1890)),
 ("marr-shepherd-holmes",   dict(surname="Shepherd",s_surname="Holmes",type_="Marriages",start=1837,end=1890)),
 ("births-holmes-langley-lincs", dict(surname="Holmes",given="Langley",type_="Births",countyid=LINCS,start=1837,end=1900)),
 ("births-holmes-fanny-lincs",   dict(surname="Holmes",given="Fanny",type_="Births",countyid=LINCS,start=1850,end=1870)),
 ("deaths-holmes-langley",  dict(surname="Holmes",given="Langley",type_="Deaths",start=1837,end=1900)),
 ("births-jacklin-abraham-lincs", dict(surname="Jacklin",given="Abraham",type_="Births",countyid=LINCS,start=1837,end=1900)),
 ("deaths-jacklin-abraham-lincs", dict(surname="Jacklin",given="Abraham",type_="Deaths",countyid=LINCS,start=1837,end=1920)),
 ("births-jacklin-william-louth", dict(surname="Jacklin",given="William",type_="Births",districtid=LOUTH,start=1837,end=1900)),
]
for name,kw in JOBS:
    try:
        h=F.search(**kw); c=clean(h)
        open(f"{OUT}/freebmd-{name}.txt","w").write(f"FreeBMD search {name}: {kw}\nSource: https://www.freebmd.org.uk/cgi/search.pl\n\n"+c)
        n=len(re.findall(r'\n(Births|Deaths|Marriages)\s+\w{3}\d{4}',c))
        print(f"{name}: {n}",flush=True)
    except Exception as e: print("FAIL",name,e,flush=True)
    time.sleep(3)
