#!/usr/bin/env python3
"""Mobile artboards at 390px — authored for the phone, not shrunk from desktop.

Rules applied throughout:
  * nav collapses to logo + Donate + hamburger (44px touch targets)
  * every multi-column grid becomes one column
  * display type drops 62px -> 34px, h2 44px -> 29px
  * buttons go full-width, min-height 52px
  * the Schools register stops being a table and becomes stacked cards
"""
A = "{{accent}}"
G = "20px"          # gutter

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

<div style="width: 390px; background: #ffffff; color: #181818; font-family: Manrope, system-ui, sans-serif; overflow: hidden;">
"""

TAIL = """
</div>
</x-dc>

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

HEADER = ('\n  <!-- HEADER: nav collapses to a hamburger; Donate stays reachable -->\n'
          '  <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px ' + G + '; background: rgba(44,42,42,.96);">\n'
          '    <img src="./corafrica-lockup-white.svg" alt="CORAfrica" style="height: 32px; width: auto; display: block;">\n'
          '    <div style="display: flex; align-items: center; gap: 10px;">\n'
          '      <span style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 18px; background: ' + A + '; color: #fff; border-radius: 0.7rem; font-size: 14px; font-weight: 700;">Donate</span>\n'
          '      <span style="display: flex; flex-direction: column; justify-content: center; gap: 5px; width: 44px; height: 44px; padding: 0 10px; box-sizing: border-box;">\n'
          '        <span style="display: block; height: 2px; background: #f2efe9; border-radius: 2px;"></span>\n'
          '        <span style="display: block; height: 2px; background: #f2efe9; border-radius: 2px;"></span>\n'
          '        <span style="display: block; height: 2px; background: #f2efe9; border-radius: 2px;"></span>\n'
          '      </span>\n    </div>\n  </div>\n')

FOOTER = ('\n  <!-- FOOTER: three columns become one stack -->\n'
          '  <div style="background: #474545; color: #e9e5df; padding: 36px ' + G + ' 28px;">\n'
          '    <img src="./corafrica-lockup-white.svg" alt="CORAfrica" style="height: 38px; width: auto; display: block; margin-bottom: 14px;">\n'
          '    <p style="margin: 0 0 26px; font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.72);">Helping children and communities thrive. A registered 501(c)(3) non-profit in the United States, operating in Cross River and Benue States, Nigeria.</p>\n'
          '    <div style="display: flex; flex-direction: column; gap: 20px;">\n'
          '      <div><div style="font-size: 11.5px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: rgba(233,229,223,.55); margin-bottom: 6px;">Nigeria</div>\n'
          '      <div style="font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.86);">No 48 Mbube Road, Opposite Govt. Technical College, Abakpa, Ogoja, Cross River State</div></div>\n'
          '      <div><div style="font-size: 11.5px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: rgba(233,229,223,.55); margin-bottom: 6px;">United States</div>\n'
          '      <div style="font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.86);">PO Box 13, Evans City, PA 16033</div></div>\n'
          '      <div><div style="font-size: 11.5px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: rgba(233,229,223,.55); margin-bottom: 6px;">Contact</div>\n'
          '      <div style="font-size: 13.5px; line-height: 1.5; color: rgba(233,229,223,.86);">info@corafrica.org.ng<br>+234 915 314 2288</div></div>\n'
          '    </div>\n'
          '    <div style="margin-top: 26px; padding-top: 16px; border-top: 1px solid rgba(233,229,223,.16); display: flex; flex-direction: column; gap: 5px; font-size: 12px; color: rgba(233,229,223,.55);">\n'
          '      <span>&copy; 2026 Children of Rural Africa</span>\n'
          '      <span>EIN [REQUEST] &middot; CAC [REQUEST]</span>\n    </div>\n  </div>\n')


