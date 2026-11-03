# typ-self-split-text-reveal — entry reference

Status: `planned` (not implemented) · Authority: **adapt** · Source licence: MIT
(https://github.com/matinmonshizadeh/animation-handbook — verified via GitHub API,
2026-11-02) · Manifest record: `library/manifest.json` → `typ-self-split-text-reveal`

---

## LAYER 1 — PLAIN-WORDS

A heading splits into individual characters and reveals character-by-character —
each char animates from `y: -100%`-style organic offsets with `opacity: 0` and
staggered delays, producing a wave of letters falling into their final home. No
canvas or WebGL is involved: pure DOM spans with per-character CSS transitions.
Best for hero titles, headline entrance on landing pages.
Copyable prompt: "Split this heading into characters and reveal them one by one
with a 0.014 s stagger per char, each taking 0.5 s to rise 0.4 em from below with
an ease-out curve and opacity fade-in."

---

## LAYER 2 — PASS-GRAPH

```
[DOMContentLoaded]
  → split text into char spans (keep aria: wrap real text accessibly —
    preserve an sr-only clone or aria-label on the parent)
  → assign per-char CSS via `--i` custom properties (stagger index)
  → CSS transition-delay = calc(var(--i) * <staggerValue>)
  → translate/opacity keyframes in per char
  → (handbook implementation is dependency-free: verified fingerprints —
    DOM/text approach, 31.5 KB single-file index.html, NO canvas/GLSL,
    split + stagger + easing tokens present in source)
```

Fallback tier: when splitting is unavailable (or needs reduced JS), apply
`clip-path: inset(0 0 100% 0)` wipe per line — lower fidelity but keeps the
motion shape without introducing JS.

Reference implementation locations:
- Live: https://matinmonshizadeh.github.io/animation-handbook/animations/02-entrance-and-exit/split-text-reveal/
- Source (verified MIME `text/html`, 31,554 bytes, browser-verified with 0 console errors):
  https://raw.githubusercontent.com/matinmonshizadeh/animation-handbook/main/animations/02-entrance-and-exit/split-text-reveal/index.html
- Cross-referenced constants source (Codrops stagger article, GSAP+Splitting:
  staggerValue = 0.014, charsDuration = 0.5, ease Power3.easeOut):
  https://tympanus.net/codrops/2020/06/17/making-stagger-reveal-animations-for-text/
- Dependency reference in scope (MIT verified, `dist/splitting.js` read):
  https://github.com/shshaw/Splitting

## LAYER 3 — PARAMETERS (only measured values; no invented numbers)

| Parameter | Value | Source |
|---|---|---|
| staggerValue | 0.014 s per char | Codrops stagger article source (`typography-009`) — cross-reference template constant |
| charsDuration | 0.5 s | same |
| ease | Power3.easeOut | same |
| transform vars | translateY + opacity only (no layout thrash) | handbook split-text source fingerprint + universal pass rule |
| splitting pattern | char spans with aria clone | Splitting.js `dist` read |

Defaults to extend at implementation time (must be *read from the raw
index.html* during coding, not guessed): exact per-char order, direction,
keyframe offsets, font stack.

### Suggested implementation checklist (verify in browser after build)

- [ ] both viewports load clean (0 console errors)
- [ ] screenshot diff proves the reveal fires per char
- [ ] prefers-reduced-motion degrades to fully-visible text
- [ ] split is aria-safe: hidden true-clone or labeled parent
- [ ] no layout reads inside the reveal loop
- [ ] MIT attribution header included (see §LAYER-4 below)

## LAYER 4 — ATTRIBUTION BLOCK (must ship in the file header)

```text
<!--
  Otxyn Motion — typ-self-split-text-reveal
  Technique adapted from matinmonshizadeh/animation-handbook (MIT).
  https://github.com/matinmonshizadeh/animation-handbook
  Stagger constants cross-referenced from Codrops stagger tutorial (2020):
  https://tympanus.net/codrops/2020/06/17/making-stagger-reveal-animations-for-text/
-->
```

## Font requirement

No specific font is required. If a variable/display face is used, restrict to
manifest `fonts.verified` (OFL-only): Inter, Anton (heavy display), Space Grotesk.
