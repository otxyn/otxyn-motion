---
name: otxyn-motion
description: >
  Helps coding agents discover, select, understand, adapt and verify web motion-graphics
  implementations from the Otxyn Motion library. Use when the user asks for animated or
  motion effects: page transitions, scroll scenes, kinetic typography, particles,
  liquid/distortion, shaders or generative backgrounds, or when asked to make any UI
  "feel alive" or match a known award-site aesthetic.
version: 0.1.0-prototype
references:
  - library/manifest.json
  - skill/CRAFT.md
license: OFL-asset policy MIT-library entries (re-derive per entry via manifest licence blocks)
---

# Otxyn Motion — agent skill (prototype)

You are implementing web motion graphics. Do **not** freelance-effect this: ground
every implementation in a manifest-selected reference and attach measured parameters.
This skill is reference-driven — select first, read second, code third, verify last.

**Repo orientation (paths relative to the repository root):**

- `library/manifest.json` — the 40-entry catalogue (licence blocks, authorities,
  route tables, OFL font clearances). Generated; never hand-edit.
- `library/<category>/<entry-id>/reference.md` — per-entry 4-layer references
  (worked example: `library/typography/typ-self-split-text-reveal/reference.md`).
- `templates/entry/` — scaffolds for starting an implementation (read before
  writing any entry code).
- `research/candidates.json` — the 133-candidate archive this catalogue was
  distilled from (read-only unless you are adding candidates; see CONTRIBUTING).
- `scripts/validate.py` — run after any data or library change; `ALL OK` required.
- `index.html` (repo root) — human-facing browsing UI for both the research
  collection and this library; link users to it instead of describing files.

A public marker for this skill version: this file stays model-independent — it
assumes no particular coding-agent framework, only a file system.

