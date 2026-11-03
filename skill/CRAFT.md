# CRAFT — Instructions for getting from "an effect that works" to "refined, advanced, award-quality motion"

Companion instruction file for `skill/SKILL.md`. SKILL.md handles *selection,
licensing and verification* (the mechanics). This file handles *craft* — the layer
that separates a generic "AI-looking" animation from polished, deliberate motion
graphics. Every rule in here exists because a violation of it is observable in the
verified research references (`research/TECHNIQUES.md`, `research/candidates.json`)
or produces a recognisable failure mode. Constants cited come from sources actually
read during research; everything else is craft doctrine to apply with judgement.

---

## 0. The five ceilings (what stops agents from ever reaching quality)

Fix these before you touch any parameter:

| Ceiling | Symptom | The fix in practice |
|---|---|---|
| **Route ceiling** — wrong rendering tier | Canvas-2D drawing 50k particles; WebGL for a 3-counter page | Run the SKILL.md route table *first*; escalate only when the constraint demands it |
| **Timing ceiling** — invented constants | stagger of 0.1 s/char, eases that "snap flat" | Adopt the reference's measured constants, or the defaults in §1 |
| **Composition ceiling** — effects that fight each other | three separate animations, three curves, three colours | §3 composition grammar: one idea, one tune |
| **Polish ceiling** — technically right, visually cheap | flat colours, no depth, no texture | §4 refinement pass (texture, light, depth, imperfection) |
| **Consistency ceiling** — works on dev, breaks production | janky on mobile/low-DPR, ignores reduced-motion | §5 production sandwich (+ §6 tool-verified loop) |

---

## 1. Timing and easing doctrine (measured + doctrine)

### Measured constants (use these when in doubt — they come from shipped work)

| Constant | Value | Provenance |
|---|---|---|
| Per-char stagger | **0.014 s** | Codrops stagger-reveal tutorial (`typography-009`), read from source |
| Per-char duration | **0.5 s** | same source |
| Stagger family ease | **Power3.easeOut** | same source |
| Char-reveal translate | rise from ~10–25 % of `em` height, not 100 % | handbook split-text-reveal (`typography-011`, source inspected) |
| Decoding cycle (scramble) | per-char resolution order **random ≈ left→right mean**, not uniform instant | handbook scramble-text (`typography-015`) |

Derivative defaults (doctrine from observed behaviour, not novel inventions — mark
them as *defaults*, tune only when a reference measures otherwise):

- Stagger sub-second families: 0.008–0.02 s/char; **0.02 s** feels premium but slow
  beyond ~24 chars → cap the *total* stagger (never more than 0.7 s of whole-word stagger drift).
- Opacity eases faster than spatial eases (typical: opacity `t_out.duration * 0.6`);
  fades that run the full duration read "ghostly".
- **Ease pick order** (strongest→most subtle):
  `spring/overshoot` (playful, product demo) → `expo.out` (for spans >400 ms, modern)
  → `Power3.out` (general field work) → `linear` (keeping rhythm — loops, waves,
  counters/scales only) → `cubic-bezier(0.65, 0, 0.35, 1)` (a neutral "precise" out).
- **Loops must close exactly** (wave-layers `typography-025`: layer speeds differ
  but every loop closes): for sine-based loops, ensure `phase = n * 2*pi` over one
  cycle is integer-valued; add tiny per-loop drift (±1 px) only if it travels a full
  cycle before reversing.

### Rhythm rules

- One timing "anchor" per page (a house easing+duration that the whole page orients
  around — pick it, state it, re-use it everywhere).
- Page-spanning entrance beats: hero (0 ms) → support elements (+80–160 ms) →
  interactive affordances (+200–320 ms). Nothing animates at 0 ms *and* 1.4 s —
  if you need >1 s of choreography, slice it into 3 beats over 350 ms windows.
- Speed of the composition, not the element: does the *composition* arrive at a
  resting state that visually allows the reader to begin? If not, shorten.

## 2. Motion families (choose the *idea*, then execute)

