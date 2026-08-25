---
name: read-the-docs
description: Use when a task requires authoritative technical research before planning, recommending, or implementing a solution.
---

# Read the docs

Research enough to make the next decision with evidence. Match the depth to the task instead of applying a fixed research ritual.

## Frame the research

- Start from the user's goal, the repository context, and the decision the research must support.
- Go broad for unfamiliar ecosystems, architecture choices, or consequential work. Stay narrow for a specific API, behavior, or uncertainty.
- Identify relevant versions when they can change the answer. Do not turn version inventory into the main task.

## Gather authoritative evidence

- Inspect enough local code and configuration to know which external guidance applies.
- Use [references/source-authority.md](references/source-authority.md) to choose and compare sources.
- Use Context7 first for documentation lookup when it is available.
- Look for a project-authored agent skill or guidance and the official documentation. Read both when each adds useful context.
- Go to the project's official documentation or source directly when Context7 lacks coverage, precision, provenance, or the required version.
- Verify important claims against primary sources. Cite the exact pages that support them.
- Search further when sources conflict, appear stale, or do not cover the local constraints.

## Reach a decision

- Translate the evidence into guidance for this repository; do not repeat documentation without applying it.
- Stop when the evidence supports the next decision and additional research is unlikely to change it.
- State conflicts, gaps, assumptions, and residual uncertainty instead of smoothing them over.
- Use [assets/research-brief.md](assets/research-brief.md) when a written research brief would help.

## Continue or confirm

- In plan mode, present the findings and recommendation, then wait for confirmation before implementation.
- Otherwise, continue when implementation is already authorized and the research reveals no material new choice.
- Ask before continuing when the findings introduce a consequential dependency, architecture choice, scope change, or external action.
