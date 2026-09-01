# CORAfrica website rebuild — brief
_Interview with Ethan Suquet, 2026-09-01. Source doc: `WEB PAGES 3.docx` (Fr. Peter Abue)._

## The situation
Fr. Peter Abue is unhappy with https://corafrica.org.ng/ — a generic WordPress nonprofit
template (WordPress 7.1 + GiveWP). Broken hero image, footer reads © 2023, newest post Apr 2025.
He supplied a content doc and wants a site that reads as clean and professional.

Reference standard: teeej.ai / teeejfit.ai. **Fr. Peter's praise was specifically "how clean,
crisp and professional it looked."** That is a quality bar, not a style brief.

## Decisions (locked)

| Question | Decision |
|---|---|
| Platform | **Static site**, same approach as the Teeej sites. No CMS. |
| Audience priority | **1. NGOs/governments that give grants → 2. donors → 3. supporters & learners** |
| Primary CTA | **Donate**, kept prominent in the nav |
| Brand | **Keep the logo.** Ethan rebuilds it as a clean SVG. |
| Source of truth | **The docx supersedes the live site** (see caveat below) |
| Pages added back | **Schools, Donate, Photo gallery.** Partners: not included. |
| Copy | **Rewrite properly, keep every fact.** Nothing invented, nothing dropped. |
| Faith framing | **Honest but not the lead.** Mission and impact lead; the Catholic foundation is stated plainly on Philosophy and Founder. Never hidden, never the headline. |
| Launch path | **Replace corafrica.org.ng entirely.** WordPress retired. |
| Photography | Only a handful of decent photos. Design must not expose the gap. |
| Approvals | Ethan iterates with Claude; Ethan takes it to Fr. Peter when it is genuinely good. |
| Timeline | No hard deadline. Do it right. |

## Design implications
- **Grant-officer-first** means evidence is structural, not decorative: numbers, named projects,
  registration status, governance, and SDG alignment need real estate above the fold and their
  own blocks — not a paragraph buried on an About page.
- **Scarce photography** means the layout carries the weight: typography, generous air, an
  editorial grid, and the brand orange used sparingly. No full-bleed photo walls we cannot fill.
  The gallery ships as a curated set of a few strong images, not a thumbnail grid.
- **Donate on a static site is solved** — two live Stripe Payment Links already exist
  (verified 200 on 2026-09-01), so no backend is required.

## Brand tokens
- Brand orange sampled from the logo artwork: **#FB600A** (Teeej's accent is #F16908 — near-identical)
- Logo lockup: circular seal (Africa silhouette + torch) + "CORAfrica" brush wordmark +
  "CHILDREN OF RURAL AFRICA-NIGERIA" + tagline _"Helping Children and Communities Thrive"_
