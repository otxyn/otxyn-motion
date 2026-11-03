# templates/entry — how to start a new library entry

When work begins on one of the 40 planned manifest entries:

1. Copy this folder's two templates into the entry folder
   (`library/<category>/<entry-id>/`).
2. Fill `reference.md` from the entry's manifest block + the inspiration source
   (rules inline in the template). **Delete nothing honestly unknown — mark it.**
3. The implementation files `index.html` / `assets` live beside `reference.md`
   inside the entry folder only AFTER the SKILL.md licence gate passes and the
   implementation itself passes the SKILL.md §6 + CRAFT.md §6 verification loops.
4. Update `library/manifest.json` (via `scripts/build_manifest.py` of the research
   toolchain, never hand-edits) to set `implementation.status` accordingly:
   `planned -> researching -> documented -> implemented -> verified`.

Statuses (honest states, mutually agreed vocabulary):

| Status | Means |
|---|---|
| `planned` | approved intent, nothing authored |
| `researching` | inspiration source is being read/measured |
| `documented` | LAYERS 1-4 of reference.md complete, code not started |
| `implemented` | code exists and passes the mechanical checks locally |
| `verified` | full SKILL.md §6 craft loop passed at both viewports |
