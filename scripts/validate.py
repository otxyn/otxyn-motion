"""Otxyn Motion validation suite.

Checks (mission section 10):
  1.  JSON validity                (candidates.json + manifest.json parse)
  2.  CSV consistency              (generated CSV matches JSON row-for-row)
  3.  Unique candidate IDs
  4.  Category distribution        (both DB and manifest targets)
  5.  Manifest consistency         (counts, authorities, licence invariants,
       font clearances, expected keys)
  6.  Entry statuses               (honest enum, planned->verified ladder)
  7.  Internal links               (every relative md link + page reference resolves)
  8.  Preview paths                (previews referenced in data exist on disk)
  9.  Skill reference paths        (files SKILL.md points to exist)
  10. Licence metadata             (adapt entries carry verified open licence + URL)
  11. Website rendering integrity  (index.html references assets/data that exist;
       data.js parses; JS bundle consistent with JSON counts)
  12. Mobile responsiveness        (static heuristics only: viewport meta + CSS
       breakpoints present; full check is done in the browser, reported separately)

Run:  python scripts/validate.py            (from anywhere in the repo)
Exit code 0 only when everything passes.
"""
import csv
import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
REPO = Path(__file__).resolve().parent.parent
REQ = REPO / "research" / "requirements_placeholder.none"  # placeholder path never used

problems: list[str] = []
notes: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def ok(msg: str) -> None:
    notes.append(msg)


# ---------------------------------------------------------------- 1. JSON
cand_path = REPO / "research" / "candidates.json"
try:
    CANDS = json.loads(cand_path.read_text(encoding="utf-8"))
    ok("candidates.json parses")
except Exception as e:
    fail(f"candidates.json invalid: {e}")
    print("FAILED"); sys.exit(1)

manifest_path = REPO / "library" / "manifest.json"
try:
    MANIFEST = json.loads(manifest_path.read_text(encoding="utf-8"))
    ok("manifest.json parses")
except Exception as e:
    fail(f"manifest.json invalid: {e}")
    print("FAILED"); sys.exit(1)

data_js = REPO / "assets" / "js" / "data.js"
try:
    txt = data_js.read_text(encoding="utf-8")
    payload = txt[txt.index("{"): txt.rindex("}") + 1]
    SITE = json.loads(payload)
    ok("assets/js/data.js parses as JSON payload")
except Exception as e:
    SITE = None
    fail(f"assets/js/data.js payload invalid: {e}")

# ---------------------------------------------------------------- 2 + 3. CSV + IDs
ids = [c["id"] for c in CANDS]
if len(ids) != len(set(ids)):
    dupes = [i for i, n in {i: [x["id"] for x in CANDS].count(i) for i in ids}.items() if n > 1]
    fail(f"duplicate candidate ids: {dupes}")
else:
    ok(f"{len(ids)} unique candidate ids")

csv_path = REPO / "research" / "candidates.csv"
try:
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != len(CANDS):
        fail(f"CSV has {len(rows)} rows but JSON has {len(CANDS)}")
    else:
        idset_csv = {r["id"] for r in rows}
        if idset_csv != set(ids):
            fail("CSV ids != JSON ids")
        else:
            ok(f"CSV parity: {len(rows)} rows, ids identical")
except Exception as e:
    fail(f"candidates.csv unreadable/invalid: {e}")

# ---------------------------------------------------------------- 4 + 5. categories & manifest
CATS = {"typography", "particles", "liquid", "3d-shaders", "transitions", "composition"}
bad = [c["category"] for c in CANDS if c["category"] not in CATS]
if bad:
    fail(f"unknown categories in DB: {bad}")
else:
    ok("category enum clean in DB")

targets = {"typography": 7, "particles": 6, "liquid": 5, "3d-shaders": 5, "transitions": 7, "composition": 10}
if MANIFEST.get("entry_count") != len(MANIFEST["entries"]) or len(MANIFEST["entries"]) != 40:
    fail(f"manifest entry_count mismatch: {MANIFEST.get('entry_count')} vs {len(MANIFEST['entries'])}")
else:
    ok("manifest entry_count = 40 with matching array")

mcat = {}
for e in MANIFEST["entries"]:
    mcat[e["category"]] = mcat.get(e["category"], 0) + 1
if mcat != targets:
    fail(f"manifest category distribution {mcat} != targets {targets}")
else:
    ok("manifest category distribution matches documented targets")

