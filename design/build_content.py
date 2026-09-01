#!/usr/bin/env python3
"""Page bodies. Every fact traces to the docx or to CONTENT-FACTS.md."""
from build_pages import *

# ============================================================ WHO WE ARE
hist = [
    ("2006", "Conceived at Cornell",
     "Fr. Peter Obele Abue, completing a PhD in International Development at Cornell University, sets out to close the gap he had watched open between the developed and the developing world."),
    ("2006", "Incorporated in the United States",
     "CORAfrica is granted 501(c)(3) non-profit status, with a founding Board of Trustees of Bruno Schickel, Royal Colle, Thomas Lickona and Carolann Darling. Building begins in Nigeria that same year."),
    ("2009", "Fr. Peter returns to Nigeria",
     "Empowerment programmes and projects follow across the Diocese of Ogoja &mdash; St. Joseph&rsquo;s Primary and Secondary School, the Sr. Augustina Abuo Medical Clinic, Little Flower School at Ipong-Obudu."),
    ("2010s", "A second board, from Western Pennsylvania",
     "Ray Ferguson, Fr. Jim Murphy, Anne Goetler, Tom Rooney, Jeannine Goetz and Ethan Suquet join. With Abode for Children Inc. of Evans City, led by Tom and Mary Rutkoski, they upgrade St. Joseph&rsquo;s Schools and Orphanage and CORAfrica Farms."),
    ("2020", "John Bosco Academy",
     "Founded at Adagom, Ogoja, to reach the influx of refugee children arriving from Cameroon with no access to basic education."),
    ("2021", "The John Stilley Schools",
     "Founded at Victoria, Ikom, where no secondary school existed. St. Peter&rsquo;s Primary is registered at Adagom 3. John Stilley and his family have given time, funds and energy to make these projects last."),
    ("Today", "Two states, and a model that travels",
     "Headquartered in Abuja, CORAfrica works across Cross River and Benue States, reaching rural communities, IDP camps and refugee settlements."),
]
rows = ""
for yr, t, b in hist:
    rows += ('      <div style="display: grid; grid-template-columns: 108px 1fr; gap: 30px; padding: 24px 0; border-top: 1px solid #e8e2d8;">\n'
             '        <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 17px; font-weight: 600; color: {{accent}}; letter-spacing: -0.02em;">' + yr + "</div>\n"
             '        <div><div style="font-size: 19px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 6px;">' + t + "</div>"
             '<div style="font-size: 14.5px; line-height: 1.55; color: #4f4d4b; max-width: 74ch;">' + b + "</div></div>\n"
             "      </div>\n")

vals = [
    ("Dignity of the human person",
     "Each person &mdash; each child &mdash; has an inalienable dignity, and should be treated as an end and never only as a means. Every child deserves the chance to achieve their dreams, no matter where they were born."),
    ("Solidarity and the common good",
     "Faced with globalisation and the growing interdependence of peoples, the universal human family remains one. We are obliged to increase our sensitivity toward children, especially those who suffer deprivation."),
    ("Self-reliance",
     "We look for the explicit ways a community or institution can design its structures so that children and young people become independent &mdash; rather than relying permanently on outside intervention."),
]

body = photo_hero(
    "Who we are", "Twenty years of building schools where there were none.",
    "CORAfrica is a development agency with 501(c)(3) status in the United States and operations across rural Nigeria. We believe a child&rsquo;s education is inseparable from their health, their food and their family&rsquo;s income &mdash; so we build all four.",
    "founder.jpg", "Fr. Peter Abue with pupils")

