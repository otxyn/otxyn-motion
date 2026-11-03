# cmp-self-baked-scene-scroll-tour - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** My Room in 3D
**Category:** composition / fullscreen
**Authority:** reinvent  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence high

Research provenance: `composition-006` in `research/candidates.json`.
Inspiration demo: https://my-room-in-3d.vercel.app/
Source: https://github.com/brunosimon/my-room-in-3d

---

## LAYER 1 - PLAIN-WORDS

A fully open-source three.js rebuild of Bruno Simon's actual room, using a baked textured plane plus multiple cameras with on-scroll camera transitions—an unusually clean composition of baked 3D + scroll choreography. Often referenced as the minimal 'full experience' codebase.

Adaptation plan (from the manifest):
my-room-in-3d has NO licence — technique (baked textures + scroll camera path) re-documented from mixed-licence reference; implementation from scratch.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `webgl-3d`
- Complexity: `medium`
- Primary techniques: baked lighting/textures; multi-camera scroll transitions; -controls via fullscreen prompt
- Technologies involved: three.js; Vite

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

**Reinvention.** The source has no verified open licence; nothing may be copied. Document the technique only and implement from scratch. 

Licence evidence: https://github.com/brunosimon/my-room-in-3d
Block from manifest: GitHub API 2026-11-03: ★4527, no SPDX licence — reference-only.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
