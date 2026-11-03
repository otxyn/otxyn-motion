# liq-self-webgl-fluid - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** WebGL Fluid Simulation
**Category:** liquid / fluid-sim
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `liquid-001` in `research/candidates.json`.
Inspiration demo: https://paveldogreat.github.io/WebGL-Fluid-Simulation/
Source: https://github.com/PavelDoGreat/WebGL-Fluid-Simulation

---

## LAYER 1 - PLAIN-WORDS

Full-screen real-time Navier-Stokes fluid simulation that renders advected dye/smoke splats you can paint with the cursor. Implemented with raw WebGL using ping-ponged framebuffers, velocity/dye/divegence/pressure texture passes and optional multi-pass bloom.

Adaptation plan (from the manifest):
PavelDoGreat WebGL-Fluid-Simulation (MIT, source read). Adapt solver pass order; document ping-pong/FBO graph rather than minimising the original single file.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-2d`
- Complexity: `high`
- Primary techniques: stable-fluids solver; ping-pong framebuffers; render-to-texture; multi-render-target; curl/vorticity; optional pseudo-3D shading pass
- Technologies involved: WebGL 1/2; GLSL; vanilla JS

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
  Otxyn Motion - liq-self-webgl-fluid
  Technique adapted from Pavel Dobryakov's work (MIT).
  Upstream: https://github.com/PavelDoGreat/WebGL-Fluid-Simulation
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://raw.githubusercontent.com/PavelDoGreat/WebGL-Fluid-Simulation/master/LICENSE
Block from manifest: LICENSE fetched raw: 'MIT License, Copyright (c) 2017 Pavel Dobryakov'. Single-file (~2k lines) structure makes it easy to port.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
