"""Generate assets/js/data.js — the website's data bundle.

Derived strictly from research/candidates.json + library/manifest.json.
Pre-generated so the site works from file:// (no fetch/CORS requirement);
when served over http, app.js re-checks the JSON files for freshness.

Run:  python scripts/gen_website_data.py
"""
import json
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "assets" / "js" / "data.js"

CANDS = json.loads((REPO / "research" / "candidates.json").read_text(encoding="utf-8"))
MANIFEST = json.loads((REPO / "library" / "manifest.json").read_text(encoding="utf-8"))

CATEGORY_ORDER = ["typography", "particles", "liquid", "3d-shaders", "transitions", "composition"]


def slim_candidate(c: dict) -> dict:
    prev = c.get("preview") or {}
    return {
        "id": c["id"],
        "name": c["name"],
        "category": c["category"],
        "subcategory": c["subcategory"],
        "creator": c.get("creator") or "",
        "description": c.get("description") or "",
        "demo_url": c.get("demo_url") or "",
        "source_url": c.get("source_url") or "",
        "repository_url": c.get("repository_url") or "",
        "rendering": c.get("rendering_method") or "",
        "technologies": c.get("technologies") or [],
        "techniques": c.get("techniques") or [],
        "interaction": c.get("interaction") or [],
        "complexity": c.get("complexity") or "",
        "status": c.get("status") or "",
        "licence": (c.get("licensing") or {}).get("license") or "unknown",
        "licence_url": (c.get("licensing") or {}).get("license_url") or "",
        "score": (c.get("evaluation") or {}).get("weighted_score"),
        "source_inspected": bool((c.get("inspection") or {}).get("source_inspected")),
        "browser_inspected": bool((c.get("inspection") or {}).get("browser_inspected")),
        "interaction_tested": bool((c.get("inspection") or {}).get("interaction_tested")),
        "preview_desktop": prev.get("desktop"),
        "preview_mobile": prev.get("mobile"),
        "notes": c.get("research_notes") or "",
    }


def slim_entry(e: dict) -> dict:
    lic = e["licensing"]
    return {
        "id": e["id"],
        "name": e["name"],
        "category": e["category"],
        "subcategory": e["subcategory"],
        "description": e["description"],
        "complexity": e.get("complexity"),
        "rendering": e.get("rendering"),
        "authority": e["adaptation"]["authority"],
        "plan": e["adaptation"]["plan"],
        "status": e["implementation"]["status"],
        "reference_path": f"library/{e['category']}/{e['id']}/reference.md",
        "licence": lic.get("source_license") or "unknown",
        "verified": bool(lic.get("verified")),
        "licence_url": lic.get("license_url") or lic.get("technique_reference_url") or "",
        "demo_url": e["inspiration"].get("demo_url") or "",
        "source_url": (e["inspiration"].get("repository_url")
                       or e["inspiration"].get("source_url") or ""),
        "creator": e["inspiration"].get("creator") or "",
    }


counts = {cat: {"candidates": 0, "shortlisted": 0, "source_inspected": 0,
                "browser_inspected": 0, "entries": 0} for cat in CATEGORY_ORDER}
for c in CANDS:
    d = counts[c["category"]]
    d["candidates"] += 1
    if c["status"] == "shortlisted": d["shortlisted"] += 1
    if (c.get("inspection") or {}).get("source_inspected"): d["source_inspected"] += 1
    if (c.get("inspection") or {}).get("browser_inspected"): d["browser_inspected"] += 1
for e in MANIFEST["entries"]:
    counts[e["category"]]["entries"] += 1

data = {
    "generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
    "categories": CATEGORY_ORDER,
    "counts": {
        "candidates": len(CANDS),
        "shortlisted": sum(1 for c in CANDS if c["status"] == "shortlisted"),
        "source_inspected": sum(1 for c in CANDS if (c.get("inspection") or {}).get("source_inspected")),
        "browser_inspected": sum(1 for c in CANDS if (c.get("inspection") or {}).get("browser_inspected")),
        "previewed": sum(1 for c in CANDS if c.get("preview")),
        "entries": len(MANIFEST["entries"]),
        "implemented_entries": sum(1 for e in MANIFEST["entries"] if e["implementation"]["status"] == "implemented"),
        "authorities": {a: sum(1 for e in MANIFEST["entries"] if e["adaptation"]["authority"] == a)
                        for a in ("adapt", "reinvent", "pattern")},
        "fonts_verified": len(MANIFEST["fonts"]["verified"]),
    },
    "per_category": [dict(category=cat, **counts[cat]) for cat in CATEGORY_ORDER],
    "candidates": [slim_candidate(c) for c in sorted(CANDS, key=lambda x: -(x.get("evaluation", {}).get("weighted_score") or 0))],
    "library": {
        "manifest_version": MANIFEST["manifest_version"],
        "entries": [slim_entry(e) for e in MANIFEST["entries"]],
        "reserves": MANIFEST["reserves"],
        "fonts": MANIFEST["fonts"]["verified"],
        "authorities": MANIFEST["adaptation_authorities"],
    },
}

OUT.write_text(
    "/* GENERATED by scripts/gen_website_data.py - do not edit by hand */\n"
    "window.OTXYN_DATA = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n",
    encoding="utf-8",
)
print(f"website data OK -> {OUT.relative_to(REPO)} "
      f"({len(data['candidates'])} candidates, {len(data['library']['entries'])} entries)")
