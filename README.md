# CORAfrica — corafrica.org.ng

Static rebuild of the Children of Rural Africa website. Replaces the WordPress 7.1 + GiveWP
site. Built in the same manner as `Teeej Website/` — hand-written HTML and CSS, no framework,
no build toolchain beyond one Python script.

```
site/            ← the deployable. Upload this directory, nothing else.
  *.html            9 pages (generated — see below)
  styles.css        the whole design system
  script.js         mobile nav only; the site works without JS
  img/              logo SVGs + photography
build.py         ← content + page generator. EDIT THIS, not site/*.html
make_preview.py  ← bundles site/ into one self-contained file for client review
brand/           ← logo masters, the tracer, and the original raster source
docs/            ← brief, sourced facts, responsive spec, the ask list for Fr. Peter
design/          ← Claude Design canvas working files
```

## Building

```bash
python3 build.py
```

Regenerates all nine pages into `site/`. **The generated HTML carries a do-not-edit banner** —
the header, footer and `<head>` are defined once in `build.py`, so a nav change is one edit
rather than nine. Content lives in `build.py` too, near the page it belongs to.

`python3 make_preview.py` bundles everything into a single self-contained
`design/corafrica-site-preview.html` for sharing with the client.

## Design system

Lifted from the Teeej stylesheet, which is the look Fr. Peter approved:

| | |
|---|---|
| Display | Space Grotesk 600, `-0.05em` tracking (`-0.04em` on mobile) |
| Body | Manrope, 15–16px / 1.55 |
| Accent | `#fb600a` — sampled from the CORAfrica logo artwork |
| Surfaces | warm gradients, `#ffffff` → `#fffdf9` → `#f5f2ec` |
| Panels | `3rem` radius, `0 34px 76px rgba(14,18,24,.10)` |
| Buttons | `0.7rem` radius, 700 weight, `translateY(-2px)` on hover |

Breakpoints and every layout transform: [`docs/RESPONSIVE-SPEC.md`](docs/RESPONSIVE-SPEC.md).

## 🔴 Donations — read before launching

Retiring WordPress **removes the GiveWP donation form.** The old page offered a grid of monthly
and one-time amounts; only two of those were raw Stripe Payment Links, and both were verified
live on 2026-09-01 by opening them:

| Link | What it actually is |
|---|---|
| `donate.stripe.com/eVq14p1O83Q66iT71Wcwg00` | **Subscribe — $10/month**, fixed |
| `donate.stripe.com/7sYdRbeAUcmCgXx3PKcwg01` | **Subscribe — $25/month**, fixed |

**There is no one-time giving link, and no other amounts.** Everything else on the old page was
rendered by the GiveWP plugin and dies with WordPress.

Before launch, CORAfrica needs to create in Stripe either:
- a Payment Link with **customer-chosen amount** (one-time), plus one for recurring; or
- individual links for each tier they want to offer.

Until then `donate.html` routes the third option to email, and this is marked
`[STRIPE LINK NEEDED]` in `build.py`. **Do not launch with dead donate buttons.**

## Placeholders still in the markup

Written in `[SQUARE BRACKETS]` so they cannot ship unnoticed. Grep for them:

```bash
grep -rn "\[.*REQUEST\|\[.*TO BE\|\[.*NEEDED" site/*.html
```

- **EIN** and **CAC** registration numbers — in every page footer
- **Financial breakdown** — `donate.html`
- **Scope and cost** for the Children's Hospital and VASAC projects — `strategic-plan.html`
- **Further roles** on the administrative team — `contact.html`

Full list of what to request: [`docs/ASK-FR-PETER.md`](docs/ASK-FR-PETER.md) (26 items).

## 🔴 Before this goes live

1. **Confirm the Board of Trustees in writing.** `contact.html` uses the list from Fr. Peter's
   docx, which shares **no names** with the list currently published on corafrica.org.ng.
   Publishing the wrong trustees is the one error here that could genuinely embarrass him.
2. **Create the missing Stripe links** (above).
3. **Fill the EIN and CAC placeholders.**
4. Decide what happens to the existing WordPress content — the two news posts, the GiveWP
   donation records, and the media library. **Nothing should be deleted until Fr. Peter confirms.**
5. Get DNS/host access for corafrica.org.ng.

## Deploying

The site is plain static files — any host works.

**Preview:** `.github/workflows/pages.yml` publishes `site/` to GitHub Pages on every push to
`main`, injecting `noindex` at deploy time so the staging URL cannot be indexed or compete with
corafrica.org.ng. No `CNAME` is committed — adding one would make Pages claim the live domain,
which still serves WordPress. Restore it only once DNS actually points at Pages.

Repo: <https://github.com/EthanSuquet/corafrica-website> (public).

## Photography

The images in `site/img/` were pulled from the existing WordPress media library and are already
twice-compressed. They are adequate for review and weak for launch. A proper photo request is
item 14 in `docs/ASK-FR-PETER.md` — and note the mobile finding: **only two of the six usable
frames survive a mobile hero crop**, so the request must ask for close, centred subjects, not
just landscape wides.

## Content sourcing

Every claim on the site traces to [`docs/CONTENT-FACTS.md`](docs/CONTENT-FACTS.md), which lists
each fact against its source — Fr. Peter's docx, the National Catholic Reporter (2024), Vanguard
and ThisDay (July 2026). That file also records eight conflicts between the docx and the live
site that are still unresolved. Nothing on the site is invented.
