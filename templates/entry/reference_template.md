# {OTXYN_ID} — entry reference

**Status:** `{STATUS}`  <!-- planned | researching | documented | implemented | verified -->
**Name:** {ENTRY_NAME}
**Category:** {CATEGORY} / {SUBCATEGORY}
**Authority:** {ADAPT_REINVENT_OR_PATTERN} | **Source licence:** {LICENSE_NAME} (verified: {TRUE_OR_FALSE})
**Inspection basis:** {SOURCE_OR_BROWSER_STAGE_FROM_RESEARCH}

Research provenance: `{CANDIDATE_ID}` in `research/candidates.json`.
Inspiration demo: {DEMO_URL}
Source: {SOURCE_URL}

---

## LAYER 1 — PLAIN-WORDS

Write ≤4 sentences here describing what the animation does, purely visually, in words
that a coding agent could turn into a prompt with no code in front of it. Include the
one-line "copyable prompt" phrasing. No jargon that a DOM/CSS/Canvas beginner cannot
parse.

---

## LAYER 2 — PASS-GRAPH

The rendering pipeline itself, drawn as a one-way chain:

```
[trigger] -> [stage 1] -> [stage 2] -> ... -> [paint]
```

- Who owns each uniform / CSS variable / canvas state?
- What is the fallback tier when a capability is missing (WebGL1 float textures,
  reduced motion, no-composited-layer mobile)?
- Cite the exact inspiration files/lines read, with URLs.

---

## LAYER 3 — PARAMETERS

ONLY measured constants, provenance required. If a value is a doctrine default rather
than measured (CRAFT.md §1), write the source as "doctrine default" and tag the code
comment `// default`. Never invent a magic number.

| Parameter | Value | Source |
|---|---|---|
| | | |

---

## LAYER 4 — ATTRIBUTION

{ATTRIBUTION_RULES_PER_AUTHORITY_SEE_MANIFEST}

Licence evidence: {LICENCE_EVIDENCE_URL}

---

## Verification requirements (from manifest.verification_required)

- Viewports: 1440x900 AND 390x844
- Console: 0 errors (browser_console_messages({ level: "error" }))
- Reduced motion: degrade to a still
- Licence gate: re-verify licence URL live at merge time
