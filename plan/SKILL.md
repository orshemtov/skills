---
name: plan
description: Use for software idea exploration, solution planning, or turning an accepted software solution into an implementation-ready plan. Do not use for personal plans, direct implementation, or simple factual lookups.
metadata:
  "orshemtov/skill-dependencies": "research writing-for-humans tdd"
---

# Plan

Turn a software idea into an accepted solution, then into work that is safe to implement.

## Start

1. Verify the direct dependencies are available. If one is missing, stop with its source and installation instruction:

| Skill | Source | Install |
| --- | --- | --- |
| `research` | `orshemtov/skills` | `npx skills add orshemtov/skills --skill research` |
| `writing-for-humans` | `orshemtov/skills` | `npx skills add orshemtov/skills --skill writing-for-humans` |
| `tdd` | `mattpocock/skills` | `npx skills add mattpocock/skills --skill tdd` |

2. Use solution planning until the user accepts a solution. Use implementation planning only from an accepted solution.
3. Keep drafts conversational. After acceptance, maintain one current-state artifact using the repository convention or `docs/plans/<slug>.md`. Invoke `writing-for-humans`; replace obsolete reasoning instead of narrating the document's history.

## Solution planning

1. Inspect the current code, architecture decisions, constraints, and existing artifacts.
2. Invoke `research` for the solution's unknowns and external claims.
3. Ask the current frontier of material questions in dependency-aware batches. Include a recommendation and consequence for each choice.
4. Request approval before building a prototype.
5. Produce a decision-focused plan covering:
   - problem and outcome
   - constraints and current state
   - credible options and tradeoffs
   - chosen solution and boundaries
   - success criteria
6. Ask for explicit acceptance. On acceptance, update the artifact and mark it `SOLUTION_APPROVED`.

If the user defers the work, offer one issue that states its planning maturity. Create it only after separate approval.

## Implementation planning

1. Confirm the solution is accepted. Inspect the code, tests, dependencies, configuration, and relevant read-only live-system state.
2. Refresh authoritative documentation when feasibility depends on versions, APIs, migrations, or compatibility.
3. Invoke `tdd` before choosing tests or implementation order. Agree the public behavioral seams with the user before planning tests.
4. Plan vertical red → green slices: one failing behavioral test through an agreed public interface, the minimum implementation to pass, then the next slice. Use independent expected values and mock only system boundaries.
5. Depart from TDD only when no meaningful failing behavioral seam exists. Record why and define alternative verification.
6. Produce an exact add/change/delete map covering:
   - modules or files and interfaces
   - dependencies and configuration
   - data, migration, or infrastructure work
   - commands and verification
   - risks and proportionate rollout or rollback concerns
7. Finish with one status:

| Status | Meaning |
| --- | --- |
| `READY` | Exact plan is safe to implement. |
| `NEEDS_DECISION` | A material user choice remains. |
| `BLOCKED` | An external condition prevents progress. |
| `NO_GO` | Evidence invalidates the solution; return to solution planning. |

Ask for explicit acceptance before implementation.