def hero(kicker, title, lede, img, alt, h="470", tsize="34"):
    return ('\n  <!-- HERO -->\n'
            '  <div style="padding: 14px ' + G + ' 0; background: linear-gradient(180deg,#ffffff 0%,#fffdf9 100%);">\n'
            '    <div style="position: relative; height: ' + h + 'px; border-radius: 1.5rem; overflow: hidden; background: #101317; box-shadow: 0 20px 44px rgba(14,18,24,.20);">\n'
            '      <img src="./' + img + '" alt="' + alt + '" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 38%;">\n'
            '      <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,12,16,.55) 0%, rgba(8,12,16,.34) 32%, rgba(8,12,16,.90) 100%);"></div>\n'
            '      <div style="position: relative; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; padding: 0 22px 26px;">\n'
            '        <span style="display: inline-flex; align-self: flex-start; padding: 6px 11px; border-radius: 999px; background: rgba(255,255,255,.12); color: rgba(255,255,255,.80); font-size: 11px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 14px;">' + kicker + "</span>\n"
            '        <h1 style="margin: 0 0 12px; font-family: \'Space Grotesk\', sans-serif; font-weight: 600; font-size: ' + tsize + 'px; line-height: 1.06; letter-spacing: -0.04em; color: #fff;">' + title + "</h1>\n"
            '        <p style="margin: 0; font-size: 14.5px; line-height: 1.5; color: rgba(255,255,255,.84);">' + lede + "</p>\n"
            "      </div>\n    </div>\n  </div>\n")


def sec(inner, bg="linear-gradient(180deg,#fffdf9 0%,#faf8f4 100%)", pad="44px " + G):
    return '\n  <div style="padding: ' + pad + '; background: ' + bg + ';">\n' + inner + "  </div>\n"


def kh2(kicker, title, lede=None):
    o = ('    <div style="margin: 0 0 .7rem; color: ' + A + '; font-size: 11.5px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase;">' + kicker + "</div>\n"
         '    <h2 style="margin: 0 0 ' + ("12px" if lede else "22px") + '; font-family: \'Space Grotesk\', sans-serif; font-size: 29px; font-weight: 600; line-height: 1.08; letter-spacing: -0.04em;">' + title + "</h2>\n")
    if lede:
        o += '    <p style="margin: 0 0 24px; font-size: 15px; line-height: 1.55; color: #4f4d4b;">' + lede + "</p>\n"
    return o


def card(title, body, tag=None):
    t = ""
    if tag:
        t = ('      <div style="display: inline-flex; align-self: flex-start; padding: 4px 10px; border-radius: 999px; background: rgba(251,96,10,.10); color: ' + A + '; font-size: 10.5px; font-weight: 800; letter-spacing: .07em; text-transform: uppercase;">' + tag + "</div>\n")
    return ('    <div style="background: #fff; border: 1px solid #ece7df; border-radius: 1.2rem; padding: 20px 20px 22px; display: flex; flex-direction: column; gap: 9px; box-shadow: 0 14px 32px rgba(14,18,24,.05);">\n'
            + t + '      <div style="font-size: 17.5px; font-weight: 700; letter-spacing: -0.03em;">' + title + "</div>\n"
            '      <div style="font-size: 14px; line-height: 1.5; color: #4f4d4b;">' + body + "</div>\n    </div>\n")


def stack(items, gap="12px"):
    return '    <div style="display: flex; flex-direction: column; gap: ' + gap + ';">\n' + "".join(items) + "    </div>\n"


def fullbtn(label, kind="accent"):
    if kind == "accent":
        return ('    <span style="display: flex; align-items: center; justify-content: center; min-height: 52px; background: ' + A + '; color: #fff; border-radius: 0.7rem; font-size: 16px; font-weight: 700; box-shadow: 0 12px 24px rgba(251,96,10,.26);">' + label + "</span>\n")
    if kind == "onDark":
        return ('    <span style="display: flex; align-items: center; justify-content: center; min-height: 52px; background: rgba(255,255,255,.13); border: 1px solid rgba(255,255,255,.34); color: #fff; border-radius: 0.7rem; font-size: 16px; font-weight: 700;">' + label + "</span>\n")
    return ('    <span style="display: flex; align-items: center; justify-content: center; min-height: 52px; background: #fff; border: 1px solid #ddd6cb; color: #181818; border-radius: 0.7rem; font-size: 16px; font-weight: 700;">' + label + "</span>\n")


