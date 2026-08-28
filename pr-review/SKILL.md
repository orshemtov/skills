---
name: pr-review
description: Use when reviewing a pull request, branch, commit range, or code diff before merge.
---

# PR review

Review changes for defects that could cause incorrect behavior, regressions, security problems, data loss, performance degradation, compatibility breaks, or inadequate behavioral coverage.

## Workflow

1. Identify the review target and its base revision.
2. Read the repository's applicable agent instructions and contribution guidance.
3. Inspect the complete changed-file list before reviewing individual hunks.
4. Load every reference selected by the table below.
5. Read the diff, relevant surrounding code, and affected tests.
6. Validate each potential finding against an affected execution path or requirement.
7. Report actionable findings first, ordered by severity. Include the file and line, impact, evidence, and the smallest credible remediation.

Do not modify the reviewed code unless the user explicitly asks for fixes.

## Reference routing

| Changed-file extension | Read |
| --- | --- |
| `.py` | [references/python.md](references/python.md) |

Apply the core workflow to every changed file. A missing specialized reference does not exclude a file from review.