body += sec(
    '      <div style="display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 20px;">\n'
    '        <div style="background: #ffffff; border: 1px solid #ece7df; border-radius: 1.6rem; padding: 34px 34px 36px; box-shadow: 0 18px 44px rgba(14,18,24,.06);">\n'
    '          <div style="margin: 0 0 .9rem; color: {{accent}}; font-size: 0.88rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase;">Our vision</div>\n'
    '          <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.04em;">To impact the lives of children throughout Africa, beginning with Nigeria.</div>\n'
    "        </div>\n"
    '        <div style="background: #ffffff; border: 1px solid #ece7df; border-radius: 1.6rem; padding: 34px 34px 36px; box-shadow: 0 18px 44px rgba(14,18,24,.06);">\n'
    '          <div style="margin: 0 0 .9rem; color: {{accent}}; font-size: 0.88rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase;">Our mission</div>\n'
    '          <div style="font-family: \'Space Grotesk\', sans-serif; font-size: 28px; font-weight: 600; line-height: 1.16; letter-spacing: -0.04em;">To change the face of education and healthcare for indigent children in Africa, one community at a time.</div>\n'
    "        </div>\n"
    "      </div>\n", pad="60px 40px")

body += sec(
    '      <div style="display: grid; grid-template-columns: 260px 1fr; gap: 4.5rem; align-items: center;">\n'
    '        <img src="./corafrica-seal.svg" alt="The CORAfrica seal" style="width: 230px; height: auto; display: block; margin: 0 auto;">\n'
    "        <div>\n"
    + kicker_h2("Our logo", "The map, and the light.",
                "The seal carries the map of Africa and a torch. The torch stands for the Light our programmes are meant to bring &mdash; the conviction that education is what changes a continent&rsquo;s prospects, one community at a time. The ring around it carries our name and our promise: <em>Helping Children and Communities Thrive</em>.")
    + "        </div>\n      </div>\n",
    bg="linear-gradient(180deg,#faf8f4 0%,#ffffff 100%)")

body += sec(kicker_h2("Our history", "From a doctorate to a network of schools.") + rows,
            bg="#ffffff", pad="20px 40px 76px")

