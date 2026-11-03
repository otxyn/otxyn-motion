# cmp-self-css-shape-storytelling - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** In Pieces — 30 Endangered Species, 30 Pieces
**Category:** composition / storytelling
**Authority:** pattern  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence medium

Research provenance: `composition-027` in `research/candidates.json`.
Inspiration demo: http://www.species-in-pieces.com
Source: http://www.species-in-pieces.com

---

## LAYER 1 - PLAIN-WORDS

Bryan James's classic composition: 30 endangered species built from exactly 30 CSS polygons each, morphing between species with pure CSS transitions over a singular fullscreen simplification system. The best-known 'CSS-only full experience' composition.

Adaptation plan (from the manifest):
In Pieces — CSS polygon storytelling; no public source; pattern study.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `css`
- Complexity: `medium`
- Primary techniques: CSS polygon morphing system; species navigation UI; fullscreen rarity-driven narrative; scroll/click fact panels
- Technologies involved: CSS clip-path/polygon; HTML; JS minimal

Fallback tier: define at implementation time (document the degraded, dependency-free
variant of this effect - e.g. static presentation of the same subject).

---

## LAYER 3 - PARAMETERS

No constant in this scaffold is measured - measure from the inspiration source during
implementation and record provenance for each value. Suggested slots to fill
(delete as appropriate per technique):

| Parameter | Measured value | Source |
|---|---|---|
| duration(s) | _measure_ | |
| easing | _measure_ | |
| stagger | _measure_ | |
| counts / thresholds | _measure_ | |
| fallback constants | _set_ | |

---

## LAYER 4 - ATTRIBUTION

**Pattern study.** Closed-source showcase; documented for agent study. Never adopt its code or assets.

Licence evidence: n/a
Block from manifest: Concept/release page still live; source not published.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
