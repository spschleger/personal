import sys,re,os,time
sys.path.insert(0,'/Users/shane/personal/family-history/jacklin/sources')
import freebmd as F
OUT='/Users/shane/personal/family-history/jacklin/sources/england'
LOUTH="937"; SPILSBY=None; LINCS="LIN,6,33,49,50,52,102,103,154,175,176,225,226"
def clean(h):
    t=re.sub(r'(?s)<script.*?</script>',' ',h); t=re.sub(r'(?s)<style.*?</style>',' ',t)
    t=re.sub(r'(?s)<[^>]+>','\n',t); t=re.sub(r'&nbsp;?',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    i=t.find('Surname \n'); j=t.find('Space for Advertisement')
    if i<0: return "NO RESULTS / ERROR\n"+t[:600]
    return t[i:(j if j>0 else len(t))].strip()
JOBS=[
 ("marr-holmes-sheppard",  dict(surname="Holmes",s_surname="Sheppard",type_="Marriages",start=1837,end=1875)),
 ("marr-holmes-shepperd",  dict(surname="Holmes",s_surname="Shepperd",type_="Marriages",start=1837,end=1875)),
 ("marr-holmes-langley-lincs", dict(surname="Holmes",given="Langley",type_="Marriages",countyid=LINCS,start=1837,end=1900)),
 ("deaths-jacklin-maria-lincs", dict(surname="Jacklin",given="Maria",type_="Deaths",countyid=LINCS,start=1860,end=1900)),
 ("marr-jacklin-abraham-lincs", dict(surname="Jacklin",given="Abraham",type_="Marriages",countyid=LINCS,start=1837,end=1900)),
 ("births-shepherd-fanny-lincs", dict(surname="Shepherd",given="Fanny",type_="Births",countyid=LINCS,start=1837,end=1845)),
 ("deaths-jacklin-thomas-lincs", dict(surname="Jacklin",given="Thomas",type_="Deaths",countyid=LINCS,start=1860,end=1890)),
 ("births-holmes-spilsby",  dict(surname="Holmes",type_="Births",districtid="265",start=1855,end=1890)),
]
for name,kw in JOBS:
    try:
        h=F.search(**kw); c=clean(h)
        open(f"{OUT}/freebmd-{name}.txt","w").write(f"FreeBMD {name}: {kw}\n\n"+c)
        print(name, len(re.findall(r'\n(Births|Deaths|Marriages)\s+\w{3}\d{4}',c)),flush=True)
    except Exception as e: print("FAIL",name,e,flush=True)
    time.sleep(3)
