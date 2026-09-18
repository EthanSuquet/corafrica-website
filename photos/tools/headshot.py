"""Cut a square headshot for site/img/team/ at the two sizes the site uses.

    python3 photos/tools/headshot.py SOURCE SLUG CX CY SIZE [--preview]

CX and CY are the centre of the crop as fractions of the image's width and height; SIZE is the
side of the square as a fraction of the width. --preview writes the crop to the scratchpad and
changes nothing under site/, which is the way to check the framing before committing to it.

168px is the card on Contact, 440px the portrait on the bio page; both are square and both are
sharpened after the downscale, because a headshot reduced this far goes soft otherwise. The
existing files sit at 5-8KB and 20-35KB, and quality 84 lands in that range.
"""
import sys, os
from PIL import Image, ImageFilter

src, slug, cx, cy, size = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
preview = "--preview" in sys.argv

im = Image.open(src)
im = im.convert("RGB")
W, H = im.size
s = size * W
box = (cx * W - s / 2, cy * H - s / 2, cx * W + s / 2, cy * H + s / 2)
if box[0] < 0 or box[1] < 0 or box[2] > W or box[3] > H:
    print("  ! crop runs outside the image (%.0f,%.0f)-(%.0f,%.0f) in %dx%d" % (box + (W, H)))
cut = im.crop(tuple(int(round(v)) for v in box))
print("source %dx%d -> crop %dx%d at (%.0f, %.0f)" % (W, H, cut.width, cut.height, box[0], box[1]))

out = "/tmp" if preview else "site/img/team"
if preview:
    out = os.environ.get("SCRATCH", "/tmp")
for px in (440, 168):
    r = cut.resize((px, px), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1, percent=62, threshold=3))
    p = "%s/%s%s.jpg" % (out, slug, "-lg" if px == 440 else "")
    r.save(p, "JPEG", quality=84, optimize=True, progressive=True)
    print("  %-40s %6d bytes" % (p, os.path.getsize(p)))
