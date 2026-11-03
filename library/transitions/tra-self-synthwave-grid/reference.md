# tra-self-synthwave-grid - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Handbook — Synthwave Grid
**Category:** transitions / grid-animation
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `transitions-024` in `research/candidates.json`.
Inspiration demo: https://matinmonshizadeh.github.io/animation-handbook/animations/07-ambient-background/synthwave-grid/
Source: https://github.com/matinmonshizadeh/animation-handbook

---

## LAYER 1 - PLAIN-WORDS

Animated perspective grid floor (synthwave/retro aesthetic): CSS 3D perspective grid with animated translateZ loop; canvas+svg fingerprints in source (24,653 bytes).

Adaptation plan (from the manifest):
Handbook CSS perspective grid loop (MIT).

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `dom`
- Complexity: `low`
- Primary techniques: perspective grid; translateZ loop; neon gradient styling
- Technologies involved: CSS 3D transforms; rAF

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

```text
<!--
  Otxyn Motion - tra-self-synthwave-grid
  Technique adapted from Matin Monshizadeh's work (MIT).
  Upstream: https://github.com/matinmonshizadeh/animation-handbook
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://github.com/matinmonshizadeh/animation-handbook
Block from manifest: Repo MIT.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
