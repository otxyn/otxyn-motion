"""Build library/manifest.json — the Otxyn Motion curation manifest (initial 40-entry roster).

Inputs : research/candidates.json (research database produced by consolidate.py)
Output : library/manifest.json (+ validation report)

Rules encoded (from mission §11 + LICENSES.md):
- Research candidates are NOT approved library entries; manifest entries are separate
  curations with per-entry licence blocks and explicit adaptation authority.
- Only entries whose inspiration source carries a verified open licence (MIT /
  Apache-2.0 / CC0) may be marked  adapt (attributed adaptation).
- Sources with no licence or unverified licence become  reinvent (technique-level
  reimplementation; the *technique* is documented, the code is not reused).
- Font assets: OFL-only policy; each family verified against google/fonts METADATA.pb
  on the build date (clearances recorded below).
- No third-party code or assets are shipped in this phase; every implementation
  status is 'planned'.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   # research/
REPO = ROOT.parent
OUT = REPO / "library" / "manifest.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

CAND_IMPORTANT = json.loads((ROOT / "candidates.json").read_text(encoding="utf-8"))
CAND = {c["id"]: c for c in CAND_IMPORTANT}

BUILD_DATE = "2026-11-03"

# ---------------------------------------------------------------------------
# Curated roster: candidates.json id  ->  (otxyn id, otxyn name, authority, notes)
# authority: adapt | reinvent | pattern
# Targets: typography 7, particles 6, liquid 5, 3d-shaders 5, transitions 7, composition 10
# ---------------------------------------------------------------------------
ROSTER = {
  "typography": [
    ("typography-011", "typ-self-split-text-reveal", "adapt",
      "Adapt the handbook's dependency-free char-split stagger pipeline (MIT); split -> per-char spans -> staggered translateY/opacity with authored easing."),
    ("typography-012", "typ-self-variable-font-morph", "adapt",
      "Adapt font-variation-settings keyframe loop (MIT); bundle only OFL variable fonts — Honk verified OFL."),
    ("typography-013", "typ-self-text-on-path", "adapt",
      "Adapt SVG textPath startOffset animation (MIT)."),
    ("typography-014", "typ-self-kinetic-typography", "adapt",
      "Adapt rAF per-line kinetic layout (MIT); parameterise line timings."),
    ("typography-015", "typ-self-scramble-text", "adapt",
      "Adapt decode-from-noise per-char cycling (MIT); keep layout width stable via fixed box."),
    ("typography-004", "typ-self-rolling-counter", "adapt",
      "INSP Odometer.js MIT (★7.3k, source read). Re-uses the documented digit-column technique; MIT permits adaptation with attribution — rebuild with tabular-nums + CSS transforms and keep the Odometer attribution header."),
    ("typography-006", "typ-self-text-mask-glitch", "reinvent",
      "Technique reference (Prismic CSS roundup) is an article, not an OSS repo — reimplement background-clip shimmer + ::before/::after clip-path glitch from the documented rules; no code reuse."),
  ],
  "particles": [
    ("particles-023", "par-self-text-particles", "adapt",
      "Adapt pixel-sampling text particles (MIT; mobile-verified pointer physics)."),
    ("particles-024", "par-self-canvas-emitter", "adapt",
      "Adapt spawn/ttl/fade emitter with delta-time physics (MIT)."),
    ("particles-025", "par-self-gpgpu-particles", "adapt",
      "Adapt ping-pong framebuffer particle simulation (MIT); include float-texture fallback path."),
    ("particles-026", "par-self-fireworks-burst", "adapt",
      "Adapt launch->burst two-state machine (MIT)."),
    ("particles-027", "par-self-particle-constellation", "adapt",
      "Adapt proximity-link ambient field (MIT); parameterise link threshold/alpha falloff."),
    ("particles-003", "par-self-threejs-point-waves", "adapt",
      "Official three.js webgl_points_waves example (MIT); ship as parameterised vertex-wave points scene."),
  ],
  "liquid": [
    ("liquid-001", "liq-self-webgl-fluid", "adapt",
      "PavelDoGreat WebGL-Fluid-Simulation (MIT, source read). Adapt solver pass order; document ping-pong/FBO graph rather than minimising the original single file."),
    ("liquid-019", "liq-self-liquid-glass", "adapt",
      "Handbook liquid glass (MIT): backdrop-filter + edge displacement map + drag."),
    ("liquid-020", "liq-self-morphing-blob", "adapt",
      "Handbook noise-contour blob (MIT)."),
    ("liquid-021", "liq-self-displacement-hover", "adapt",
      "Handbook pointer displacement shader (MIT)."),
    ("liquid-011", "liq-self-svg-goo-metaballs", "reinvent",
      "Technique reference: Codrops 'Creative Gooey Effects' (demo rights; technique is standard SVG filter primitives). Reimplement the feGaussianBlur->feColorMatrix chain from documented filter math; credit Lucas Bebber's technique article as inspiration only."),
  ],
  "3d-shaders": [
    ("3d-shaders-002", "shd-self-fragment-noise-field", "adapt",
      "three.js webgl_shader_lava (MIT): fullscreen quad + animated procedural noise."),
    ("3d-shaders-001", "shd-self-vertex-displacement-map", "adapt",
      "three.js webgl_materials_displacementmap (MIT): heightmap-vertex displacement + normals."),
    ("3d-shaders-007", "shd-self-chromatic-displacement-hover", "adapt",
      "akella webgl-mouseover-effects (MIT, demos fetched): mouse-velocity displacement + RGB-offset chromatic aberration."),
    ("3d-shaders-012", "shd-self-scroll-3d-rotation", "adapt",
      "Handbook CSS-3D scroll rotation (MIT): scrollY -> perspective/rotateX with smoothing."),
    ("3d-shaders-005", "shd-self-gpgpu-water", "adapt",
      "three.js webgl_gpgpu_water (MIT, source read): GPGPU heightfield -> deformed grid with recomputed normals."),
  ],
  "transitions": [
    ("transitions-022", "tra-self-mesh-gradient", "adapt", "Handbook SVG-filter mesh gradient (MIT)."),
    ("transitions-023", "tra-self-morph-page-transition", "adapt", "Handbook shape-morph page transition (MIT)."),
    ("transitions-024", "tra-self-synthwave-grid", "adapt", "Handbook CSS perspective grid loop (MIT)."),
    ("transitions-025", "tra-self-wave-layers", "adapt", "Handbook layered SVG waves (MIT)."),
    ("transitions-026", "tra-self-animated-gradient-bg", "adapt", "Handbook generative gradient background (MIT)."),
    ("transitions-027", "tra-self-parallax-depth-of-field", "adapt",
      "Handbook parallax depth layers (MIT). NOTE: browser-inspected only — inspect raw index.html during implementation before coding."),
    ("transitions-007", "tra-self-curtains-geometry-mask", "reinvent",
      "curtains.js (MIT, ★1827) — our entry re-implements ONE geometry-mask transition pattern using the documented DOM-plane approach; credit Martin Laxenaire."),
  ],
  "composition": [
    ("composition-005", "cmp-self-physics-playground-portfolio", "adapt",
      "folio-2019 (MIT, ★4753): study scene-config-driven composition and Box2D navigation; our composition recipe documents the data-driven pattern."),
    ("composition-030", "cmp-self-audio-reactive-suite", "adapt",
      "Chrome Music Lab (Apache-2.0): adapt one audio+canvas coupling pattern; keep Google attribution."),
    ("composition-006", "cmp-self-baked-scene-scroll-tour", "reinvent",
      "my-room-in-3d has NO licence — technique (baked textures + scroll camera path) re-documented from mixed-licence reference; implementation from scratch."),
    ("composition-031", "cmp-self-scrollytelling-data-essay", "reinvent",
      "The Pudding house style (licence per-essay unverified): document stepper/scroll-beat pattern; implement from scratch."),
    ("composition-024", "cmp-self-immersive-story-scroll", "pattern",
      "SBS The Boat — demo verified, no public source; pattern study of audio-illustration scroll coupling only."),
    ("composition-027", "cmp-self-css-shape-storytelling", "pattern",
      "In Pieces — CSS polygon storytelling; no public source; pattern study."),
    ("composition-028", "cmp-self-scroll-story-capsules", "pattern",
      "Neal.fun Deep Sea — no public source; pattern study of depth-coded scroll frames."),
    ("composition-029", "cmp-self-timeline-artifacts-explorer", "pattern",
      "Neal.fun Internet Artifacts — no public source; pattern study of era-sampled artifact browsing."),
    ("composition-021", "cmp-self-cinematic-product-intro", "pattern",
      "Apple AirPods Pro page — marketing demo; pattern study only, no source."),
    ("composition-001", "cmp-self-webgl-agency-hero", "pattern",
      "Lusion v3 — benchmark reference; closed source; documents the persistent-WebGL-scene pattern qualitatively."),
  ],
}

TARGETS = {"typography": 7, "particles": 6, "liquid": 5, "3d-shaders": 5, "transitions": 7, "composition": 10}

CATEGORY_SUB = {  # subcategory carried over from research record
}

def licence_for(cand, authority):
    lic = cand.get("licensing", {})
    raw = (lic.get("license") or "").strip()
    lurl = lic.get("license_url") or ""
    if authority == "pattern":
        return {
            "source_license": raw or "unverified",
            "license_url": lurl,
            "verified": raw in ("MIT", "Apache-2.0", "CC0-1.0"),
            "evidence": lic.get("notes", ""),
            "verified_date": BUILD_DATE if raw in ("MIT", "Apache-2.0", "CC0-1.0") else "",
            "redistribution_allowed": False,
            "mode": "reference showcase only (pattern study); nothing adopted"
        }
    verified = raw in ("MIT", "Apache-2.0", "CC0-1.0")
    if authority == "adapt":
        return {
            "source_license": raw,
            "license_url": lurl,
            "verified": verified,
            "evidence": lic.get("notes", ""),
            "verified_date": BUILD_DATE,
            "redistribution_allowed": bool(verified and raw != "Apache-2.0"),
            "mode": (f"adapted/derived work permitted with attribution under {raw}"
                     if raw == "MIT" else
                     f"Apache-2.0: adaptation permitted with licence + NOTICE-file attribution" if raw == "Apache-2.0" else
                     "adaptation requires explicit permission — flag for re-evaluation"),
            "mode": f"adapt permitted with attribution ({raw})" if verified else raw,
        }
    # reinvent
    return {
        "source_license": raw or "unverified",
        "license_url": lurl,
        "technique_reference_url": lurl or cand.get("source_url") or cand.get("demo_url") or None,
        "verified": verified,
        "evidence": lic.get("notes", ""),
        "verified_date": BUILD_DATE,
        "redistribution_allowed": "technique-level only; no source ingestion",
        "mode": "reimplementation from documented technique",
    }


def entry(cid, oid, authority, notes):
    c = CAND[cid]
    demo = c.get("demo_url") or ""
    isb = c.get("inspection", {})
    return {
        "id": oid,
        "name": c.get("name", ""),
        "category": c["category"],
        "subcategory": c["subcategory"],
        "complexity": c.get("complexity"),
        "rendering": c.get("rendering_method"),
        "research_candidate": cid,
        "inspiration": {
            "demo_url": demo,
            "source_url": c.get("source_url"),
            "repository_url": c.get("repository_url"),
            "creator": c.get("creator"),
        },
        "description": c.get("description", ""),
        "licensing": licence_for(c, authority),
        "adaptation": {
            "authority": authority,
            "plan": notes,
        },
        "implementation": {
            "status": "planned",
            "target_file": f"library/{c['category']}/{oid}/",
            "name": "not implemented yet (research phase ended at curation)",
        },
        "verification_required": {
            "viewports": ["1440x900", "390x844"],
            "console_errors": "0 required",
            "reduced_motion": "prefers-reduced-motion must degrade to a still",
            "licence_gate": "per-entry licence block must remain verified at merge time",
        },
        "inspection_basis": {
            "source_inspected": bool(isb.get("source_inspected")),
            "browser_inspected": bool(isb.get("browser_inspected")),
            "demo_fetched": bool(isb.get("demo_fetched")),
            "confidence": isb.get("confidence"),
        },
        "research_notes": c.get("research_notes", ""),
    }


def build():
    entries, missing = [], []
    for cat, items in ROSTER.items():
        if len(items) != TARGETS[cat]:
            raise SystemExit(f"roster size mismatch for {cat}: {len(items)} != {TARGETS[cat]}")
        for cid, oid, authority, notes in items:
            if cid not in CAND:
                missing.append(cid)
                continue
            e = entry(cid, oid, authority, notes)
            e["category"] = cat if cid.startswith("composition") or cat == "typography" else e["category"]
            entries.append(e)
    # category fix for composition entries whose subcategory we keep
    for e in entries:
        if e["id"].startswith("cmp-"):
            e["category"] = "composition"
        if e["id"].startswith("typ-"):
            e["category"] = "typography"
        if e["id"].startswith("par-"):
            e["category"] = "particles"
        if e["id"].startswith("liq-"):
            e["category"] = "liquid"
        if e["id"].startswith("shd-"):
            e["category"] = "3d-shaders"
        if e["id"].startswith("tra-"):
            e["category"] = "transitions"

    # ---- reserves: strong shortlisted / inspected entries NOT in the initial 40 ----
    selected = {r[0] for items in ROSTER.values() for r in items}
    reserves = []
    for c in CAND_IMPORTANT:
        if c["id"] in selected:
            continue
        if c.get("status") in ("shortlisted", "inspected") and (c.get("evaluation", {}).get("weighted_score") or 0) >= 7.0:
            reserves.append({
                "research_candidate": c["id"], "name": c["name"], "category": c["category"],
                "score": c["evaluation"]["weighted_score"], "licence": c["licensing"]["license"],
                "reason": "reserve pool for post-v1 expansion / technique reference",
            })

    fonts = {
        "policy": "OFL-only. No unlicensed display font is ever bundled. Verified per family against google/fonts METADATA.pb on " + BUILD_DATE + ".",
        "verified": [
            {"family": "Honk", "variant": "variable", "licence": "OFL", "evidence": "https://raw.githubusercontent.com/google/fonts/main/ofl/honk/METADATA.pb", "used_by": ["typ-self-variable-font-morph"]},
            {"family": "Inter", "licence": "OFL", "evidence": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/METADATA.pb", "used_by": ["all DOM/UI text"]},
            {"family": "Roboto Flex", "variant": "variable", "licence": "OFL", "evidence": "https://raw.githubusercontent.com/google/fonts/main/ofl/robotoflex/METADATA.pb", "used_by": ["typ-self-rolling-counter (variable height/width for digit morphing)"]},
            {"family": "Anton", "licence": "OFL", "evidence": "https://raw.githubusercontent.com/google/fonts/main/ofl/anton/METADATA.pb", "used_by": ["split-text/kinetic display headline"]},
            {"family": "Space Grotesk", "licence": "OFL", "evidence": "https://raw.githubusercontent.com/google/fonts/main/ofl/spacegrotesk/METADATA.pb", "used_by": ["scramble/tech-flavoured text"]},
            {"family": "Archivo Black", "licence": "OFL", "evidence": "https://raw.githubusercontent.com/google/fonts/main/ofl/archivoblack/METADATA.pb", "used_by": ["text-particles raster source (heaviest mass)"]},
        ],
        "avoided": [
            "Any font referenced by third-party demos without asserted OFL status",
            "GSAP-provided or Codrops-bundled fonts (unknown packaged licence)",
            "Third-party images/shaders/images used by inspiration demos (assets != code licences)",
        ],
    }

    route_tables = [
        {"family": "char/word stagger", "default": "DOM spans + CSS variables",
         "escalate": "GSAP timeline (licence: GSAP no-charge — do not vendor)", "never": "Canvas re-draw", "ref": "typography-009 constants"},
        {"family": "rolling counter", "default": "DOM digit columns + CSS transform",
         "escalate": "rAF count-up + tabular-nums", "never": "image-sprite flips", "ref": "typography-004"},
        {"family": "text to particles", "default": "Canvas 2D pixel sampling",
         "escalate": "WebGL points above ~20k particles", "never": "SVG element-per-pixel", "ref": "particles-023"},
        {"family": "ambient metaballs", "default": "SVG goo filter chain",
         "escalate": "Canvas physics + goo above ~50 moving bodies", "never": "WebGL solver (overkill)", "ref": "liq-self-svg-goo-metaballs"},
        {"family": "interactive fluid", "default": "canvas heightfield ripple",
         "escalate": "WebGL stable-fluids solver", "never": "CSS approximation", "ref": "liquid-001"},
        {"family": "image distortion hover", "default": "SVG feDisplacementMap (static)",
         "escalate": "WebGL displacement shader (pointer-driven)", "never": "per-pixel canvas ops", "ref": "3d-shaders-007"},
        {"family": "mesh gradient", "default": "SVG turbulence chain",
         "escalate": "WebGL fbm mesh-gradient shaders", "never": "animated bitmap", "ref": "transitions-022"},
        {"family": "3D scroll scene", "default": "CSS 3D transforms",
         "escalate": "three.js camera-path tour", "never": "position:fixed hacks", "ref": "3d-shaders-012"},
        {"family": "GPU particle equation", "default": "Canvas 2D emitter",
         "escalate": "GPGPU ping-pong textures >10k", "never": "thread-per-particle", "ref": "particles-025"},
    ]

    verification_checklist = [
        "Load demo/implementation at 1440x900 AND 390x844 (Playwright: browser_resize then browser_take_screenshot with scale:'css').",
        "browser_console_messages({level:'error'}) must report 0 errors for both passes.",
        "Screenshot before/after the effect trigger and diff to prove the animation actually fires.",
        "Toggle prefers-reduced-motion (browser_emulate_media) — the effect must degrade to a still frame or cut immediately.",
        "Check frame-budget: rAF loops must use delta-time and not scale work with devicePixelRatio unclamped.",
        "Verify the entry's licence block still resolves to a live licence URL at merge time.",
    ]

    manifest = {
        "name": "Otxyn Motion Library",
        "manifest_version": "0.1.0",
        "generated": BUILD_DATE,
        "generated_by": "research/tools/build_manifest.py",
        "note": "Curation manifest: entries are approved *intent*, not shipped implementations. Research candidates remain in research/candidates.json and are never referenced from the website build.",
        "library_targets": TARGETS,
        "entry_count": len(entries),
        "adaptation_authorities": {
            "adapt": "source licence verified open (MIT/Apache-2.0/CC0) — adapted implementation ships with attribution block",
            "reinvent": "source absent/unclear — technique-only documentation; implementation written from scratch",
            "pattern": "closed-source demo — documented as design pattern for agent study, explicitly never adopted as code",
        },
        "licence_blocks": {
            "MIT": "Copyright notice + licence text must accompany any MIT-derived file in library/; MIT adaptation keeps upstream attribution in the entry header comment.",
            "Apache-2.0": "A NOTICE file and the Apache 2.0 text are required; modifications must be marked.",
            "unknown/unverified": "BLOCKED from adoption — read reason in entry block; escalate to the licence owners or re-implement.",
        },
        "fonts": fonts,
        "route_tables": route_tables,
        "verification_checklist": verification_checklist,
        "entries": entries,
        "reserves": reserves,
        "inspection": {
            "source_inspected_entries": sum(1 for e in entries if e["inspection_basis"]["source_inspected"]),
            "browser_inspected_entries": sum(1 for e in entries if e["inspection_basis"]["browser_inspected"]),
            "reinvent_or_pattern_entries": sum(1 for e in entries if e["adaptation"]["authority"] != "adapt"),
        },
    }
    OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    # ---------------------------- validation ----------------------------
    errs = []
    if missing:
        errs.append(f"missing candidate ids: {missing}")
    if len(entries) != 40:
        errs.append(f"entry count {len(entries)} != 40")
    counts = {}
    for e in entries:
        counts[e["category"]] = counts.get(e["category"], 0) + 1
        if e["category"] not in TARGETS:
            errs.append(f"bad category {e['category']}")
        if counts[e["category"]] > TARGETS[e["category"]]:
            errs.append(f"over-target category {e['category']}")
        if e["adaptation"]["authority"] == "adapt" and not e["licensing"]["verified"]:
            errs.append(f"adapt entry without verified licence: {e['id']}")
        if not e["licensing"]["license_url"] and e["adaptation"]["authority"] == "reinvent" and not e["licensing"].get("technique_reference_url"):
            errs.append(f"reinvent entry without technique reference url: {e['id']}")
        if e["adaptation"]["authority"] == "adapt" and not e["licensing"]["license_url"]:
            errs.append(f"adapt entry missing licence evidence url: {e['id']}")
        if e["licensing"]["verified"] and e["licensing"]["source_license"] not in ("MIT", "Apache-2.0", "CC0-1.0"):
            errs.append(f"unrecognised licence {e['id']}")
    ids = [e["id"] for e in entries]
    if len(ids) != len(set(ids)):
        errs.append("duplicate otxyn ids")

    print(f"entries: {len(entries)}  counts: {counts}")
    print("reserves logged:", len(reserves))
    if errs:
        print("FAILED:", *errs, sep="\n  ")
        raise SystemExit(1)
    print("MANIFEST OK ->", OUT)


if __name__ == "__main__":
    build()
