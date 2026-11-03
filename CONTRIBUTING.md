# Contributing to Otxyn Motion

## The rule that governs everything

**Research candidates are not library entries.** The research archive
(`research/candidates.json`) is a growing lead database. The library
(`library/manifest.json`) is a small curated catalogue. An idea moves from one to the
other only via the curation placeholders in `research/tools/build_manifest.py` — the
manifest's roster is authored there, then validated.

## Changing data

- `research/candidates.json` is the **canonical** research database. Edit only this;
  never hand-edit `research/candidates.csv` (it is generated: `python
  scripts/gen_candidates_csv.py`).
- `library/manifest.json` is **generated** by `research/tools/build_manifest.py`.
  To change the roster or licence blocks, edit the `ROSTER`/data structures in that
  script and re-run it. Never hand-edit the manifest.
- Per-entry `reference.md` files in `library/<category>/<entry-id>/` are hand-authored
  after the scaffold stage; the generator (`scripts/gen_entry_references.py`) only
  fills scaffolds from manifest data and will overwrite manual late-stage work if
  re-run naively on a `planned` entry — check the entry's implementation status first
  and only re-run it for entries still `planned`.

## Adding a research candidate

1. Verify the source URL actually resolves (HTTP 200 or real-content extraction) —
   **never** record a fabricated URL, name, licence or technique.
2. Record inspection truthfully (`source_inspected` / `browser_inspected` are boolean
   claims with date + confidence). Missing values must be `unknown`/`not_inspected`.
3. Never bypass paywalls or CAPTCHAs to inspect.
4. Run `python scripts/validate.py` before finishing your change.

## Adding / implementing a library entry

Read [`skill/SKILL.md`](skill/SKILL.md) (selection → licence gate → two-stage
verification) and [`skill/CRAFT.md`](skill/CRAFT.md) (craft doctrine) end to end
first. Then follow [`templates/entry/README.md`](templates/entry/README.md).

- Licence gate: only MIT / Apache-2.0 / CC0-1.0 sources may be adapted. Anything else
  is `reinvent` (technique documented, code written from scratch) or `pattern`
  (documentation only).
- Fonts are OFL-only, verified against `google/fonts/*/METADATA.pb`, as recorded in
  the manifest `fonts` block.
- Implemented entries pass both SKILL.md §6 (mechanical: viewports, console, reduced
  motion, frame budget, licence re-check) and CRAFT.md §6 (craft) before `verified`
  status may be claimed.

## Pull-request checklist

- [ ] `python scripts/validate.py` passes with **ALL OK**
- [ ] Data edits come from the canonical JSON, not the CSV
- [ ] No third-party code or assets copied without a verified licence block
- [ ] Attribution preserved for every referenced creator
- [ ] New claims (counts, constants) are measured, not asserted
