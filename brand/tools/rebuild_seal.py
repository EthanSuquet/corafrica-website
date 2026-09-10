"""Rebuild the CORAfrica seal from Fr. Peter's current logo (400px JPEG) as a clean vector.
Rings and dots are constructed from measured geometry, ring lettering is Arial Bold set on the
measured arcs, the map is traced from the JPEG, the book-and-torch emblem is redrawn. Everything
is rendered to a 6x master and traced to one evenodd path in the old seal's coordinate frame."""
import sys, math, collections, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, "brand/tools"); import trace as T
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
SRC = "brand/source/corafrica-seal-2026-09-04.jpeg"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
src = Image.open(SRC).convert("L"); g = np.array(src).astype(float); H, W = g.shape
dark = g < 128; cx = cy = 201.0
yy, xx = np.mgrid[0:H, 0:W]; rr = np.hypot(xx - cx, yy - cy); aa = (np.degrees(np.arctan2(yy - cy, xx - cx)) + 360) % 360
ang = np.radians(np.arange(0, 360, 0.25))
def frac(r):
    px = np.clip(np.round(cx + r * np.cos(ang)).astype(int), 0, W - 1); py = np.clip(np.round(cy + r * np.sin(ang)).astype(int), 0, H - 1)
    return dark[py, px].mean()
rs = np.arange(120, 200, 0.25); fr = np.array([frac(r) for r in rs]); solid = rs[fr > 0.9]
RO0, RO1 = solid[solid > 180].min(), solid[solid > 180].max(); RI0, RI1 = solid[solid < 180].min(), solid[solid < 180].max()
print("outer ring %.2f-%.2f  inner ring %.2f-%.2f" % (RO0, RO1, RI0, RI1))
band = dark & (rr > RI1 + 2.5) & (rr < RO0 - 2.5)
lab = np.zeros(dark.shape, int); comps = []; n = 0
for sy, sx in zip(*np.nonzero(band)):
    if lab[sy, sx]: continue
    n += 1; q = collections.deque([(sy, sx)]); lab[sy, sx] = n; pix = []
    while q:
        y, x = q.popleft(); pix.append((y, x))
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W and band[ny, nx] and not lab[ny, nx]:
                    lab[ny, nx] = n; q.append((ny, nx))
    p = np.array(pix)
    if len(p) < 6: continue
    a = aa[p[:, 0], p[:, 1]]; r = rr[p[:, 0], p[:, 1]]
    ca = (math.degrees(math.atan2(p[:, 0].mean() - cy, p[:, 1].mean() - cx)) + 360) % 360
    comps.append(dict(n=len(p), ca=ca, a=a, rmin=r.min(), rmax=r.max(), w=np.ptp(p[:, 1]) + 1, h=np.ptp(p[:, 0]) + 1, c=(p[:, 1].mean(), p[:, 0].mean())))
top = [c for c in comps if c["ca"] >= 171 or c["ca"] <= 9]
bot = [c for c in comps if 21 <= c["ca"] <= 159]
dots = [c for c in comps if c not in top and c not in bot and c["n"] > 40]
unwrap = lambda a: np.where(a < 90, a + 360, a)
ta0 = min(unwrap(c["a"]).min() for c in top); ta1 = max(unwrap(c["a"]).max() for c in top)
ba_left = max(c["a"].max() for c in bot); ba_right = min(c["a"].min() for c in bot)
t_base = float(np.median([c["rmin"] for c in top])); t_cap = float(np.median([c["rmax"] - c["rmin"] for c in top]))
b_base = float(np.median([c["rmax"] for c in bot])); b_cap = float(np.median([c["rmax"] - c["rmin"] for c in bot]))
print("top: %d comps, span %.1f-%.1f deg, baseline r %.1f, cap %.1f" % (len(top), ta0, ta1, t_base, t_cap))
print("bottom: %d comps, span %.1f->%.1f deg, baseline r %.1f, cap %.1f" % (len(bot), ba_left, ba_right, b_base, b_cap))
print("dots:", [("(%.1f,%.1f)" % d["c"], round(math.sqrt(d["n"] / math.pi), 2), round(d["ca"], 1)) for d in dots])

M = 6.0; SZ = int(402 * M)
tm = lambda v: v * M + M / 2
C = tm(201.0)
mask = Image.new("L", (SZ, SZ), 0); d = ImageDraw.Draw(mask)
def disc(x, y, r, fill): d.ellipse([x - r, y - r, x + r, y + r], fill=fill)
disc(C, C, (RO1 + 0.25) * M, 255); disc(C, C, (RO0 - 0.25) * M, 0)
disc(C, C, (RI1 + 0.25) * M, 255); disc(C, C, (RI0 - 0.25) * M, 0)
for dt in dots:
    disc(tm(dt["c"][0]), tm(dt["c"][1]), math.sqrt(dt["n"] / math.pi) * M * 1.02, 255)

