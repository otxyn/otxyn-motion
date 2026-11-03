# COVERAGE MATRIX

Computed by `research/tools/consolidate.py` on 2026-11-03 from all `.discovery` sources.

| Category | Discovery target | Actual | Status | Subcategories covered |
|---|---:|---:|---|---|
| `typography` | 18 | **15** | CLOSE | 3d-type, counter, kinetic-layout, split-text, text-distort, text-mask, text-path, variable-font |
| `particles` | 18 | **27** | OK | burst, emitter, flow-field, generative-organic, gpu-sim, interactive, morph, organic-physics, text-particles, trails |
| `liquid` | 15 | **21** | OK | blob, chromatic, displacement, fluid-sim, glass-distort, metaballs, noise-distort, refraction, ripple, wave |
| `3d-shaders` | 15 | **12** | CLOSE | camera-move, fragment-shader, perspective, post-fx, procedural-geometry, procedural-noise, vertex-distort |
| `transitions` | 24 | **27** | OK | ambient-light, generative-bg, grid-animation, image-reveal, mask-transition, mesh-gradient, morph, morphix, page-transition, ribbon, scroll, wave, wipe |
| `composition` | 30 | **31** | OK | cinematic-hero, data-viz-motion, editorial, fullscreen, multi-scene, portfolio, product-intro, scroll-story, showcase, storytelling |
| **Total** | **120** | **133** | | |

## Inspection depth (all categories)
- Candidates whose **source code was actually read**: 65
- Candidates **browser-inspected** (Playwright, screenshots saved): 22
- **Shortlisted** (score ≥6.5 + verified licence + real inspection evidence): 37

## Scoring coverage
- Scored by the session-lead with recorded rationale: 50 of 133 candidates (others intentionally left `null` — no evidence, no score).

## Gaps and honest notes
- No fabricated candidates: every record's URLs were fetched this research phase.
- `composition` records are mostly URL-verified showcases without inspectable source; they count as discovery, not library-adoptable entries.
- Several strong Codrops repos (ImageRevealHover, AnimatedGridPreviews, BlockRevealers, MorphingPageTransition, AmbientCanvasBackgrounds) have **no licence** — recorded and excluded from the licence gate.
