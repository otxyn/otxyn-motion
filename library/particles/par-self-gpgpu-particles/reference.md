# par-self-gpgpu-particles - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Handbook — GPGPU Particle System
**Category:** particles / gpu-sim
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `particles-025` in `research/candidates.json`.
Inspiration demo: https://matinmonshizadeh.github.io/animation-handbook/animations/06-3d-advanced/gpgpu-particle-system/
Source: https://github.com/matinmonshizadeh/animation-handbook

---

## LAYER 1 - PLAIN-WORDS

Thousands of particles simulated on GPU via ping-pong framebuffer state textures (position/velocity) and rendered as GL point sprites — the GPGPU particle architecture. Source fingerprints: rAF, canvas, GLSL, render-target/texture feedback; 40,900 bytes.

Adaptation plan (from the manifest):
Adapt ping-pong framebuffer particle simulation (MIT); include float-texture fallback path.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `high`
- Primary techniques: state-in-texture simulation; ping-pong feedback; point sprite rendering
- Technologies involved: WebGL; GLSL; ping-pong render targets

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
  Otxyn Motion - par-self-gpgpu-particles
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
