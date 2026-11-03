# cmp-self-audio-reactive-suite - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Chrome Music Lab
**Category:** composition / multi-scene
**Authority:** adapt  |  **Source licence:** Apache-2.0 (verified: true)
**Inspection basis:** demo-fetched, confidence high

Research provenance: `composition-030` in `research/candidates.json`.
Inspiration demo: https://musiclab.chromeexperiments.com
Source: https://github.com/googlecreativelab/chrome-music-lab

---

## LAYER 1 - PLAIN-WORDS

Google Creative Lab's music suite composing a dozen separately authored experiments (Kandinsky, Song Maker, Rhythm, Harmonics...) under one launcher design system, all built on Web Audio API with canvas-based visualizers. Fully open-source composition suite.

Adaptation plan (from the manifest):
Chrome Music Lab (Apache-2.0): adapt one audio+canvas coupling pattern; keep Google attribution.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `canvas-2d`
- Complexity: `medium`
- Primary techniques: suite-level launcher composition; canvas visualizers coupled to audio; touch/keyboard playable instruments; coherent shared visual language
- Technologies involved: Web Audio API; canvas 2D; JavaScript

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

Adaptation permitted under Apache-2.0; attribution block to be filled from the upstream LICENSE at implementation time.

Licence evidence: https://api.github.com/repos/googlecreativelab/chrome-music-lab
Block from manifest: Apache-2.0 verified via GitHub API 2026-11-03 (★2417).

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
