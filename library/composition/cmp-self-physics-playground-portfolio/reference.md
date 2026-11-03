# cmp-self-physics-playground-portfolio - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Bruno Simon's Folio 2019 portfolio
**Category:** composition / portfolio
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** demo-fetched, confidence high

Research provenance: `composition-005` in `research/candidates.json`.
Inspiration demo: https://bruno-simon.com
Source: https://github.com/brunosimon/folio-2019

---

## LAYER 1 - PLAIN-WORDS

Drivable-car navigation through a compiled portfolio world, combining three.js 3D customization, physics (custom Box2D setup), video billboards, pothole mini-games and a chat Easter egg. It is the most-cited example of a complete playful composition with fully published source.

Adaptation plan (from the manifest):
folio-2019 (MIT, ★4753): study scene-config-driven composition and Box2D navigation; our composition recipe documents the data-driven pattern.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `high`
- Primary techniques: physics-driven navigation; in-page 3D world with video billboards; config objects for scene composition; gamified scroll-free exploration
- Technologies involved: three.js; JavaScript; Blender

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
  Otxyn Motion - cmp-self-physics-playground-portfolio
  Technique adapted from Bruno Simon's work (MIT).
  Upstream: https://github.com/brunosimon/folio-2019
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://api.github.com/repos/brunosimon/folio-2019
Block from manifest: MIT verified via GitHub API 2026-11-03 (★4753). 

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
