# typ-self-kinetic-typography - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Handbook — Kinetic Typography
**Category:** typography / kinetic-layout
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `typography-014` in `research/candidates.json`.
Inspiration demo: https://matinmonshizadeh.github.io/animation-handbook/animations/05-text-typography/kinetic-typography/
Source: https://github.com/matinmonshizadeh/animation-handbook

---

## LAYER 1 - PLAIN-WORDS

Kinetic type layout where text blocks animate position/lightness by an authored timeline (rAF loop with easing curves per line). Source fingerprints: rAF, easing; 28,051 bytes.

Adaptation plan (from the manifest):
Adapt rAF per-line kinetic layout (MIT); parameterise line timings.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `dom`
- Complexity: `medium`
- Primary techniques: timed per-line motion; easing curves
- Technologies involved: DOM; rAF; easing functions

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
  Otxyn Motion - typ-self-kinetic-typography
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
