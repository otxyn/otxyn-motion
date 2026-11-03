# SHORTLIST — Strongest candidates with scores and evidence

Scoring framework: see `RESEARCH_PLAN.md` (weights: visual 25 / source 20 / reuse 15 /
agent 15 / integration 10 / performance 10 / resp+access 5). Only candidates with a
**verified open licence** pass the eligibility gate into this list (rule in
`LICENSES.md`). 37 of 133 candidates are shortlisted; full data in
`candidates.json` (`status: "shortlisted"`).

## A. Best overall (heading the initial 40-library candidate pool)

| Rank | ID | Name | Cat | Score | Licence | Evidence |
|---:|---|---|---|---:|---|---|
| 1 | particles-023 | Handbook — Text Particles | particles/text-particles | 8.75 | MIT | browser+source+mobile, 0 console errors |
| 2 | liquid-011* | Creative Gooey Effects (SVG goo) | liquid/metaballs | 8.55 | unverified (Codrops technique — score kept, **reserved from adoption** until licence of the technique demo is resolved) | technique demo verified |
| 3 | 3d-shaders-002 | three.js — webgl_shader_lava | 3d-shaders/procedural-noise | 8.45 | MIT (three.js) | raw source read |
| 4 | typography-011 | Handbook — Split Text Reveal | typography/split-text | 8.40 | MIT | browser+source |
| 5 | typography-010 | Splitting.js | typography/split-text | 8.35 | MIT | source read + demo |
| 6 | 3d-shaders-007 | akella Interactive WebGL Hover Effects | 3d-shaders/vertex-distort | 8.35 | MIT | GLSL snippet read, demos fetched |
| 7 | liquid-001 | WebGL Fluid Simulation (PavelDoGreat) | liquid/fluid-sim | 8.20 | MIT | demo 200 + `script.js` (51.8 KB, solver passes confirmed) |
| 8 | particles-025 | Handbook — GPGPU Particle System | particles/gpu-sim | 8.15 | MIT | browser+source |
| 9 | typography-015 | Handbook — Scramble Text | typography/text-distort | 8.10 | MIT | browser+source |
| 10 | particles-006 | THREE Particles (NewKrok) | particles/emitter | 8.05 | MIT | live editor inspected by agent |

\* liquid-011 sits at `inspected` status in the data (licence gate blocks adoption);
its technique (30-line SVG goo filter) remains a top re-engineering target.

## B. All shortlisted by category

**Typography (15 total in category; 7 shortlisted):** `typography-004` Odometer.js
(MIT, source read; 7.80) · `typography-010` · `typography-011` · `typography-012`
Handbook Variable Font Morph (7.80) · `typography-013` Handbook Text on Path ·
`typography-014` Handbook Kinetic Typography · `typography-015` Scramble Text.

**Particles (27; 7 shortlisted):** `particles-023` Text Particles · `particles-024`
Canvas Particle Effect (8.05) · `particles-025` GPGPU · `particles-026` Fireworks ·
`particles-027` Particle Constellation (7.90) · `particles-006` THREE Particles
(NewKrok, 8.05) · `particles-008` Photons 2 (Mark Kellogg, 7.80). (Scored-but-licence-blocked
strong references: CURL EXPLORER `particles-001` 7.60 unverified; three.js
`webgl_points_waves`/`webgpu_compute_particles` verified MIT but scored slightly
lower than the handbook equivalents.)

**Liquid (21; 4 shortlisted):** `liquid-001` Fluid Sim (8.20) · `liquid-019`
Handbook Liquid Glass (8.20) · `liquid-020` Morphing Blob (8.20) · `liquid-021`
Image Distortion Hover (7.95). *(Best unscored pool: goo filter, flowmap,
displacement configurator — see COVERAGE_MATRIX for the reference-only set.)*

**3D & shaders (12; 10 shortlisted):** all six official three.js examples studied
(`3d-shaders-001..006` — displacementmap 8.15, lava 8.45, TSL earth 7.65, TSL
terrain 7.45, GPGPU water 7.90, god-rays 7.05) plus akella's hover effects
(`3d-shaders-007` 8.35) and three handbook entries (`3d-shaders-010` WebGL Shader
Animation 7.95, `3d-shaders-011` Noise-Based Motion 8.20, `3d-shaders-012`
Scroll-Driven 3D Rotation 7.30).

**Transitions (27; 7 shortlisted):** `transitions-007` curtains.js (MIT, 7.60) ·
`transitions-022` Mesh Gradient · `transitions-023` Morph Transition ·
`transitions-024` Synthwave Grid · `transitions-025` Wave Layers (7.60) ·
`transitions-026` Animated Gradient Background · `transitions-027` Parallax
Depth-of-Field.

**Compositions (31; 2 shortlisted):** `composition-005` Bruno Simon folio-2019
(**MIT verified via API 2026-11-03**, ★4753, 7.95 — the composition benchmark with
open code) · `composition-030` Chrome Music Lab (**Apache-2.0 verified**,
★2417, 7.10).

*Category shortlist counts recomputed from `candidates.json` on 2026-11-03
(7 particles / 10 3d-shaders / 7 transitions corrected against the data here —
the earlier draft under-counted; see `reports/DATA_AUDIT.md`).*

## C. Strong "inspected" candidates that missed the licence gate

These scored ≥7 but stay reference-only until licences resolve:
`typography-002` Honk variable-font pen (8.20, pen-default rights) ·
`typography-009` Codrops stagger constants (8.00, article) · `liquid-011` goo
(8.55) · `liquid-006` robin-dela/flowmap-effect (7.75, **no licence**) ·
`transitions-011` vaneenige/scroll-transitions-webgl (7.80, **no licence**, agent's
"codrops-style free-use" string is not a licence) · `particles-001` CURL EXPLORER
(7.60) · `transitions-002` Barba+GSAP Astro (7.70, unverified).

## D. Duplicates and rejections detected

- `transitions-005` ≡ `liquid-003`: identical demo URL
  (`tympanus.net/Development/DistortionHoverEffect/`) — consolidated to the liquid
  record; 1 candidate dropped in consolidation.
- `particles-006`/`particles-007`: NewKrok library vs its projectile demo — kept
  separately (distinct repos), flagged near-duplicate family.
- Composition hero sites (Lusion, Active Theory, …) kept as `discovered`
  showcase references — not library-adoptable (no source; licences unverifiable).
