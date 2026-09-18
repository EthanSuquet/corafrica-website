"""Set the tagline in the logo's own hand.

Fr. Peter, 2026-09-18: the hero's "Education for Africa's Future" should be enlarged to the size
of the headline, in the same face and colour as CORAfrica, and sit towards the top of the card.

The CORAfrica wordmark is Bradley Hand. Rendered at 200px and laid beside the traced wordmark it
matches glyph for glyph -- the C, the R's curved leg, the f, the tilted dot on the i. Bradley
Hand is a macOS system face and no web font, so the line is traced to paths here exactly as the
wordmark and the seal were, and the finished SVG carries no font dependency. The fill is read
out of the wordmark's own path, so the two oranges cannot drift apart.

Mixed case, not the caps the old pill showed: at the headline's cap height the caps run 1237px
wide against 927px, which no hero can hold. Mixed case is also what CORAfrica itself is set in.
"""
import re, io, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "brand/tools"); import trace as T

LINE = "Education for Africa’s Future"
FONT = "/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf"
PX = 300                                  # trace size; the SVG is resolution-free after this
OUT = sys.argv[1] if len(sys.argv) > 1 else "brand"

src = io.open("brand/corafrica-lockup.svg", encoding="utf-8").read()
INK = re.findall(r'<path fill="([^"]+)" d="([^"]+)"', src)[1][0]

f = ImageFont.truetype(FONT, PX)
l, t, r, b = f.getbbox(LINE)
im = Image.new("L", (r - l + 24, b - t + 24), 0)
ImageDraw.Draw(im).text((12 - l, 12 - t), LINE, font=f, fill=255)
a = np.array(im) > 110
ys, xs = np.nonzero(a)
a = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]   # tight, so the viewBox has no dead air
H, W = a.shape
d = T.trace(a, scale=1, eps=1.6, ox=0.0, oy=0.0, prec=2)

cap = f.getbbox("H")[3] - f.getbbox("H")[1]           # what "the same size as the headline" means
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
       'role="img" aria-label="Education for Africa&#8217;s Future" fill-rule="evenodd">'
       '<title>Education for Africa&#8217;s Future</title>'
       '<path fill="%s" d="%s"/></svg>\n' % (W, H, W, H, INK, d))
io.open(OUT + "/corafrica-tagline.svg", "w", encoding="utf-8").write(svg)
print("%dx%d  cap %d  -> width is %.2f cap-heights, height %.3f of the width"
      % (W, H, cap, W / float(cap), H / float(W)))
print("  at a 62px headline (Space Grotesk cap 0.7em = 43.4px): %.0f x %.0f css px"
      % (W / float(cap) * 43.4, H / float(cap) * 43.4))
print("  %s  %d bytes" % (OUT + "/corafrica-tagline.svg", len(svg)))
