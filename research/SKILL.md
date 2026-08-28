---
name: research
description: Use when a decision, comparison, or unfamiliar topic needs multi-source research and a cited report before planning or implementation.
metadata:
  "orshemtov/skill-dependencies": "writing-for-humans"
---

# Research

Research to reduce a decision's uncertainty, then produce an evidence-backed report.

## Workflow

1. Verify `writing-for-humans` is available. If missing, stop with its source (`orshemtov/skills`) and installation command: `npx skills add orshemtov/skills --skill writing-for-humans`.
2. Define the decision, reader, scope, constraints, freshness, report destination, and a small set of answerable questions. Define comparison dimensions before judging options.
3. Inspect existing material first: user-provided sources, prior reports, repository context, and relevant internal knowledge. Update an existing artifact when it owns the topic.
4. Gather the strongest evidence for each claim:
   - Primary sources for behavior, contracts, status, and factual records.
   - Credible independent sources for operational experience and interpretation.
   - Current versions, dates, and pricing for time-sensitive claims.
5. Follow decisive claims to their source, triangulate when consequences are high, and record conflicts or gaps. Prefer independent evidence over repeated copies of one claim.
6. Synthesize across questions rather than summarizing sources. Distinguish fact, inference, and recommendation; test the recommendation against counterevidence.
7. Stop when the questions are answered, contradictions are resolved or exposed, and more searching is unlikely to change the decision.

## Report

Invoke `writing-for-humans`, then apply these research-specific requirements:

- Lead with the current answer.
- Use a matrix for repeated comparisons and prose for reasoning.
- Cite claims inline and list sources with freshness dates.
- State tradeoffs, risks, gaps, assumptions, and what could change the recommendation.
- End with the next decision or action when evidence supports one.

Write or update the requested destination. Without one, follow the project's convention or create a clearly named Markdown report in a sensible location.

Research is the checkpoint before planning or implementation. Continue only when already authorized and no material new choice emerged.
