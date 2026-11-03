"""Generate research/candidates.csv from the canonical research/candidates.json.

Run from anywhere inside the repo:
    python scripts/gen_candidates_csv.py

The JSON file is the single source of truth. This script is the ONLY producer of
the CSV so the two can never drift apart. Rows are emitted in `id` order.
"""
import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JSON_PATH = REPO / "research" / "candidates.json"
CSV_PATH = REPO / "research" / "candidates.csv"

HEADER = [
    "id", "name", "category", "subcategory", "demo_url", "source_url",
    "repository_url", "creator", "rendering_method", "complexity", "status",
    "license", "licence_evidence", "weighted_score",
    "source_inspected", "browser_inspected", "interaction_tested",
    "inspection_date", "confidence",
    "technologies", "dependencies", "rendering_method_detail", "techniques",
    "interaction", "responsive_status",
    "visual_quality", "source_quality", "reusability", "agent_value",
    "integration", "performance", "responsive_accessibility",
    "research_notes",
]


def flatten(cand: dict) -> dict:
    lic = cand.get("licensing", {}) or {}
    ev = cand.get("evaluation", {}) or {}
    insp = cand.get("inspection", {}) or {}
    return {
        "id": cand.get("id", ""),
        "name": cand.get("name", ""),
        "category": cand.get("category", ""),
        "subcategory": cand.get("subcategory", ""),
        "demo_url": cand.get("demo_url", ""),
        "source_url": cand.get("source_url", ""),
        "repository_url": cand.get("repository_url", ""),
        "creator": cand.get("creator", ""),
        "rendering_method": cand.get("rendering_method", ""),
        "complexity": cand.get("complexity", ""),
        "status": cand.get("status", ""),
        "license": lic.get("license", ""),
        "licence_evidence": lic.get("license_url", ""),
        "weighted_score": ev.get("weighted_score", ""),
        "source_inspected": int(bool(insp.get("source_inspected", False))),
        "browser_inspected": int(bool(insp.get("browser_inspected", False))),
        "interaction_tested": int(bool(insp.get("interaction_tested", False))),
        "inspection_date": insp.get("date", ""),
        "confidence": insp.get("confidence", ""),
        "technologies": ";".join(cand.get("technologies") or []),
        "dependencies": ";".join(cand.get("dependencies") or []),
        "rendering_method_detail": cand.get("rendering_method", ""),
        "techniques": ";".join(cand.get("techniques") or []),
        "interaction": ";".join(cand.get("interaction") or []),
        "responsive_status": cand.get("responsive_status", ""),
        "visual_quality": ev.get("visual_quality", ""),
        "source_quality": ev.get("source_quality", ""),
        "reusability": ev.get("reusability", ""),
        "agent_value": ev.get("agent_value", ""),
        "integration": ev.get("integration", ""),
        "performance": ev.get("performance", ""),
        "responsive_accessibility": ev.get("responsive_accessibility", ""),
        "research_notes": (cand.get("research_notes") or "").replace("\n", " ⏎ "),
    }


def main() -> None:
    candidates = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    candidates.sort(key=lambda c: c["id"])
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for c in candidates:
            writer.writerow(flatten(c))
    print(f"CSV OK -> {CSV_PATH.relative_to(REPO)}  ({len(candidates)} rows)")


if __name__ == "__main__":
    main()
