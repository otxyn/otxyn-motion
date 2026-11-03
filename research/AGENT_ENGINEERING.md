# AGENT_ENGINEERING — Why AI coding models fail at motion, and what Otxyn must give them

Written 2026-11-03 from the evidence of this research phase: what it took a real
agent pipeline (OpenCode + Tavily/Exa + GitHub API + Playwright + multiple LLM
subagents) to find, verify, understand and document a motion implementation —
plus observed library-side documentation patterns (animation-handbook's
"no-code prompts", Codrops' code-bearing articles, component registries).

## 1. Observed failure modes (with evidence from this research)

1. **Defaulting to the most familiar rendering route.** Asked for "liquid", a model
   writes a CSS border-radius blob; the correct route is a displacement-map shader
   or an SVG goo filter (the difference between amateur and award quality). Evidence:
   the liquid category has 4 distinct routes (DOM filter / SVG filter / Canvas
   heightfield / WebGL solver) and most sites this survey inspected pick a
   *deliberate* one (see COVERAGE_MATRIX categories for `liquid`).
2. **Timing/easing invented per attempt.** The stagger recipe that actually ships:
   stagger 0.014s/char, 0.5s/char duration, Power3.easeOut (`typography-009` source
   constants). Models that improvise these constants produce "AI-looking" stagger.
   Same discipline needed for spring stiffness, wave phase, noise octaves.
3. **Shader copy-paste breakage.** When models hand-write GLSL they mix up attribute
   names, don't wire ping-pong frame buffers (—met in GPGPU particle architecture,
   `particles-025`), and forget fallbacks (float texture support). What they need:
   the *pass graph*, not shaders alone (see `liquid-001` solver stage order).
4. **Uncontrolled `requestAnimationFrame` loops + DPR overwork.** Multiple inspected
   demos guard this (delta-time, DPR clamp). Models rarely do, producing
   battery-melters on mobile.
5. **Composition blindness.** Good sources compose via *data-driven scenes*
   (folio-2019 scene configs, `composition-005`) rather than individual effects.
   Models assembling three bespoke effects produce incoherence unless given
   "composition grammar" (shared palette, shared easing, one interaction idea).
6. **Licensing/provenance absent from models' vocabulary.** Several popular repos
   found in this research have **no licence** (BlockRevealers, ImageRevealHover,
   AmbientCanvasBackgrounds, oframe/ogl, SplitType…) — harmless to a human browsing,
   dangerous when a blind copy-paste lands in a release. See LICENSES.md.
7. **Search-to-source decay (sub-agent reliability).** Pure LLM subagents died
   mid-flight (free quota) and tended to accept snippets as evidence. Bottom-up
   structural mining (repo file listing → raw files → fingerprints) held up better
   and was cheaper in web-request budget.

## 2. What this survey proved about making agents succeed

- **Structured parameterised references beat prose.** The single most
  "engineered" improvement candidates found here all expose named constants and
  clean pass graphs — what the model needs to *not improvise is the arithmetic*.
- **Fingerprint verification works cheaply.** A tiny keyword fingerprint
  (rAF? canvas? gl_FragColor? pointermove? noise?) over a raw file both
  *verified* the technique and is machine-checkable. The same fingerprint checks can
  drive automated library QA during the implementation phase.
- **Visual verification loops catch what docs miss.** 22 of this round's browser
  inspections produced zero console errors *and* real screenshots at both required
  viewports (1440×900, 390×844). Playwright's quirks (console with `level`,
  screenshot with `scale`) are exactly the kind of footgun a skill must encode.
- **Route-selection must be opinionated.** "Route tables" that say when to use
  CSS vs SVG vs Canvas vs WebGL are the missing documentation that higher-quality
  demos imply (e.g. stick to SVG goo below ~50 particles; WebGL above 1M).

## 3. Recommended skill architecture (for `skill/SKILL.md`)

1. **Manifest-first retrieval** (`library/manifest.json`): id, category,
   subcategory, complexity, rendering route, licence — machine-readable, so the
   agent selects via structured query, not trial and error.
2. **One reference file per effect**, in three mandatory layers:
   - *PLAIN-WORDS PROMPT* (what the animation does; ≤4 sentences — the layer
     animation-handbook proved works for prompting);
   - *PASS GRAPH* (rendering steps + uniform/state ownership);
   - *PARAMETERS* (named constants: durations, easings, particle counts, noise
     octaves, fallback thresholds, no-fail defaults).
3. **Per-category route tables** (§4) with default参数 choices that guarantee a
   passable result even when parameters are guessed.
4. **Verification checklist every effect must run in-browser:**
   - console errors === 0 at 1440×900 and 390×844;
   - screenshot diff between "on" and "off" states to prove the effect fired;
   - reduced-motion check: does `prefers-reduced-motion` collapse it to a still?
5. **Licence gate built into selection.** The skill reads per-entry licence metadata;
   entries without verified licence are blocked from adoption (this research's own
   gate stopped storytelling duplicates from e.g. Unseen's no-licence sites).
6. **Budget discipline defaults.**interrogate ≤40 requests/subject; batch fetches;
   fallback extraction chain (raw fetch → Tavily extract → Jina) when a host 403s.

## 4. Draft route table (from inspected sources)

| Effect family | Default route | Escalate to | Never use |
|---|---|---|---|
| Char/word stagger | DOM spans + CSS vars | GSAP timeline (licences pending) | Canvas text re-draw |
| Rolling counter | DOM digit columns + CSS transform | rAF counter w/ tabular-nums | Image-sprite flipbooks |
| Text→particles | Canvas 2D pixel sampling | WebGL points >20k | SVG circle-per-pixel |
| Ambient metaball | SVG goo filter | Canvas physics + goo | WebGL solver (overkill) |
| Interactive fluid | Canvas heightfield ripple | WebGL stable-fluids (`liquid-001`) | Some CSS approximation |
| Image distortion hover | SVG feDisplacementMap (static) | WebGL displacement shader | Canvas pixel ops |
| Mesh gradients | SVG turbulence chain | WebGL fbm mesh-gradient | Animated JPG |
| 3D scroll scene | CSS 3D transforms | three.js camera path | Position:fixed hacks |
