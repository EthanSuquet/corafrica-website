"""Rebuild the CORAfrica lockup to Fr. Peter's instruction of 2026-09-17, 6:33 and 6:42 PM:

    "Pls remove 'Helping children and communities thrive' from the insignia. Also remove
     NIGERIA. Just say CHILDREN OF RURAL AFRICA in between two lines, just as it looks
     above or on the shirt."
    "It's too crowded. It should just be CORAfrica / CHILDREN OF RURAL AFRICA (with logo).
     The logo should be the one that says EDUCATION FOR AFRICA'S FUTURE."

The seal and the wordmark are reused verbatim from brand/corafrica-lockup.svg. That seal is
already the EDUCATION FOR AFRICA'S FUTURE one -- it was traced on 2026-09-10 from the JPEG he
sent on 09-04, which is byte-identical to the one he sent again on 09-17.

Everything else is drawn here from the charity's own artwork, brand/source/CORAfrica-Logo-
Footer.png, which shares the lockup's coordinate frame 1:1 (the wordmark sits at x 320..999,
y 73..181 in both). The caps line is Times New Roman Bold: the artwork's letters have serifs at
5x, and its measured width comes to 28.1 cap-heights against Times New Roman Bold's 29.6 -- the
earlier build set this line in Arial Narrow Bold, which was the wrong face.

The line is rendered to a 6x raster and traced to paths with brand/tools/trace.py, so the
finished file carries no font dependency, exactly like every other mark on the site. The two
rules are exact rectangles; there is nothing to trace about a straight edge.
"""
import re, io, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "brand/tools"); import trace as T

SRC = "brand/corafrica-lockup.svg"
LINE = "CHILDREN OF RURAL AFRICA"
FONT = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"

# Measured off CORAfrica-Logo-Footer.png. The rules start at the wordmark's left edge and run
# a little past its right; the line is set to a slightly narrower measure between them.
RULE_W, RULE_T = 698.0, 5.0
GAP_WORD, GAP_ABOVE, GAP_BELOW = 4.0, 12.0, 13.0
TEXT_W = 675.0

# One scalar for the whole assembly. At 1.0 the lines are the artwork's own size; the header
# shows the lockup only 58px tall, and a wider measure is the only lever on how big the line
# lands there -- the lockup's height is pinned by the seal, not by the text.
SPREAD = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
OUT = sys.argv[2] if len(sys.argv) > 2 else "brand"

src = io.open(SRC, encoding="utf-8").read()
paths = re.findall(r'<path fill="([^"]+)" d="([^"]+)"', src)
assert len(paths) == 2, "expected the seal and the wordmark"
(seal_fill, seal_d), (word_fill, word_d) = paths

pts = [tuple(map(float, p.split(","))) for p in re.findall(r"[ML]([-\d.]+,[-\d.]+)", word_d)]
X0, WY1 = min(p[0] for p in pts), max(p[1] for p in pts)

rule_w, rule_t = RULE_W * SPREAD, RULE_T * SPREAD
text_w = TEXT_W * SPREAD
y_r1 = WY1 + GAP_WORD * SPREAD
y_txt = y_r1 + rule_t + GAP_ABOVE * SPREAD

UP = 6                                    # render at 6x, trace, divide back down
f = ImageFont.truetype(FONT, 200)
l, t, r, b = f.getbbox(LINE)
im = Image.new("L", (r - l + 8, b - t + 8), 0)
ImageDraw.Draw(im).text((4 - l, 4 - t), LINE, font=f, fill=255)
s = (text_w * UP) / im.size[0]
im = im.resize((int(round(im.size[0] * s)), int(round(im.size[1] * s))), Image.LANCZOS)
mask = np.array(im) > 110
text_h = im.size[1] / float(UP)
d_txt = T.trace(mask, scale=UP, eps=0.55, ox=X0 + (rule_w - text_w) / 2.0, oy=y_txt, prec=2)

y_r2 = y_txt + text_h + GAP_BELOW * SPREAD
bottom = y_r2 + rule_t
rules = " ".join("M%.2f,%.2f L%.2f,%.2f L%.2f,%.2f L%.2f,%.2f Z"
                 % (X0, y, X0 + rule_w, y, X0 + rule_w, y + rule_t, X0, y + rule_t)
                 for y in (y_r1, y_r2))

# viewBox: keep the original left/top, grow only to fit whatever is now lowest or furthest right.
vx, vy, vw, vh = (float(v) for v in re.search(r'viewBox="([\d.\- ]+)"', src).group(1).split())
vh = max(vh, bottom - vy + 2)
vw = max(vw, X0 + rule_w - vx + 2)

def emit(ink, out):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%g %g %.2f %.2f" width="%.2f" '
           'height="%.0f" role="img" aria-label="CORAfrica &#8212; Children of Rural Africa" '
           'fill-rule="evenodd"><title>CORAfrica &#8212; Children of Rural Africa</title>'
           % (vx, vy, vw, vh, vw, round(vh))
           + '<path fill="%s" d="%s"/>' % (ink, seal_d)
           + '<path fill="%s" d="%s"/>' % (word_fill, word_d)
           + '<path fill="%s" d="%s"/>' % (ink, rules)
           + '<path fill="%s" d="%s"/>' % (ink, d_txt)
           + "</svg>\n")
    io.open(out, "w", encoding="utf-8").write(svg)
    print("  %-46s %7d bytes" % (out, len(svg)))

print("spread %.2f | rules %.1f wide x %.1f at y %.1f and %.1f | line cap %.1f, %.1f wide"
      % (SPREAD, rule_w, rule_t, y_r1, y_r2, text_h, text_w))
print("viewBox %g %g %.2f %.2f -> at a 58px header the line is %.1fpx"
      % (vx, vy, vw, vh, text_h * 58.0 / vh))
emit("#111111", OUT + "/corafrica-lockup-full.svg")
emit("#FFFFFF", OUT + "/corafrica-lockup-full-white.svg")
