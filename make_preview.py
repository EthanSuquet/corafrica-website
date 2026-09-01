#!/usr/bin/env python3
"""Bundle site/ into ONE self-contained HTML for review.

This is a preview harness, not the deliverable. It inlines the stylesheet,
the script and every image as a data URI, stacks all nine pages, and swaps
between them on nav clicks — so the real built pages can be clicked through
from a single hosted file. site/ remains the thing that ships.
"""
import base64, mimetypes, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
PAGES = ["index.html", "who-we-are.html", "our-model.html", "schools.html",
         "what-we-do.html", "strategic-plan.html", "news.html", "donate.html", "contact.html"]


def data_uri(rel):
    path = os.path.join(SITE, rel)
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as fh:
        return "data:%s;base64,%s" % (mime, base64.b64encode(fh.read()).decode())


IMGS = {f: data_uri("img/" + f) for f in sorted(os.listdir(os.path.join(SITE, "img")))}


def inline_assets(text):
    for name, uri in IMGS.items():
        text = text.replace('"img/%s"' % name, '"%s"' % uri)
        text = text.replace("url(img/%s)" % name, "url(%s)" % uri)
    return text


css = inline_assets(open(os.path.join(SITE, "styles.css"), encoding="utf-8").read())
js = open(os.path.join(SITE, "script.js"), encoding="utf-8").read()

sections = []
for p in PAGES:
    raw = open(os.path.join(SITE, p), encoding="utf-8").read()
    body = re.search(r"<body>(.*)</body>", raw, re.S).group(1)
    body = re.sub(r"<script\b.*?</script>", "", body, flags=re.S)
    body = inline_assets(body)
    # Internal page links become in-bundle switches.
    for q in PAGES:
        body = body.replace('href="%s"' % q, 'href="#/%s"' % q)
    hidden = "" if p == "index.html" else ' hidden'
    sections.append('<div class="pv-page" data-page="%s"%s>%s</div>' % (p, hidden, body))

html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CORAfrica — built site preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap" rel="stylesheet">
<style>
%s
.pv-bar{position:fixed;left:50%%;bottom:16px;transform:translateX(-50%%);z-index:90;display:flex;gap:4px;
 flex-wrap:wrap;justify-content:center;max-width:calc(100vw - 24px);
 background:rgba(24,24,24,.94);backdrop-filter:blur(10px);padding:7px;border-radius:999px;
 box-shadow:0 18px 44px rgba(0,0,0,.3)}
.pv-bar button{background:none;border:0;color:#d8d3cb;font:600 12.5px Manrope,sans-serif;
 padding:8px 13px;border-radius:999px;cursor:pointer;white-space:nowrap}
.pv-bar button:hover{color:#fff;background:rgba(255,255,255,.09)}
.pv-bar button[aria-pressed=true]{background:#fb600a;color:#fff}
@media(max-width:639px){.pv-bar{bottom:8px;padding:5px}.pv-bar button{padding:7px 10px;font-size:11.5px}}
</style>
</head>
<body>
%s
<nav class="pv-bar" aria-label="Preview pages">%s</nav>
<script>
%s
(function(){
  var pages=[].slice.call(document.querySelectorAll('.pv-page'));
  var btns=[].slice.call(document.querySelectorAll('.pv-bar button'));
  function show(name){
    pages.forEach(function(p){p.hidden = p.dataset.page!==name;});
    btns.forEach(function(b){b.setAttribute('aria-pressed', String(b.dataset.go===name));});
    window.scrollTo(0,0);
  }
  function fromHash(){
    var m=(location.hash||'').match(/^#\\/(.+)$/);
    show(m?m[1]:'index.html');
  }
  btns.forEach(function(b){b.addEventListener('click',function(){location.hash='#/'+b.dataset.go;});});
  document.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="#/"]');
    if(a){location.hash=a.getAttribute('href');}
  });
  window.addEventListener('hashchange',fromHash);
  fromHash();
})();
</script>
</body>
</html>
""" % (css, "\n".join(sections),
       "".join('<button data-go="%s" aria-pressed="%s">%s</button>'
               % (p, "true" if p == "index.html" else "false",
                  p.replace(".html", "").replace("-", " ").title().replace("Index", "Home"))
               for p in PAGES),
       js)

out = os.path.join(ROOT, "design", "corafrica-site-preview.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote %s — %.1f MB, %d pages, %d images inlined"
      % (os.path.relpath(out, ROOT), len(html) / 1e6, len(PAGES), len(IMGS)))
