# tra-self-morph-page-transition - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Handbook — Morph Transition (page transition)
**Category:** transitions / morph
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `transitions-023` in `research/candidates.json`.
Inspiration demo: https://matinmonshizadeh.github.io/animation-handbook/animations/03-page-transitions/morph-transition/
Source: https://github.com/matinmonshizadeh/animation-handbook

---

## LAYER 1 - PLAIN-WORDS

Page transition where a shape morphs across the viewport to reveal the next view (SVG shape morphing with rAF). Source fingerprints: rAF, svg; 27,404 bytes.

Adaptation plan (from the manifest):
Handbook shape-morph page transition (MIT).

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `svg`
- Complexity: `medium`
- Primary techniques: expanding shape mask; path interpolation; view swap at midpoint
- Technologies involved: SVG path morphing; rAF

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
  Otxyn Motion - tra-self-morph-page-transition
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
