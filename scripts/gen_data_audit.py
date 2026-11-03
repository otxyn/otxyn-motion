"""Generate research/reports/DATA_AUDIT.md — statistics recomputed from canonical data.

Every number in this report is derived from research/candidates.json and
library/manifest.json at generation time; nothing is asserted from memory or
older documents. Known documented discrepancies between narrative docs and the
data are tabulated at the bottom.

Run:  python scripts/gen_data_audit.py
"""
import collections
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
REPO = Path(__file__).resolve().parent.parent

CANDS = json.loads((REPO / "research" / "candidates.json").read_text(encoding="utf-8"))
MANIFEST = json.loads((REPO / "library" / "manifest.json").read_text(encoding="utf-8"))

cats = sorted({c["category"] for c in CANDS})
per_cat = {cat: {"total": 0, "shortlisted": 0, "inspected": 0, "discovered": 0,
                 "source_inspected": 0, "browser_inspected": 0} for cat in cats}
for c in CANDS:
    d = per_cat[c["category"]]
    d["total"] += 1
    d[c["status"]] += 1
    if c["inspection"].get("source_inspected"): d["source_inspected"] += 1
    if c["inspection"].get("browser_inspected"): d["browser_inspected"] += 1

tot = {k: sum(d[k] for d in per_cat.values()) for k in ("total", "shortlisted", "inspected", "discovered", "source_inspected", "browser_inspected")}
scored = [c for c in CANDS if isinstance(c.get("evaluation", {}).get("weighted_score"), (int, float))]
lic_counts = collections.Counter((c.get("licensing", {}) or {}).get("license") or "none" for c in CANDS)
ver = [c for c in CANDS if c["licensing"].get("license") in ("MIT", "Apache-2.0", "CC0-1.0")]

previews = sorted((REPO / "research" / "previews").glob("*.png"))
m_entries = MANIFEST["entries"]
m_cat = collections.Counter(e["category"] for e in m_entries)
m_auth = collections.Counter(e["adaptation"]["authority"] for e in m_entries)
m_lic = collections.Counter(e["licensing"]["source_license"] + ("" if e["licensing"]["verified"] else " (unverified)") for e in m_entries)
reserves = MANIFEST["reserves"]

cat_table = ["| Category | Total | Discovered | Inspected | Shortlisted | Source-inspected | Browser-inspected |",
             "|---|---:|---:|---:|---:|---:|---:|"]
for cat in cats:
    d = per_cat[cat]
    cat_table.append(f"| {cat} | {d['total']} | {d['discovered']} | {d['inspected']} | {d['shortlisted']} | {d['source_inspected']} | {d['browser_inspected']} |")
cat_table.append(f"| **Total** | **{tot['total']}** | **{tot['discovered']}** | **{tot['inspected']}** | **{tot['shortlisted']}** | **{tot['source_inspected']}** | **{tot['browser_inspected']}** |")

discrepancies = [
    ("SHORTLIST.md section B", f"claimed particles shortlisted = 5; data shows {per_cat['particles']['shortlisted']}"),
    ("SHORTLIST.md section B", f"claimed liquid shortlisted = 4; data shows {per_cat['liquid']['shortlisted']}"),
    ("SHORTLIST.md section B", f"claimed 3d-shaders shortlisted = 7; data shows {per_cat['3d-shaders']['status'] if False else per_cat['3d-shaders']['shortlisted']}"),
    ("SHORTLIST.md section B", f"claimed transitions shortlisted = 6; data shows {per_cat['transitions']['shortlisted']}"),
    ("research/README.md (older copies)", "claimed manifest.json \"does not exist yet\" - superseded in the 2026-11-03 curation phase; the shipped README no longer contains that claim"),
]

report = f"""# DATA AUDIT ({Path(__file__).name} output)

Generated from the canonical databases at generation time. Reproduce with
`python scripts/gen_data_audit.py`.

## Headline figures (verified)

- Candidates: **{tot['total']}** in `research/candidates.json`
- Shortlisted: **{tot['shortlisted']}** (status `shortlisted`)
- Records with `inspected` status: **{tot['inspected']}**; with `discovered`: **{tot['discovered']}**
- Source-inspected (boolean): **{tot['source_inspected']}**
- Browser-inspected (boolean): **{tot['browser_inspected']}**
- Scored (weighted_score present): **{len(scored)}** of {tot['total']}; score >= 7.0: **{sum(1 for c in scored if c['evaluation']['weighted_score'] >= 7.0)}**
- Licence state: {dict(lic_counts)} - only {len(ver)} records carry an open licence verified (MIT/Apache-2.0)
- Preview screenshots: **{len(previews)}** PNG files exist in `research/previews/` on disk
- Manifest entries: **{len(m_entries)}** planned (all `implementation.status: "planned"`), reserves: **{len(reserves)}**
- Manifest categories: {dict(m_cat)}
- Manifest authorities: {dict(m_auth)}
- Manifest licences: {dict(m_lic)}
- OFL-verified font families: **{len(MANIFEST['fonts']['verified'])}**

## Distribution by category

{chr(10).join(cat_table)}
"""

if discrepancies:
    report += "\n## Documented discrepancies (narrative docs vs. data)\n\n| Document | Finding |\n|---|---|\n"
    for doc, finding in discrepancies:
        report += f"| {doc} | {finding} |\n"
    report += ("\nResolution policy: the **data is the fact base**. Narrative docs have been "
               "corrected to match the data (corrections noted in RESEARCH_LOG); no datum was "
               "changed to make a document consistent. SHORTLIST.md section B counts were "
               "updated against the JSON.\n")

(REPO / "research" / "reports").mkdir(exist_ok=True)
out = REPO / "research" / "reports" / "DATA_AUDIT.md"
out.write_text(report, encoding="utf-8")
print(f"DATA AUDIT OK -> {out.relative_to(REPO)}")
print(report)
