# Otxyn Motion

A curated, evidence-based **motion-graphics research library** for the web — plus an
agent skill that teaches coding agents to select, adapt, and verify web motion effects
at award-quality craft level.

Repo contents, in three layers that are logically independent but work together:

| Layer | Location | What it is |
|---|---|---|
| **Research** | [`research/`](research/README.md) | The discovery archive: 133 verified motion-graphics candidates, 37 shortlisted, inspection records, licence findings, technique documentation. Machine-readable database: [`research/candidates.json`](research/candidates.json). |
| **Library** | [`library/`](library/README.md) | The curated catalogue: 40 approved entries (kinetic typography 7 / particle systems 6 / liquid 5 / 3d & shaders 5 / transitions 7 / compositions 10) with per-entry licence-blocks, adaptation authority, implementation route tables, and per-entry reference documents. |
| **Skill** | [`skill/SKILL.md`](skill/SKILL.md) | The agent skill: manifest-first selection, four-layer entry references, licence gate, and a two-stage verification loop (mechanical + craft). Companion craft doctrine: [`skill/CRAFT.md`](skill/CRAFT.md). |
| **Website** | [`index.html`](index.html) | A dependency-free static site that lets humans browse the research collection and the library catalogue. Run `python -m http.server` and open `http://localhost:8000` (double-clicking `index.html` also works — it falls back to the pre-generated `assets/js/data.js`). |

**Key rule — the research set and the library are separate.** Research candidates are
leads with evidence; library entries are approved intents with licence-clearance.
Nothing is marked implemented that is not actually implemented: **all 40 library
entries are currently `planned`** (curation phase complete; implementation phase not
started). See [`research/reports/DATA_AUDIT.md`](research/reports/DATA_AUDIT.md) for
the verified figures behind every number in these docs.

## Status of honesty

- Every candidate record says what was actually verified
  (`discovered` / `inspected`; per-record `source_inspected`, `browser_inspected`,
  `interaction_tested` booleans + date + confidence). Missing values are
  `unknown` / `not_inspected`, never invented.
- Licence findings carry evidence URLs; 89 of 133 candidates remain licence-unverified
  and are blocked from library adoption until resolved.
- Preview screenshots are Playwright captures of inspiration demos, kept for internal
  evidence only — they are not assets we own or redistribute.

## Quick start

```bash
# validate the whole repo (JSON, CSV parity, unique IDs, manifest invariants,
# internal links, preview paths, skill references, licence metadata)
python scripts/validate.py

# regenerate research/candidates.csv from the canonical candidates.json
python scripts/gen_candidates_csv.py

# regenerate all per-entry reference scaffolds from the manifest
python scripts/gen_entry_references.py

# regenerate the website data bundle from candidates.json + manifest.json
python scripts/gen_website_data.py

# serve the website
python -m http.server 8000
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Short version: candidates are not entries,
income values are only measured ones, licences gate everything, and every data edit
goes through the validation script.
