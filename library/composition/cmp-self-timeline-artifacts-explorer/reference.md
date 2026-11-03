# cmp-self-timeline-artifacts-explorer - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Neal.fun — Internet Artifacts
**Category:** composition / multi-scene
**Authority:** pattern  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence medium

Research provenance: `composition-029` in `research/candidates.json`.
Inspiration demo: https://neal.fun/internet-artifacts/
Source: https://neal.fun/internet-artifacts/

---

## LAYER 1 - PLAIN-WORDS

A museum-style timeline of internet history composed as sequential 'artifact' scenes: click-through chaptered modules, each with bespoke micro-interactions, unified by a consistent archival visual system. A multi-scene composition with per-scene uniqueness under one design language.

Adaptation plan (from the manifest):
Neal.fun Internet Artifacts — no public source; pattern study of era-sampled artifact browsing.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `dom`
- Complexity: `high`
- Primary techniques: chaptered timeline scenes; bespoke per-scene micro-interactions; consistent archival design system
- Technologies involved: DOM; CSS; JavaScript; SVG

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
Block from manifest: No public source.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
