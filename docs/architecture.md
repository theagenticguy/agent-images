# Architecture

> Placeholder. Document the ERPAVal phases (Explore → Research → Plan → Act → Validate → Compound) and how they map to module boundaries here.

## Phases

- **Explore** — `src/erpaval/explore/` — Lightweight reconnaissance.
- **Research** — `src/erpaval/research/` — Grounding via Context7 / docs / code search.
- **Plan** — `src/erpaval/plan/` — EARS specs, task decomposition.
- **Act** — `src/erpaval/act/` — Subagent execution + write protocol.
- **Validate** — `src/erpaval/validate/` — Type-check, lint, test, smoke.
- **Compound** — `src/erpaval/compound/` — Lesson capture into `.erpaval/solutions/`.

Each phase is a standalone module with a stable input/output contract so they can be reordered, skipped, or swapped per the adaptive classifier's decision.
