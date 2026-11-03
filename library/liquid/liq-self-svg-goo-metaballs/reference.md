# liq-self-svg-goo-metaballs - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Creative Gooey Effects
**Category:** liquid / metaballs
**Authority:** reinvent  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence high

Research provenance: `liquid-011` in `research/candidates.json`.
Inspiration demo: https://tympanus.net/Development/CreativeGooeyEffects/
Source: https://tympanus.net/codrops/2015/03/10/creative-gooey-effects/

---

## LAYER 1 - PLAIN-WORDS

Lucas Bebber's canonical SVG 'goo' filter: a heavy feGaussianBlur combined with an feColorMatrix alpha-contrast boost fuses separate DOM/SVG elements into metaball-like blobs that stretch and split, used for menus, buttons and droplets.

Adaptation plan (from the manifest):
Technique reference: Codrops 'Creative Gooey Effects' (demo rights; technique is standard SVG filter primitives). Reimplement the feGaussianBlur->feColorMatrix chain from documented filter math; credit Lucas Bebber's technique article as inspiration only.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `svg`
- Complexity: `low`
- Primary techniques: feGaussianBlur + feColorMatrix goo filter; metaball approximation via filter stacking; filter-element reuse
- Technologies involved: SVG filters; CSS filter; JS

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

**Reinvention.** The source has no verified open licence; nothing may be copied. Document the technique only and implement from scratch. 

Licence evidence: https://tympanus.net/codrops/2015/03/10/creative-gooey-effects/
Block from manifest: Demo + article fetched; license not stated. | licence gate FAIL: cannot be adopted into library until licence resolved

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
