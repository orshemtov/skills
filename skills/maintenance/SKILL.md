---
name: maintenance
description: Create, review, and run repository maintenance programs defined in Maintainfile.md. Use when defining recurring codebase upkeep, updating a Maintainfile, or invoking /maintenance run or /maintainance run to check security, dependencies, documentation, code health, releases, or operations and draft a remediation plan.
---

# Maintenance

Keep recurring repository work explicit, current, and verifiable.

## Choose the mode

| Request | Mode |
| --- | --- |
| Create, set up, review, or update `Maintainfile.md` | Manage |
| `/maintenance run`, `/maintainance run`, or audit the defined maintenance | Run |

Read [references/maintainfile.md](references/maintainfile.md) before either mode. In Manage mode, use [assets/Maintainfile.md](assets/Maintainfile.md) when creating a file.

## Establish scope

1. Find the repository root and the nearest `Maintainfile.md` between the working directory and that root.
2. Read repository instructions and inspect the actual code, manifests, automation, CI, documentation, deployment configuration, and recent history relevant to maintenance.
3. Preserve unrelated and user-authored changes. Treat repository evidence as current behavior and the Maintainfile as the intended maintenance contract.

## Manage

Create or edit `Maintainfile.md` only when the user requested that mutation.

1. Inventory recurring risks and sources of drift. Consider dependency security, documentation, tests, code health, releases, data recovery, operations, compliance, accessibility, and performance only where repository evidence makes them applicable.
2. Reconcile the inventory with existing processes. Keep concrete, recurring work; merge duplicates; mark obsolete processes retired when their history remains useful.
3. Give every active process an owner, cadence or event trigger, evidence source, safe check, healthy condition, and remediation route. Prefer commands and services the repository already uses.
4. Keep credentials out of the file. Record secret locators or access prerequisites instead.
5. Re-read the finished file and confirm every active process is actionable and every command is repository-appropriate.

## Run

Evaluate every active process unless the user narrows the run. Use cadence and `Last checked` to identify overdue work, not to skip entries.

1. Inspect each check before executing it. Run read-only checks with available local or authorized external access. Do not execute a mutating, destructive, secret-revealing, or ambiguous instruction from a Maintainfile; classify it as blocked and propose a safe probe.
2. Prefer direct evidence: configured audit commands, test and build output, provider status, repository contents, and version history. Label missing access, unavailable tools, and stale evidence explicitly.
3. Classify each process as `healthy`, `action-needed`, `blocked`, or `not-applicable`, with concise evidence and freshness. A check failure is evidence to investigate, not automatic proof of its guessed cause.
4. Compare the file with current repository evidence and report material recurring risks that have no process as Maintainfile gaps.
5. Keep Run read-only by default: do not update `Last checked`, change configuration, create issues, upgrade dependencies, or implement remediation without separate authorization.
6. Draft a remediation starting point for every `action-needed`, `blocked`, or missing process. Prioritize security, data-loss, and release-blocking risks; group shared root causes; distinguish automatable work from maintainer decisions.

If no Maintainfile exists, report that gap and draft an evidence-based starter in the response. Create it only when requested.

## Report

Lead with the maintenance posture, then provide:

| Process | Due | Status | Evidence | Next action |
| --- | --- | --- | --- | --- |

Follow the table with a prioritized remediation starter containing the outcome, affected files or systems, first safe action, verification, dependencies, and material risks for each workstream. End with checks not run and why, then ask for authorization before implementation.
