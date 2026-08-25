# Source authority

Choose sources by provenance, applicability, and maintenance—not search rank alone.

## Retrieval order

Use Context7 as the first documentation lookup when it is available. It is a retrieval path, not an authority tier: check the provenance, version, and applicability of the material it returns. Fall back to the project's official site, repository, or other primary sources when Context7 does not provide what the decision needs.

## Preferred sources

Use the strongest sources available for the claim:

1. Project-authored agent skills or agent guidance for the task at hand, checked against the project's official documentation when useful.
2. Official documentation, specifications, migration guides, and release notes.
3. First-party source code and tests when documented behavior is incomplete or ambiguous.
4. Maintainer-authored proposals, issues, discussions, talks, and examples.
5. Established third-party material with clear authorship, evidence, maintenance, and relevant adoption.

An official agent skill may provide the most actionable workflow, while official documentation remains important for supported behavior and precise details. Use both when they answer different parts of the question.

## Evaluate applicability

Before relying on a source, check:

- Does it cover the technology and version in use?
- Is it maintained by the project or a credible practitioner?
- Is the advice current, supported, and intended for this use case?
- Does it conflict with repository constraints or newer primary evidence?

Popularity is supporting evidence, not proof. Treat a new, low-adoption, unofficial project as a weak authority unless it provides direct evidence that can be independently verified. Do not penalize an official project merely because it is new.

## Resolve conflicts

When sources disagree:

1. Prefer the source closest to the implementation and version in question.
2. Check dates, release lines, and whether one source supersedes another.
3. Verify behavior in source code, tests, or a minimal local experiment when practical.
4. Report the disagreement and its consequence if the evidence remains inconclusive.

Do not use secondary sources to overrule a clear primary source without stronger, directly verifiable evidence.
