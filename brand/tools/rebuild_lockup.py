"""Rebuild the CORAfrica lockup with the two lines Fr. Peter asked for on 2026-09-17:
"Also use this complete image at the menu instead of just CORAfrica and logo."

His reference (WhatsApp 1:52 PM) is the seal, the CORAfrica wordmark, and beneath it
"CHILDREN OF RURAL AFRICA-NIGERIA" and "Helping Children and Communities Thrive".

The seal and the wordmark are reused verbatim from the existing lockup -- they were traced on
2026-09-10 and nothing about them changed. Only the two lines are new: set in Arial Narrow Bold
and Georgia Bold Italic, rendered to a 6x raster and traced to paths with brand/tools/trace.py,
so the finished file carries no font dependency, exactly like every other mark on the site.
"""
import re, io, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "brand/tools"); import trace as T

SRC = "brand/corafrica-lockup.svg"
L2, L3 = "CHILDREN OF RURAL AFRICA-NIGERIA", "Helping Children and Communities Thrive"
F2 = "/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf"
F3 = "/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf"

src = io.open(SRC, encoding="utf-8").read()
paths = re.findall(r'<path fill="([^"]+)" d="([^"]+)"', src)
assert len(paths) == 2, "expected the seal and the wordmark"
(seal_fill, seal_d), (word_fill, word_d) = paths

# The wordmark's own box tells us where the lines belong: same left edge, same width, stacked
# into the empty space beneath it.
pts = [tuple(map(float, p.split(","))) for p in re.findall(r"[ML]([-\d.]+,[-\d.]+)", word_d)]
X0, X1 = min(p[0] for p in pts), max(p[0] for p in pts)
WY1 = max(p[1] for p in pts)
W = X1 - X0

UP = 6                                    # render at 6x, trace, divide back down
def line(text, font_path, target_w, px):
    """Render one line as a mask and return (mask, scale) with width == target_w*UP."""
    f = ImageFont.truetype(font_path, px)
    l, t, r, b = f.getbbox(text)
    im = Image.new("L", (r - l + 8, b - t + 8), 0)
    ImageDraw.Draw(im).text((4 - l, 4 - t), text, font=f, fill=255)
    w, h = im.size
    s = (target_w * UP) / w
    im = im.resize((int(round(w * s)), int(round(h * s))), Image.LANCZOS)
    return np.array(im) > 110, im.size

def traced(mask, ox, oy):
    return T.trace(mask, scale=UP, eps=0.55, ox=ox, oy=oy, prec=2)

TW = 1140.0                               # the two lines run wider than the wordmark:
                                          # at a fixed lockup height that is what makes them
                                          # readable (~12px in a 58px header, vs ~5px at the
                                          # wordmark's own width)
m2, (w2, h2) = line(L2, F2, TW, 160)
m3, (w3, h3) = line(L3, F3, TW, 160)

GAP1, GAP2 = 16.0, 10.0                   # wordmark -> line 2 -> line 3, in lockup units
y2 = WY1 + GAP1
y3 = y2 + h2 / UP + GAP2
d2 = traced(m2, X0, y2)
d3 = traced(m3, X0, y3)
bottom = y3 + h3 / UP

# viewBox: keep the original left/top, grow only to fit whatever is now lowest.
vb = re.search(r'viewBox="([\d.\- ]+)"', src).group(1).split()
vx, vy, vw, vh = (float(v) for v in vb)
vh = max(vh, bottom - vy + 4)
vw = max(vw, X0 + TW - vx + 4)            # grow the box to hold the wider lines

def emit(ink, out):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%g %g %g %.2f" width="%g" '
           'height="%.0f" role="img" aria-label="CORAfrica &#8212; Children of Rural Africa '
           'Nigeria" fill-rule="evenodd"><title>CORAfrica &#8212; Children of Rural Africa '
           'Nigeria</title>' % (vx, vy, vw, vh, vw, round(vh))
           + '<path fill="%s" d="%s"/>' % (ink, seal_d)
           + '<path fill="%s" d="%s"/>' % (word_fill, word_d)
           + '<path fill="%s" d="%s"/>' % (ink, d2)
           + '<path fill="%s" d="%s"/>' % (ink, d3)
           + "</svg>\n")
    io.open(out, "w", encoding="utf-8").write(svg)
    print("  %-46s %7d bytes" % (out, len(svg)))

print("wordmark x %.1f..%.1f  baseline %.1f -> lines at %.1f and %.1f (viewBox h %.1f)"
      % (X0, X1, WY1, y2, y3, vh))
emit("#111111", "brand/corafrica-lockup-full.svg")
emit("#FFFFFF", "brand/corafrica-lockup-full-white.svg")
