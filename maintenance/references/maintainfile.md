# Maintainfile format

`Maintainfile.md` is the repository's current contract for recurring maintenance. It describes processes, not a growing transcript of past runs.

## Location and precedence

- Put the canonical file at the repository root.
- In a monorepo, a nested Maintainfile may add or override processes for its subtree. State the inherited root file in Scope.
- Follow repository instructions with higher precedence. Surface conflicts instead of silently rewriting them.

## Required shape

Keep the prose flexible, but give each process these fields so a run is decidable:

```markdown
### dependency-security — Dependency security review

| Field | Value |
| --- | --- |
| Status | active |
| Area | security |
| Owner | maintainers |
| Cadence | weekly; before a production release |
| Applies when | The repository consumes third-party packages. |
| Evidence | Lockfiles, updater configuration, advisory source, CI results |
| Check | Run the repository's read-only audit; inspect updater coverage and unresolved alerts. |
| Healthy when | Supported dependencies have no unresolved actionable advisories and update automation covers every manifest. |
| Remediation | Triage advisories by exploitability, update the smallest safe set, and run affected tests. |
| Last reviewed | YYYY-MM-DD |
| Last checked | YYYY-MM-DD or never |
```

Process IDs use lowercase letters, numbers, and hyphens and remain stable when titles change. Allowed status values are `active`, `paused`, and `retired`. Dates use ISO `YYYY-MM-DD`.

## Writing good processes

- **Recurring:** Describe work that repeats on a cadence or event. One-off debt belongs in an issue or plan.
- **Applicable:** Tie each process to observed technology, delivery, data, or policy. Dependabot is appropriate only for GitHub repositories that choose it; name another updater when that is the actual system.
- **Observable:** Make `Healthy when` independently decidable. “Review code quality” is incomplete; name the evidence and threshold that changes the result.
- **Safe:** Make checks read-only. Put mutations in `Remediation`, where they remain proposals until authorized.
- **Durable:** Prefer repository-native commands and stable file paths over copied tool manuals or volatile CLI syntax.
- **Owned:** Name a role or team even when no individual is assigned. A process with no owner is a finding.

Use prose below a process table for rationale, exceptions, or provider links that do not fit cleanly in a field. Keep run history in issues, reports, CI, or another existing system; update `Last checked` only when the user wants the Maintainfile to carry that state.

## Discovery prompts

Use these as questions, not a mandatory checklist:

| Signal | Candidate recurring process |
| --- | --- |
| Package manifests or lockfiles | Advisories, dependency updates, runtime support |
| Dependabot/Renovate configuration | Coverage, alert triage, stale update PRs |
| Public API, generated docs, examples | Documentation drift and link checks |
| Repeated TODOs, complexity hotspots, flaky tests | Bounded refactoring or test-health review |
| Release automation and artifacts | Release rehearsal, signing, rollback readiness |
| Persistent or customer data | Backup restore tests, retention, migration checks |
| Hosted services, queues, cron, certificates | Operational health, failure queues, expiry checks |
| Licenses, regulated data, accessibility commitments | Compliance-specific verification |

Do not add a process merely because it appears in this table.