def set_arc(text, a_start, a_end, base, cap, outward):
    size = 400; f = ImageFont.truetype(FONT, size); ch = -f.getbbox("H", anchor="ls")[1]
    size = max(8, int(round(size * cap * M / ch))); f = ImageFont.truetype(FONT, size)
    adv = [f.getlength(c) for c in text]
    r_mid = (base + cap / 2 if outward else base - cap / 2) * M
    span = math.radians(abs(a_end - a_start)) * r_mid
    track = (span - sum(adv) + adv[0] * 0.08 + adv[-1] * 0.08) / (len(text) - 1)
    s = -adv[0] * 0.04
    for i, chh in enumerate(text):
        mid = s + adv[i] / 2; s += adv[i] + track
        if chh == " ": continue
        phi = a_start + math.degrees(mid / r_mid) * (1 if outward else -1)
        gsz = int(size * 2.2); im = Image.new("L", (gsz, gsz), 0)
        ImageDraw.Draw(im).text((gsz / 2, gsz / 2), chh, font=f, fill=255, anchor="ms")
        im = im.rotate((270 - phi) if outward else (90 - phi), resample=Image.BICUBIC)
        px = C + base * M * math.cos(math.radians(phi)); py = C + base * M * math.sin(math.radians(phi))
        mask.paste(255, (int(round(px - gsz / 2)), int(round(py - gsz / 2))), im)
    return size, track
print("top font px %d track %.1f" % set_arc("CHILDREN OF RURAL AFRICA", ta0, ta1, t_base, t_cap, True))
print("bottom font px %d track %.1f" % set_arc("EDUCATION FOR AFRICA’S FUTURE", ba_left, ba_right, b_base, b_cap, False))

# map: dark pixels well inside the inner ring, emblem holes filled, smoothed on upsampling
mm = dark & (rr < RI0 - 3)
bg = np.zeros_like(mm); q = collections.deque([(0, 0)]); bg[0, 0] = True
while q:
    y, x = q.popleft()
    for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
        if 0 <= ny < H and 0 <= nx < W and not mm[ny, nx] and not bg[ny, nx]:
            bg[ny, nx] = True; q.append((ny, nx))
filled = ~bg
big = Image.fromarray((filled * 255).astype(np.uint8)).resize((int(400 * M), int(400 * M)), Image.LANCZOS).filter(ImageFilter.GaussianBlur(M * 0.7))
mapmask = big.point(lambda v: 255 if v >= 128 else 0)
mask.paste(255, (0, 0), mapmask)

# emblem, redrawn in logo pixel coordinates (measured from a 6x zoom of the JPEG)
P = lambda pts: [(tm(x), tm(y)) for x, y in pts]
d.polygon(P([(226, 128.5), (232, 133), (236.5, 138), (237.5, 143), (234.5, 148.5), (226, 150.5), (217.5, 148.5), (214.5, 143), (215.5, 138), (220, 133)]), fill=0)
d.polygon(P([(226, 134), (229.5, 138.5), (231, 142.5), (229.5, 146.5), (226, 147.5), (222.5, 146.5), (221, 142.5), (222.5, 138.5)]), fill=255)
d.rectangle([tm(221), tm(149.5), tm(231), tm(153.5)], fill=0)
disc(tm(226), tm(159.5), 6.2 * M, 0); disc(tm(226), tm(159.5), 2.0 * M, 255)
d.rectangle([tm(223), tm(164), tm(229), tm(172)], fill=0)
d.polygon(P([(197.5, 172.5), (226, 169.5), (256.5, 172.5), (256.5, 210.5), (226.5, 206.5), (197.5, 210.5)]), fill=0)
d.rounded_rectangle([tm(221.5), tm(205), tm(231), tm(232.5)], radius=4.5 * M, fill=0)
lw = int(1.1 * M)
for x in (204, 209.5, 215, 220.5, 232, 237.5, 243, 248.5):
    d.line([tm(x), tm(176.5), tm(x), tm(201.5)], fill=255, width=lw)
d.line([tm(226.2), tm(172), tm(226.2), tm(206)], fill=255, width=int(1.3 * M))

mask.resize((600, 600), Image.LANCZOS).save(OUT + "/master-preview.png")
arr = np.array(mask) >= 128
loops = T.contours(arr)
k = 140.2 / ((RO1 + 0.25) * M); OX, OY = 160.0, 176.95
parts, npts = [], 0
for loop in loops:
    sp = T.dp(loop, 1.1)
    if len(sp) < 4: continue
    npts += len(sp)
    parts.append(" ".join(("M" if i == 0 else "L") + "%.2f,%.2f" % (OX + (x - 1 - C) * k, OY + (y - 1 - C) * k) for i, (x, y) in enumerate(sp)) + "Z")
dstr = " ".join(parts)
open(OUT + "/seal-d.txt", "w").write(dstr)
old = open("brand/corafrica-seal.svg").read()
new = re.sub(r'(<path\b[^>]*\sd=")[^"]+(")', lambda m: m.group(1) + dstr + m.group(2), old, count=1)
open(OUT + "/corafrica-seal.svg", "w").write(new)
print("loops %d, points %d, svg %d bytes" % (len(parts), npts, len(new)))