def write(name, body):
    html = HEAD + HEADER + body + FOOTER + TAIL
    open(name, "w").write(html)
    print("%-26s %6d bytes" % (name, len(html)))


# ==================================================== HOME
stats = [("2,000+", "Pupils educated", "At St. Joseph’s, Idum-Mbube alone"),
         ("500+", "Women financed", "Soft loans and grants to date"),
         ("5", "Schools founded", "Across Cross River State"),
         ("2", "Centres running", "Mbube-Ogoja and Victoria-Ikom")]
sc = ""
for n, l, note in stats:
    sc += ('      <div style="display: flex; flex-direction: column; gap: 4px;">\n'
           '        <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 36px; font-weight: 600; line-height: 1; letter-spacing: -0.045em;">' + n + "</div>\n"
           '        <div style="font-size: 13.5px; font-weight: 700; letter-spacing: -0.02em;">' + l + "</div>\n"
           '        <div style="font-size: 12px; line-height: 1.35; color: #78726a;">' + note + "</div>\n      </div>\n")

creds = ["Registered 501(c)(3) since 2006", "Cross River and Benue States",
         "Aligned to five UN SDGs", "Partnered with the Diocese of Ogoja"]
cl = ""
for c in creds:
    cl += ('      <div style="display: flex; align-items: flex-start; gap: 10px;">\n'
           '        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="' + A + '" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="flex: 0 0 auto; margin-top: 2px;" aria-hidden="true"><path d="M20 6 9 17l-5-5"></path></svg>\n'
           '        <span style="font-size: 13.5px; font-weight: 600; color: #4f4d4b;">' + c + "</span>\n      </div>\n")

pillars = [("Education", "Primary and secondary schools, built where no school exists, plus vocational and skills centres."),
           ("Healthcare", "A clinic on the school site, and care concentrated on a child’s first 1,000 days."),
           ("Agriculture", "A demonstration farm that feeds the school and teaches the trade hands-on."),
           ("Livelihoods", "Soft loans so a parent can build a business and afford to keep a child in class.")]

schools_m = [("300+ students", "John Stilley Secondary School", "Victoria, Ikom — the only secondary school in its community", "school.jpg"),
             ("Founded 2020", "John Bosco Academy", "Adagom, Ogoja — for refugee children arriving from Cameroon", "hands.jpg"),
             ("2,000+ pupils", "St. Joseph’s School", "Idum-Mbube — school and orphanage, now run by the Diocese of Ogoja", "clinic.jpg")]
sch = ""
for stat, name, note, img in schools_m:
    sch += ('    <div style="position: relative; height: 270px; border-radius: 1.4rem; overflow: hidden; background: #101317; box-shadow: 0 18px 40px rgba(20,24,30,.18);">\n'
            '      <img src="./' + img + '" alt="' + name + '" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;">\n'
            '      <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,12,16,0) 24%, rgba(8,12,16,.34) 56%, rgba(8,12,16,.90) 100%);"></div>\n'
            '      <div style="position: absolute; inset: auto 0 0 0; padding: 20px; display: flex; flex-direction: column; gap: 7px;">\n'
            '        <div style="display: inline-flex; align-self: flex-start; padding: 4px 10px; border-radius: 999px; background: rgba(251,96,10,.92); color: #fff; font-size: 10.5px; font-weight: 800; letter-spacing: .07em; text-transform: uppercase;">' + stat + "</div>\n"
            '        <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 20px; font-weight: 600; letter-spacing: -0.035em; color: #fff; line-height: 1.15;">' + name + "</div>\n"
            '        <div style="font-size: 12.5px; line-height: 1.4; color: rgba(255,255,255,.80);">' + note + "</div>\n      </div>\n    </div>\n")

press = [("National Catholic Reporter", "May 2024", "Catholic-run CORAfrica aims to fill learning gap fueled by poverty in Nigeria"),
         ("Vanguard", "Jul 2026", "CORAfrica expands community development through education, healthcare, livelihood programmes"),
         ("ThisDay", "Jul 2026", "CORAfrica expands access to education for children in rural communities")]
