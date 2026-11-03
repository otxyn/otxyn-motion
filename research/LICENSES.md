# LICENSES — Licence findings, evidence and restrictions

Research date: 2026-11-02. Licence for **candidate** demos is tracked per-candidate in
`candidates.json` (`licensing` block); this file records the ecosystem-level rulings
that gate which libraries/techniques Otxyn entries may depend on, plus unresolved
questions. `verified` always means: read from the GitHub API `license` field or the
repo LICENSE file referenced below. **A public demo URL is never evidence of an open
licence.**

## 1. Library licences (ecosystem gate for Otxyn dependency choices)

| Library | SPDX licence (verified 2026-11-02) | Evidence | Implication for Otxyn entries |
|---|---|---|---|
| three.js | MIT | GitHub API `mrdoob/three.js` | May be referenced and vendored (attribution). Official `examples/` same licence. |
| anime.js | MIT | GitHub API `juliangarnier/anime` | Safe dependency. |
| lottie-web | MIT | GitHub API `airbnb/lottie-web` | Safe runtime; **.json/.aep animation assets carry their own rights** — never assume. |
| matter.js | MIT | GitHub API `liabru/matter-js` | Safe. |
| tsParticles | MIT | GitHub API `matteobruni/tsParticles` | Safe. |
| mo.js | MIT | GitHub API `mojs/mojs` | Safe. |
| Splitting.js | MIT | GitHub API `shshaw/Splitting` | Safe. |
| **GSAP** | **none (GSAP Standard No-Charge License, custom)** | GitHub API shows no SPDX; proprietary free | **Do not publish GSAP source in Otxyn.** Entries may *reference* GSAP by name and use OSC in spirit, but code we ship should be dependency-light or reasonably bundled per GSAP's own terms. Flag every GSAP-based candidate. |
| OGL (oframe/ogl) | **no license file in repo** | GitHub API | Unverified — do not vendor; check npm metadata + upstream billing before any dependency. |
| SplitType (lukePeavey/SplitType) | **no license file in repo** | GitHub API | Unverified — npm metadata must be checked before vendoring. |
| animation-handbook | MIT | GitHub API | Safe to study Inspirations from its READMEs/demos; copy not needed. |
| magicui, motion-primitives | MIT | GitHub API | Component-kit reference. |
| WebGL-Fluid-Simulation (PavelDoGreat) | MIT | GitHub API | Safe technique reference for liquid area. |
| amandaghassaei/FluidSimulation | MIT | GitHub API | Safe. |
| Codrops sample repos | MIT except samples with **no licence** (`atelier-north-collective` etc.) | GitHub Contents/API sample 2026-11-02 | **Per-repo licence check mandatory** — several studio-driven Codrops repos ship without a licence. |

## 2. Licence questions that must be resolved before the library phase

1. **Awwwards SOTD works** — showcase pages with world-class work generally have **no public source**. Treat all as reference-only; `redistribution_allowed: never`.
2. **Studio portfolios (Lusion, Active Theory, Studio Freight/Darkroom, Resn)** — some publish code; most do not. Per-composition check required; default `unverified`.
3. **Fonts used by strong typography demos** (variable fonts, display faces) — glyph software licences propagate. Any Otxyn entry must bundle only OFL/open fonts (e.g., Inter, Roboto Flex) or specify a font stack that avoids restricted faces.
4. **GSAP plugin boundaries** — SplitText/Shock etc. are part of the no-charge bundle; our adaptations should describe *techniques* (splitting, stagger math) rather than ship GSAP code.
5. **Shadertoy channel assets** — Shadertoy shaders have a "CC BY-NC-SA"-default policy for uploads but site **textures** are restricted ("CC for own content; textures not for redistribution"). Any Shadertoy-derived technique paper must re-implement, not import.

## 3. Ruling for this research phase

- No third-party code or assets are copied into this repository during research.
- Candidates may be recorded with `licensing.license: "unverified"` — that is expected.
- Each candidate shortlisted later must have a `license` + `license_url` + explicit
  redistribution statement **before** library adoption; scoring cannot override this gate.
