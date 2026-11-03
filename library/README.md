# Library entry reference layer

Each approved entry (see `library/manifest.json` → `entries[]`) ships a reference
folder in this pattern:

```
library/<category>/<otxyn-id>/
└── reference.md      # 4 layers: PLAIN WORDS → PASS GRAPH → PARAMETERS → ATTRIBUTION
```

`PLAIN WORDS` is the prose an agent can turn into a prompt.
`PASS GRAPH` is the actual rendering pipeline, verified during the research phase
(fingerprints/source reads — audit trail referenced inside each document).
`PARAMETERS` lists only *measured* constants with their source; unmeasured values
say "read from the raw source at implementation time" instead of inventing numbers.
`ATTRIBUTION` / licence block is mandatory whenever the manifest entry's
`adaptation.authority` is `adapt` (per-entry `licensing` block in the manifest).

No reference here contains any third-party code in bulk — they are technical
descriptions of techniques, with links out to the original work. Otxyn
implementations are created in a later phase and live in these same folders.

Worked example: `library/typography/typ-self-split-text-reveal/reference.md`.

When implementing an entry, also read `skill/SKILL.md` (selection, licence gate,
verification) and `skill/CRAFT.md` (craft doctrine: timing, composition, refinement,
production budgets). Measured constants in a reference layer always outrank CRAFT.md
doctrine defaults.
