from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.utils import ImageReader
import fitz

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT.parent / 'YesMandarin SEO' / 'Images and Other'
logo = Image.open(ASSETS / 'Logo.jpg').convert('RGB')
bg = logo.getpixel((0, 0))
W, H = 595.276, 419.528  # A5 landscape
pdf = ROOT / 'YesMandarin-Gift-Voucher-Readon.pdf'
c = canvas.Canvas(str(pdf), pagesize=(W, H))
c.setTitle('A special gift for Readon | YesMandarin')
c.setAuthor('YesMandarin')
c.setFillColor(Color(*(v/255 for v in bg)))
c.rect(0, 0, W, H, fill=1, stroke=0)
ink = HexColor('#303938')
accent = HexColor('#d44732')
c.setStrokeColor(accent)
c.setLineWidth(0.65)
c.roundRect(17, 17, W-34, H-34, 3, fill=0, stroke=1)
lw = 205
lh = lw * logo.height / logo.width
c.drawImage(ImageReader(logo), (W-lw)/2, 339, width=lw, height=lh)

def centre(text, y, font, size, colour=ink):
    c.setFillColor(colour)
    c.setFont(font, size)
    c.drawCentredString(W/2, y, text)

centre('G I F T   V O U C H E R', 305, 'Helvetica', 9, accent)
centre('A special gift for Readon', 257, 'Times-Roman', 30)
centre('From Jordan', 231, 'Helvetica', 12)
c.setStrokeColor(accent)
c.line(W/2-23, 209, W/2+23, 209)
centre('5 private Mandarin lessons', 174, 'Helvetica-Bold', 20)
centre('60 minutes each  |  In person  |  One-to-one', 150, 'Helvetica', 11)
centre('To book your lessons, contact Yujie', 93, 'Helvetica', 10)
centre('0414 163 003', 72, 'Helvetica-Bold', 14)
centre('yesmandarin.com.au', 41, 'Helvetica', 9)
c.linkURL('tel:+61414163003', (235, 68, 360, 88), relative=0)
c.linkURL('https://www.yesmandarin.com.au', (235, 37, 360, 50), relative=0)
c.showPage()
c.save()
doc = fitz.open(pdf)
assert len(doc) == 1
text = doc[0].get_text()
for expected in ['Readon', 'Jordan', '5 private Mandarin lessons', '60 minutes each', 'In person', 'Yujie', '0414 163 003']:
    assert expected in text, expected
out = ROOT / 'YesMandarin-Gift-Voucher-Readon.png'
doc[0].get_pixmap(matrix=fitz.Matrix(3,3), alpha=False).save(out)
print(text)
print(f'Verified one-page A5 PDF: {pdf}')
print(f'Preview: {out}')