pr = ""
for o, d, t in press:
    pr += ('    <div style="background: #fff; border: 1px solid #ece7df; border-radius: 1.2rem; padding: 18px 20px 20px; display: flex; flex-direction: column; gap: 7px; box-shadow: 0 14px 32px rgba(14,18,24,.05);">\n'
           '      <div style="display: flex; align-items: baseline; justify-content: space-between; gap: 10px;">\n'
           '        <span style="font-size: 11.5px; font-weight: 800; letter-spacing: .06em; text-transform: uppercase;">' + o + "</span>\n"
           '        <span style="font-size: 11.5px; color: #a09889; flex: 0 0 auto;">' + d + "</span>\n      </div>\n"
           '      <div style="font-size: 15.5px; font-weight: 700; line-height: 1.3; letter-spacing: -0.025em;">' + t + "</div>\n"
           '      <span style="font-size: 13px; font-weight: 700; color: ' + A + ';">Read the article &rarr;</span>\n    </div>\n')

body = hero("Education for Africa’s Future", "A school, and everything that keeps a child in it.",
            "CORAfrica builds schools in rural Nigeria where none exist — then adds the clinic, the farm and the workshop that keep children coming back.",
            "hero.jpg", "Pupils at a CORAfrica school", h="500")
body += sec('    <div style="display: flex; flex-direction: column; gap: 10px;">\n' + fullbtn("Donate") + fullbtn("Partner with us", "plain") + "    </div>\n",
            bg="#fffdf9", pad="18px " + G + " 4px")
body += sec('    <div style="display: flex; flex-direction: column; gap: 11px;">\n' + cl + "    </div>\n", bg="#fffdf9", pad="22px " + G + " 8px")
body += sec('    <div style="border-radius: 1.6rem; background: linear-gradient(180deg,#f1efea 0%,#efede8 100%); box-shadow: 0 20px 48px rgba(14,18,24,.10); padding: 26px 22px 28px;">\n'
            '      <div style="color: ' + A + '; font-size: 11.5px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 20px;">Twenty years on the ground</div>\n'
            '      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px 18px;">\n' + sc + "      </div>\n"
            '      <div style="font-size: 11.5px; color: #78726a; margin-top: 20px; line-height: 1.4;">Independently reported — National Catholic Reporter, Vanguard, ThisDay</div>\n    </div>\n',
            bg="linear-gradient(180deg,#fffdf9 0%,#faf8f4 100%)", pad="28px " + G)
body += sec(kh2("The Community Education Centre", "A school on its own does not keep a child in school.",
                "Hunger, illness, and a family with no income take more children out of class than any exam does. So our model puts four things on one site.")
            + stack([card(n, b) for n, b in pillars])
            + '    <div style="margin-top: 20px;">' + fullbtn("Read the strategic plan", "plain") + "</div>\n",
            bg="linear-gradient(180deg,#faf8f4 0%,#ffffff 100%)")
