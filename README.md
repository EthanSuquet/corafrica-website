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
brand/           ← logo masters, the seal rebuild script, the tracer, and the raster sources
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

## Logo

The current seal (*Children of Rural Africa* above, *Education for Africa's Future* below, the map of
Africa with an open book and a torch) arrived from Fr. Peter only as a 400 × 400 JPEG, on 2026-09-04
(`brand/source/corafrica-seal-2026-09-04.jpeg`). It was rebuilt as a vector on 2026-09-10 by
`brand/tools/rebuild_seal.py`, run from the repo root:

- the rings and dots are constructed from geometry measured off the JPEG;
- the ring lettering is set in Arial Bold on the measured arcs;
- the map is traced, and the book-and-torch emblem is redrawn;
- the result is traced into one path in the old seal's coordinate frame, so it drops straight into
  every lockup.

| File (`brand/`) | What |
|---|---|
| `corafrica-seal.svg`, `-white`, `-orange` | the seal alone; `site/img/favicon.svg` is the black one |
| `corafrica-lockup.svg`, `-white` | seal and wordmark; the site header and footer use the white one |
| `corafrica-logo.svg`, `-white`, `-mono` | the full logo; the italic line under the wordmark now reads *Education for Africa's Future* |

`site/img/` carries copies of the seal and lockup files. If an original `.ai` or `.eps` ever turns
up, prefer it.

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
| **Once, any amount** | `buy.stripe.com/cNi4gBfEY4Ua22D860cwg07` |

**One-time giving** is a separate Payment Link on which the donor chooses the amount. Ethan sent it
on 2026-09-10, and it was opened to confirm it reads *One Time Donation* for Children of Rural
Africa. It replaces the old GiveWP embed (`form-id=2804`), which dies with WordPress. `donate.html`
offers it directly under the monthly ladder, with cheques by post as the offline route.

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
2. **Jeannine confirms the cheque payee and US address** on the Donate page. The EIN, 68-0619454, is
   confirmed (Ethan, 2026-09-10).
3. **Six bios still to come**: Jeannine Goelz, Ethan Suquet, Elijah Ugani, Olurotimi Padonu, Edwin
   Okungbowa and Blessing Ana (see People).
4. **WordPress comes down**; its GiveWP donation records and media library pass to the new site
   (Fr. Peter, 2026-09-04). Export both before anything is switched off.
5. **DNS.** Ethan is the sole controller of the domain (Fr. Peter, 2026-09-04). Point
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

The WhatsApp thread the photos came from also carries trustees' dates of birth, national ID
numbers, phone numbers and home addresses. None of it belongs on the site or in this repository.

## Photography

Most photos now come from Fr. Peter's own set (WhatsApp, 2026-09-06). The originals are in
`photos/source/whatsapp-2026-09/` (gitignored), cropped to 900 × 675 for cards and 1400 × 560 for
heroes in `site/img/`. They are WhatsApp-compressed, at most 1280px wide: fine for cards and
borderline for a full-width hero, so ask for originals of any that become permanent. A few older
images from the WordPress library remain (`hero`, `hands`, `clinic`, `farm`, `empower`, `school`).

Headshots live in `site/img/team/` (168 × 168, plus a larger `-lg` version for the bio pages) and are
wired by name in `HEADSHOTS` in `build.py`; anyone without one shows their initials. **Only add a
headshot once you are certain who is in it.** All fifteen people on the Contact page have one. Thirteen
were matched on 2026-09-10 against Fr. Peter's messages of 2026-09-06: each board photo sits between
that trustee's name and their details, and each admin-team photo is followed by its "Name (Role)"
caption. Olurotimi Padonu's comes from `rotimi.docx`, and Ethan supplied his own.

## People

The Contact page lists both Boards of Trustees and the administrative team exactly as Fr. Peter wrote
them on 2026-09-04 (`BOARD_NG`, `BOARD_US` and `ADMIN` in `build.py`). **Titles follow that written
answer, even where a later message or a bio words them differently** (Ethan, 2026-09-10).

Anyone with an entry in `BIOS` gets a page of their own, `team-<name>.html`, and their card on Contact
becomes a link to it. Those pages are in no menu: clicking the card is the only way in. The people still
without a bio are listed in `docs/ASK-FR-PETER.md`; add a bio to `BIOS` and the page and link appear
on the next build.

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
