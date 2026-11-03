# Attribution — who made what

Otxyn Motion is a *reference library*: it documents, adapts (only with verified open
licences), or re-invents the work of many web-graphics creators. This page names the
key people and organisations behind the material the project refers to, and separates
Otxyn's original work from everything third-party. Underlying records with full URL
provenance live in [`research/candidates.json`](../research/candidates.json) and
[`library/manifest.json`](../library/manifest.json).

## Direct inspiration for the 40 library entries

| Creator | Count of entries | Their contribution |
|---|---:|---|
| **Matin Monshizadeh** — [animation-handbook](https://github.com/matinmonshizadeh/animation-handbook) (MIT) | 20 | The dependency-free, single-file demo handbook that anchors most typography, particles, liquid, transition and composition entries. Verified MIT via GitHub API 2026-11-03. |
| **three.js contributors** (mrdoob et al., examples by various authors incl. David Sjetel) — [three.js](https://github.com/mrdoob/three.js) (MIT) | 4 | Official examples (`webgl_points_waves`, `webgl_shader_lava`, `webgl_materials_displacementmap`, `webgl_gpgpu_water`) anchor the 3d-shaders and particles families. |
| **Bruno Simon** — folio-2019 (MIT) and my-room-in-3d (**no licence**) | 2 | Composition benchmarks: folio-2019 is adapt-authority (verified MIT ★4753); my-room-in-3d is a no-licence reinvent reference. |
| **Neal Agarwal** — neal.fun (Deep Sea, Internet Artifacts) | 2 | Closed-source pattern studies of scroll storytelling. |
| **Pavel Dobryakov** ([PavelDoGreat](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation), MIT) | 1 | The canonical WebGL stable-fluids demo (naming note: "Pavel Dobryakov" is the author's display name; the GitHub handle is `PavelDoGreat` — the repo URL in the manifest is the authoritative handle and resolves correctly). |
| **Adam Schwartz / HubSpot** — [Odometer.js](https://github.com/adamwdraper/Odometer-js) (MIT) | 1 | Rolling-counter digit-column technique. |
| **Lucas Bebber** (Codrops, *Creative Gooey Effects*) | 1 | SVG goo filter technique (technique-level reference; demo not licence-cleared). |
| **akella (Dennis Sylka) / Codrops** — webgl-mouseover-effects (MIT) | 1 | Mouse-velocity displacement + RGB-split hover. |
| **Martin Laxenaire** — [curtains.js](https://github.com/martin-laxenaire/curtainsjs) (MIT) | 1 | DOM-mapped WebGL planes; geometry-mask transition pattern. |
| **Google Creative Lab + Use All Five** — [Chrome Music Lab](https://github.com/googlecreativelab/chrome-music-lab) (Apache-2.0) | 1 | Audio-reactive canvas coupling (requires Apache NOTICE handling). |
| **The Pudding** — scrollytelling essays | 1 | Per-essay licences unverified; document-as-pattern only. |
| **SBS Australia / Matt Huynh** — *The Boat* | 1 | Pattern study only (no public source). |
| **Bryan James** — *In Pieces* | 1 | CSS polygon storytelling pattern study (no public source). |
| **Apple Inc.** — AirPods Pro page | 1 | Marketing-demo pattern study; not adoptable. |
| **Lusion Ltd** — Lusion v3 | 1 | Closed benchmark reference for the persistent-WebGL-scene pattern. |

## Broader research-archive creators (top contributors by record count)

- **Codrops / tympanus.net** (Manoela Ilic & guest authors: Mario Carrillo's kinetic
  typography, Stephen Shaw's Splitting cross-references, Robin Delaporte's flowmap
  effect, and ~25 more articles whose demos were fetched for inspection). Note:
  several popular Codrops sample repositories are **unlicensed** (ImageRevealHover,
  AnimatedGridPreviews, BlockRevealers, MorphingPageTransition, AmbientCanvasBackgrounds,
  TextDistortionEffects) — recorded as licence-blocked, and *no* Codrops-licensed
  blanket is assumed.
- **three.js contributors** (~9 example records) — MIT.
- **Mandy Michael** (variable-font demos), **NewKrok** (THREE.Particles), **Unseen
  Studio**, **odina101**, **nitin42**, **Stephen Shaw (shshaw)**.

## Licence posture summary (from the 40-entry manifest)

- `adapt` — **29 entries**, every one backed by a *live-verified* open licence
  (MIT 29, Apache-2.0 1 — total 29 MIT + 1 Apache across the manifest; each block
  stores a licence URL + verified date).
- `reinvent` — **5 entries**: technique documented, upstream code never vendored
  (sources unlicensed or article-only).
- `pattern` — **6 entries**: closed-source showcases documented for study; adoption
  of their code or assets is prohibited.

## Asset classes kept separate

1. **Otxyn originals** — everything authored in this repo (docs, manifest, skill,
   website) under the repo MIT licence.
2. **Third-party references** — name + URL only, under their own licences.
3. **Third-party implementations** — *never copied* into the library without a
   verified open licence; `adapt` attributions ship in every derived file header.
4. **Screenshots** — `research/previews/` are Playwright captures of other people's
   demos, kept as internal inspection evidence; not licensed to us, not for
   redistribution as assets.

## Fonts

Only OFL-verified families are cleared for bundling (verified live against
`google/fonts/*/METADATA.pb` on 2026-11-03): **Honk, Inter, Roboto Flex, Anton,
Space Grotesk, Archivo Black** — each mapped to the entries that use it in the
manifest's `fonts` block. Codrops/GSAP-bundled or otherwise unknown-licence font
files are on the manifest's explicit avoided list.
