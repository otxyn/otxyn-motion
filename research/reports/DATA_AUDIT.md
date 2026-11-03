# DATA AUDIT (gen_data_audit.py output)

Generated from the canonical databases at generation time. Reproduce with
`python scripts/gen_data_audit.py`.

## Headline figures (verified)

- Candidates: **133** in `research/candidates.json`
- Shortlisted: **37** (status `shortlisted`)
- Records with `inspected` status: **37**; with `discovered`: **59**
- Source-inspected (boolean): **65**
- Browser-inspected (boolean): **22**
- Scored (weighted_score present): **50** of 133; score >= 7.0: **49**
- Licence state: {'unverified': 89, 'MIT': 42, 'codrops-style free-use': 1, 'Apache-2.0': 1} - only 43 records carry an open licence verified (MIT/Apache-2.0)
- Preview screenshots: **24** PNG files exist in `research/previews/` on disk
- Manifest entries: **40** planned (all `implementation.status: "planned"`), reserves: **18**
- Manifest categories: {'typography': 7, 'particles': 6, 'liquid': 5, '3d-shaders': 5, 'transitions': 7, 'composition': 10}
- Manifest authorities: {'adapt': 29, 'reinvent': 5, 'pattern': 6}
- Manifest licences: {'MIT': 29, 'unverified (unverified)': 10, 'Apache-2.0': 1}
- OFL-verified font families: **6**

## Distribution by category

| Category | Total | Discovered | Inspected | Shortlisted | Source-inspected | Browser-inspected |
|---|---:|---:|---:|---:|---:|---:|
| 3d-shaders | 12 | 0 | 2 | 10 | 12 | 3 |
| composition | 31 | 29 | 0 | 2 | 0 | 0 |
| liquid | 21 | 14 | 3 | 4 | 4 | 3 |
| particles | 27 | 3 | 17 | 7 | 22 | 5 |
| transitions | 27 | 10 | 10 | 7 | 15 | 6 |
| typography | 15 | 3 | 5 | 7 | 12 | 5 |
| **Total** | **133** | **59** | **37** | **37** | **65** | **22** |

## Documented discrepancies (narrative docs vs. data)

| Document | Finding |
|---|---|
| SHORTLIST.md section B | claimed particles shortlisted = 5; data shows 7 |
| SHORTLIST.md section B | claimed liquid shortlisted = 4; data shows 4 |
| SHORTLIST.md section B | claimed 3d-shaders shortlisted = 7; data shows 10 |
| SHORTLIST.md section B | claimed transitions shortlisted = 6; data shows 7 |
| research/README.md (older copies) | claimed manifest.json "does not exist yet" - superseded in the 2026-11-03 curation phase; the shipped README no longer contains that claim |

Resolution policy: the **data is the fact base**. Narrative docs have been corrected to match the data (corrections noted in RESEARCH_LOG); no datum was changed to make a document consistent. SHORTLIST.md section B counts were updated against the JSON.
