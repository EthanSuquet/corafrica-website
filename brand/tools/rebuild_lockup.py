"""Rebuild the CORAfrica lockup to Fr. Peter's instruction of 2026-09-17, 6:33 and 6:42 PM:

    "Pls remove 'Helping children and communities thrive' from the insignia. Also remove
     NIGERIA. Just say CHILDREN OF RURAL AFRICA in between two lines, just as it looks
     above or on the shirt."
    "It's too crowded. It should just be CORAfrica / CHILDREN OF RURAL AFRICA (with logo).
     The logo should be the one that says EDUCATION FOR AFRICA'S FUTURE."

and to his two adjustments of 2026-09-18: more air between the wordmark and the line beneath
it, and a larger seal.

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
GAP_ABOVE, GAP_BELOW = 12.0, 13.0
TEXT_W = 675.0

# The artwork sets the first rule 4 units under the wordmark. 2026-09-18, Fr. Peter: "a tad more
# space for the logo between the CORAfrica line and the Children of Rural Africa line."
GAP_WORD = 14.0

# 2026-09-18, Fr. Peter: "enlarge the actual circle SVG on the side." The gap between the seal
# and the wordmark grows with it, so the two stay in the same relation.
SEAL_K = 1.18

# One scalar for the text assembly. At 1.0 the lines are the artwork's own size; the header
# shows the lockup only 58px tall, and a wider measure is the only lever on how big the line
# lands there -- the lockup's height is pinned by the seal, not by the text.
SPREAD = 1.0

OUT = "brand"
for a in sys.argv[1:]:                    # spread=1.1 seal=1.25 gap=18 out=/tmp/try
    k, v = a.split("=", 1)
    if k == "out": OUT = v
    else: globals()[{"spread": "SPREAD", "seal": "SEAL_K", "gap": "GAP_WORD"}[k]] = float(v)

src = io.open(SRC, encoding="utf-8").read()
paths = re.findall(r'<path fill="([^"]+)" d="([^"]+)"', src)
assert len(paths) == 2, "expected the seal and the wordmark"
(seal_fill, seal_d), (word_fill, word_d) = paths

def pts_of(d):
    return [tuple(map(float, p.split(","))) for p in re.findall(r"[ML]([-\d.]+,[-\d.]+)", d)]

def bbox(d):
    p = pts_of(d)
    return min(q[0] for q in p), max(q[0] for q in p), min(q[1] for q in p), max(q[1] for q in p)

def xform(d, k, ox, oy):
    """These paths are only M/L point lists, so a scale-and-shift is a rewrite of the numbers."""
    return re.sub(r"([-\d.]+),([-\d.]+)",
                  lambda m: "%.2f,%.2f" % (ox + k * float(m.group(1)), oy + k * float(m.group(2))), d)

SX0, SX1, SY0, SY1 = bbox(seal_d)
X0, X1, WY0, WY1 = bbox(word_d)

# The seal keeps its left edge and grows to the right; the wordmark and the lines move right by
# as much, so the space between seal and wordmark scales with the seal rather than closing up.
dx = SX0 + SEAL_K * (SX1 - SX0 + X0 - SX1) - X0
word_d = xform(word_d, 1.0, dx, 0.0)
TX0 = X0 + dx

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
d_txt = T.trace(mask, scale=UP, eps=0.55, ox=TX0 + (rule_w - text_w) / 2.0, oy=y_txt, prec=2)

y_r2 = y_txt + text_h + GAP_BELOW * SPREAD
bottom = y_r2 + rule_t
rules = " ".join("M%.2f,%.2f L%.2f,%.2f L%.2f,%.2f L%.2f,%.2f Z"
                 % (TX0, y, TX0 + rule_w, y, TX0 + rule_w, y + rule_t, TX0, y + rule_t)
                 for y in (y_r1, y_r2))

# The seal sits on the text block's own centre line, which is what keeps it looking hung on the
# words rather than floating beside them.
seal_d = xform(seal_d, SEAL_K, SX0 * (1 - SEAL_K),
               (WY0 + bottom) / 2.0 - SEAL_K * (SY0 + SY1) / 2.0)
sx0, sx1, sy0, sy1 = bbox(seal_d)

M = 1.0                                   # a hair of margin, as the original mark carried
vx, vy = min(sx0, TX0) - M, min(sy0, WY0) - M
vw, vh = max(sx1, TX0 + rule_w) + M - vx, max(sy1, bottom) + M - vy

def emit(ink, out):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.2f %.2f %.2f %.2f" width="%.2f" '
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

print("seal x%.2f (%.1f wide) | wordmark moved %+.1f | wordmark-to-rule gap %.1f"
      % (SEAL_K, sx1 - sx0, dx, GAP_WORD * SPREAD))
print("viewBox %.2f %.2f %.2f %.2f -> at a 58px header: %.0fpx wide, line %.1fpx"
      % (vx, vy, vw, vh, vw * 58.0 / vh, text_h * 58.0 / vh))
emit("#111111", OUT + "/corafrica-lockup-full.svg")
emit("#FFFFFF", OUT + "/corafrica-lockup-full-white.svg")
