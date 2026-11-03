# Research Plan — Otxyn Motion

## Goal

Produce an evidence-based research database (~120 candidates, must-report if fewer)
covering seven animation domains, plus six analysis documents, to feed a curated
40-implementation motion library for AI coding agents.

## Areas & coverage targets

| # | Area | Category key | Discovery target | Library target |
|---|---|---|---:|---:|
| A | Kinetic typography | `typography` | 18 | 7 |
| B | Particle systems | `particles` | 18 | 6 |
| C | Liquid & distortion | `liquid` | 15 | 5 |
| D/E | 3D & shaders | `3d-shaders` | 15 | 5 |
| F | Transitions & backgrounds | `transitions` | 24 | 7 |
| G | Complete compositions | `composition` | 30 | 10 |
|  | **Total** |  | **120** | **40** |

Sub-categories per area are enumerated in §3 of the mission; each candidate's
`subcategory` field uses a kebab-case token from that enumeration.

## Methodology — stages

1. **Environment audit** (done — `TOOL_AUDIT.md`).
2. **Ecosystem discovery**: find existing collections (GitHub search + web), catalogue how they organize/preview/license examples.
3. **Broad candidate collection**: parallel per-area discovery agents. Each agent must:
   - Use ≥2 independent search strategies (semantic Exa query + keyword Tavily query).
   - Only record candidates whose URLs were actually opened/fetched by the agent (HTTP 200).
   - Tag every record `discovered` (default) or higher if it inspected source.
   - Write machine-readable output to `research/.discovery/<area>.json`.
4. **Technical inspection** (centralised): read implementation files via raw.githubusercontent / Jina Reader;
   load selected live demos in Playwright (1440×900, 390×844), record console errors and screenshots.
5. **Evaluation**: dedupe (URL + technique signature), score, classify (discovered/inspected/shortlisted/rejected/blocked).
6. **Documentation**: write the six markdown analysis docs + consume into `candidates.json` / `.csv`.
7. **Validation**: JSON parse, CSV row parity, unique IDs, category enums, URL spot-checks, weighted-score arithmetic.

## Scoring framework

Score 1–10 per criterion, weighted:

| Criterion | Weight |
|---|---:|
| visual_quality | 25% |
| source_quality | 20% |
| reusability | 15% |
| agent_value | 15% |
| integration | 10% |
| performance | 10% |
| responsive_accessibility | 5% |

`weighted_score = Σ score·weight`, rounded to 2 dp. Only candidates with weights-bearing
scores may reach `shortlisted`. Licensing is a separate eligibility *gate*, not scored.

## Search strategies per area

- **Typography**: GSAP SplitText / Splitting.js demos, CodePen collections, variable-font animation showcases, rolling odometer libraries (AdjustText animations, CountUp), kinetic type galleries (whatdesigncando kinetic type, studios: Resn/Active Theory/Lusion).
- **Particles**: three.js particle examples, PixiJS v8 demos (emitter/burst), particle.js/tsparticles, flow-field canvas sketches, text→particle pens (shockwave, disintegration).
- **Liquid/distortion**: creative WebGL distortion libraries (Cartesia, blotti?), metaball SVG/canvas pens, liquid demos from Codrops (Fluid, displacement articles), hover displacement from studio heroes.
- **3D & shaders**: three.js official examples (displacement, raymarching, exploded-view, camera choreo), Codrops demos, Shadertoy featured SDF, OGL examples, framer-3d.
- **Transitions/backgrounds**: view-transition API demos, CSS mask wipes, mesh-gradient libraries, animated-grid galleries, section transition patterns from Awwwards SOTD.
- **Compositions**: Awwwards SOTD heroes, awards portfolios (Lusion’s own home, Active Theory works, Resn), Ceros/Templates editorial scroll experiences, three.js journey hero etc.

## Rules

- Never fabricate a URL, name, technique, or licence. Unknowns recorded as unknown.
- Primary sources over aggregators; snippets are not evidence.
- Respect robots/rate limits; skip and record failures (`FAILED_SOURCES.md`).
- No third-party code/assets copied into this repository as if original.
- Checkpoint everything into `candidates.json`/`.discovery` continuously.

## Validation checklist (Stage 7)

[ ] JSON parses; CSV has identical records; IDs unique
[ ] All categories use approved enum tokens
[ ] Every shortlisted candidate has ≥1 verified URL + evidence note
[ ] `weighted_score` recomputed values match stored values
[ ] No candidate licensed "verified" without a licence URL + evidence note
[ ] `FAILED_SOURCES.md` lists every recorded failure reason
