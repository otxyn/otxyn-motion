# FAILED_SOURCES — Unavailable pages, failed extractions, access restrictions

Compiled 2026-11-03 from every `.discovery/*.json` `failures` block plus the
session-lead's own live failures. Entries are verbatim-outcome records; nothing was
silently dropped.

## Environment / tool-level

| Target | Outcome | Date | Follow-up |
|---|---|---|---|
| Firecrawl (MCP, keyless) | "Anonymous keyless access is unavailable for this request" for both `scrape` and `search` on this network path | 2026-11-02 | Substituted with Jina Reader + Tavily extract + raw fetch for the entire phase. Re-test if a Firecrawl API key is later approved; never bypassed. |
| Exa web_search (free MCP tier) | HTTP 429 / `-32000` rate limit after ~6 combined calls in liquid + composition sessions | 2026-11-02 | Switched to Tavily search + direct fetch; no candidates lost. |
| Code Mode sandbox | `setTimeout` and `AbortController` unavailable (ReferenceError) — earlier demo batches and one transitions batch initially failed | 2026-11-02/03 | Retried with `browser_wait_for({time})` and plain fetch (no signal); all succeeded. |
| Playwright MCP arg requirements | `browser_console_messages` requires `level`; `browser_take_screenshot` requires `scale` | 2026-11-02 | Encoded into AGENT_ENGINEERING.md as a skill footgun. |
| GitHub unauthenticated API | Budgeted at ~60 req/h per IP; several licence batches hit late in phase — future work should token-ise | 2026-11-03 | Reduced to targeted batches. |

## URL-level failures (kept for honesty)

| URL / target | Outcome | Date |
|---|---|---|
| `alex8224298/Awesome-Web-Effects` (GitHub repo guess) | 404 — repo moved/renamed or name wrong; **not counted** as a discovery | 2026-11-02 |
| `sghall/awesome-webgl` | 404 | 2026-11-02 |
| `PavelDobryakov/WebGL-Fluid-Simulation` (misspelling) | 404 → corrected to **PavelDoGreat** | 2026-11-02 |
| `motion-primitives.dev` | DNS/422 unresolvable via Jina | 2026-11-02 |
| `brunosimon/folie-sdk` | 404 | 2026-11-02 |
| `https://tympanus.net/Development/LiquidDistortionEffects/` (guess) | 404 → correct demo page located via article: `/Development/LiquidDistortion/` (200) | 2026-11-03 |
| `https://tympanus.net/Tutorials/InteractiveWebGLHoverEffects/` (guess) | 404 → actual pattern `/Tutorials/webgl-mouseover-effects/step1.html`, `step3.html` (both 200) | 2026-11-03 |
| `codrops/kinetic-typo` (guessed repo name) | GitHub API 404; demo exists at tympanus.net — repo field left empty rather than guessed | 2026-11-03 |
| `https://raw.githubusercontent.com/shshaw/Splitting/master/src/lib/index.js` | 404 → correct source at `/master/dist/splitting.js` (200) | 2026-11-03 |
| `https://raw.githubusercontent.com/PavelDoGreat/WebGL-Fluid-Simulation/master/webgl.js` | 404 — actual main source is `script.js` (51,849 bytes, 200) | 2026-11-03 |
| `https://raw.githubusercontent.com/evanw/webgl-water/master/LICENSE` | 404 — no licence file at that path → `webgl-water` recorded `unverified` instead of guessing | 2026-11-02 |
| `https://codepen.io/georgedoescode/pen/oNzamjV` | 403 — CodePen blocks direct fetch; blob pen candidate **dropped** (its parent dev.to article was verified but the pen was not) | 2026-11-02 |
| `https://www.ray-ban.com/usa/l/discover-meta-ray-ban-display` | HTTP 403 anti-bot — composition candidate abandoned | 2026-11-02 |
| `https://www.bmwgroup.com/en/report/2025/index.html` | fetch timeout — composition candidate abandoned | 2026-11-02 |
| `https://neal.fun/the-deep-sea/` | 404 — wrong slug; correct `https://neal.fun/deep-sea/` (200) recorded instead | 2026-11-02 |
| Codrops stagger-reveal demo URL | Article HTML fetched but no demo link found (JS-injected) → `demo_url` left empty, not guessed | 2026-11-03 |
| Several Smashing-magazine CodePen widget IDs (abQGGew, wvQOJrZ, vYQPxWr, wvQOJmb, YzRgZvj) | Extracted from article HTML but not individually verified → not recorded as candidates | 2026-11-02 |
| "Mark Kozlov" (particles) | No such developer — real author is **Mark Kellogg** (`mkkellogg/Photons2`); search mistake documented | 2026-11-02 |
| "Demonix-projects" | Unverified org; only an unrelated gist found → not recorded | 2026-11-02 |
| `parallax-depth-of-field` raw index.html | Not fetched this pass → handbook entry recorded browser-only (source available next pass) | 2026-11-03 |

## Licence-level blocks (not failures, but action-limiting)

- **No-licence repos verified**: `codrops/ImageRevealHover`, `codrops/AnimatedGridPreviews`,
  `codrops/BlockRevealers`, `codrops/MorphingPageTransition`,
  `codrops/AmbientCanvasBackgrounds`, `codrops/codrops/TextDistortionEffects`,
  `odina101/kinetic-text-3d`, `nitin42/react-text-fun`, `koji014/interactive-droplets`,
  `akella/webgl-mouseover-effects` — wait, correction: akella **is MIT** (verified);
  the no-licence set is the five Codrops repos above (+ our `robin-dela/flowmap-effect`,
  `vaneenige/scroll-transitions-webgl`, `brunosimon/my-room-in-3d`).
- **GSAP** (greensock/GSAP, ★30k): custom "GSAP Standard No-Charge License" — free
  to use in YOUR project, not redistributable; reflected in LICENSES.md.
- **Shadertoy** — not mined this pass; redistribution/texture policy documented as an
  unresolved question in LICENSES.md.