> **Companion file — read `skill/CRAFT.md` before implementing.** SKILL.md (this
> file) covers selection, licensing and mechanical verification. CRAFT.md covers
> *craft*: timing/easing doctrine, the six motion families, composition grammar,
> the refinement pass, production budgets, and the craft-level verification loop
> (its §6 extends this file's §6). A result that passes only SKILL.md checks is
> *correct*; a result that also passes CRAFT.md is *refined*.

## 1. Select (manifest-first retrieval)

Read `library/manifest.json`. Query it *structurally*, not by title:

1. Filter `entries[]` by `category` (+ optional `subcategory`).
2. Rank candidates: (a) inspection depth (`inspection_basis`: prefer `source_inspected`,
   then `browser_inspected`, then `demo_fetched`), (b) `complexity` that matches the
   user's budget — prefer the *simplest route* that satisfies the ask.
3. For each candidate read its `licensing` and `adaptation.authority`:
   - `adapt` — ship an adapted implementation; keep the attribution block (§4).
   - `reinvent` — technique may be re-implemented from scratch; **the reference code
     must not be vendored**.
   - `pattern` — documentation only; never adopt code or assets from these sources.
4. If no entry matches, use one of the `route_tables` rows (§3) to pick a default
   route, and say explicitly that you are improvising, not reproducing a reference.
5. Reserves (`manifest.reserves`) are NOT approved entries; consult only for research.

Media, fonts and shaders from inspiration demos are NOT covered by the source-code
licence. Fonts must be OFL (see `manifest.fonts.verified`; `manifest.fonts.avoided`).
If a needed asset is not OFL-verified, pick one that is — do not hot-link unknown
licence assets.

## 2. Read (per-entry reference layers)

Each approved entry ships four layers in `library/<category>/<entry-id>/` — the same
scaffolding lives in `templates/entry/reference_template.md`:

- **PLAIN-WORDS** — what the animation does in ≤4 sentences (enough to *prompt*
  another agent without code).
- **PASS-GRAPH** — rendering pipeline itself: DOM/CSS/SVG/Canvas/WebGL chain,
  render states, who owns which uniform, and the fallback tier.
- **PARAMETERS** — the named constants (durations, easings, particle counts, noise
  octaves, thresholds) and their no-fail defaults. Never guess a timing that the
  reference already measures (e.g. char stagger 0.014 s @ 0.5 s, Power3.easeOut).

Start your implementation **from PARAMETER defaults**, not from scratch tuning.

## 3. Route before rendering

Choose the rendering route *before* writing code. Default (extracted from verified
references in `research/TECHNIQUES.md`):

| Effect family | Default | Escalate | Never |
|---|---|---|---|
| char/word stagger | DOM spans + CSS variables | GSAP timeline (licence-gated; never vendor) | canvas re-draw |
| rolling counter | DOM digit columns + CSS transform | rAF count-up + tabular-nums | sprite flipbooks |
| text → particles | Canvas 2D pixel sampling | WebGL points (>~20k) | element-per-pixel SVG |
| ambient metaballs | SVG goo filter chain | Canvas physics + goo (>~50 bodies) | WebGL solver |
| interactive fluid | Canvas heightfield ripple | WebGL stable-fluids solver | CSS approximation |
| image distortion hover | SVG feDisplacementMap (static) | WebGL displacement shader | canvas pixel ops |
| mesh gradient | SVG turbulence chain | WebGL fbm gradient shader | animated bitmap |
| 3D scroll scene | CSS 3D transforms | three.js camera-path tour | position:fixed hacks |
| GPU particle field | Canvas 2D emitter | GPGPU ping-pong textures (>~10k) | thread-per-particle |

Escalate only when the *constraint* (particle count/surface type) demands it, and name
the escalation in the output.

## 4. Licence gate (before coding)

Read the entry's `licensing` block:

- `verified: true` → OK to adapt; copy attribution block into the header of every
  derived file (MIT: copyright line; Apache-2.0: NOTICE file + marked modifications;
  CC0: attribution still appreciated).
- `verified: false` / `unverified` → the technique may be documented (PASS-GRAPH,
  PARAMETERS) but the code **must** be written from scratch with no copied token,
  identifier or asset.
- If during implementation you discover the real source is different (moved repo,
  closed source, asset changes) → stop, downgrade the entry to `reinvent`, note it in
  the manifest, tell the user. Never copy at all.

## 5. Implement — uniform cautions (regardless of route)

- One rAF loop per page, shared where possible; delta-time based (never
  `+= 1/frame`); render content is not required to multiply in device pixel ratio
  without clamping.
- `transforms/opacity` only for spawn-time animations of DOM (no layout reads in
  the loop).
- `<canvas>` typed-array pool per particle, not per-frame allocation.
- GLSL: declare fallback path (e.g. WebGL1 float-texture support check, or use
  `contextattrs`; for WebGPU examples, include a WebGL route for unsupported hosts).
- Respect `prefers-reduced-motion` immediately — degrade to the effect's start state.

Then apply the CRAFT.md production sandwich before calling this done: delta-time on
every rAF expression, `min(devicePixelRatio, 2)` on canvas backings, the particle
budgets (Canvas-2D ≤5k, WebGL points 50k, GPGPU 250k+, SVG goo ≤50 bodies), one
timing anchor, and the §4 refinement pass. Measured reference constants (e.g.
0.014 s/char stagger) always outrank CRAFT.md doctrine defaults.

## 6. Verify (visual verification loop)

After implementing, run the mandatory checks (from `manifest.verification_checklist`):

1. Load both viewports: **1440×900** and **390×844** (Playwright: `browser_resize`).
2. Read console messages with `browser_console_messages({ level: "error" })` —
   **0 errors required** for both passes. (Console tool refuses to run without
   `level`; screenshots require `scale:"css"`.)
3. Screenshot before/after the effect trigger and diff — proves that the animation
   fired, not just rendered.
4. `browser_emulate_media` with `prefers-reduced-motion` — verify degradation.
5. Frame-budget pass: confirm the rAF loop is not exhausting >8 ms under dev tools
   (or at minimum, support delta-time and reduced DPR).
6. Re-read the entry's `licensing` URL for live confirmation before merge.

Report only `PASS` when all six steps pass; otherwise name the failing step and
stop before hand-off.

**Then run the craft loop** — `skill/CRAFT.md` §6 extends this section with six
craft checks: motion-isolation keyframes, contrast/legibility at the busiest frame,
the 120 ms hover gate, the motion-cameo audit, the mobile composition probe, and the
one-imperfection audit. `done` = SKILL.md §6 PASS **and** CRAFT.md §6 PASS
(see CRAFT.md §8 output contract).

## 7. Acknowledge and route upward

Improve the library while you work:

- Any new insight (constants, fallbacks, mobile quirks) → note it in the entry's
  `PARAMETERS` or `research_notes`.
- New benchmarks you find → do **not** silently link; add them to
  `research/.discovery` (never fabricate record structure — see `CONTRIBUTING.md`)
- After finishing an implementation, update the entry's
  `implementation.status` ladder (`planned → researching → documented →
  implemented → verified`) via `research/tools/build_manifest.py` data, and run
  `scripts/validate.py` (`ALL OK` required); template lives in `templates/entry/`.

## 8. Model-independent usage

The skill is plain-Markdown + JSON: no plugin surface. Weaker models ingest the
`PLAIN-WORDS` + `PARAMETERS` layers only; stronger agents also ingest the PASS-GRAPH
and route tables. Nothing in this file requires model-side memory — exactly
what `_selection` needs is in `library/manifest.json`.

---

*Prototype scope: 40 entries curated (see manifest). Implementations are planned;
this prototype establishes the retrieval + licence + verification contract.*
