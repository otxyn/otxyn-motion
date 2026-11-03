# cmp-self-webgl-agency-hero - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Lusion v3 (lusion.co)
**Category:** composition / cinematic-hero
**Authority:** pattern  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence medium

Research provenance: `composition-001` in `research/candidates.json`.
Inspiration demo: https://lusion.co
Source: https://lusion.co

---

## LAYER 1 - PLAIN-WORDS

Award-winning studio site composing a real-time 3D WebGL hero character with scroll-coupled scene transitions, physics-driven interaction and micro-interaction UI throughout. It is coherent because the single 3D scene persists and morphs across the entire page rather than being a one-off hero effect. Winner of Awwwards Site of the Year (Lusion v3) and CSSDA WOTY.

Adaptation plan (from the manifest):
Lusion v3 — benchmark reference; closed source; documents the persistent-WebGL-scene pattern qualitatively.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `high`
- Primary techniques: persistent 3D scene across page; scroll-coupled camera/scene transitions; physics-interaction hero; cursor-reactive displacement
- Technologies involved: WebGL; GLSL

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

**Pattern study.** Closed-source showcase; documented for agent study. Never adopt its code or assets.

Licence evidence: n/a
Block from manifest: Commercial studio site; no public source.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
