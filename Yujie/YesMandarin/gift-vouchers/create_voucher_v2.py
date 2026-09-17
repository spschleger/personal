from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
import pymupdf
import math

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT.parent / 'YesMandarin SEO' / 'Images and Other'
# Remove the cream backdrop from the supplied brand mark, retaining its ink.
logo = Image.open(ASSETS / 'Logo.jpg').convert('RGBA')
pixels = []
for r,g,b,a in logo.getdata():
    if r > 210 and g > 200 and b > 175:
        pixels.append((255,255,255,0))
    elif r > 150 and r > g * 1.25 and g > b * 1.15:
        pixels.append((255,107,61,255))
    else:
        pixels.append((r,g,b,255))
logo.putdata(pixels)
logo = logo.crop(logo.getbbox())
W,H = 595.276,419.528
pdf = ROOT / 'YesMandarin-Gift-Voucher-Readon-v2.pdf'
c=canvas.Canvas(str(pdf),pagesize=(W,H))
c.setTitle('A special gift for Readon | YesMandarin')
c.setAuthor('YesMandarin')
ink=HexColor('#202B2C')
orange=HexColor('#FF6B3D')
muted=HexColor('#637172')
c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
# Full-height colour panel with concentric arcs and a playful gift motif.
c.setFillColor(orange); c.rect(386,0,W-386,H,fill=1,stroke=0)
c.saveState()
p=c.beginPath(); p.rect(386,0,W-386,H); c.clipPath(p,stroke=0,fill=0)
c.setStrokeColor(HexColor('#F57C60')); c.setLineWidth(0.7)
for radius in [65,88,111,134,157]:
    c.circle(596,417,radius,stroke=1,fill=0)
for radius in [48,71,94]:
    c.circle(397,-20,radius,stroke=1,fill=0)
c.restoreState()

def text(s,x,y,size=12,font='Helvetica',colour=ink):
    c.setFillColor(colour); c.setFont(font,size); c.drawString(x,y,s)

def star(x,y,r):
    p=c.beginPath()
    for i in range(16):
        a=math.pi/2+i*math.pi/8
        rr=r if i%2==0 else r*0.36
        xx,yy=x+rr*math.cos(a),y+rr*math.sin(a)
        if i==0: p.moveTo(xx,yy)
        else: p.lineTo(xx,yy)
    p.close(); c.setFillColor(white); c.drawPath(p,fill=1,stroke=0)

lw=165
c.drawImage(ImageReader(logo),34,351,width=lw,height=lw*logo.height/logo.width,mask='auto')
text('G I F T   V O U C H E R',35,309,9,colour=orange)
text('A special gift',33,265,32,'Helvetica-Bold')
text('for Readon.',33,227,32,'Helvetica-Bold')
text('From Jordan',35,197,13,colour=muted)
c.setStrokeColor(HexColor('#E1E5E5')); c.setLineWidth(0.75); c.line(35,172,349,172)
text('5 private Mandarin lessons',35,145,18,'Helvetica-Bold')
text('60 minutes each',35,122,11,colour=muted)
text('In person  /  One-to-one',35,104,11,colour=muted)
text('To book, contact Felicity',35,64,10,colour=muted)
text('0414 163 003',35,44,15,'Helvetica-Bold')
text('yesmandarin.com.au',35,24,8,colour=muted)
# The lesson count is the graphic centrepiece, with small sparkle details.
star(431,297,15); star(553,139,12)
c.setFillColor(white); c.setFont('Helvetica-Bold',158); c.drawCentredString(490,179,'5')
c.setFont('Helvetica-Bold',11); c.drawCentredString(490,151,'PRIVATE LESSONS')
c.setStrokeColor(white); c.setLineWidth(1); c.line(469,124,511,124)
c.setFont('Helvetica',10); c.drawCentredString(490,102,'A little gift.')
c.drawCentredString(490,86,'A whole new language.')
c.linkURL('tel:+61414163003',(34,40,163,60),relative=0)
c.linkURL('https://www.yesmandarin.com.au',(34,20,146,34),relative=0)
c.showPage(); c.save()
doc=pymupdf.open(pdf)
assert len(doc)==1
extracted=doc[0].get_text()
for s in ['Readon','Jordan','5 private Mandarin lessons','60 minutes each','In person','Felicity','0414 163 003']:
    assert s in extracted,s
out=ROOT/'YesMandarin-Gift-Voucher-Readon-v2.png'
doc[0].get_pixmap(matrix=pymupdf.Matrix(3,3),alpha=False).save(out)
print(extracted)
print(f'Verified PDF: {pdf}\nPreview: {out}')
