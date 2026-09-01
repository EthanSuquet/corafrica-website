"""Minimal raster->SVG tracer: Lanczos upsample, threshold, marching squares,
Douglas-Peucker, emit one evenodd path. numpy + Pillow only."""
import numpy as np
from PIL import Image

SEGS = {
    1:[((0,.5),(.5,1))], 2:[((.5,1),(1,.5))], 3:[((0,.5),(1,.5))],
    4:[((.5,0),(1,.5))], 5:[((0,.5),(.5,0)),((.5,1),(1,.5))],
    6:[((.5,0),(.5,1))], 7:[((0,.5),(.5,0))], 8:[((0,.5),(.5,0))],
    9:[((.5,0),(.5,1))], 10:[((0,.5),(.5,1)),((.5,0),(1,.5))],
    11:[((.5,0),(1,.5))], 12:[((0,.5),(1,.5))], 13:[((.5,1),(1,.5))],
    14:[((0,.5),(.5,1))],
}

def contours(mask):
    m = np.pad(mask.astype(np.uint8), 1)
    h, w = m.shape
    tl, tr = m[:-1,:-1], m[:-1,1:]
    br, bl = m[1:,1:],   m[1:,:-1]
    idx = (tl<<3) | (tr<<2) | (br<<1) | bl
    segs = {}
    ys, xs = np.nonzero((idx>0) & (idx<15))
    for i, j in zip(ys.tolist(), xs.tolist()):
        for (ax,ay),(bx,by) in SEGS[idx[i,j]]:
            a = (round((j+ax)*2), round((i+ay)*2))
            b = (round((j+bx)*2), round((i+by)*2))
            segs.setdefault(a, []).append(b)
            segs.setdefault(b, []).append(a)
    loops, seen = [], set()
    for start in list(segs):
        if start in seen: continue
        loop, cur, prev = [start], start, None
        seen.add(start)
        while True:
            nxt = None
            for cand in segs.get(cur, ()):
                if cand != prev and cand not in seen:
                    nxt = cand; break
            if nxt is None:
                if any(c == start for c in segs.get(cur, ())) and len(loop) > 2:
                    loop.append(start)
                break
            seen.add(nxt); loop.append(nxt); prev, cur = cur, nxt
        if len(loop) > 8:
            loops.append([(x/2.0, y/2.0) for x, y in loop])
    return loops

def dp(pts, eps):
    if len(pts) < 3: return pts
    p = np.asarray(pts, float)
    keep = np.zeros(len(p), bool); keep[0] = keep[-1] = True
    stack = [(0, len(p)-1)]
    while stack:
        i, j = stack.pop()
        if j <= i+1: continue
        a, b = p[i], p[j]
        d = b - a; n = np.hypot(*d)
        seg = p[i+1:j]
        dist = (np.abs(np.cross(d, seg-a))/n) if n > 1e-9 else np.hypot(*(seg-a).T)
        k = int(dist.argmax())
        if dist[k] > eps:
            k += i+1; keep[k] = True; stack += [(i,k),(k,j)]
    return [tuple(v) for v in p[keep]]

def trace(mask, scale=1.0, eps=0.35, ox=0.0, oy=0.0, prec=2):
    out = []
    for loop in contours(mask):
        s = dp(loop, eps*ScaleGuard(scale))
        if len(s) < 4: continue
        d = " ".join(
            ("M" if k == 0 else "L") + f"{(x/scale+ox):.{prec}f},{(y/scale+oy):.{prec}f}"
            for k, (x, y) in enumerate(s))
        out.append(d + "Z")
    return " ".join(out)

def ScaleGuard(s): return s  # eps expressed in upsampled px

def masks(path, up=4):
    im = Image.open(path).convert("RGBA")
    W, H = im.size
    big = im.resize((W*up, H*up), Image.LANCZOS)
    a = np.array(big).astype(int)
    al = a[...,3]; r, g, b = a[...,0], a[...,1], a[...,2]
    op = al > 140
    orange = op & (r > 140) & (r-b > 60) & (g < 200)
    dark = op & (r < 110) & (g < 110) & (b < 110)
    return dark, orange, up, (W, H)
