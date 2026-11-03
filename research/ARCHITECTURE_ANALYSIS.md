# ARCHITECTURE_ANALYSIS — How existing motion collections work (and Otxyn's opportunities)

Analysis date: 2026-11-02. Evidence basis: direct repo inspection (GitHub Contents API,
raw README/llms.txt), API metadata verification, and site fetches listed in SOURCES.md.

## 1. The four architecture archetypes found

### A. Curated link lists (awesome-web-animation)
- **Organisation:** flat categories of external links; no demos of their own.
- **Preview:** none; reader follows out (link rot risk).
- **Source:** none provided.
- **Metadata:** one-line descriptions; no machine-readable manifest.
- **Agent support:** zero (lists are for humans).
- **Missing:** technique docs, licences, licensing tracking.

### B. Live-handbook with prompt-first agent support (**animation-handbook** — the benchmark)
- **Organisation:** `animations/<NN-category>/<technique>/`, plus `famous/` recreations in one repo; static site on GitHub Pages.
- **Preview:** every entry is a live, self-contained standalone `index.html` that runs offline (dependency-free; no build).
- **Source:** full code per technique in the same folder; a per-technique README documents *how it works, values that matter, production notes*.
- **Metadata:** `llms.txt` machine-readable catalogue; hero badge counts; per-technique "plain settings" sliders that parameterise the *prompt text*.
- **Agent support:** explicit — "ready-made prompt for your AI assistant" (verbatim: plain words, no code), installable skill via `npx skills add`, `.claude-plugin/`, `skills/` dir, `CLAUDE.md`, `tests/`.
- **Key discovery:** their agent prompts are **deliberately code-free** — the AI must reinvent code from description. That is the main quality ceiling this architecture imposes and **Otxyn Motion's primary differentiation opportunity** (see §3).

### C. Copy-paste component kits (motion-primitives, magicui)
- **Organisation:** registry manifests (components keyed by ID, install via CLI), React-centric.
- **Preview:** site gallery with live interactive previews; code shown inline.
- **Source:** MIT-style code vendored into user projects.
- **Metadata:** registry/manifest JSON — the strongest machine-readability pattern observed.
- **Agent support:** incidental (registry helps trained agents; no prompts, no technique docs).
- **Missing:** technique explanations, non-React plain-web versions, animation parameter docs.

### D. Article+repo per technique (Codrops)
- **Organisation:** editorial article + demo page + repo per effect (`tympanus.net/Development/…`).
- **Preview:** full-bleed live demos.
- **Source:** MIT in sample; repo quality varies; some sample repos had **no licence file** (verified).
- **Metadata:** none standardised.
- **Missing:** searchable index across repos, docs of parameters, agent files; discoverability relies on article SEO.

## 2. What all of them miss (cross-cutting gaps)

1. **Code-level, parameterised documentation** — even the handbook's per-technique README stops before code fingerprints (uniform names, tuning constants, fallbacks). Agents still have to guess/every-time re-derive shaders, easing laws, stagger math.
2. **Render-technique routing.** No collection tells an agent *when* a thing must be CSS vs SVG vs Canvas vs WebGL vs WebGPU — the #1 failure mode for average models.
3. **Verification loops.** Nobody documents a screenshot/console-error self-check loop for the implementation model.
4. **Licence provenance surfaced per entry.** Collections embed third-party work without licence callouts ( Webster sample: codrops repo without licence; awards pages show work of studios with no source).
5. **Non-React breadth.** Component kits are React+TS-only; handbook is vanilla; no kit serves the "plain web + adapt-with-ease" niche with structured docs.

## 3. Concrete opportunities for Otxyn Motion

Let me define Otxyn positioning against the gap list (research-grade recommendations, decisions later):

1. **Parameterised reference code per entry** (short, heavily-commented, named constants, low/medium/high render paths) — complements rather than copies animation-handbook's no-code prompts. Position: `PROMPT (plain words) + HOW (architecture) + CODE (parameters + fallbacks)`.
2. **Route guidance table per area:** e.g., split-text → CSS+GSAP > DSP? char-split canvas; flow field → canvas2D unless >5k particles; metaballs gooey filter; displacement → WebGL; raymarch → GLSL/WebGPU — encoded in `skills` metadata (area-specific, machine-readable).
3. **Verification loop doc**: `playwright snapshot → console check → rect/opacity probe` recipe (viewport pairs: 1440×900 and 390×844).
4. **Provenance-forward manifest**: per-entry `license`, `license_url`, `assets_verified`, `adaptation_level` (learning vs copied) — published alongside previews.
5. **Manifest-first agent UX:** `library/manifest.json` + one-file-per-entry references with reduced context — the pattern motion-primitives' registry already proves works with agents; apply it for motion.

## 4. Data table — displayed evidence

| Collection | Live demos | Per-entry docs | Machine metadata | Agent files | Licence per entry | Params in docs |
|---|---|---|---|---|---|---|
| awesome lists | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| animation-handbook | ✓ | ✓ (mechanism, values, production notes) | llms.txt | ✓ skill+prompts | MIT repo-wide | prompt settings, not code params |
| motion-primitives | ✓ | ✗ (API text) | registry ✓ | partial (registry) | ✓ MIT | component props |
| Codrops | ✓ | article-level | ✗ | ✗ | repo-by-repo | ✗ |
| MagicUI | ✓ | ✗ | registry ✓ | partial | ✓ MIT | props |
| *(Otxyn target)* | ✓ | ✓ mechanism **and** code | manifest ✓ | ✓ skill | ✓ per entry | ✓ named constants |

*(This table will be re-validated in Stage 5 once agent findings land; no rows are speculative beyond the sample verified above.)*
