# TECHNIQUES — Technical animation techniques with source references

Every entry below is grounded in source this research phase actually read (raw file
fetch, extraction of article code, or Playwright inspection). References give the
candidate ID in `candidates.json` and the primary URL.

---

## 1. Text splitting + stagger reveals (typography / split-text)

**Mechanism.** Wrap each character/word in a span (preserving a hidden
accessibility clone), then apply per-character transforms via CSS variables or a
GSAP timeline. The canonical timing core reference in this research is the Codrops
stagger tutorial (`typography-009`,
<https://tympanus.net/codrops/2020/06/17/making-stagger-reveal-animations-for-text/>),
whose timeline reads `staggerValue: 0.014` (seconds between chars) and
`charsDuration: 0.5` with `Power3.easeOut` — real constants measured from source.
The a11y-aware splitting implementation is Splitting.js (`typography-010`, MIT —
source `dist/splitting.js` read): char/word splitting + `data-*` custom properties
that carry per-item indices, enabling pure-CSS `transition-delay` staggering.
The handbook's Split Text Reveal (`typography-011`, browser+source verified)
implements the same split → stagger → ease pipeline dependency-free.

**Why it works.** Per-char spans convert one text change into N independent
transitions; stagger converts a single event into a moving wave, which produces the
"designed" feel. Order matters: from-left stagger reveals areComposited more cheaply
when using opacity + translateY only (no layout).

**Agent guidance.** Layout-thrash risk: avoid animating `left/right`; use
`transform`. Fallback: if splitting is unavailable, a `clip-path: inset` wipe per
line is the reduced-context variant.

## 2. Variable-font axis animation (typography / variable-font)

**Mechanism.** `font-variation-settings: "MORF" x, "SHLN" y` interpolated in
keyframes or by interaction. Primary evidence: Mandy Michael's Honk pen
(`typography-002`, CSS keyframes read: MORF 25→45, SHLN 0→100, 5s ease-in-out
alternate infinite); handbook Variable Font Morph (`typography-012`) and the 24ways
article (`typography-003`). Cheap (GPU-free; font raster rebuilt per frame but
fine for single headings), distinctive; weight axis (`wght`) also pairs well with
counters.

**Cautions.** Font file licences propagate (use OFL fonts such as Honk — Google
Fonts OFL). Not all variable axes are in all builds; check the font's fvar table.

## 3. Rolling counters / odometers (typography / counter)

**Mechanism.** Split the number into digits; each digit sits in a masked column of
0–9 (or 0–9→tens slots vertically) and translates by percentage. Odometer.js
(`typography-004`, MIT — `odometer.js` source read: `DIGIT_FORMAT`, `FRAMES_PER_VALUE`,
`MS_PER_FRAME`, mutation-driven updates + CSS keyboard) is the canonical base.
Alternative approach: rAF count-up with easing that drives `textContent` (simpler,
but character-width jitter; pair with `font-variant-numeric: tabular-nums`).

## 4. Text-driven particles (particles / text-particles)

**Mechanism.** Draw string on offscreen 2D canvas → `getImageData` → sample opaque
pixels at a stride → each sampled pixel becomes a particle with a home target.
Particles ease toward homes; pointer can repel and release restores. Verified
primary: handbook Text Particles (`particles-023`: source read — rAF loop, canvas,
`pointermove`, easing; browser+mobile verified, 0 console errors).
Complexity O(P) per frame; stride choice controls the count. Mutations: explosion
(reset homes scrambled, return), float cycles, colour by index.

## 5. Canvas emitters, burst fireworks, constellation links (particles)

- **Emitter:** spawn → velocity/ttl/fade lifecycle with delta-time (handbook
  Canvas Particle Effect, `particles-024`, source read: rAF + canvas + pointer).
- **Burst/fireworks:** two-state machines — launch (gravity arc) → explode (rays +
  particle branch children) (hb Fireworks, `particles-026`).
- **Constellation:** classic proximity graph — for each pair within threshold `d`,
  draw a segment with alpha ∝ (d−threshold) (hb Particle Constellation,
  `particles-027`).
All Canvas-2D; single-file friendly; colour palette carries most of the polish.

## 6. GPU particle simulation (GPGPU ping-pong) (particles / gpu-sim)

State lives in textures; each frame two render targets alternate: a simulation
shader reads the previous state and writes the next; a mesh/point-sprite pass
samples the textures as attributes. Verified references: handbook GPGPU Particle
System (`particles-025`, source read: GLSL + render-target texture feedback present),
three.js `webgl_gpgpu_water` (heightfield-to-mesh: `3d-shaders-005`) and
`webgpu_compute_particles` (`particles-004`). Necessary when particle counts are
10k+ (CPU loop would stall the main thread). Integration cost is real: state
initialisation, float-texture support checks, and DPR clamping to keep GPU work sane.

## 7. Curl noise & flow fields (particles / flow-field)

`curl(noise(x–t))` gives divergence-free velocity — particles don't cluster or leak,
they flow like wind (mechanism: unmatched for organic ambient motion). Verified
reference: CURL EXPLORER advecting 4.19M particles (`particles-001`, source
inspected by the particles agent); handbook Noise-Based Motion (`3d-shaders-011`)
is the low-cost 2D variant (single-file, Canvas 2D + simplex noise).

## 8. SVG "goo" metaball filter & displacement filters (liquid)

**Mechanism.** Stack `feGaussianBlur` (large stdDev) → `feColorMatrix` boosting
alpha contrast so the blurred union snaps into a liquid outline; children then
merge/split. Verified primary: Creative Gooey Effects (`liquid-011`, technique
demonstration verified; ~30 lines; framework-free). Companion Canvas+physics
variant: Matter.js bodies post-processed with the same filter chain
(`liquid-012`). SVG `feTurbulence + feDisplacementMap` handles static image
distortion on hover (`liquid-009`).

## 9. Displacement-map shaders (liquid / image distortion)

**Mechanism.** Two textures — image + displacement map; fragment shader offsets UVs
by `map.rg * strength`. Pairs with (a) concept art maps (`DistortionHoverEffect` →
`liquid-003`), (b) pointer velocity flowmaps (`liquid-006`,
`https://github.com/robin-dela/flowmap-effect`), (c) chromatic RGB offsets —
akella's form: sample r/g/b channels at three velocity-scaled offsets
(`3d-shaders-007`, GLSL snippet read from the article; MIT repo). The
handbook's Image Distortion Hover (`liquid-021`) implements exactly this pipeline
dependency-free (browser + source verified).

## 10. Fluid simulation (highest-end liquid)

Navier-Stokes stable-fluids on GPU: curl → divergence → pressure solve (Jacobi) →
subtract gradient → advect dye. Verified primary: PavelDoGreat/WebGL-Fluid-Simulation
(`liquid-001`, MIT; source read — solver/FBO/splat architecture present; demo 200).
Lower-cost alternatives: two-buffer height-field ripple (Almer water-canvas,
`liquid-014`); WebGL Water's raytracing/caustics (`liquid-015`) as the teaching
benchmark for real refraction.

## 11. Glass / liquid-glass refraction (liquid)

`backdrop-filter: blur/saturate` + a derived edge displacement map give the
Apple-style glass panel whose edges bend the background. Verified primary examples:
handbook Liquid Glass (`liquid-019`, source read: backdrop-filter + pointer logic)
and the CSS+SVG refraction blog demo (`liquid-010`). Preset: keep displacement only
near the rim to preserve readability; pair with specular highlight overlay.

## 12. Blob morphing (liquid / blob)

Noise-driven radial contour: radius(θ) = base·(1 + Σ Aᵢ·noise(fᵢθ, t)) smoothed via
spline, drawn as filled path. Verified: handbook Morphing Blob (`liquid-020`,
source read). GPU alternative: SDF ray-marched metaballs (`liquid-018`,
koji014/interactive-droplets — repo fetched, repo has **no licence** →
reference-only).

## 13. Fragment-shader generative backgrounds (3d-shaders)

Fullscreen quad + time uniform + a 2–4 octave noise field is the entire engine.
Verified: three.js `webgl_shader_lava` (`3d-shaders-002`, source read; no assets),
WebGL Shader Animation (`3d-shaders-010`), Mesh Gradient via SVG filters
(`transitions-022`, mobile verified), Synthwave Grid (`transitions-024` — CSS 3D
perspective grid), Wave Layers (`transitions-025`). Cheap and battery-friendly when
fps unforced (request throttled rAF).

## 14. Vertex displacement & GPGPU surfaces (3d-shaders)

three.js `webgl_materials_displacementmap` (`3d-shaders-001`, source read) is the
canonical heightmapped-plane example; the camera/scroll variant of the same
archetype is `3d-shaders-008` (scroll→camera path mapping, tutorial code read).
Scroll-driven 3D rotation in CSS (`3d-shaders-012`, source read:
`transform: perspective/rotate` + scrollY) covers the DOM route.

## 15. Page transitions (transitions)

- **View Transitions API** — spec-native route (Bramus demos, `transitions-999`
  none; discovery `transitions-003/004`): element-level screenshot cross-fades in one API.
- **SVG/shape morph transitions** (`transitions-023`, handbook) — expanding shape
  mask that reveals the next view at path midpoint.
- **Barba.js + GSAP systems** (`transitions-002`, repo `Ibaliqbal/codrops-barbajs-page-transition`
  fetched; article taxonomy inspected) for MPA/SSR stacks.
- Panels: curtains.js geometry masks (`transitions-007`, MIT) turn DOM↔WebGL.

## 16. Compositions (engineering taught by full pieces)

- `composition-005` folio-2019 (MIT): scene-config-driven composition — every
  section is config objects passed to instanced three objects; physics (Box2D)
  carries navigation. Lesson: make each animated section data, not bespoke code.
- `composition-006` / `my-room-in-3d`: baked lighting + scroll camera choreography —
  the minimal full-experience template (no open licence → texture reference only).
- `composition-030` Chrome Music Lab (Apache-2.0): suite-level launcher design
  system; every experiment canvas is audio-coupled but shares one interaction
  grammar.

---

Corrections learned during research (recorded to avoid agent repetition):
- The fluid-sim author is **PavelDoGreat** (not PavelDobryakov).
- The particle-system author is **Mark Kellogg (`mkkellogg/Photons2`)** — "Mark
  Kozlov" does not exist.
- `codrops/kinetic-typo` does not exist as a repo — only the tympanus.net demo.
