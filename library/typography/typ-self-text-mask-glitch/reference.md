# typ-self-text-mask-glitch - entry reference

**Status:** `planned`   (not implemented - scaffold generated from the manifest)
**Name:** CSS Text Animations collection (Prismic, 40 examples)
**Category:** typography / text-mask
**Authority:** reinvent  |  **Source licence:** unverified (verified: false)
**Inspection basis:** source-inspected, confidence medium

Research provenance: `typography-006` in `research/candidates.json`.
Inspiration demo: https://prismic.io/blog/css-text-animations
Source: https://prismic.io/blog/css-text-animations

---

## LAYER 1 - PLAIN-WORDS

Curated 40-example collection of CSS text animation demos: background-clip:text shimmer, glitch via ::before/::after + clip-path polygon slices, staggered word loops via @for-sass generated delays.

Adaptation plan (from the manifest):
Technique reference (Prismic CSS roundup) is an article, not an OSS repo — reimplement background-clip shimmer + ::before/::after clip-path glitch from the documented rules; no code reuse.

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `css`
- Complexity: `low`
- Primary techniques: background-clip shimmer; clip-path glitch slices; stagger via computed delays
- Technologies involved: CSS; clip-path; background-clip

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

Licence evidence: https://prismic.io/blog/css-text-animations
Block from manifest: Article fetched with real CSS technique excerpts; individual CodePens not opened (credit their authors before reuse).

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: 1440x900 and 390x844
- Console: 0 required
- Reduced motion: prefers-reduced-motion must degrade to a still
- Licence gate: per-entry licence block must remain verified at merge time

## Fonts

No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).
