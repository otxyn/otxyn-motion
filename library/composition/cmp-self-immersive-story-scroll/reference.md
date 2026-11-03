# cmp-self-immersive-story-scroll - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** The Boat (SBS)
**Category:** composition / storytelling
**Authority:** pattern  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence medium

Research provenance: `composition-024` in `research/candidates.json`.
Inspiration demo: https://www.sbs.com.au/theboat/
Source: https://www.sbs.com.au/theboat/

---

## LAYER 1 - PLAIN-WORDS

SBS's adaptation of Nam Le's 'The Boat': a five-chapter interactive graphic novel combining horizontal-scroll chapter navigation, HTML5 canvas frame animation, atmospheric sound and parallax manuscript surfaces. Widely cited as a landmark web storytelling composition.

Adaptation plan (from the manifest):
SBS The Boat — demo verified, no public source; pattern study of audio-illustration scroll coupling only.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `dom`
- Complexity: `high`
- Primary techniques: horizontal chapter storytelling; canvas frame animation over scroll; ambient audio encoding; parallax ink illustration
- Technologies involved: HTML5 canvas; Web Audio; DOM

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
Block from manifest: Published piece—no public source.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