body += sec(
    kicker_h2("Our philosophy", "Three convictions we build on.",
              "CORAfrica&rsquo;s philosophy is rooted in Catholic Social Teaching, and reduces to three core values that govern how we choose projects and how we hand them on.")
    + grid([card(t, b) for t, b in vals], cols=3),
    bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")

write("WhoWeAre.dc.html", "Who We Are", body)


# ============================================================ OUR MODEL
comp = [
    ("Education", "hands.jpg", "01",
     "Primary and secondary schools, built where children have no educational opportunity at all, and educational amenities supplied where schools exist but lack them. Small classes, high-quality instruction, and a holistic education that grows a child academically, personally and spiritually."),
    ("Healthcare", "clinic.jpg", "02",
     "A clinic inside the school system, so a child&rsquo;s health is not a reason to miss class. Particular emphasis on diarrhoeal disease and malaria in the under-fives, and heavy investment in the first 1,000 days of life &mdash; the window that sets brain development, growth and immune strength."),
    ("Agriculture", "farm.jpg", "03",
     "Agricultural centres and school farms where children learn agriculture with their hands, not from a textbook. The farm feeds the school, and the skill outlasts the schooling."),
    ("Economic empowerment", "empower.jpg", "04",
     "Where a family cannot afford to keep a child in class, the barrier is income. Soft loans let poor parents start small businesses and farms. More than 500 women have been supported this way."),
]
blocks = ""
for i, (name, img, num, txt) in enumerate(comp):
    img_col = ('        <div style="border-radius: 1.6rem; overflow: hidden; box-shadow: 0 26px 70px rgba(12,18,28,.12); background: #efebe6;">\n'
               '          <img src="./' + img + '" alt="' + name + '" style="width: 100%; height: 320px; object-fit: cover; display: block;">\n        </div>\n')
    txt_col = ('        <div>\n'
               '          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 14px;">\n'
               '            <span style="font-family: \'Space Grotesk\', sans-serif; font-size: 15px; font-weight: 600; color: {{accent}};">' + num + "</span>\n"
               '            <span style="width: 26px; height: 2px; background: {{accent}}; display: block;"></span>\n          </div>\n'
               '          <h3 style="margin: 0 0 12px; font-family: \'Space Grotesk\', sans-serif; font-size: 34px; font-weight: 600; line-height: 1.06; letter-spacing: -0.045em;">' + name + "</h3>\n"
               '          <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #4f4d4b;">' + txt + "</p>\n        </div>\n")
    order = (img_col + txt_col) if i % 2 == 0 else (txt_col + img_col)
    blocks += ('      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4.5rem; align-items: center; padding: 34px 0; border-top: 1px solid #e8e2d8;">\n'
               + order + "      </div>\n")

body = photo_hero("Our model", "Four components. One site. One system.",
                  "The Community Education Centre is our answer to a hard lesson: a school on its own does not keep a child in school. Hunger, illness and a family without income take more children out of class than any exam does.",
                  "farm.jpg", "A CORAfrica demonstration farm")
body += sec(kicker_h2("The Community Education Centre", "Built from what actually keeps children out of class.",
                      "Each CEC combines a primary and secondary school, a medical clinic with a running water system, an agricultural demonstration farm, and a vocational and skills acquisition centre. Children learn from the school and the community at once, with hands-on experience in each.")
            + blocks, bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)")
body += sec(
    kicker_h2("Where we operate", "Two centres running, and a model designed to travel.",
              "Our two Community Education Centres are at Mbube-Ogoja and Victoria-Ikom. We are seeking funding to equip and operate both to their full plan. Our wider work reaches rural communities, IDP camps and refugee settlements across Cross River and Benue States.")
    + grid([
        card("Mbube-Ogoja", "Home of St. Joseph&rsquo;s Primary and Secondary School and the Sr. Augustina Abuo Medical Clinic.", "Centre one"),
        card("Victoria-Ikom", "Home of the John Stilley Schools, founded where the community had no secondary school at all.", "Centre two"),
        card("Adagom, Ogoja", "John Bosco Academy and St. Peter&rsquo;s Primary, serving refugee and host communities together.", "Refugee response"),
    ], cols=3), bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
write("OurModel.dc.html", "Our Model", body)


# ============================================================ WHAT WE DO
vasac = [
    ("Computer studies", "Functional computer laboratories with stable connectivity, reliable power with backup, trained ICT staff and proper security."),
    ("Fashion design", "Sewing, pattern drafting and fabric selection &mdash; creativity and entrepreneurship, with income from garment production."),
    ("Beauty &amp; aesthetics", "Hairdressing, make-up artistry and skincare, with the customer-service grounding that makes self-employment viable."),
    ("Home economics", "Cooking, nutrition, budgeting, childcare and household management &mdash; supporting healthy living and catering businesses."),
    ("Music", "Performance, production and teaching. Discipline, confidence and teamwork, with a route into content creation."),
    ("Technical drawing", "Precise drawing for engineering and architecture &mdash; critical thinking, and the foundation for every technical trade."),
    ("Visual arts", "Creativity, innovation and communication, with income from art sales and design services across the creative industries."),
    ("Building trades", "Masonry, blocklaying and concreting, carpentry and joinery, furniture and upholstery, plumbing, tiling, painting and interior finishing, aluminium work, and solar PV installation and maintenance."),
    ("Agriculture", "Mechanised agriculture and operations, and livestock farming &mdash; beekeeping, poultry and animal husbandry."),
]
rights = [
    "Every child has the right to a standard of living adequate for their health and well-being.",
    "Every child has the right to learn how to work, to free choice of employment, to just and favourable conditions of work, and to protection against unemployment.",
    "Everyone, without discrimination, has the right to equal pay for equal work.",
    "Everyone who works has the right to remuneration that ensures an existence worthy of human dignity for themselves and their family.",
]
rl = ""
for r in rights:
    rl += ('        <div style="display: grid; grid-template-columns: 22px 1fr; gap: 14px; padding: 15px 0; border-top: 1px solid rgba(255,255,255,.14);">\n'
           '          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="{{accent}}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"></path></svg>\n'
           '          <div style="font-size: 15px; line-height: 1.5; color: rgba(255,255,255,.86);">' + r + "</div>\n        </div>\n")

body = photo_hero("What we do", "Education is the bedrock. Everything else is built on it.",
                  "Getting a good education as a child is the essential building block of a tolerant, well-adjusted, healthy and prosperous adult. Families where parents completed primary and secondary school have higher incomes, better health and longer lives &mdash; and pass all of it on.",
                  "hands.jpg", "Children at a CORAfrica school")

body += sec(kicker_h2("Education", "A high-quality education is an inherent right of every child.",
                      "We build and equip primary and secondary schools in rural areas, creating sustainable livelihoods for indigent children and preventing the poverty, abuse and exploitation that follow when a child is out of school. Our schools keep classes small, instruction high, and the atmosphere curious.")
            + grid([
                card("Primary and secondary", "Conventional schooling, run properly &mdash; small classes, quality instruction, and preparation for an increasingly globalised world."),
                card("Holistic by design", "Children are encouraged to grow academically, personally and spiritually, in an environment of curiosity, creativity and enthusiasm."),
                card("Tertiary and vocational", "Our educational component runs from primary through secondary to tertiary support and vocational skills acquisition."),
            ], cols=3), bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)")

body += sec(kicker_h2("VASAC", "Vocational and Skills Acquisition Centres.",
                      "We go a step beyond the conventional school system and equip our schools so students leave with a trade. Each centre runs pilot systems where students practise the skills that will sustain them for life &mdash; actively involved, hands-on, in every area below.")
            + grid([card(t, b) for t, b in vasac], cols=3)
            + '      <div style="display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 18px; margin-top: 18px;">\n'
            + card("Staffing", "Reputable staff recruited from known institutions, with experts drawn from local artisans known to us over many years &mdash; administrative staff, professional teachers and skilled labourers.")
            + card("Equipment and certification", "Every department furnished and equipped to match its training. Partnerships with donors and bilateral organisations are intended to carry students through to certification and job placement.")
            + "      </div>\n",
            bg="linear-gradient(180deg,#ffffff 0%,#faf8f4 100%)")

body += sec(kicker_h2("Healthcare", "A child too ill to learn is not being educated.",
                      "We establish health clinics inside the school system to address children&rsquo;s health where they already are, and we teach healthcare awareness and sanitation as part of school life. We place particular emphasis on preventing and treating diarrhoeal disease and malaria in children under five, and on the first 1,000 days of life &mdash; the period that determines future brain activity, growth, resilience and immune strength. Our investment extends to the health of their mothers.")
            + grid([
                card("Preventive first", "Preventive care, combating malnutrition, and community education on preventing the transmission of HIV."),
                card("Community health workers", "A growing team providing health education and accompanying families through the process of seeking care."),
                card("Water and sanitation", "Practical hand-washing hygiene, toilets, and water collection and treatment &mdash; taught in school, extended into the community and to refugee settlements."),
            ], cols=3), bg="#ffffff")

body += ('\n  <div style="padding: 0 40px 56px; background: linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%);">\n'
         '    <div style="max-width: 1360px; margin: 0 auto; border-radius: 3rem; background: #2c2a2a; box-shadow: 0 34px 76px rgba(14,18,24,.18); padding: 50px 56px 46px;">\n'
         '      <div style="margin: 0 0 .9rem; color: rgba(255,255,255,.62); font-size: 0.88rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase;">What we believe</div>\n'
         '      <h2 style="margin: 0 0 1.6rem; font-family: \'Space Grotesk\', sans-serif; font-size: 38px; font-weight: 600; line-height: 1.06; letter-spacing: -0.05em; color: #fff; max-width: 26ch;">In CORAfrica, we hold that:</h2>\n'
         + rl + "    </div>\n  </div>\n")
write("WhatWeDo.dc.html", "What We Do", body)


# ============================================================ SCHOOLS
schools = [
    ("John Stilley Secondary School", "Victoria, Ikom", "2021", "300+ students", "Founded where the community had no secondary school at all. A new classroom block has since been added, supported by the John Stilley Family Trust Fund."),
    ("John Bosco Academy", "Adagom, Ogoja", "2020", "Refugee response", "Founded to reach the high influx of refugee children arriving from Cameroon who could not access basic and quality education. Formerly St. Peter&rsquo;s Catholic School."),
    ("St. Peter&rsquo;s Primary School", "Adagom 3, Ogoja", "2021", "300+ pupils", "Registered with the education authorities in June 2021. A six-classroom block serves children from both refugee and host communities who cannot afford school fees."),
    ("St. Joseph&rsquo;s Primary &amp; Secondary", "Idum-Mbube, Ogoja", "&mdash;", "2,000+ pupils", "Also an orphanage, caring for children from five years and above. Now handed over to be owned and run by the Diocese of Ogoja &mdash; as our projects are designed to be."),
    ("Little Flower Nursery &amp; Primary", "Ipong-Obudu", "&mdash;", "Nursery &amp; primary", "One of the earliest schools initiated across the diocese, and part of the network that established the model we now build to."),
    ("Thomas McGettrick Institute of Technology", "Ogoja Diocese", "&mdash;", "Technical", "A technical institute among the projects facilitated in collaboration with the diocesan bishops, and since handed on."),
]
srows = ""
for name, place, yr, stat, note in schools:
    srows += ('      <div style="display: grid; grid-template-columns: 1fr 210px 130px 150px; gap: 26px; align-items: start; padding: 26px 0; border-top: 1px solid #e8e2d8;">\n'
              '        <div><div style="font-family: \'Space Grotesk\', sans-serif; font-size: 22px; font-weight: 600; letter-spacing: -0.035em; margin-bottom: 7px;">' + name + "</div>"
              '<div style="font-size: 14px; line-height: 1.5; color: #4f4d4b; max-width: 62ch;">' + note + "</div></div>\n"
              '        <div style="font-size: 14.5px; color: #4f4d4b; padding-top: 5px;">' + place + "</div>\n"
              '        <div style="font-size: 14.5px; color: #78726a; padding-top: 5px;">' + yr + "</div>\n"
              '        <div style="font-size: 14px; font-weight: 700; color: {{accent}}; text-align: right; padding-top: 5px;">' + stat + "</div>\n      </div>\n")

body = photo_hero("Our schools", "Built where there was nothing.",
                  "We found schools where the need is greatest &mdash; and then hand them over to be owned and run by the local diocese. The work is built to outlast whoever started it.",
                  "school.jpg", "John Stilley Secondary School")
body += sec(kicker_h2("The register", "Every school CORAfrica has founded or upgraded.",
                      "Some of these are now run by the Diocese of Ogoja. That is the intended end state, not a loss &mdash; a project that cannot be handed on has not really been built.")
            + '      <div style="display: grid; grid-template-columns: 1fr 210px 130px 150px; gap: 26px; padding-bottom: 10px; font-size: 11.5px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: #a09889;">\n'
            + '        <div>School</div><div>Location</div><div>Founded</div><div style="text-align: right;">Scale</div>\n      </div>\n'
            + srows, bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)")
body += sec(kicker_h2("Also under our care", "Clinics, farms and empowerment programmes.")
            + grid([
                card("Sr. Augustina Abuo Medical Clinic", "Idum-Mbube. The health component of the Mbube Community Education Centre.", "Health"),
                card("CORAfrica Farms", "Demonstration farms feeding the schools and teaching mechanised agriculture and livestock.", "Agriculture"),
                card("ODAIP", "The Ogoja Diocesan Agriculture and Investment Programme, run in collaboration with the diocese.", "Agriculture"),
                card("St. Thomas Aquinas Programme", "Economic empowerment, launched in 2022 with $40,000 and commissioned by Bishop Donatus Akpan.", "Livelihoods"),
                card("Holy Family Parish Programme", "Economic empowerment at Ikom, giving parishioners access to funds for small and larger enterprises.", "Livelihoods"),
                card("Help-a-Kid", "Scholarships for children who cannot afford fees, with educational materials and school uniforms provided.", "Scholarships"),
            ], cols=3), bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
write("Schools.dc.html", "Schools", body)


# ============================================================ STRATEGIC PLAN
body = photo_hero("Our strategic plan", "What we are building next.",
                  "Our plan concerns the development of children in rural Nigeria, and the operational capacity and administration to deliver it &mdash; all within the setting of the Community Education Centre model.",
                  "empower.jpg", "The economic empowerment programme")
body += sec(kicker_h2("The method", "Study teams, not just classes.",
                      "Through our Vocational and Skills Acquisition Centres, pilot systems are operated in which children and young people form study teams together with parents, teachers and community members. The point is that a skill practised alongside the adults who will employ or finance it is a skill that survives leaving school.")
            + grid([
                card("Community Education Centre model", "Extending the four-component centre to further communities, and fully equipping the two that already run at Mbube-Ogoja and Victoria-Ikom.", "Programme in view"),
                card("The Children&rsquo;s Hospital Project", "A dedicated children&rsquo;s hospital, extending the school-clinic model into full paediatric care. [SCOPE AND COST TO BE CONFIRMED]", "Programme in view"),
                card("The VASAC Project", "Purpose-built vocational and skills acquisition centres, equipped across all nine trade areas, with certification and job placement partnerships. [SCOPE AND COST TO BE CONFIRMED]", "Programme in view"),
            ], cols=3), bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)")
body += sec(kicker_h2("Alignment", "Where our work meets the global agenda.",
                      "CORAfrica&rsquo;s programmes are aligned to five United Nations Sustainable Development Goals. Our livelihood strategy seeks to improve access to food, healthcare, education, clean water and skills development for vulnerable households, with particular emphasis on rural women.")
            + grid([
                card("No poverty", "Reducing poverty through education, and through soft loans that let a family build an income."),
                card("Zero hunger", "Food security through demonstration farms and school feeding."),
                card("Gender equality", "Increasing rural women&rsquo;s access to livelihood opportunities, agricultural resources and women-led enterprise."),
                card("Decent work", "Vocational and skills training that leads to sustainable, dignified livelihoods."),
                card("Reduced inequality", "Reaching refugee, IDP and host communities together, without distinction."),
                card("Partnerships", "Working with communities, dioceses, institutions and bilateral organisations rather than around them."),
            ], cols=3), bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
write("StrategicPlan.dc.html", "Strategic Plan", body)


# ============================================================ NEWS
press = [
    ("National Catholic Reporter", "10 May 2024", "Catholic-run CORAfrica aims to fill learning gap fueled by poverty in Nigeria",
     "Valentine Benjamin reports from Ogoja on the schools, the empowerment programme and the families behind the numbers.", True),
    ("Vanguard", "28 July 2026", "CORAfrica expands community development through education, healthcare, livelihood programmes",
     "A full account of the Community Education Centre model, our partners, and our alignment to the UN Sustainable Development Goals.", True),
    ("ThisDay", "30 July 2026", "CORAfrica expands access to education for children in rural communities",
     "On the new classroom block at John Stilley Secondary School and the six-classroom block at St. Peter&rsquo;s, Adagom 3.", True),
    ("CrossRiverWatch", "September 2015", "Community Champion: how a Catholic priest is empowering orphans in Cross River State",
     "An early profile of Fr. Peter Abue and the founding work of CORAfrica.", False),
    ("CrossRiverWatch", "November 2014", "US Country Representative of Children of Rural Africa rounds off visit to Cross River",
     "Coverage of the American board&rsquo;s visit to the projects in Cross River State.", False),
]
items = ""
for outlet, date, title, blurb, feat in press:
    items += ('      <div style="display: grid; grid-template-columns: 240px 1fr 150px; gap: 30px; align-items: start; padding: 28px 0; border-top: 1px solid #e8e2d8;">\n'
              '        <div><div style="font-size: 13px; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: #181818;">' + outlet + "</div>"
              '<div style="font-size: 12.5px; color: #a09889; margin-top: 5px;">' + date + "</div></div>\n"
              '        <div><div style="font-family: \'Space Grotesk\', sans-serif; font-size: 21px; font-weight: 600; letter-spacing: -0.035em; line-height: 1.2; margin-bottom: 7px;">' + title + "</div>"
              '<div style="font-size: 14px; line-height: 1.5; color: #4f4d4b; max-width: 70ch;">' + blurb + "</div></div>\n"
              '        <div style="font-size: 14px; font-weight: 700; color: {{accent}}; text-align: right; padding-top: 3px;">Read &rarr;</div>\n      </div>\n')

body = light_hero("In the news", "CORAfrica, reported independently.",
                  "Our work has been covered by the National Catholic Reporter and by two of Nigeria&rsquo;s largest national dailies. Where we make a claim on this site, these are the places you can check it.")
body += sec(items, bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)", pad="10px 40px 70px")
body += sec(kicker_h2("Press enquiries", "For interviews, images or further information.",
                      "Contact our office in Ogoja and we will put you in touch with Fr. Peter Abue or the relevant programme lead.")
            + '      <div style="display: flex; gap: 12px;">' + btn("info@corafrica.org.ng") + btn("+234 915 314 2288", "plain") + "</div>\n",
            bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
write("News.dc.html", "News", body)


# ============================================================ DONATE
tiers = [
    ("$25", "a month", "School materials and a uniform for a child through the Help-a-Kid programme."),
    ("$100", "a month", "Contributes to teacher salaries and the running of a classroom."),
    ("$250", "a month", "Supports the clinic &mdash; preventive care and treatment for children under five."),
]
tc = ""
for amt, per, txt in tiers:
    tc += ('      <div style="background: #ffffff; border: 1px solid #ece7df; border-radius: 1.6rem; padding: 28px 28px 30px; display: flex; flex-direction: column; gap: 10px; box-shadow: 0 18px 44px rgba(14,18,24,.06);">\n'
           '        <div style="display: flex; align-items: baseline; gap: 7px;">\n'
           '          <span style="font-family: \'Space Grotesk\', sans-serif; font-size: 40px; font-weight: 600; letter-spacing: -0.05em;">' + amt + "</span>\n"
           '          <span style="font-size: 14px; font-weight: 600; color: #78726a;">' + per + "</span>\n        </div>\n"
           '        <div style="font-size: 14.5px; line-height: 1.5; color: #4f4d4b;">' + txt + "</div>\n      </div>\n")

body = photo_hero("Donate", "&#8358;150,000 started a business. $40,000 started a programme.",
                  "Ada Okoli took a &#8358;150,000 soft loan in 2022 and turned a small trade into a wholesale and retail business. The St. Thomas Aquinas empowerment programme launched with $40,000 and has since supported more than 500 women. Small sums, placed carefully, compound.",
                  "hero.jpg", "Pupils at a CORAfrica school")

body += sec(kicker_h2("Give", "Monthly gifts are what let us plan.",
                      "A school year is twelve months long, and so is a teacher&rsquo;s salary. Recurring gifts are worth far more to us than their size suggests, because they are the only kind we can build a budget on.")
            + '      <div style="display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 18px;">\n' + tc + "      </div>\n"
            + '      <div style="display: flex; gap: 12px; margin-top: 34px; align-items: center;">' + btn("Give monthly") + btn("Give once", "plain")
            + '<span style="font-size: 13px; color: #78726a; margin-left: 8px;">Processed securely by Stripe</span></div>\n',
            bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)")

body += ('\n  <div style="padding: 0 40px 46px; background: #ffffff;">\n'
         '    <div style="max-width: 1360px; margin: 0 auto; border-radius: 3rem; background: linear-gradient(180deg,#f1efea 0%,#efede8 100%); box-shadow: 0 34px 76px rgba(14,18,24,.10); padding: 44px 48px 46px;">\n'
         '      <div style="display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 40px;">\n'
         '        <div><div style="font-size: 17px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 8px;">Tax-deductible in the US</div>\n'
         '        <div style="font-size: 14px; line-height: 1.55; color: #4f4d4b;">CORAfrica has held 501(c)(3) status in the United States since 2006. Gifts from US taxpayers are tax-deductible. EIN [REQUEST FROM FR. PETER].</div></div>\n'
         '        <div><div style="font-size: 17px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 8px;">Where it goes</div>\n'
         '        <div style="font-size: 14px; line-height: 1.55; color: #4f4d4b;">Directly into the schools, clinics, farms and loan funds described on this site &mdash; and into projects designed to be handed over to the communities that run them. [FINANCIAL BREAKDOWN TO BE SUPPLIED].</div></div>\n'
         '        <div><div style="font-size: 17px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 8px;">Other ways to give</div>\n'
         '        <div style="font-size: 14px; line-height: 1.55; color: #4f4d4b;">Fund a named project, sponsor a classroom or a VASAC workshop, or partner with us as an institution. Write to info@corafrica.org.ng.</div></div>\n'
         "      </div>\n    </div>\n  </div>\n")
write("Donate.dc.html", None, body)


# ============================================================ CONTACT
trustees = [("Michael Ana", "Chairman"), ("Cornelius Okochi", "Vice Chairman"), ("Mark Okpatuma", "Member"),
            ("Michael Abuo", "Member"), ("Pamela Enamhe", "Member"), ("James Bulem", "Member"),
            ("Adewale Ajayi", "Member / Secretary")]
admin = [("Adewale Ajayi", "National Programmes Coordinator"), ("Elijah Ugani", "Projects Manager")]


def person(name, role):
    return ('      <div style="background: #ffffff; border: 1px solid #ece7df; border-radius: 1.4rem; padding: 22px 24px 24px; box-shadow: 0 18px 44px rgba(14,18,24,.05);">\n'
            '        <div style="font-size: 17px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 5px;">' + name + "</div>\n"
            '        <div style="font-size: 13.5px; color: {{accent}}; font-weight: 600;">' + role + "</div>\n      </div>\n")


body = light_hero("Contact us", "Talk to the people running the work.",
                  "Our operations are directed from Ogoja, in Cross River State, and overseen by our Board of Trustees. For partnership, grant or press enquiries, write to us and we will route you to the right person.")
body += sec(kicker_h2("Board of Trustees", "Governance.")
            + grid([person(n, r) for n, r in trustees], cols=4, gap="16px"),
            bg="linear-gradient(180deg,#fffdf9 0%,#ffffff 100%)", pad="10px 40px 60px")
body += sec(kicker_h2("Administrative team", "Delivery.")
            + grid([person(n, r) for n, r in admin] + [person("[FURTHER ROLES]", "To be confirmed")], cols=4, gap="16px"),
            bg="#ffffff", pad="0 40px 70px")
body += sec(kicker_h2("Offices", "Where to find us.")
            + grid([
                card("Nigeria &mdash; operations", "No 48 Mbube Road, Opposite Govt. Technical College, Abakpa, Ogoja, Cross River State."),
                card("Nigeria &mdash; headquarters", "Abuja. Our national office directs programmes across Cross River and Benue States."),
                card("United States", "PO Box 13, Evans City, PA 16033. Our 501(c)(3) entity and US board."),
            ], cols=3)
            + '      <div style="display: flex; gap: 12px; margin-top: 30px;">' + btn("info@corafrica.org.ng") + btn("+234 915 314 2288", "plain") + "</div>\n",
            bg="linear-gradient(180deg,#ffffff 0%,#f5f2ec 100%)")
write("Contact.dc.html", "Contact", body)
