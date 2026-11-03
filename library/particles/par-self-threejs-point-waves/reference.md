# par-self-threejs-point-waves - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** three.js example: webgl_points_waves
**Category:** particles / generative-organic
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** demo-fetched, confidence high

Research provenance: `particles-003` in `research/candidates.json`.
Inspiration demo: https://threejs.org/examples/webgl_points_waves.html
Source: https://github.com/mrdoob/three.js

---

## LAYER 1 - PLAIN-WORDS

Official three.js example where a grid of GL points undulates as organic sine-wave hills with per-point color variation — a classic minimal 'living surface of dots' composition.

Adaptation plan (from the manifest):
Official three.js webgl_points_waves example (MIT); ship as parameterised vertex-wave points scene.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `low`
- Primary techniques: THREE.Points grid; sine-wave displaced point cloud; per-vertex color
- Technologies involved: three.js; WebGL; Points / BufferGeometry

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
  Otxyn Motion - par-self-threejs-point-waves
  Technique adapted from three.js contributors (mrdoob et al.)'s work (MIT).
  Upstream: https://github.com/mrdoob/three.js
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://github.com/mrdoob/three.js/blob/dev/LICENSE
Block from manifest: three.js repository and its examples ship under the MIT license.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