body += sec(kh2("Our schools", "Built where there was nothing.") + stack([sch]),
            bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
body += sec('    <div style="border-radius: 1.4rem; overflow: hidden; box-shadow: 0 20px 48px rgba(12,18,28,.12); margin-bottom: 22px;">\n'
            '      <img src="./founder.jpg" alt="Fr. Peter Abue with pupils" style="width: 100%; height: 240px; object-fit: cover; display: block;">\n    </div>\n'
            + kh2("Our founder", "“Most of my peers in our village could not. So I decided to fill that gap.”",
                  "Fr. Peter Obele Abue conceived CORAfrica in 2006 while completing a PhD in International Development at Cornell. He is Vicar General of the Catholic Diocese of Ogoja."),
            bg="linear-gradient(180deg,#f5f2ec 0%,#fffdfa 100%)")
body += sec(kh2("In the news", "Reported independently.") + stack([pr]), bg="#fffdfa")
body += sec('    <div style="border-radius: 1.6rem; background: #2c2a2a; box-shadow: 0 20px 48px rgba(14,18,24,.18); padding: 30px 22px 28px;">\n'
            '      <div style="color: rgba(255,255,255,.62); font-size: 11.5px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 12px;">Support the work</div>\n'
            '      <h2 style="margin: 0 0 12px; font-family: \'Space Grotesk\', sans-serif; font-size: 27px; font-weight: 600; line-height: 1.08; letter-spacing: -0.04em; color: #fff;">&#8358;150,000 started a business. $40,000 started a programme.</h2>\n'
            '      <p style="margin: 0 0 22px; font-size: 14px; line-height: 1.55; color: rgba(255,255,255,.74);">CORAfrica is a registered 501(c)(3), so gifts from US donors are tax-deductible. Give once, or monthly.</p>\n'
            '      <div style="display: flex; flex-direction: column; gap: 10px;">\n' + fullbtn("Give monthly") + fullbtn("Give once", "onDark") + "      </div>\n"
            '      <div style="font-size: 11.5px; color: rgba(255,255,255,.52); text-align: center; margin-top: 12px;">Processed securely by Stripe</div>\n    </div>\n',
            bg="#fffdfa", pad="10px " + G + " 40px")
write("MobileHome.dc.html", body)


# ==================================================== WHO WE ARE
hist = [("2006", "Conceived at Cornell", "Fr. Peter Obele Abue, completing a PhD in International Development, sets out to close the gap between the developed and developing world."),
        ("2006", "Incorporated in the US", "501(c)(3) status granted, with a founding board of Bruno Schickel, Royal Colle, Thomas Lickona and Carolann Darling. Building begins in Nigeria."),
        ("2009", "Fr. Peter returns to Nigeria", "Projects follow across the Diocese of Ogoja — St. Joseph’s, the Sr. Augustina Abuo Medical Clinic, Little Flower School at Ipong-Obudu."),
        ("2010s", "A second board, from Western Pennsylvania", "With Abode for Children Inc. of Evans City, they upgrade St. Joseph’s Schools and Orphanage and CORAfrica Farms."),
        ("2020", "John Bosco Academy", "Founded at Adagom, Ogoja, for refugee children arriving from Cameroon with no access to basic education."),
        ("2021", "The John Stilley Schools", "Founded at Victoria, Ikom, where no secondary school existed. St. Peter’s Primary is registered at Adagom 3."),
        ("Today", "Two states, and a model that travels", "Headquartered in Abuja, working across Cross River and Benue States, reaching IDP camps and refugee settlements.")]
hr = ""
for yr, t, b in hist:
    hr += ('      <div style="padding: 18px 0; border-top: 1px solid #e8e2d8;">\n'
           '        <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 15px; font-weight: 600; color: ' + A + '; letter-spacing: -0.02em; margin-bottom: 5px;">' + yr + "</div>\n"
           '        <div style="font-size: 17px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 5px;">' + t + "</div>\n"
           '        <div style="font-size: 14px; line-height: 1.5; color: #4f4d4b;">' + b + "</div>\n      </div>\n")

vals = [("Dignity of the human person", "Each child has an inalienable dignity, and should be treated as an end and never only as a means. Every child deserves the chance to achieve their dreams, no matter where they were born."),
        ("Solidarity and the common good", "Faced with globalisation and the growing interdependence of peoples, the universal human family remains one. We must increase our sensitivity toward children who suffer deprivation."),
        ("Self-reliance", "We look for the ways a community can design its structures so that children become independent — rather than relying permanently on outside intervention.")]

body = hero("Who we are", "Twenty years of building schools where there were none.",
            "A development agency with 501(c)(3) status in the US and operations across rural Nigeria.",
            "founder.jpg", "Fr. Peter Abue with pupils", h="420", tsize="31")
body += sec(stack([
    '    <div style="background: #fff; border: 1px solid #ece7df; border-radius: 1.2rem; padding: 24px 22px 26px; box-shadow: 0 14px 32px rgba(14,18,24,.05);">\n'
    '      <div style="color: ' + A + '; font-size: 11.5px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 10px;">Our vision</div>\n'
    '      <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 22px; font-weight: 600; line-height: 1.2; letter-spacing: -0.035em;">To impact the lives of children throughout Africa, beginning with Nigeria.</div>\n    </div>\n',
    '    <div style="background: #fff; border: 1px solid #ece7df; border-radius: 1.2rem; padding: 24px 22px 26px; box-shadow: 0 14px 32px rgba(14,18,24,.05);">\n'
    '      <div style="color: ' + A + '; font-size: 11.5px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 10px;">Our mission</div>\n'
    '      <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 22px; font-weight: 600; line-height: 1.2; letter-spacing: -0.035em;">To change the face of education and healthcare for indigent children in Africa, one community at a time.</div>\n    </div>\n'
]), bg="linear-gradient(180deg,#fffdf9 0%,#faf8f4 100%)", pad="32px " + G)
body += sec('    <img src="./corafrica-seal.svg" alt="The CORAfrica seal" style="width: 150px; height: auto; display: block; margin: 0 auto 24px;">\n'
            + kh2("Our logo", "The map, and the light.",
                  "The seal carries the map of Africa and a torch — the Light our programmes are meant to bring. The ring carries our name and our promise: <em>Helping Children and Communities Thrive</em>."),
            bg="linear-gradient(180deg,#faf8f4 0%,#ffffff 100%)")
body += sec(kh2("Our history", "From a doctorate to a network of schools.") + hr, bg="#ffffff", pad="10px " + G + " 44px")
body += sec(kh2("Our philosophy", "Three convictions we build on.",
                "Rooted in Catholic Social Teaching, and reduced to three core values that govern how we choose projects and how we hand them on.")
            + stack([card(t, b) for t, b in vals]),
            bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
write("MobileWhoWeAre.dc.html", body)


# ==================================================== SCHOOLS (table -> cards)
reg = [("John Stilley Secondary School", "Victoria, Ikom", "2021", "300+ students", "Founded where the community had no secondary school at all. A new classroom block has since been added."),
       ("John Bosco Academy", "Adagom, Ogoja", "2020", "Refugee response", "Founded to reach refugee children arriving from Cameroon who could not access basic education."),
       ("St. Peter’s Primary School", "Adagom 3, Ogoja", "2021", "300+ pupils", "A six-classroom block serving children from refugee and host communities who cannot afford fees."),
       ("St. Joseph’s Primary &amp; Secondary", "Idum-Mbube", "—", "2,000+ pupils", "Also an orphanage. Now handed over to be owned and run by the Diocese of Ogoja."),
       ("Little Flower Nursery &amp; Primary", "Ipong-Obudu", "—", "Nursery &amp; primary", "One of the earliest schools initiated across the diocese."),
       ("Thomas McGettrick Institute", "Ogoja Diocese", "—", "Technical", "A technical institute facilitated with the diocesan bishops, and since handed on.")]
rc = ""
for name, place, yr, stat, note in reg:
    rc += ('    <div style="background: #fff; border: 1px solid #ece7df; border-radius: 1.2rem; padding: 20px; box-shadow: 0 14px 32px rgba(14,18,24,.05);">\n'
           '      <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 19px; font-weight: 600; letter-spacing: -0.035em; line-height: 1.2; margin-bottom: 10px;">' + name + "</div>\n"
           '      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 11px;">\n'
           '        <span style="padding: 4px 10px; border-radius: 999px; background: rgba(251,96,10,.10); color: ' + A + '; font-size: 11px; font-weight: 800; letter-spacing: .05em; text-transform: uppercase;">' + stat + "</span>\n"
           '        <span style="padding: 4px 10px; border-radius: 999px; background: #f2efe9; color: #4f4d4b; font-size: 11px; font-weight: 700;">' + place + "</span>\n"
           '        <span style="padding: 4px 10px; border-radius: 999px; background: #f2efe9; color: #78726a; font-size: 11px; font-weight: 700;">' + yr + "</span>\n      </div>\n"
           '      <div style="font-size: 13.5px; line-height: 1.5; color: #4f4d4b;">' + note + "</div>\n    </div>\n")

care = [("Sr. Augustina Abuo Medical Clinic", "Idum-Mbube. The health component of the Mbube Community Education Centre.", "Health"),
        ("CORAfrica Farms", "Demonstration farms feeding the schools and teaching mechanised agriculture and livestock.", "Agriculture"),
        ("ODAIP", "The Ogoja Diocesan Agriculture and Investment Programme, run with the diocese.", "Agriculture"),
        ("St. Thomas Aquinas Programme", "Economic empowerment, launched 2022 with $40,000, commissioned by Bishop Donatus Akpan.", "Livelihoods"),
        ("Holy Family Parish Programme", "Economic empowerment at Ikom, giving parishioners access to enterprise funds.", "Livelihoods"),
        ("Help-a-Kid", "Scholarships for children who cannot afford fees, with materials and uniforms provided.", "Scholarships")]

body = hero("Our schools", "Built where there was nothing.",
            "We found schools where the need is greatest — then hand them over to be owned and run by the local diocese.",
            "school.jpg", "John Stilley Secondary School", h="420", tsize="31")
body += sec(kh2("The register", "Every school CORAfrica has founded or upgraded.",
                "Some are now run by the Diocese of Ogoja. That is the intended end state — a project that cannot be handed on has not really been built.")
            + stack([rc]), bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)")
body += sec(kh2("Also under our care", "Clinics, farms and empowerment programmes.")
            + stack([card(t, b, tag) for t, b, tag in care]),
            bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
write("MobileSchools.dc.html", body)


# ==================================================== DONATE
tiers = [("$25", "a month", "School materials and a uniform for a child through the Help-a-Kid programme."),
         ("$100", "a month", "Contributes to teacher salaries and the running of a classroom."),
         ("$250", "a month", "Supports the clinic — preventive care and treatment for children under five.")]
tc = ""
for amt, per, txt in tiers:
    tc += ('    <div style="background: #fff; border: 1px solid #ece7df; border-radius: 1.2rem; padding: 20px 20px 22px; box-shadow: 0 14px 32px rgba(14,18,24,.05);">\n'
           '      <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">\n'
           '        <span style="font-family: \'Space Grotesk\', sans-serif; font-size: 32px; font-weight: 600; letter-spacing: -0.045em;">' + amt + "</span>\n"
           '        <span style="font-size: 13px; font-weight: 600; color: #78726a;">' + per + "</span>\n      </div>\n"
           '      <div style="font-size: 14px; line-height: 1.5; color: #4f4d4b;">' + txt + "</div>\n    </div>\n")

info = [("Tax-deductible in the US", "CORAfrica has held 501(c)(3) status since 2006. Gifts from US taxpayers are tax-deductible. EIN [REQUEST FROM FR. PETER]."),
        ("Where it goes", "Directly into the schools, clinics, farms and loan funds described on this site. [FINANCIAL BREAKDOWN TO BE SUPPLIED]."),
        ("Other ways to give", "Fund a named project, sponsor a classroom or a VASAC workshop, or partner with us as an institution.")]
ic = ""
for t, b in info:
    ic += ('      <div style="padding: 16px 0; border-top: 1px solid #e3ddd2;">\n'
           '        <div style="font-size: 16px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 6px;">' + t + "</div>\n"
           '        <div style="font-size: 13.5px; line-height: 1.5; color: #4f4d4b;">' + b + "</div>\n      </div>\n")

body = hero("Donate", "&#8358;150,000 started a business. $40,000 started a programme.",
            "Ada Okoli took a &#8358;150,000 soft loan in 2022 and turned a small trade into a wholesale business. Small sums, placed carefully, compound.",
            "hero.jpg", "Pupils at a CORAfrica school", h="470", tsize="30")
body += sec(kh2("Give", "Monthly gifts are what let us plan.",
                "A school year is twelve months long, and so is a teacher’s salary. Recurring gifts are worth more to us than their size suggests, because they are the only kind we can budget on.")
            + stack([tc])
            + '    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 22px;">\n' + fullbtn("Give monthly") + fullbtn("Give once", "plain") + "    </div>\n"
            '    <div style="font-size: 12px; color: #78726a; text-align: center; margin-top: 12px;">Processed securely by Stripe</div>\n',
            bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)")
body += sec('    <div style="border-radius: 1.6rem; background: linear-gradient(180deg,#f1efea 0%,#efede8 100%); box-shadow: 0 20px 48px rgba(14,18,24,.10); padding: 8px 22px 22px;">\n' + ic + "    </div>\n",
            bg="#ffffff", pad="0 " + G + " 44px")
write("MobileDonate.dc.html", body)
