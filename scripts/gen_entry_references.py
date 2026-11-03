"""Generate library/<category>/<entry-id>/reference.md for every manifest entry.

Policy:
- Content is derived EXCLUSIVELY from library/manifest.json (+ the research
  candidate it points to when linked). No constants are invented; every
  unmeasured slot is explicitly marked "measure from the source at
  implementation time".
- Entries whose implementation.status is not "implemented" get a scaffold marked
  as such. The worked example (typ-self-split-text-reveal) already has a
  hand-authored richer reference; it is left untouched.
- For authoritative=adapt entries with a verified MIT/Apache licence, the
  attribution header template is pre-filled; for reinvent/pattern entries the
  reference is technique-only.

Run:  python scripts/gen_entry_references.py
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((REPO / "library" / "manifest.json").read_text(encoding="utf-8"))
CANDS = {c["id"]: c for c in json.loads((REPO / "research" / "candidates.json").read_text(encoding="utf-8"))}

WORKED_EXAMPLE = "typ-self-split-text-reveal"  # hand-authored richer reference stays

FONTS_FOR = {}
for f in MANIFEST["fonts"]["verified"]:
    for eid in f.get("used_by", []):
        FONTS_FOR.setdefault(eid, []).append(f'{f["family"]} ({f["licence"]})')


def attribution_block(entry: dict) -> str:
    lic = entry["licensing"]
    if entry["adaptation"]["authority"] == "adapt" and lic.get("verified") and lic["source_license"] == "MIT":
        rep = entry["inspiration"].get("repository_url") or entry["inspiration"].get("source_url") or ""
        creator = entry["inspiration"].get("creator") or "original author"
        return (
            "```text\n"
            "<!--\n"
            f"  Otxyn Motion - {entry['id']}\n"
            f"  Technique adapted from {creator}'s work ({lic['source_license']}).\n"
            f"  Upstream: {rep}\n"
            "  Include the upstream MIT copyright + licence text alongside any\n"
            "  derived file (copy it from the upstream repository's LICENSE).\n"
            "-->\n"
            "```"
        )
    if entry["adaptation"]["authority"] == "adapt":
        return f"Adaptation permitted under {lic['source_license']}; attribution block to be filled from the upstream LICENSE at implementation time."
    if entry["adaptation"]["authority"] == "reinvent":
        return (
            "**Reinvention.** The source has no verified open licence; nothing may be "
            "copied. Document the technique only and implement from scratch. "
        )
    return (
        "**Pattern study.** Closed-source showcase; documented for agent study. "
        "Never adopt its code or assets."
    )


def ref_markdown(entry: dict) -> str:
    lic = entry["licensing"]
    auth = entry["adaptation"]["authority"]
    insp = entry["inspection_basis"]
    c = CANDS.get(entry["research_candidate"], {})
    demo = entry["inspiration"].get("demo_url") or ""
    src = (
        entry["inspiration"].get("repository_url")
        or entry["inspiration"].get("source_url")
        or ""
    )
    fonts = FONTS_FOR.get(entry["id"], [])
    depth = (
        "source-inspected" if insp.get("source_inspected") else
        "browser-inspected" if insp.get("browser_inspected") else
        "demo-fetched"
    )
    return f"""# {entry['id']} - entry reference

**Status:** `{entry['implementation']['status']}`   (not implemented - scaffold generated from the manifest)
**Name:** {entry['name']}
**Category:** {entry['category']} / {entry['subcategory']}
**Authority:** {auth}  |  **Source licence:** {lic['source_license']} (verified: {str(bool(lic.get('verified'))).lower()})
**Inspection basis:** {depth}, confidence {insp.get('confidence') or 'not_recorded'}

Research provenance: `{c.get('id', entry['research_candidate'])}` in `research/candidates.json`.
Inspiration demo: {demo or 'none recorded'}
Source: {src or 'none recorded'}

---

## LAYER 1 - PLAIN-WORDS

{entry['description']}

Adaptation plan (from the manifest):
{entry['adaptation']['plan']}

---

## LAYER 2 - PASS-GRAPH

To be authored during implementation by reading the inspiration source directly.
Starting facts from the research record:

- Rendering method: `{entry['rendering']}`
- Complexity: `{entry['complexity']}`
- Primary techniques: {"; ".join(c.get("techniques") or []) if c else "recorded in the candidate research notes"}
- Technologies involved: {"; ".join(c.get("technologies") or []) if c else "see research_candidates record"}

Fallback tier: define at implementation time (document the degraded, dependency-free
variant of this effect - e.g. static presentation of the same subject).

---

## LAYER 3 - PARAMETERS

No constant in this scaffold is measured - measure from the inspiration source during
implementation and record provenance for each value. Suggested slots to fill
(delete as appropriate per technique):

| Parameter | Measured value | Source |
|---|---|---|
| duration(s) | _measure_ | |
| easing | _measure_ | |
| stagger | _measure_ | |
| counts / thresholds | _measure_ | |
| fallback constants | _set_ | |

---

## LAYER 4 - ATTRIBUTION

{attribution_block(entry)}

Licence evidence: {lic.get('license_url') or lic.get('technique_reference_url') or 'n/a'}
{('Block from manifest: ' + (lic.get('evidence') or '')) if lic.get('evidence') else ''}

---

## Verification requirements (from `manifest.verification_required`)

- Viewports: {' and '.join(i for i in entry['verification_required']['viewports'])}
- Console: {entry['verification_required']['console_errors']}
- Reduced motion: {entry['verification_required']['reduced_motion']}
- Licence gate: {entry['verification_required']['licence_gate']}

## Fonts

{('May use OFL-verified families: ' + '; '.join(fonts) + ' (see manifest fonts block).') if fonts else 'No specific font required; if a display face is needed, restrict to manifest `fonts.verified` (OFL-only).'}
"""


def main() -> None:
    written, skipped = [], []
    for entry in MANIFEST["entries"]:
        cat_dir = REPO / "library" / entry["category"] / entry["id"]
        out = cat_dir / "reference.md"
        if entry["id"] == WORKED_EXAMPLE:
            # already authored; regenerate only if the data changed materially is
            # out of scope here - keep the rich hand-written version.
            if not out.exists():
                out.write_text(ref_markdown(entry), encoding="utf-8")
            skipped.append(entry["id"])
            continue
        cat_dir.mkdir(parents=True, exist_ok=True)
        out.write_text(ref_markdown(entry), encoding="utf-8")
        written.append(entry["id"])
    print(f"entry references generated: {len(written)} / kept worked example: {len(skipped)}")


if __name__ == "__main__":
    main()