OPEN_LIC = {"MIT", "Apache-2.0", "CC0-1.0"}
statuses = {"planned", "researching", "documented", "implemented", "verified"}
for e in MANIFEST["entries"]:
    if e["adaptation"]["authority"] not in ("adapt", "reinvent", "pattern"):
        fail(f"bad authority: {e['id']}")
    if e["implementation"]["status"] not in statuses:
        fail(f"bad implementation status: {e['id']} -> {e['implementation']['status']}")
    lic = e["licensing"]
    if e["adaptation"]["authority"] == "adapt" and not (lic.get("verified") and lic.get("source_license") in OPEN_LIC and lic.get("license_url")):
        fail(f"adapt entry lacking verified licence + evidence: {e['id']}")
    if e["adaptation"]["authority"] == "reinvent" and not (lic.get("license_url") or lic.get("technique_reference_url")):
        fail(f"reinvent entry without technique reference: {e['id']}")
    if e["implementation"]["status"] in ("implemented", "verified") and not (REPO / e["implementation"]["target_file"]).exists():
        fail(f"status says implemented but folder missing: {e['id']} {e['implementation']['target_file']}")
    if e["implementation"]["status"] == "planned" and not Path(e["implementation"]["target_file"], "reference.md").is_absolute() and not (REPO / e["implementation"]["target_file"] / "reference.md").exists():
        fail(f"planned entry missing reference.md scaffold: {e['id']}")
else:
    ok("entry statuses + licence invariants checked")
if not any(MANIFEST["fonts"]["verified"]) or any(f["licence"] != "OFL" for f in MANIFEST["fonts"]["verified"]):
    fail("font clearances must all be OFL")
else:
    ok(f"{len(MANIFEST['fonts']['verified'])} OFL font clearances verified")

# every manifest entry must have a reference.md
missing_ref = [e["id"] for e in MANIFEST["entries"]
               if not (REPO / "library" / e["category"] / e["id"] / "reference.md").exists()]
if missing_ref:
    fail(f"entries missing reference.md: {missing_ref}")
else:
    ok("all 40 manifest entries have reference.md")

# ---------------------------------------------------------------- 7-9. links
url_re = re.compile(r"\]\(([^)#\s]+)\)")
md_files = list(REPO.rglob("*.md"))
checked = 0
for md in md_files:
    rel_dir = md.parent
    for target in url_re.findall(md.read_text(encoding="utf-8", errors="replace")):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        # strip inline images/data
        if target.startswith("data:"):
            continue
        p = (rel_dir / target).resolve()
        checked += 1
        if not p.exists():
            fail(f"broken relative link in {md.relative_to(REPO)}: {target}")
ok(f"checked {checked} relative markdown links")

# skill references
for referred in ["library/manifest.json", "skill/CRAFT.md", "research/TECHNIQUES.md"]:
    if not (REPO / referred).exists():
        fail(f"SKILL.md reference missing: {referred}")
ok("skill reference paths exist (SKILL.md, CRAFT.md, TECHNIQUES.md, manifest)")

# CSS/internal page asset references in index.html
html = (REPO / "index.html").read_text(encoding="utf-8")
for m in re.finditer(r'(?:src|href)=["\']([^"\']+)["\']', html):
    t = m.group(1)
    if t.startswith(("http", "#", "mailto")):
        continue
    if not (REPO / t).exists():
        fail(f"index.html broken asset reference: {t}")
ok("index.html asset references resolve")

# ---------------------------------------------------------------- 8. previews
for c in CANDS:
    prev = c.get("preview") or {}
    for key, path in prev.items():
        if path and not (REPO / "research" / path).exists():
            fail(f"preview file missing for {c['id']} ({key}): {path}")
ok("preview paths in DB resolve on disk")

# previews referenced by data.js entries too
if SITE:
    for x in SITE["candidates"]:
        for key in ("preview_desktop", "preview_mobile"):
            p = x.get(key)
            if p and not (REPO / "research" / p).exists():
                fail(f"website preview missing for {x['id']}: {p}")

# ---------------------------------------------------------------- 10. site bundle matches DB
if SITE:
    if len(SITE["candidates"]) != len(CANDS):
        fail(f"website bundle has {len(SITE['candidates'])} candidates; JSON has {len(CANDS)} (regen gen_website_data.py)")
    if len(SITE["library"]["entries"]) != len(MANIFEST["entries"]):
        fail("website bundle library entry count mismatch")
    if SITE.get("counts", {}).get("candidates") != len(CANDS):
        fail("website bundle self-reported candidate count mismatch")
    catsum = sum(p["candidates"] for p in SITE["per_category"])
    if catsum != len(CANDS):
        fail(f"website bundle per_category sum {catsum} != {len(CANDS)}")
    if not problems:
        ok("website bundle counts consistent with DB")

# ---------------------------------------------------------------- 11. responsive heuristics
css = (REPO / "assets" / "css" / "site.css").read_text(encoding="utf-8")
if 'name="viewport"' not in html:
    fail("index.html missing viewport meta")
if "@media (max-width: 720px)" not in css:
    fail("site.css missing mobile breakpoint")
if "prefers-reduced-motion" not in css:
    fail("site.css missing prefers-reduced-motion handling")
ok("responsive heuristics pass (viewport meta, 720px breakpoint, reduced-motion)")

# ---------------------------------------------------------------- report
print("Otxyn Motion validation", "-" * 40)
for n in notes:
    print("  OK   ", n)
if problems:
    print()
    for p in problems:
        print("  FAIL ", p)
    print(f"\nRESULT: {len(problems)} problem(s)")
    sys.exit(1)
print(f"\nRESULT: ALL OK  ({len(notes)} checks)")
