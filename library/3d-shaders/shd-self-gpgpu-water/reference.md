# shd-self-gpgpu-water - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** three.js — webgl_gpgpu_water
**Category:** 3d-shaders / vertex-distort
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `3d-shaders-005` in `research/candidates.json`.
Inspiration demo: https://threejs.org/examples/#webgl_gpgpu_water
Source: https://github.com/mrdoob/three.js

---

## LAYER 1 - PLAIN-WORDS

GPGPU water surface: a heightfield is computed in texture-space (ping-pong render targets) and rendered as a deformed grid mesh with dynamic normals — the reference architecture for GPU-computed surfaces that animate meshes.

Adaptation plan (from the manifest):
three.js webgl_gpgpu_water (MIT, source read): GPGPU heightfield -> deformed grid with recomputed normals.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `high`
- Primary techniques: gpgpu texture state storage; ping-pong render targets; heightfield-to-mesh vertex shader; normal recomputation
- Technologies involved: Three.js; WebGL; GPGPU ping-pong; GLSL

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
  Otxyn Motion - shd-self-gpgpu-water
  Technique adapted from three.js contributors (by David Sjetel)'s work (MIT).
  Upstream: https://github.com/mrdoob/three.js
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://github.com/mrdoob/three.js/blob/dev/LICENSE
Block from manifest: MIT (three.js). Source fetched raw (22,596 bytes, HTTP 200 — the largest, confirming the GPGPU pass structure).

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
