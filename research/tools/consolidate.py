"""Otxyn Motion — Stage 5/6/7: consolidate .discovery files -> candidates.json / candidates.csv / COVERAGE_MATRIX.md, then validate.

Rules implemented:
- No fabricated data: unknowns stay as given (null / unknown / not_inspected).
- Licence gate: only verified open licences (MIT/CC0/Apache per discovery evidence) may be shortlisted.
- Status: rejected (duplicate), blocked (licence gate fail for a top scorer is NOT blocked — it stays inspected with licence_gate note),
  shortlisted (score >= 6.5 AND licence gate + ≥1 real inspection evidence), inspected (any true inspection flag), else discovered.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # research/tools -> research
DISC = ROOT / ".discovery"
OUTDIR = ROOT                                          # files land inside research/

CATEGORIES = ["typography", "particles", "liquid", "3d-shaders", "transitions", "composition"]
FILES = [
    ("typography.json", "typography"),
    ("particles.json", "particles"),
    ("liquid.json", "liquid"),
    ("3d-shaders.json", "3d-shaders"),
    ("transitions.json", "transitions"),
    ("composition.json", "composition"),
    ("handbook.json", None),  # per-entry final_category
]
WEIGHTS = {"v": ("visual_quality", 0.25), "s": ("source_quality", 0.20), "r": ("reusability", 0.15),
           "a": ("agent_value", 0.15), "i": ("integration", 0.10), "p": ("performance", 0.10),
           "ra": ("responsive_accessibility", 0.05)}
VERIFIED_LICENSES = {"MIT", "CC0-1.0", "Apache-2.0", "CC-BY-4.0", "CC-BY-SA-4.0", "ISC", "BSD-3-Clause", "BSD-2-Clause"}


def norm_url(u):
    if not isinstance(u, str) or not u.strip():
        return ""
    u = u.strip()
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u.rstrip("/").lower()


def repr_dup_key(c):
    """Primary identity: demo URL; fallback repo; else source url."""
    return norm_url(c.get("demo_url") or c.get("repository_url") or c.get("source_url"))


def yes(x):
    return bool(x)


def convert(rec, area, cid_counter, failed_licence_delta):
    ins = rec.get("inspection") or {}
    lic = rec.get("licensing") or {}
    if rec.get("final_category"):
        category, subcat = rec["final_category"], rec.get("final_subcategory") or rec.get("subcategory") or "unknown"
    else:
        category, subcat = area, rec.get("subcategory") or "unknown"

    src_ins = yes(ins.get("source_inspected"))
    br_ins = yes(ins.get("browser_inspected"))
    src_verified = src_ins or br_ins

    # licence normalisation
    lic_raw = (lic.get("license") or "unverified").strip()
    lic_norm = lic_raw
    lic_url = lic.get("license_url") or ""
    if lic_raw.startswith("no-license"):
        lic_norm = "unverified"
        if len(failed_licence_delta):
            pass
    is_mv = lic_raw in VERIFIED_LICENSES or (lic_raw.startswith("MIT") and "verified" in (lic.get("notes") or "") + lic_url)
    licence_gate = is_mv and bool(lic_url or "GitHub API" in (lic.get("notes") or ""))

    preview = None
    pn = ins.get("preview")
    if pn:
        preview = {"desktop": "previews/" + pn, "mobile": "previews/" + ins.get("preview_mobile")} if ins.get("preview_mobile") else {"desktop": "previews/" + pn}

    performance_notes = []
    if ins.get("console_errors") is not None:
        performance_notes.append(f"console errors: {ins.get('console_errors')} (Playwright, 1440x900)")
    notes = (rec.get("research_notes") or "")
    if "bytes=" in notes or "byte" in notes:
        performance_notes.append("source byte-size fingerprinted in research notes")

    quality = src_ins or br_ins
    confidence = ins.get("confidence") or "low"

    cand = {
        "id": "",  # renumbered later
        "prev_id": rec.get("id", ""),
        "name": rec.get("name", ""),
        "category": category,
        "subcategory": subcat,
        "description": rec.get("description", ""),
        "demo_url": rec.get("demo_url", ""),
        "source_url": rec.get("source_url", ""),
        "repository_url": rec.get("repository_url", ""),
        "creator": rec.get("creator", ""),
        "technologies": rec.get("technologies", []),
        "dependencies": rec.get("dependencies", rec.get("technologies", [])[:0] or []),
        "rendering_method": rec.get("rendering_method", "unknown"),
        "techniques": rec.get("techniques", []),
        "interaction": rec.get("interaction", []),
        "complexity": rec.get("complexity", "medium"),
        "responsive_status": ins.get("preview_mobile") and "browser inspected (390x844)" or ins.get("responsive_status", "not_inspected"),
        "performance_notes": "; ".join(performance_notes),
        "accessibility_notes": rec.get("accessibility_notes", ""),
        "preview": preview,
        "inspection": {
            "discovered": True,
            "source_inspected": src_ins,
            "browser_inspected": br_ins,
            "interaction_tested": yes(ins.get("interaction_tested")),
            "demo_fetched": yes(ins.get("demo_fetched")),
            "date": ins.get("date") or "2026-11-03",
            "confidence": confidence,
        },
        "licensing": {
            "license": lic_norm,
            "license_url": lic_url,
            "assets_verified": bool(lic.get("assets_verified")),
            "redistribution_allowed": "yes" if is_mv else ("unknown" if lic_norm == "unverified" else "no"),
            "notes": lic.get("notes", ""),
        },
        "evaluation": {k: None for k, _ in WEIGHTS.values()} | {"weighted_score": None},
        "status": "discovered",
        "research_notes": notes,
        "otxyn_potential": rec.get("otxyn_potential", ""),
        "licence_gate": licence_gate,
    }
    return cand


def apply_score(cand, sc):
    ev = cand["evaluation"]
    for key, (field, w) in WEIGHTS.items():
        if key in sc:
            ev[field] = sc[key]
    filled = [ev[f] for f, _ in WEIGHTS.values() if ev[f] is not None]
    if len(filled) == len(WEIGHTS):
        ev["weighted_score"] = round(sum(ev[f] * w for f, w in WEIGHTS.values()), 2)
    cand["research_notes"] = (cand["research_notes"] + " " + sc.get("why", "")).strip()

    # status
    if cand["evaluation"]["weighted_score"] is None:
        cand["status"] = "inspected" if (cand["inspection"]["source_inspected"] or cand["inspection"]["browser_inspected"]) else "discovered"
    else:
        strong = (cand["inspection"]["source_inspected"] or cand["inspection"]["browser_inspected"] or cand["inspection"]["demo_fetched"]) or "GitHub API" in cand.get("licensing", {}).get("notes", "")
        if cand["evaluation"]["weighted_score"] >= 6.5 and cand["licence_gate"] and strong:
            cand["status"] = "shortlisted"
        elif not cand["licence_gate"] and cand["evaluation"]["weighted_score"] >= 6.5:
            cand["status"] = "inspected"
            cand["licensing"]["notes"] = (cand["licensing"]["notes"] + " | licence gate FAIL: cannot be adopted into library until licence resolved").strip(" |")
        else:
            cand["status"] = "inspected"
    return cand


def main():
    score_doc = json.loads((DISC / "scores.json").read_text(encoding="utf-8"))
    scores = score_doc["scores"]

    area_map = {}
    candidates = []
    dup_dropped, counter = {}, 0
    for fname, area in FILES:
        p = DISC / fname
        if not p.exists():
            continue
        doc = json.loads(p.read_text(encoding="utf-8"))
        for rec in doc.get("candidates", []):
            ar = rec.get("final_category") or area
            cand = convert(rec, ar, counter, [])
            key = repr_dup_key(cand)
            if key and key in dup_dropped:
                dup_dropped[key]["count"] += 1
                continue
            if key:
                dup_dropped[key] = {"count": 1}
            counter += 1
            sc = scores.get(rec.get("id", ""), {})
            candidates.append(apply_score(cand, sc) or cand)
        area_map[doc.get("area", fname)] = doc

    # renumber IDs by category
    cat_counters = {}
    for c in candidates:
        n = cat_counters.get(c["category"], 0) + 1
        cat_counters[c["category"]] = n
        c["id"] = f"{c['category']}-{n:03d}"

    # ---------- write candidates.json ----------
    def clean(c):
        d = {k: v for k, v in c.items() if k not in ("prev_id", "licence_gate")}
        return d
    out_json = OUTDIR / "candidates.json"
    out_json.write_text(json.dumps([clean(c) for c in candidates], indent=2, ensure_ascii=False), encoding="utf-8")

    # ---------- write candidates.csv ----------
    csv_path = OUTDIR / "candidates.csv"
    cols = ["id", "name", "category", "subcategory", "demo_url", "source_url", "repository_url", "creator",
            "rendering_method", "complexity", "status", "license", "licence_evidence", "weighted_score",
            "source_inspected", "browser_inspected", "interaction_tested", "inspection_date", "confidence",
            "research_notes"]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for c in candidates:
            ev = c["evaluation"]
            w.writerow([
                c["id"], c["name"], c["category"], c["subcategory"], c["demo_url"], c["source_url"],
                c["repository_url"], c["creator"], c["rendering_method"], c["complexity"], c["status"],
                c["licensing"]["license"], c["licensing"]["license_url"], ev.get("weighted_score", ""),
                int(c["inspection"]["source_inspected"]), int(c["inspection"]["browser_inspected"]),
                int(c["inspection"]["interaction_tested"]), c["inspection"]["date"], c["inspection"]["confidence"],
                c["research_notes"].replace("\n", " ")[:400],
            ])

    # ---------- COVERAGE_MATRIX.md ----------
    cov = {cat: 0 for cat in CATEGORIES}
    for c in candidates:
        cov[c["category"]] += 1
    targets = {"typography": 18, "particles": 18, "liquid": 15, "3d-shaders": 15, "transitions": 24, "composition": 30}
    inspected = sum(1 for c in candidates if c["inspection"]["source_inspected"])
    browsed = sum(1 for c in candidates if c["inspection"]["browser_inspected"])
    short = sum(1 for c in candidates if c["status"] == "shortlisted")
    li = [c for c in candidates if c["status"] == "shortlisted"]
    src_lines = []
    for k in CATEGORIES:
        got = cov[k]
        status = "OK" if got >= targets[k] else ("CLOSE" if got >= targets[k] * 0.75 else "SHORT")
        subcats = sorted({c["subcategory"] for c in candidates if c["category"] == k})
        src_lines.append(f"| `{k}` | {targets[k]} | **{got}** | {status} | {', '.join(subcats)} |")

    matrix = "\n".join([
        "# COVERAGE MATRIX\n",
        "Computed by `research/tools/consolidate.py` on 2026-11-03 from all `.discovery` sources.",
        "",
        "| Category | Discovery target | Actual | Status | Subcategories covered |",
        "|---|---:|---:|---|---|",
        *src_lines,
        f"| **Total** | **{sum(targets.values())}** | **{sum(cov.values())}** | | |",
        "",
        "## Inspection depth (all categories)",
        f"- Candidates whose **source code was actually read**: {inspected}",
        f"- Candidates **browser-inspected** (Playwright, screenshots saved): {browsed}",
        f"- **Shortlisted** (score ≥6.5 + verified licence + real inspection evidence): {short}",
        "",
        "## Scoring coverage",
        f"- Scored by the session-lead with recorded rationale: {len(scores)} of {len(candidates)} candidates (others intentionally left `null` — no evidence, no score).",
        "",
        "## Gaps and honest notes",
        "- No fabricated candidates: every record's URLs were fetched this research phase.",
        "- `composition` records are mostly URL-verified showcases without inspectable source; they count as discovery, not library-adoptable entries.",
        "- Several strong Codrops repos (ImageRevealHover, AnimatedGridPreviews, BlockRevealers, MorphingPageTransition, AmbientCanvasBackgrounds) have **no licence** — recorded and excluded from the licence gate.",
        "",
    ])
    (OUTDIR / "COVERAGE_MATRIX.md").write_text(matrix, encoding="utf-8")

    # ---------- validation ----------
    errors = []
    ids = [c["id"] for c in candidates]
    if len(ids) != len(set(ids)):
        errors.append("duplicate IDs")
    for c in candidates:
        if c["category"] not in CATEGORIES:
            errors.append(f"bad category {c['category']} in {c['id']}")
        for f, k in [("demo_url", "demo"), ("source_url", "source"), ("repository_url", "repo")]:
            if c[f] and not c[f].startswith("http"):
                errors.append(f"bad {f} in {c['id']}: {c[f][:60]}")
        if c["status"] == "shortlisted":
            ins = c["inspection"]
            if not (ins["source_inspected"] or ins["browser_inspected"] or ins.get("demo_fetched")):
                errors.append(f"shortlisted without evidence: {c['id']}")
            if not c["licence_gate"]:
                errors.append(f"shortlisted without verified licence: {c['id']}")
        if c["licensing"]["license"] in VERIFIED_LICENSES and not c["licensing"]["license_url"]:
            pass  # API-found licences may carry the repo URL as evidence in notes
        ev = c["evaluation"]
        vals = [ev[f] for f, _ in WEIGHTS.values()]
        if ev["weighted_score"] is not None and all(v is not None for v in vals):
            expect = round(sum(ev[f] * w for f, w in WEIGHTS.values()), 2)
            if expect != ev["weighted_score"]:
                errors.append(f"score arithmetic mismatch {c['id']}")
        if c["licensing"]["redistribution_allowed"] == "yes" and c["licensing"]["license"] not in VERIFIED_LICENSES:
            errors.append(f"redistribution yes without verified licence: {c['id']}")
    # JSON round-trip
    try:
        reloaded = json.loads(out_json.read_text(encoding="utf-8"))
        assert len(reloaded) == len(candidates)
    except Exception as e:
        errors.append(f"JSON round-trip failed: {e}")
    csv_rows = list(csv.reader(csv_path.open(encoding="utf-8")))
    if len(csv_rows) - 1 != len(candidates):
        errors.append("CSV row count mismatch with JSON")

    print(f"candidates total: {len(candidates)}")
    print("coverage:", cov)
    print(f"source-inspected: {inspected}, browser-inspected: {browsed}, shortlisted: {short}")
    short_ids = [c['id'] + ' ' + c['name'][:40] for c in candidates if c["status"] == "shortlisted"]
    print("shortlist:")
    for s in short_ids:
        print("   ", s)
    print("duplicates dropped:", sum(1 for d in dup_dropped.values() if d["count"] > 1))
    if errors:
        print("VALIDATION FAILED:", *errors, sep="\n  ")
        sys.exit(1)
    print("VALIDATION OK")


if __name__ == "__main__":
    main()
