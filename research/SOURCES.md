# SOURCES — Valuable repositories, sites and collections

All entries below were verified live on **2026-11-02** (HTTP requests from this
session; licence data read directly from the GitHub API or the repo files).
Entries marked *(licence: none in repo)* have no LICENSE file — treat as
**unverified** regardless of npm metadata.

## 1. Existing research collections (direct competitors / prior art)

| Source | What it is | Licence (verified) | Why it matters |
|---|---|---|---|
| [matinmonshizadeh/animation-handbook](https://github.com/matinmonshizadeh/animation-handbook) | **176 web animation techniques**, each with a live dependency-free demo, per-technique README ("how it works, values that matter, production notes"), plain-words AI prompts, and an installable agent skill (`npx skills add matinmonshizadeh/animation-handbook`); ships `llms.txt`, `.claude-plugin`, `skills/`, `tests/` | MIT | **Closest prior work to Otxyn Motion.** Defines the "live demo + technique README + agent prompt" pattern. Key differentiator gap for Otxyn: its prompts deliberately contain *no code* — Otxyn can add code-level parameterised references. Repo layout: `animations/<category>/<technique>/`, `famous/`, `llms.txt` (verified via GitHub Contents API + raw README/llms.txt). |
| [sergey-pimenov/awesome-web-animation](https://github.com/sergey-pimenov/awesome-web-animation) | Curated list of web animation libraries/tools (1.6k★) | CC0-1.0 | Index of ecosystem libraries (Animate.css, Animista, CSShake, CSS-Doodle, Magic Animations…). Good discovery backfill, but lists links only — no demos, no technique documentation. |
| [motion-primitives (ibelick)](https://github.com/ibelick/motion-primitives) | Copy-paste animated React UI components (6.9k★) | MIT | Component-kit pattern (shadcn-like: copy into your project). Organised around Motion/framer-motion primitives; useful for "adaptation recipe" comparison. Site `motion-primitives.dev` did **not resolve** via Jina (422) on 2026-11-02 — plug documented as failure. |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | Animated design-engineering UI component library (23k★) | MIT | Includes marquee, dot-pattern, beams and similar generative background components; the component-tokens + registry-manifest approach is a reference for Otxyn's machine-readable metadata. |
| [Codrops (org `codrops`)](https://github.com/codrops) | ~450 per-technique demo repositories (verified sample: `interlude`, `RotatingOnScrollAnimations`, `SeamTransitions`, `CinemaSeatPreview`, `LookbookHoverEffects`, `EaseReverseClipMenu`, `isle-thorne-collective` — all MIT except `atelier-north-collective`-style repos with no licence) | Mostly MIT; sample shows some repos with **no licence** | The richest per-technique source archive on the web, with live demos on tampabay? (actually on `tympanus.net/Development/...`). Primary evidence pattern: article + demo + repo. Gap: no unified metadata, no agent files, licences vary per repo. |
| Awwwards / SOTD | Award/gallery listings of world-class motion sites | Content is copyright of owners | Discovers *compositions* (mission area G). Not source-providing: treat as reference catalogue; provenance must come from the studio's own public repo when it exists. |

## 2. Animation libraries (licence-verified 2026-11-02 via GitHub API)

| Library | Repo | Star ★ | Licence | Notes for the library phase |
|---|---|---:|---|---|
| three.js | mrdoob/three.js | 117k | MIT | Official `examples/` are in-repo (MIT) — top priority mine for particles, 3D, shaders. |
| GSAP | greensock/GSAP | 30k | **no-license (custom GSAP Standard No-Charge License)** | Free to use, NOT MIT — attribution/licence files must ship with any GSAP-based Otxyn entry or GSAP must not be vendored. |
| mo.js | mojs/mojs | 18.9k | MIT | Motion graphics toolbelt; burst/blur components relevant to particles/bursts. |
| anime.js | juliangarnier/anime | 74k | MIT | Stagger + timelines; stable base for DOM/SVG tasks. |
| PixiJS | pixijs/pixijs | — | MIT *(verified elsewhere in ecosystem; repo not API-checked this session)* | Sprites/bursts; v8 WebGPU renderer. |
| lottie-web | airbnb/lottie-web | 32k | MIT | Runtime for AE exports — relevant for compositions, but .aep/.riv assets need separate rights. |
| matter.js | liabru/matter-js | 18.6k | MIT | 2D physics (liquid-adjacent/organic-physics demos). |
| tsParticles | matteobruni/tsParticles | 9.1k | MIT | Full emitter/particles feature set (bursts, links, morph configs). |
| WebGL Fluid Simulation | **PavelDoGreat**/WebGL-Fluid-Simulation | 16.8k | MIT | Marker example for liquid area (PavelDobryakov/OGL-Fluid-…? — **use `PavelDoGreat`**, earlier searches with other spellings 404'd). |
| FluidSimulation | amandaghassaei/FluidSimulation | 304 | MIT | WebGL shader grid-particle fluid — alternative liquid approach. |
| Splitting.js | shshaw/Splitting | 1.8k | MIT | Text split for char reveals. |
| SplitType | lukePeavey/SplitType | 733 | **no-license in repo** | npm metadata may state MIT — verify package before any vendoring. |
| OGL | oframe/ogl | 4.7k | **no-license in repo** | Minimal WebGL lib widely used by studios; npm metadata needed before any dependency choice. |
| animation-handbook demos | matinmonshizadeh/animation-handbook | 13 | MIT | 176 self-contained demos; can seed both candidates and technique docs. |

## 3. Individual creators / studios to mine (verified to exist via search results, source URLs per-candidate TBD)

- **Bruno Simon** — three.js Journey, my-room-in-3d (`brunosimon/my-room-in-3d`, ★4.5k, **no licence in repo** — reference-only).
- **Pavel Dobryakov** — known GitHub user PavelDoGreat — 3D image effect / WebGL work.
- **Codrops authors** — individual technique articles with repos.
- **Studio Freight / Darkroom Engineering, Lusion, Active Theory, Resn** — composition-grade references (areas D–G); many are closed-source: provenance must be checked per work.

## 4. Failed lookups (kept for honesty, details in FAILED_SOURCES.md)

- `alex8224298/Awesome-Web-Effects` — 404 (repo moved/renamed or fabricated; not counted).
- `sghall/awesome-webgl` — 404.
- `PavelDobryakov/WebGL-Fluid-Simulation` (misspelling) — 404; corrected to `PavelDoGreat`.
- `motion-primitives.dev` — DNS unresolvable via Jina (422).
- `brunosimon/folie-sdk` — 404.
