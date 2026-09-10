# CORAfrica — corafrica.org.ng

Static rebuild of the Children of Rural Africa website. Replaces the WordPress 7.1 + GiveWP
site. Built in the same manner as `Teeej Website/` — hand-written HTML and CSS, no framework,
no build toolchain beyond one Python script.

```
site/            ← the deployable. Upload this directory, nothing else.
  *.html            9 pages (generated — see below)
  styles.css        the whole design system
  script.js         mobile nav and scroll reveals; the site works without JS
  img/              logo SVGs, photography, team/ headshots
build.py         ← content + page generator. EDIT THIS, not site/*.html
make_preview.py  ← bundles site/ into one self-contained file for client review
brand/           ← logo masters, the tracer, and the original raster source
docs/            ← brief and responsive spec; the sourced facts and ask list are local only (see Privacy)
design/          ← Claude Design canvas working files
photos/source/   ← raw photo downloads (gitignored)
```

## Building

```bash
python3 build.py
```

Regenerates all nine pages into `site/` — Home, Who We Are, Our Model, What We Do, Track Record,
Strategic Plan, News, Donate, Contact. **The generated HTML carries a do-not-edit banner** — the
header, footer and `<head>` are defined once in `build.py`, so a nav change is one edit rather
than nine. Content lives in `build.py` too, near the page it belongs to.

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

## Donations

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
(`form-id=2804`), rendered by the WordPress plugin, and it dies with it. A single new **Stripe
Payment Link with a customer-chosen amount** would cover it — Stripe supports that directly — and
Fr. Peter wants to settle it on a call with Ethan and Jeannine. Until then `donate.html` offers
cheques by post to the US office, and never shows a dead button.

**No per-tier impact copy, by instruction.** Fr. Peter (2026-09-04): every gift goes into one
general fund, so the site does not say what a given dollar buys. A per-project giving page is
planned for later. Every figure on the site is in **US dollars**.

## Placeholders still in the markup

Written in `[SQUARE BRACKETS]` so they cannot ship unnoticed. Grep for them:

```bash
grep -rn "TO BE SUPPLIED\|\[.*NEEDED" site/*.html
```

- **Email and phone** — the old ones are dead. Every footer, plus News, Donate and Contact. Set
  `CONTACT_EMAIL` and `CONTACT_PHONE` at the top of `build.py` and they appear everywhere.

The full list of what is still open with Fr. Peter is `docs/ASK-FR-PETER.md` (local only).

## 🔴 Before this goes live

1. **The new email address and phone number** (above).
2. **The one-time Stripe link** (above).
3. **Jeannine confirms the EIN** (68-0619454, which matches the public IRS record) **and the cheque
   payee and US address** on the Donate page.
4. **Names for the fifteen headshots**, and **the logo as a vector file** — the header and footer
   lockups still carry the old ring text, *Helping Children and Communities Thrive*.
5. **WordPress comes down**; its GiveWP donation records and media library pass to the new site
   (Fr. Peter, 2026-09-04). Export both before anything is switched off.
6. **DNS.** Ethan is the sole controller of the domain (Fr. Peter, 2026-09-04). Point
   corafrica.org.ng at the host, then restore a `CNAME`.

## Deploying

The site is plain static files — any host works.

**Preview:** `.github/workflows/pages.yml` publishes `site/` to GitHub Pages on every push to
`main`, injecting `noindex` at deploy time so the staging URL cannot be indexed or compete with
corafrica.org.ng. No `CNAME` is committed — adding one would make Pages claim the live domain,
which still serves WordPress. Restore it only once DNS actually points at Pages.

Repo: <https://github.com/EthanSuquet/corafrica-website> (public).

## Privacy

⛔ **This repository is public.** `docs/CONTENT-FACTS.md`, `docs/ASK-FR-PETER.md` and
`docs/source/` are gitignored and exist only on Ethan's machine: they quote Fr. Peter's private
answers and details from the audited accounts that he asked never to be published. Never
force-add them, and keep a private backup — git is not backing them up. The history was rewritten
on 2026-09-10 to remove an earlier commit that included them.

## Photography

Most photos now come from Fr. Peter's own set (WhatsApp, 2026-09-06). The originals are in
`photos/source/whatsapp-2026-09/` (gitignored), cropped to 900 × 675 for cards and 1400 × 560 for
heroes in `site/img/`. They are WhatsApp-compressed, at most 1280px wide: fine for cards and
borderline for a full-width hero, so ask for originals of any that become permanent. A few older
images from the WordPress library remain (`hero`, `hands`, `clinic`, `farm`, `empower`, `school`).

Headshots live in `site/img/team/` and are wired by name in `HEADSHOTS` in `build.py`; anyone
without one shows their initials. **Only add a headshot once you are certain who is in it.**

## Content sourcing

Every claim on the site traces to `docs/CONTENT-FACTS.md` (local only), which lists each fact
against its source: Fr. Peter's docx and his written answers of 2026-09-04, the Strategic Plan
2026–2030, the audited 2025 accounts, the 2023 Organizational Profile, and press from
CrossRiverWatch (2014) to Vanguard and ThisDay (2026). Nothing on the site is invented.

⚠️ **The rules that file exists to enforce.**

1. **Rank sources by the date they were written, not the date they were sent.** Fr. Peter's
   written answers are the newest authority. The 70-page Organizational Profile he sent on
   2026-09-06 was written c. 2022–23, so it is used for the track record and nothing else.
2. **Past projects stay past.** The schools and clinics now run by the St. Francis Humanitarian
   Mission appear only on Track Record, never as run by CORAfrica today.
3. **Two programmes, not four pillars** — Education and Healthcare, with Agriculture and Economic
   Empowerment built into the school.
4. **Fr. Peter is shown as Founder and kept low-profile**, at his request.
5. **Nothing about where the money came from.** The site names no donor and says nothing about how
   concentrated income is, at Fr. Peter's explicit request.