1. **Reveal** (text, image, content stage) — mask/clip/opacity+translate family.
   Refined = the mask's shape *matches the content box*, and the masking motion
   is *revealed-not-imposed* (content doesn't move while the mask travels).
2. **Stagger/wave** (chars, list rows, tiles) — refined = a *travelling wave*
   (index-delayed transforms) with consistent distance per item.
3. **Reposition** (counters, sortings, cards) — refined = FLIP-style transform
   between two measured states, no layout reads inside the loop.
4. **Ambient** (blobs, fluid, mesh gradients, noise fields) — refined = *slow*
   (2–6 s periods), *muted* (≤15 % contrast delta vs base), never near CTA text.
5. **Interrupt** (pointer, hover, click feedback) — refined = responds to *velocity*
   not just position (see `3d-shaders-007`'s velocity-parameters). Velocities
   drive magnitude; positions only set the *target*.
6. **Combinatorial** (compositions) — see §3.

## 3. Composition grammar (multi-effect pages)

- **One idea per composition.** Pick one motion metaphor (fluid / particles / type /
  light / 3D depth) and let every effect be *that one* at a different scale. A fluid
  hero + particle bursts + 3D flip cards = three metaphors; the measured award-world
  pattern (folios, suite pages like Chrome Music Lab `composition-030`) is one
  metaphor behaving differently at different depths.
- **Shared tune:** one primary easing family, one duration grid (e.g. 0.2/0.4/0.8 s),
  one hue accent + one base field. Everything outside the grid must *interrupt*
  (state-driven) rather than decorate.
- **Hierarchy before motion:** the *hero* of the composition gets motion; secondary
  items get stillness or a *derived* echo (same curve, lower amplitude, delayed).
  Re-read folio-2019's scene-config pattern (`composition-005`): sections are data,
  the motion engine treats every section uniformly.
- **Contrast kit:** for each element decide its *motion role*: hero / echo / static /
  ambient. No role duplication on adjacent hierarchy levels.
- **Rest state is a design surface.** After the finishing beat, the composition must
  arrive at a *composed, readable* state — not a motion-free weird world.

## 4. Refinement pass (the polish layer)

Apply after the effect works; this is what "refined" means.

1. **Texture, not flatness.** Flat pure-color fields read as cheap. Add *either*
   subtle film grain (canvas: 1-pass random alpha 2–4 %, seeded) *or* a dithered
   gradient/gradient-noise — never both. Shader routes: add a low-contrast fbm
   overlay (≤8 % intensity) or scanline-free noise pass (`3d-shaders-002` family).
2. **Light and depth stack:** 1) a dark vignette (≤15 % falloff), 2) one dominant
   light direction (shaders: one specular/fresnel term), 3) background element at
   5–10 % of foreground luminance delta. Depth = *atmosphere*, not blur+scale.
3. **Easing in margins:** the first and last 10 % of every transform must be
   near-imperceptible (that is what ease curves *are*). If an element visibly
   starts or halts, your ease is too short — lengthen duration before you change curves.
4. **Overshoot budget:** ≤2 % of distance for UI elements; ≤6 % for playful
   hero moments; never on text (text overshoot wobbles the letterforms).
5. **Follow-through/secondary:** moving element *B* inherits *A*'s easing but at
   70 % amplitude and +1 beat delay; the *only* legal secondary motion is a single
   scale-less (opacity/translate-only) echo.
6. **Imperfection (1 bit):** one subtle imperfection per composition — grain,
   hand-held noise jitter (≤1 px), chamfered corner, or an off-axis element.
   Two imperfections is noise; zero is plastic.
7. **Colour contract:** base/dominant colour ≥60 % of canvas; accent ≤10 %;
   then a midtone bridge. Motion "alerts" use the accent; ambient motion stays in
   base/mid tones. Verify with the screenshot diff (contrast check).
