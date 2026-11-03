# cmp-self-scrollytelling-data-essay - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** The Pudding — How Sonic DNA Connects Generations of Music
**Category:** composition / data-viz-motion
**Authority:** reinvent  |  **Source licence:** unverified (verified: false)
**Inspection basis:** demo-fetched, confidence medium

Research provenance: `composition-031` in `research/candidates.json`.
Inspiration demo: https://pudding.cool/2025/04/music-dna
Source: https://github.com/the-pudding

---

## LAYER 1 - PLAIN-WORDS

The Pudding visual essay composing animated D3/AI-style charts, scroll-driven narrative beats and visual commentary from musical-generation data — the publication's house style of data-driven motion storytelling. Representative of dozens of similar essays under the same open-source practice.

Adaptation plan (from the manifest):
The Pudding house style (licence per-essay unverified): document stepper/scroll-beat pattern; implement from scratch.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `svg`
- Complexity: `medium`
- Primary techniques: scroll-triggered chart beats; stepper/scroller narrative patterns; SVG chart animation; audio-context visuals (varies per essay)
- Technologies involved: D3; Svelte; SVG; scrollytelling helpers

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

Licence evidence: https://github.com/the-pudding
Block from manifest: Publication open-sources its codebase structure; per-essay licence not verified — library adoption requires per-essay licence check.

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
