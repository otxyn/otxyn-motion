# cmp-self-cinematic-product-intro - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Apple AirPods Pro 3 product page
**Category:** composition / product-intro
**Authority:** pattern  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence medium

Research provenance: `composition-021` in `research/candidates.json`.
Inspiration demo: https://www.apple.com/airpods-pro/
Source: https://www.apple.com/airpods-pro/

---

## LAYER 1 - PLAIN-WORDS

Apple's long-form product page composing scroll-scrubbed video sequences, device-accurate 3D/CG renders, sticky spec reveals and chaptered storytelling — the industry reference for 'scroll-scrubbed video' product intros at massive polish.

Adaptation plan (from the manifest):
Apple AirPods Pro page — marketing demo; pattern study only, no source.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `dom`
- Complexity: `high`
- Primary techniques: scroll-scrubbed video chapters; sticky pinned media; computed spec reveals; device CG-to-DOM handoffs
- Technologies involved: video scrubbing; WebGL; DOM/JS

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
Block from manifest: Proprietary; techniques widely imitated and documentable.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
