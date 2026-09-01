# CORAfrica — responsive spec
_Derived from the mobile pass, 2026-09-01. This is the contract for the real static build._

## Breakpoints
| Name | Range | Shell | Gutter |
|---|---|---|---|
| Mobile | `< 640px` | fluid, 100% | 20px |
| Tablet | `640–1023px` | fluid | 28px |
| Desktop | `≥ 1024px` | `max-width: 1220px` (panels 1360px) | 40px |

Artboards drawn: **1440px** desktop, **390px** mobile. Tablet follows the rules below by
interpolation — nothing about it is novel.

## Type ramp
| Role | Desktop | Mobile | Note |
|---|---|---|---|
| Hero h1 | 62px / -0.05em | 34px / -0.04em | Page heroes: 52px → 31px |
| Section h2 | 44px / -0.05em | 29px / -0.04em | |
| Card title | 19px / -0.03em | 17.5px | |
| Body | 15–16px / 1.55 | 14–15px / 1.5 | Never below 13px |
| Kicker | 0.88rem / .12em | 11.5px / .12em | 800 weight, uppercase, accent |
| Stat number | 54px | 36px | Space Grotesk 600 |

**Tracking eases as type shrinks.** `-0.05em` reads as confident at 62px and cramped at 34px.
This is the single most common way a scaled-down design looks wrong.

## Layout transforms at `< 640px`
| Desktop | Mobile |
|---|---|
| 7-item nav + CTA | Logo + **Donate** + hamburger. Donate never hides behind the menu — it is the primary action. |
| Credibility strip, 4 across | Vertical list, checkmark + label |
| Numbers panel, 4 columns | **2 × 2** — not 1 column. Four stacked numbers push the schools below the fold for no gain. |
| Model `30rem 1fr` + 2-col cards | Single column throughout |
| School cards, 3 across | Single column, card height 400px → 270px |
| Founder, 2 columns | Image above, copy below |
| Press, 3 across | Single column |
| Donate band, 2 columns | Stacked, buttons full-width |
| Footer `22rem 1fr` + 3 cols | One stack |
| **Schools register, 4-col table** | **Rebuilt as cards.** See below. |

## The Schools register — the one genuine redesign
A four-column table (name · location · founded · scale) cannot collapse to one column without
losing the scanning logic that makes it a table at all. On mobile each row becomes a card:

- School name, 19px Space Grotesk
- **Scale, location and year as three pills** beneath it — scale in accent, the other two neutral
- The descriptive note below, 13.5px

The pills preserve the comparison the table columns gave, in a shape that survives 350px.

## Touch and interaction
- Minimum target **44px**; primary buttons **52px** and full-width
- Root carries `overflow: hidden` so nothing can scroll horizontally
- Wide content (any future table, diagram or code block) scrolls inside its own
  `overflow-x: auto` container — never the page body

## Radii and shadows
| Token | Desktop | Mobile |
|---|---|---|
| Hero / panel | `2.6–3rem` | `1.5–1.6rem` |
| Card | `1.6rem` | `1.2rem` |
| Button | `0.7rem` | `0.7rem` |
| Panel shadow | `0 34px 76px rgba(14,18,24,.10)` | `0 20px 48px` |
| Card shadow | `0 18px 44px rgba(14,18,24,.06)` | `0 14px 32px rgba(14,18,24,.05)` |

Shadows shrink with the viewport. A 76px blur on a 390px screen reads as fog.

## Photography
The hero crop holds at 390px because the source frame is close and centred. **Wider group shots
lose their subject entirely at this width** — of the six usable frames on the current site, only
two survive a mobile hero crop. Any photo pull from Fr. Peter should ask specifically for
**close, centred subjects** as well as landscape wides, or the mobile site will be starved.

## Still to draw
Mobile artboards exist for **Home, Who We Are, Schools and Donate** — chosen because between them
they exercise every pattern on the site (hero, panel, card stack, timeline, table-to-card, CTA).
**Our Model, What We Do, Strategic Plan, News and Contact** follow these rules with no new
patterns, and can be drawn on request or built directly.