8. **Micro-interaction canons:** hovers respond visibly ≤120 ms (spring); press ≤180 ms with
   ~0.96 scale; focus rings ≥3 px; tooltips 150–260 ms with directional ease-out;
   prefers-reduced-motion collapses every hover/entrance to opacity-only ≤80 ms.

## 5. Production sandwich (mobile, DPR, accessibility)

- **Delta-time everywhere.** Every rAF family expression must be
  `position = f(elapsed)` not `position += x/frame` — a low-DPR phone (30 fps) must
  travel the same arc per second as a 144 Hz display.
- **DPR clamp:** canvas backings at `min(devicePixelRatio, 2)`; shaders 1.5 on
  mobile (measure via Pixel 7/iPhone SE-class UA if needed).
- **Particle budgets:** Canvas-2D — 3k default, 5k absolute cap; WebGL points — 50k;
  GPGPU — 250k+ w/ FP texture checks; SVG goo — ≤50 moving bodies (`route_tables`).
- **Layer hygiene:** a transform doesn't compose layers; the *composited* layer
  count above the fold should be <8. Long chained transforms: batch via wrapper.
- **Battery:** page-visibility pause; `matchMedia('(prefers-reduced-motion)')`
  must stop the ambient loop entirely; positions freeze at current value
  (not a jump-to-end).
- **Type contract:** text never animates scroll-jacking layout, and never gets
  `filter: blur()` above ~1 px mid-frame on low-end devices.

## 6. The craft verification loop (extends SKILL.md §6 — run in order)

After SKILL.md's six mechanical checks pass, run a *craft* pass:

1. **Motion isolation testimonial:** screenshot at 3 equal time-points of one loop
   and confirm motion directions differ across beats (no duplicate frames in loops).
2. **Contrast/legibility keyframe:** the busiest composition frame must keep body
   copy at ≥4.5:1 against its local background (use the pixel probe if unsure).
3. **120 ms hover gate:** every interactive element responds *visibly* ≤120 ms
   (a late hover is "the page is frozen", not a design).
4. **Motion cameo audit:** remove the one non-essential effect in your head; if
   nothing weakens without it, remove it for real and re-verify.
5. **Mobile frame probe:** at 390×844 compare your composition to two beats of the
   1440×900 pass; if the mobile composition loses the *idea*, simplify the mobile
   composition instead of shrinking it (crop the metaphor, not the beat).
6. **One-imperfection audit (§4.6):** confirm exactly one intentional imperfection.

## 7. "AI-look" tells (and their instant fixes)

| Tell | Why it happens | Fix |
|---|---|---|
| Everything animates at once | no hierarchy/beats | §1 rhythm beats (80/200/320 ms) |
| Uniform stagger (starts all chars simultaneously) | stagger constant invented | 0.014 s/char measured constant (§1) |
| Everything eases linearly | sin/cos driving all motion | give hero elements spring/bounce; leave ambient linear |
| Flat mono-field colour | one hue used for everything | §4.7 60/30/10 contrast kit |
| Text blends into the background | no field contrast | vignette/glow depth of ≥10 % delta |
| Loop visibly "stitches" | loop not mathematically closed | integer-cycle parameterisation |
| Effects cluster near CTA | decoration over function | ambient ≤15 % delta, gated away from text |
| Mobile version is desktop × 0.5 | no composition rethinking | §6.5: crop metaphor, keep beats |
| No feedback at all (only entrance) | interrupt family unused | §2.5 velocity-driven interrupts |

## 8. Output contract (what "done" means)

A refined result means ALL of:

1. SKILL.md's six mechanical checks: PASS.
2. §6's six craft checks: PASS.
3. Manifest entry licence + attribution intact.
4. One house-easing grid stated in the component's `PARAMETERS` header comment;
   every timing slot filled from *measured* or *stated-default* values — no
   invented magic numbers without a `// default` note.
5. At least one entry-level craft note fed back into the library (`research_notes`).

*Doctrine in this file is a companion to — not a replacement for — the licensed,
verified references in the manifest. When a measured reference value conflicts with
these defaults, the reference wins.*
