# shd-self-chromatic-displacement-hover - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Interactive WebGL Hover Effects — akella step3 (Codrops)
**Category:** 3d-shaders / vertex-distort
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `3d-shaders-007` in `research/candidates.json`.
Inspiration demo: https://tympanus.net/Tutorials/webgl-mouseover-effects/step3.html
Source: https://github.com/akella/webgl-mouseover-effects

---

## LAYER 1 - PLAIN-WORDS

Codrops tutorial final demo: hovering an image ripples/displaces its surface with Three.js — mouse position drives shader uniforms, and the covered article documents the chromatic-aberration-by-channel-offset GLSL snippet (RGB sampled at different velocity-scaled offsets).

Adaptation plan (from the manifest):
akella webgl-mouseover-effects (MIT, demos fetched): mouse-velocity displacement + RGB-offset chromatic aberration.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `medium`
- Primary techniques: mouse-velocity-driven displacement; RGB channel offset for chromatic aberration; stepwise tutorial build-up (step1 basic plane → step3 full effect)
- Technologies involved: Three.js; GLSL; GSAP

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
  Otxyn Motion - shd-self-chromatic-displacement-hover
  Technique adapted from akella (Dennis Sylka?) / Codrops's work (MIT).
  Upstream: https://github.com/akella/webgl-mouseover-effects
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://api.github.com/repos/akella/webgl-mouseover-effects
Block from manifest: Repo MIT verified via GitHub API (★404). Demo step1.html and step3.html both fetched 200; article GLSL snippet read directly.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
