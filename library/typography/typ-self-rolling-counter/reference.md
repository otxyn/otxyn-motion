# typ-self-rolling-counter - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** Odometer.js (HubSpot)
**Category:** typography / counter
**Authority:** adapt  |  **Source licence:** MIT (verified: true)
**Inspection basis:** source-inspected, confidence high

Research provenance: `typography-004` in `research/candidates.json`.
Inspiration demo: http://github.hubspot.com/odometer/docs/welcome
Source: https://github.com/hubspot/odometer

---

## LAYER 1 - PLAIN-WORDS

Rolling odometer/counter that animates numeric value changes with slot-machine-style digit rolls across themed styles; driven by a MutationObserver on the element's text.

Adaptation plan (from the manifest):
INSP Odometer.js MIT (★7.3k, source read). Re-uses the documented digit-column technique; MIT permits adaptation with attribution — rebuild with tabular-nums + CSS transforms and keep the Odometer attribution header.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `dom`
- Complexity: `low`
- Primary techniques: digit-splitting; CSS transition roll; mutation-driven updates
- Technologies involved: JavaScript; CSS transitions

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
  Otxyn Motion - typ-self-rolling-counter
  Technique adapted from Adam Schwartz / HubSpot's work (MIT).
  Upstream: https://github.com/hubspot/odometer
  Include the upstream MIT copyright + licence text alongside any
  derived file (copy it from the upstream repository's LICENSE).
-->
```

Licence evidence: https://github.com/hubspot/odometer
Block from manifest: MIT verified via GitHub API (★7285).

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
