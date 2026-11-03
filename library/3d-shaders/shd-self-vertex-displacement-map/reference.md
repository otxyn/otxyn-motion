# shd-self-vertex-displacement-map - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** three.js — webgl_materials_displacementmap
**Category:** 3d-shaders / vertex-distort
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `3d-shaders-001` in `research/candidates.json`.
Inspiration demo: https://threejs.org/examples/#webgl_materials_displacementmap
Source: https://github.com/mrdoob/three.js

---

## LAYER 1 - PLAIN-WORDS

Official three.js example: a plane mesh's vertices are displaced in the vertex shader by a texture heightmap with normal recomputation; classic displacement-map pattern applicable to terrain-style or fabric-like motion surfaces.

Adaptation plan (from the manifest):
three.js webgl_materials_displacementmap (MIT): heightmap-vertex displacement + normals.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `medium`
- Primary techniques: vertex displacement from heightmap; normal-map recomputation; uniform-driven displacement scale
- Technologies involved: Three.js; WebGL; GLSL vertex shader

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
  Otxyn Motion - shd-self-vertex-displacement-map
  Technique adapted from three.js contributors's work (MIT).
  Upstream: https://github.com/mrdoob/three.js
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://github.com/mrdoob/three.js/blob/dev/LICENSE
Block from manifest: three.js MIT verified via GitHub API (★117k). Example source fetched raw (6,703 bytes, HTTP 200).

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
