# Working in this repository

This repository is a personal library of Agent Skills: first-party skills we create, third-party skills we gather under `vendor/`, and skills installed for local use.

## Before adding a skill

1. Define the task, trigger conditions, expected output, and success criteria.
2. Use `find-skills` to search the ecosystem and inspect relevant existing skills.
3. Choose the smallest ownership model that fits:

| Finding | Action |
| --- | --- |
| A maintained upstream skill already fits | Vendor it as a submodule. |
| An upstream skill is close | Prefer contributing upstream or adding a thin first-party adapter. |
| Several skills already cover the work | Create a small router that points to them. |
| No suitable skill exists | Use `skill-creator` (`create-skill`) to draft and, when useful, evaluate a new one. |

Research current, primary documentation for volatile tools and formats. Record provenance and license; do not silently copy third-party content into first-party skills.

## First-party skills

Follow the [Agent Skills specification](https://agentskills.io/specification).

```text
<skill-name>/
├── SKILL.md          # required: metadata, decisions, workflow, routing
├── references/       # optional: detailed or variant-specific knowledge
├── scripts/          # optional: deterministic or repeated operations
├── assets/           # optional: templates and files used in outputs
└── evals/            # optional repo convention: behavioral verification
```

- Keep every first-party skill in a root-level `<skill-name>/SKILL.md` directory. Do not group skills under category directories. <!-- user-specified -->
- Treat the directory as a self-contained installable unit. Runtime files must live inside it.
- Give `SKILL.md` valid YAML frontmatter. `name` must match the directory and use lowercase letters, numbers, and single hyphens.
- Treat `description` only as the activation router: say what tasks should trigger the skill, using concrete contexts and keywords. Put workflow, rationale, and output details in the body or bundled resources. <!-- user-specified -->
- Keep `SKILL.md` thin. Include only instructions needed on every invocation; link optional branches directly to focused files one level deep.
- Prefer tables, code blocks, bullets, and short sections. Avoid long prose.
- Add a resource only when it earns its maintenance cost. Prefer native capabilities and existing skills before new scripts, dependencies, or abstractions.
- Preserve portability. Use agent-specific fields or instructions only when the skill requires them, and declare real environment requirements in `compatibility`.
- A skill may be mostly routing or references when existing skills already own the execution details.

### Skill dependencies

Declare direct skill dependencies as one space-separated string:

```yaml
metadata:
  "orshemtov/skill-dependencies": "research writing-for-humans tdd"
```

- Omit the field when the skill has no dependencies; do not list transitive dependencies.
- Treat every listed skill as required. Before execution, verify it is available; when missing, stop and report its source and installation instruction.

## Progressive disclosure

| Layer | Content | Rule |
| --- | --- | --- |
| Metadata | `name`, `description` | Small and precise; loaded for every skill. |
| `SKILL.md` | Decisions and common workflow | Concise; loaded whenever the skill activates. |
| Bundled resources | References, scripts, assets, evals | Load or run only for the applicable branch. |

Keep each meaning in one place. Move detail out of `SKILL.md` when it serves only some invocations, but keep the pointer and its read condition in `SKILL.md`.

## Vendored skills

- Keep third-party repositories under `vendor/` as Git submodules.
- Prefer shallow, branch-following checkouts; use sparse checkout when only part of a large upstream is relevant.
- Preserve upstream structure, history boundary, source URL, and license.
- Do not edit vendored files or change/update submodule commits without explicit approval.
- Do not present a submodule as floating: the parent repository still records an exact commit.
- If adaptation is needed, keep it in a root-level first-party skill and point to the vendored source only when that remains portable.

## Review before completion

- The workflow matches the stated trigger and success criteria.
- The skill is not duplicating a maintained existing skill.
- `SKILL.md` frontmatter follows the current Agent Skills specification.
- Every referenced file exists, is reachable from `SKILL.md`, and has a clear load condition.
- Scripts are self-contained or document dependencies, report useful errors, and handle relevant edge cases.
- Objective behavior has focused evals when they add confidence.
- `SKILL.md` has been trimmed with Ponytail: remove no-ops, duplication, speculative flexibility, and unnecessary resources.
- Run the available skill validator and repository checks; report what actually ran and any residual uncertainty.

Before committing a new or changed skill, inspect the complete diff, including untracked files, and confirm the skill remains self-contained and installable.
