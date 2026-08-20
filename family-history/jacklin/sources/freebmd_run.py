import sys,re,os,time
sys.path.insert(0,'/Users/shane/personal/family-history/jacklin/sources')
import freebmd as F
OUT='/Users/shane/personal/family-history/jacklin/sources/england'
os.makedirs(OUT,exist_ok=True)
LOUTH="937"
def clean(h):
    t=re.sub(r'(?s)<script.*?</script>',' ',h); t=re.sub(r'(?s)<style.*?</style>',' ',t)
    t=re.sub(r'(?s)<[^>]+>','\n',t); t=re.sub(r'&nbsp;?',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    i=t.find('Surname \n'); j=t.find('Space for Advertisement')
    if i<0: i=t.find('County:')
    if j<0: j=len(t)
    return t[i:j].strip()
JOBS=[
 ("births-jacklin-louth",     dict(surname="Jacklin",type_="Births",districtid=LOUTH,start=1837,end=1900)),
 ("deaths-jacklin-louth",     dict(surname="Jacklin",type_="Deaths",districtid=LOUTH,start=1837,end=1920)),
 ("marr-jacklin-skipworth",   dict(surname="Jacklin",s_surname="Skipworth",type_="Marriages",start=1837,end=1900)),
 ("marr-jacklin-holmes",      dict(surname="Jacklin",s_surname="Holmes",type_="Marriages",start=1837,end=1900)),
 ("marr-holmes-shepherd",     dict(surname="Holmes",s_surname="Shepherd",type_="Marriages",start=1837,end=1890)),
 ("births-holmes-louth",      dict(surname="Holmes",given="Fanny",type_="Births",districtid=LOUTH,start=1837,end=1900)),
 ("marr-jacklin-louth",       dict(surname="Jacklin",type_="Marriages",districtid=LOUTH,start=1837,end=1900)),
 ("births-skipworth-louth",   dict(surname="Skipworth",type_="Births",districtid=LOUTH,start=1837,end=1900)),
]
for name,kw in JOBS:
    try:
        h=F.search(**kw)
        c=clean(h)
        open(f"{OUT}/freebmd-{name}.txt","w").write(f"FreeBMD search {name}: {kw}\nSource: https://www.freebmd.org.uk/cgi/search.pl (free index, no login)\n\n"+c)
        n=len(re.findall(r'\n(Births|Deaths|Marriages)\s+\w{3}\d{4}',c))
        print(f"{name}: {n} entries -> freebmd-{name}.txt",flush=True)
    except Exception as e:
        print("FAIL",name,e,flush=True)
    time.sleep(3)
