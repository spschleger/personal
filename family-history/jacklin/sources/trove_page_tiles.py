import requests, io, sys, os, time
from PIL import Image
UA={"User-Agent":"Mozilla/5.0","Referer":"https://trove.nla.gov.au/newspaper/article/276922028"}
base="https://trove.nla.gov.au/imageservice/nla.news-page31370291/tile7-%d-%d"
cmin,cmax,rmin,rmax=9,22,6,25
os.makedirs("tiles",exist_ok=True)
S=requests.Session()
# only fetch tiles for the right-hand middle region: x 0.70-1.0, y 0.38-0.75 of page
xoff,yoff=2464-cmin*256,1764-rmin*256
x0,x1=int(3264*0.70)+xoff, 3264+xoff; y0,y1=int(4664*0.38)+yoff, int(4664*0.75)+yoff
cols=range(cmin+x0//256, cmin+x1//256+1); rows=range(rmin+y0//256, rmin+y1//256+1)
W=(cmax-cmin+1)*256; H=(rmax-rmin+1)*256
canvas=Image.new("L",(W,H),255)
n=0
for c in cols:
    for r in rows:
        fn=f"tiles/{c}-{r}.jpg"
        if not os.path.exists(fn):
            for a in range(3):
                try:
                    resp=S.get(base%(c,r),headers=UA,timeout=30)
                    if resp.status_code==200 and resp.headers.get("content-type","").startswith("image"):
                        open(fn,"wb").write(resp.content); break
                except Exception as e: time.sleep(1)
        if os.path.exists(fn):
            canvas.paste(Image.open(fn),((c-cmin)*256,(r-rmin)*256)); n+=1
print("tiles",n)
crop=canvas.crop((x0,y0,x1,y1)); crop.save("sun_crop.jpg",quality=90); print(crop.size)
