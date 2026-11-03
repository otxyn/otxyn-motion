# tra-self-curtains-geometry-mask - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** curtains.js
**Category:** transitions / mask-transition
**Authority:** reinvent  |  **Source licence:** MIT (verified: true)
**Inspection basis:** demo-fetched, confidence medium

Research provenance: `transitions-007` in `research/candidates.json`.
Inspiration demo: https://github.com/martinlaxenaire/curtainsjs
Source: https://github.com/martinlaxenaire/curtainsjs

---

## LAYER 1 - PLAIN-WORDS

WebGL library that turns DOM elements into interactive textured planes; its examples include displacement/spherical transitions where a geometry shader 'mask' moves across a plane to swap or distort images, all synced to the real HTML elements.

Adaptation plan (from the manifest):
curtains.js (MIT, ★1827) — our entry re-implements ONE geometry-mask transition pattern using the documented DOM-plane approach; credit Martin Laxenaire.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-2d`
- Complexity: `high`
- Primary techniques: DOM-synced textured planes; displacement and spherical distortion transitions; video displacement transitions; mouse position uniforms
- Technologies involved: WebGL; vanilla JS; GLSL; Three.js-independent

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

Licence evidence: https://api.github.com/repos/martinlaxenaire/curtainsjs
Block from manifest: MIT verified via GitHub API 2026-11-03 (★1827).

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
