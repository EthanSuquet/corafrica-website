#!/usr/bin/env python3
"""Generate the CORAfrica sub-page artboards from one shared design system.

Every page shares the same chrome, type scale and section rhythm, lifted from
the Teeej stylesheet (Space Grotesk -0.05em display, Manrope body, warm
white->sand section gradients, 3rem panels, 0.7rem buttons).
No f-strings in HTML: {{accent}} must survive to the renderer.
"""
import os

W = "1440"
NAV = ["Who We Are", "Our Model", "Schools", "What We Do", "Strategic Plan", "News", "Contact"]

HEAD = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap">
  <style>
    body { margin: 0; font-family: Manrope, ui-sans-serif, system-ui, sans-serif; }
    a { color: #FB600A; text-decoration: none; }
    a:hover { color: #c24f06; }
  </style>
</helmet>

<div style="width: 1440px; background: #ffffff; color: #181818; font-family: Manrope, system-ui, sans-serif;">
"""

TAIL = """
</div>
</x-dc>
"""


def header(active):
    items = []
    for n in NAV:
        col = "{{accent}}" if n == active else "#f2efe9"
        items.append('      <span style="color: ' + col + ';">' + n + "</span>")
    return (
        '\n  <!-- HEADER -->\n'
        '  <div style="display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 16px 40px; background: rgba(44,42,42,.94);">\n'
        '    <img src="./corafrica-lockup-white.svg" alt="CORAfrica" style="height: 42px; width: auto; display: block;">\n'
        '    <div style="display: flex; align-items: center; gap: 26px; font-size: 14.5px; font-weight: 600; color: #f2efe9; letter-spacing: -0.01em;">\n'
        + "\n".join(items) + "\n"
        '      <span style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 12px 24px; background: {{accent}}; color: #fff; border-radius: 0.7rem; font-weight: 700;">Donate</span>\n'
        "    </div>\n"
        "  </div>\n"
    )


def photo_hero(kicker, title, lede, img, alt, height="392"):
    return (
        '\n  <!-- PAGE HERO -->\n'
        '  <div style="padding: 26px 40px 0; background: linear-gradient(180deg,#ffffff 0%,#fffdf9 100%);">\n'
        '    <div style="position: relative; height: ' + height + 'px; border-radius: 2.6rem; overflow: hidden; background: #101317; box-shadow: 0 34px 76px rgba(14,18,24,.20), inset 0 1px 0 rgba(255,255,255,.18);">\n'
        '      <img src="./' + img + '" alt="' + alt + '" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 40%;">\n'
        '      <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,12,16,.58) 0%, rgba(8,12,16,.40) 40%, rgba(8,12,16,.86) 100%);"></div>\n'
        '      <div style="position: relative; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; padding: 0 56px 44px; max-width: 900px;">\n'
        '        <span style="display: inline-flex; align-self: flex-start; padding: 0.45rem 0.72rem; border-radius: 999px; background: rgba(255,255,255,.10); color: rgba(255,255,255,.78); font-size: 0.84rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 18px;">' + kicker + "</span>\n"
        '        <h1 style="margin: 0 0 14px; font-family: \'Space Grotesk\', sans-serif; font-weight: 600; font-size: 52px; line-height: 1.04; letter-spacing: -0.05em; color: #fff; max-width: 22ch;">' + title + "</h1>\n"
        '        <p style="margin: 0; font-size: 16px; line-height: 1.5; color: rgba(255,255,255,.82); max-width: 62ch;">' + lede + "</p>\n"
        "      </div>\n"
        "    </div>\n"
        "  </div>\n"
    )


def light_hero(kicker, title, lede):
    return (
        '\n  <!-- PAGE HERO -->\n'
        '  <div style="padding: 68px 40px 44px; background: linear-gradient(180deg,#ffffff 0%,#fffdf9 100%);">\n'
        '    <div style="max-width: 1220px; margin: 0 auto;">\n'
        '      <div style="margin: 0 0 .95rem; color: {{accent}}; font-size: 0.88rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase;">' + kicker + "</div>\n"
        '      <h1 style="margin: 0 0 16px; font-family: \'Space Grotesk\', sans-serif; font-weight: 600; font-size: 54px; line-height: 1.03; letter-spacing: -0.05em; max-width: 20ch;">' + title + "</h1>\n"
        '      <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #4f4d4b; max-width: 66ch;">' + lede + "</p>\n"
        "    </div>\n"
        "  </div>\n"
    )


def sec(inner, bg="linear-gradient(180deg,#fffdf9 0%,#faf8f4 100%)", pad="76px 40px"):
    return ('\n  <div style="padding: ' + pad + '; background: ' + bg + ';">\n'
            '    <div style="max-width: 1220px; margin: 0 auto;">\n' + inner + "\n    </div>\n  </div>\n")


def kicker_h2(kicker, title, lede=None, maxw="26ch"):
    out = ('      <div style="margin: 0 0 .9rem; color: {{accent}}; font-size: 0.88rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase;">' + kicker + "</div>\n"
           '      <h2 style="margin: 0 0 ' + ("1.1rem" if lede else "2rem") + '; font-family: \'Space Grotesk\', sans-serif; font-size: 44px; font-weight: 600; line-height: 1.05; letter-spacing: -0.05em; max-width: ' + maxw + ';">' + title + "</h2>\n")
    if lede:
        out += '      <p style="margin: 0 0 2.2rem; font-size: 16px; line-height: 1.55; color: #4f4d4b; max-width: 68ch;">' + lede + "</p>\n"
    return out


def card(title, body, tag=None):
    t = ""
    if tag:
        t = ('        <div style="display: inline-flex; align-self: flex-start; padding: 4px 10px; border-radius: 999px; background: rgba(251,96,10,.10); color: {{accent}}; font-size: 11.5px; font-weight: 800; letter-spacing: .07em; text-transform: uppercase;">' + tag + "</div>\n")
    return ('      <div style="background: #ffffff; border: 1px solid #ece7df; border-radius: 1.6rem; padding: 26px 26px 28px; display: flex; flex-direction: column; gap: 11px; box-shadow: 0 18px 44px rgba(14,18,24,.06);">\n'
            + t
            + '        <div style="font-size: 19px; font-weight: 700; letter-spacing: -0.03em;">' + title + "</div>\n"
            + '        <div style="font-size: 14px; line-height: 1.5; color: #4f4d4b;">' + body + "</div>\n"
            "      </div>\n")


def grid(cards, cols=3, gap="18px"):
    return ('      <div style="display: grid; grid-template-columns: repeat(' + str(cols) + ', minmax(0,1fr)); gap: ' + gap + ';">\n'
            + "".join(cards) + "      </div>\n")


def btn(label, kind="accent"):
    if kind == "accent":
        return ('<span style="display: inline-flex; align-items: center; justify-content: center; min-height: 3.35rem; padding: 0.85rem 2rem; background: {{accent}}; color: #fff; border-radius: 0.7rem; font-size: 1.02rem; font-weight: 700; letter-spacing: -0.01em; box-shadow: 0 16px 30px rgba(251,96,10,.28);">' + label + "</span>")
    if kind == "dark":
        return ('<span style="display: inline-flex; align-items: center; justify-content: center; min-height: 3.35rem; padding: 0.85rem 2rem; background: #4d4a4a; color: #fff; border-radius: 0.92rem; font-size: 1.02rem; font-weight: 700; letter-spacing: -0.01em; box-shadow: 0 14px 28px rgba(19,20,22,.14);">' + label + "</span>")
    return ('<span style="display: inline-flex; align-items: center; justify-content: center; min-height: 3.35rem; padding: 0.85rem 1.85rem; background: #fff; color: #181818; border: 1px solid #ddd6cb; border-radius: 0.7rem; font-size: 1.02rem; font-weight: 700; letter-spacing: -0.01em;">' + label + "</span>")


FOOTER = """
  <!-- FOOTER -->
  <div style="background: #474545; color: #e9e5df; padding: 46px 40px 34px;">
    <div style="max-width: 1220px; margin: 0 auto; display: grid; grid-template-columns: 22rem 1fr; gap: 4rem; align-items: start;">
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <img src="./corafrica-lockup-white.svg" alt="CORAfrica" style="height: 46px; width: auto; display: block;">
        <p style="margin: 0; font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.72);">
          Helping children and communities thrive. A registered 501(c)(3) non-profit in the
          United States, operating in Cross River and Benue States, Nigeria.
        </p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 30px;">
        <div style="display: flex; flex-direction: column; gap: 9px;">
          <div style="font-size: 12px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: rgba(233,229,223,.55);">Nigeria</div>
          <div style="font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.86);">No 48 Mbube Road<br>Opposite Govt. Technical College, Abakpa<br>Ogoja, Cross River State</div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 9px;">
          <div style="font-size: 12px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: rgba(233,229,223,.55);">United States</div>
          <div style="font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.86);">PO Box 13<br>Evans City, PA 16033</div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 9px;">
          <div style="font-size: 12px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: rgba(233,229,223,.55);">Contact</div>
          <div style="font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.86);">info@corafrica.org.ng<br>+234 915 314 2288</div>
        </div>
      </div>
    </div>
    <div style="max-width: 1220px; margin: 30px auto 0; padding-top: 18px; border-top: 1px solid rgba(233,229,223,.16); display: flex; justify-content: space-between; gap: 20px; font-size: 12.5px; color: rgba(233,229,223,.55);">
      <span>&copy; 2026 Children of Rural Africa</span>
      <span>EIN [REQUEST FROM FR. PETER] &middot; CAC [REQUEST FROM FR. PETER]</span>
    </div>
  </div>
"""

SCRIPT = """
<script data-dc-script data-props='{"accent":{"editor":"color","default":"#FB600A","options":["#FB600A","#f16908","#C2410C","#166534"],"section":"Brand"}}'>
class Component extends DCLogic {
  renderVals() {
    return { accent: this.props.accent ?? '#FB600A' };
  }
}
</script>
</body>
</html>
"""


def write(name, active, body):
    html = HEAD + header(active) + body + FOOTER + TAIL + SCRIPT
    open(name, "w").write(html)
    print("%-26s %6d bytes" % (name, len(html)))
