# DATA_DICTIONARY — schema of research/candidates.json

One JSON array of 133 candidate objects. Canonical source for everything derived
(CSV, website data, statistics). All fields may be present; missing/unknown data uses
the literal strings `unknown` / `not_inspected` / empty string — never fabricated.

## Fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string, `<category>-NNN` | Unique. Verified unique by `scripts/validate.py`. |
| `name` | string | Human label of the reference. |
| `category` | enum | One of `typography` \| `particles` \| `liquid` \| `3d-shaders` \| `transitions` \| `composition`. |
| `subcategory` | string | Free-form family tag (e.g. `split-text`, `fluid-sim`). |
| `description` | string | What the effect does, technically (2–4 sentences). |
| `demo_url` | URL | Live demo (verified fetched when claimed). |
| `source_url` | URL | Article/documentation page. |
| `repository_url` | URL | Code repository when one was identified. |
| `creator` | string | Display name of the author/organisation. |
| `technologies` | string[] | Libraries/APIs involved (`Three.js`, `WebGL`, `SVG filter` …). |
| `dependencies` | string[] | Runtime third-party deps of the reference. |
| `rendering_method` | enum | One of actual values in the data: `dom` \| `css` \| `svg` \| `canvas-2d` \| `webgl-2d` \| `webgl-3d` \| `webgpu`. |
| `techniques` | string[] | Discrete technique tags used by the website filters. |
| `interaction` | string[] | Input modes (`mouse`, `scroll`, `pointer`, …). |
| `complexity` | enum | `low` \| `medium` \| `high`. |
| `responsive_status` | enum | `not_inspected` \| `browser inspected (390x844)` (only two mobile-verified records exist — honest gap to close in later phases). |
| `performance_notes` | string | Free notes (byte-size fingerprints, frame budget observations). |
| `accessibility_notes` | string | Reduced-motion / assistive observations (often empty — honest gap). |
| `preview` | object \| null | Screenshot map `{desktop: path, mobile: path}` relative to `research/`; `null` when none captured. |
| `inspection` | object | `{discovered, source_inspected, browser_inspected, interaction_tested: bool, date: ISO, confidence}` — exactly what was verified, when, with what confidence. |
| `licensing` | object | `{license, license_url, assets_verified, redistribution_allowed, notes}` — findings with evidence; `"unverified"` blocks adoption. |
| `evaluation` | object | Scored 1–10 on `visual_quality, source_quality, reusability, agent_value, integration, performance, responsive_accessibility` + derived `weighted_score` (weights in `RESEARCH_PLAN.md`: 25/20/15/15/10/10/5). `-1` means unscoreable. |
| `status` | enum | Highest gate achieved: `discovered` \| `inspected` (= opened and examined) \| `shortlisted` (= passed quality + licence gauntlet). Note: inspection *method* detail lives in the `inspection` booleans; a record's `status` may be `shortlisted` while its booleans show source+browser inspection. |
| `research_notes` | string | What the agent actually did/saw during research. |
| `otxyn_potential` | string | Judgement of fit for the Otxyn library. |

## Derived artefacts

| Artefact | Producer | Notes |
|---|---|---|
| `research/candidates.csv` | `scripts/gen_candidates_csv.py` | Flat export; do NOT hand-edit. |
| `library/manifest.json` | `research/tools/build_manifest.py` | 40 entries curated from candidates; per-entry licence blocks + adaptation authority. |
| `assets/js/data.js` | `scripts/gen_website_data.py` | Website data bundle (candidates + manifest + previews). |
| `research/reports/DATA_AUDIT.md` | `scripts/gen_data_audit.py` | Verified statistics + discrepancy notes. |

## Conventions

- Booleans inside `inspection` are strict claims: `browser_inspected: true` means a
  Playwright-class browser actually loaded the demo.
- Duplicate handling is documented, not silent: the only consolidated duplicate found
  so far is `transitions-005` ≡ `liquid-003` (same tympanus demo); the liquid record
  remains, the transitions one was dropped, and `SHORTLIST.md` records decision D.
- IDs of dropped/renumbered records are never recycled.
