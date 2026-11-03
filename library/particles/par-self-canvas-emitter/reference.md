# par-self-canvas-emitter - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Handbook — Canvas Particle Effect
**Category:** particles / emitter
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `particles-024` in `research/candidates.json`.
Inspiration demo: https://matinmonshizadeh.github.io/animation-handbook/animations/06-3d-advanced/canvas-particle-effect/
Source: https://github.com/matinmonshizadeh/animation-handbook

---

## LAYER 1 - PLAIN-WORDS

Continuous 2D particle emitter on Canvas: spawn, drift, fade lifecycle with pointer emission control. Source fingerprints: rAF, canvas, pointer; 35,780 bytes.

Adaptation plan (from the manifest):
Adapt spawn/ttl/fade emitter with delta-time physics (MIT).

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `canvas-2d`
- Complexity: `low`
- Primary techniques: spawn/life/fade lifecycle; delta-time physics; pointer-driven emission
- Technologies involved: Canvas 2D

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
  Otxyn Motion - par-self-canvas-emitter
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
