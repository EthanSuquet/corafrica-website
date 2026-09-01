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

## Donations — one gap before launching

The full monthly ladder carried over. Seven Stripe Payment Links, recovered from the live
donate page's markup and each one **opened to confirm the amount matches the label**:

| Amount | Link |
|---|---|
| $10 / month | `donate.stripe.com/eVq14p1O83Q66iT71Wcwg00` |
| $25 / month | `donate.stripe.com/7sYdRbeAUcmCgXx3PKcwg01` |
| $50 / month | `donate.stripe.com/dRmbJ39gA86m22D0Dycwg02` |
| $100 / month | `donate.stripe.com/8x29AV9gAbiy5eP71Wcwg03` |
| $250 / month | `donate.stripe.com/fZu4gB1O8dqG22DgCwcwg04` |
| $500 / month | `donate.stripe.com/7sY14pakE4Ua4aLbiccwg05` |
| $1,000 / month | `donate.stripe.com/8x26oJfEY72i36Hcmgcwg06` |

🔴 **One-time giving does not carry over.** On the old site it is a GiveWP embed
(`form-id=2804`), not a Stripe link — it is rendered by the WordPress plugin and dies with it.
CORAfrica needs **one new Stripe Payment Link with a customer-chosen amount**. Until then
`donate.html` says plainly that one-time gifts are being set up and routes to email; it does not
show a dead button.

Per-tier impact copy is deliberately absent. Tying an amount to a concrete outcome lifts giving
substantially, but the figures have to be real — so the page carries
`[WHAT EACH TIER FUNDS — TO BE CONFIRMED]` rather than numbers we invented.

## Placeholders still in the markup

Written in `[SQUARE BRACKETS]` so they cannot ship unnoticed. Grep for them:

```bash
grep -rn "\[.*REQUEST\|\[.*TO BE\|\[.*NEEDED" site/*.html
```

- **EIN** — in every page footer, and on the Donate and Who We Are pages. The *only* registration
  number still missing; the Nigerian CAC number is now filled in from the audited accounts.
- **Scope and cost** for the Children's Hospital and VASAC projects — `strategic-plan.html`.
  The other two named projects (Adagom, and John Bosco University) are now fully costed.
- **Further roles** on the administrative team — `contact.html`

Full list of what to request: [`docs/ASK-FR-PETER.md`](docs/ASK-FR-PETER.md) (39 items).

## 🔴 Before this goes live

1. **Confirm the Board of Trustees in writing.** `contact.html` uses the list from Fr. Peter's
   docx — the newest source, supplied 2026-08-31, and therefore the one the site follows. But it
   shares **no names** with the list currently published on corafrica.org.ng, and the audited 2025
   accounts name a third set again (stated as at 31 Dec 2025, so an earlier snapshot). One
   sentence in writing settles it.
2. **Create the missing Stripe links** (above).
3. **Fill the EIN placeholder** — the CAC number is now known.
3b. **Get his permission to publish the 2025 financial figures.** They are on the site now
   because they are the strongest asset we have for the grant audience, but they are his accounts.
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
and ThisDay (July 2026), plus four documents supplied on 2026-09-01: the **audited 2025 financial
report**, the **Adagom academic building proposal**, the **Mission Showcase one-pager** and the
**SENT video script**. That file also records fourteen conflicts between sources. Nothing on the
site is invented.

⚠️ **Two rules that file exists to enforce.** First, **the docx is the newest source** — Fr. Peter
supplied it on 2026-08-31 — so on governance it beats the audited accounts, which state their board
as at 31 Dec 2025. The audit looks more authoritative and is older; do not let it overwrite the
board again. Second, the audited accounts attribute essentially all 2025 income to a single donor.
That is recorded in the facts file and **deliberately kept off the site**.
