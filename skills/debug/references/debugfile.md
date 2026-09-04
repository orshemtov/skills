# Debugfile

`Debugfile.md` is a repository-owned map of how to understand, observe, reproduce, and verify the system. Its YAML frontmatter holds the structured routing contract; its Markdown body may hold project-specific debugging guidance. Keep debugging method in the `debug` skill and provider mechanics in provider skills; the Debugfile only routes to them.

## Discovery

Search from the current directory upward and use the nearest `Debugfile.md`. Resolve repository-relative paths from the directory containing that file. A closer Debugfile may specialize a monorepo subtree.

Run:

```sh
python3 <debug-skill>/scripts/validate_debugfile.py <path>/Debugfile.md
```

The validator requires Python 3 and PyYAML. It validates the YAML frontmatter and leaves the Markdown body flexible. Treat warnings as freshness or portability work, not schema failure.

## Frontmatter contract

| Field | Shape | Purpose |
| --- | --- | --- |
| `version` | integer | Contract version; currently `1` |
| `defaults` | mapping | Default environment, production access, and redaction policy |
| `context.sources` | list | Architecture, developer docs, ADRs, CI/CD, runbooks, service catalogs, and incident history |
| `services` | list | Source locations, environments, dependencies, and relevant context |
| `channels` | list | Logs, traces, metrics, errors, deployments, audit, databases, and runtime evidence |
| `reproduction` | mapping | Preferred environment, instructions, fixtures, and runnable commands |
| `verification` | mapping | Focused/broad checks and live recovery signals |
| `records` | mapping | Destination and policy for material RCA records |

All top-level fields except `defaults` are required, but lists and mappings may be empty when the project has no corresponding capability.

## Context sources

Use context before querying telemetry: architecture and delivery knowledge shrink the hypothesis space and expose ownership boundaries.

```yaml
context:
  sources:
    - id: system-architecture
      kind: architecture
      source:
        type: repository
        location: docs/architecture/README.md
      applies_to: [api, worker]
      authority: canonical
      use_when: Tracing service boundaries, dependencies, and data flow.
      last_verified: 2026-08-28

    - id: engineering-handbook
      kind: developer-guide
      source:
        type: confluence
        location: ENG/Developer-Handbook
      adapter:
        cli: acli
        skill: confluence
      authority: supporting
      use_when: Understanding development and operational conventions.
      last_verified: 2026-08-28

    - id: deployment-pipeline
      kind: delivery
      source:
        type: repository
        location: .github/workflows/deploy.yml
      authority: executable
      use_when: Determining what was built, migrated, deployed, or rolled back.
```

Recommended `kind` values are `architecture`, `developer-guide`, `contributing`, `service-catalog`, `delivery`, `runbook`, `decisions`, `data-model`, and `incident-history`.

Authority means:

| Value | Interpretation |
| --- | --- |
| `executable` | Configuration or automation currently controls behavior |
| `canonical` | Maintained source of intended truth |
| `supporting` | Useful context that may be incomplete or stale |
| `historical` | Previous decisions or incidents |

Runtime evidence wins disagreements about current behavior. Preserve the disagreement because stale documentation, partial rollout, or configuration drift may itself be causal.

## Services

```yaml
services:
  - name: api
    source: src/api
    environments: [local, staging, production]
    depends_on: [postgres, payments]
    context: [system-architecture, deployment-pipeline]
```

Use project vocabulary. Avoid reproducing a full service catalog when an authoritative source already exists; point to it from `context.sources`.

## Evidence channels

```yaml
channels:
  - id: api-logs
    kind: logs
    provider: datadog
    environments: [staging, production]
    use_when: Investigating request failures or background-job errors.
    adapter:
      cli: datadog-ci
      skill: datadog
    access:
      method: cli
      instructions: docs/runbooks/datadog.md
      config: path:config/observability.yml
      credentials: env:DD_API_KEY
    scope:
      service: example-api
    correlate_by: [trace_id, request_id, deployment_sha]
    safety:
      mode: read-only
      sensitive_data: redact

  - id: deployments
    kind: deployments
    provider: github
    environments: [production]
    use_when: Correlating a regression with build and deployment changes.
    adapter:
      cli: gh
      skill: github
    access:
      method: cli
      credentials: profile:github
    correlate_by: [deployment_sha]
    safety:
      mode: read-only
      sensitive_data: redact
```

Recommended `kind` values are `logs`, `traces`, `metrics`, `errors`, `deployments`, `audit`, `database`, and `runtime`.

### Adapter rule

An `adapter` binds a provider skill to its established CLI. Invoke the named skill when available, then use the CLI rather than recreating provider commands or driving a browser. Examples:

| Provider | CLI | Skill |
| --- | --- | --- |
| GitHub | `gh` | `github` |
| Jira | `acli` | `jira` |
| Confluence | `acli` | `confluence` |

When a configured skill or CLI is unavailable, report that channel as unavailable and continue with independent evidence. Consult official documentation before improvising volatile command syntax. Use a connector, API, or browser only when the Debugfile selects it or the CLI cannot perform the required read.

## Access and secrets

Store locators, never credential values:

```yaml
credentials: env:DD_API_KEY
credentials: profile:production-readonly
credentials: connector:atlassian
credentials: secret-manager:teams/platform/datadog
credentials: keychain:work/github
credentials: instructions:docs/runbooks/access.md
```

Repository paths may use `path:`. Access instructions may point to repository files or protected documentation. Keep production `read-only` by default. A Debugfile describes possible access; verify that access exists before relying on it.

## Reproduction and verification

```yaml
reproduction:
  preferred_environment: local
  instructions: docs/debug/reproduction.md
  commands:
    focused: uv run pytest tests/api/test_orders.py
    broad: uv run pytest

verification:
  commands:
    focused: uv run pytest tests/api/test_orders.py
    broad: uv run pytest
  live:
    - channel: api-logs
      success_signal: No matching order-processing errors
      observation_window: 30m

records:
  destination: github-issues
  adapter:
    cli: gh
    skill: github
  instructions: docs/debug/bug-records.md
  record_when: Severe, recurring, or architecturally informative.
```

Commands are project-owned entrypoints, not arbitrary generated shell. Preserve them exactly unless repository changes require an update.

## Setup mode

1. Inspect repository facts before interviewing: root guidance, developer and architecture docs, ADRs, service manifests, build/test commands, CI/CD, infrastructure, migrations, telemetry libraries, runbooks, incident templates, installed skills, and available CLIs.
2. Follow external references already named by the repository. Prefer established provider CLIs and pair each with its relevant skill.
3. Ask only unresolved decisions in rounds, with a recommended conservative answer. Use `grilling` when available. Cover environment/account mappings, production access, correlation identifiers, credential locators, recovery signals, and bug-record destinations.
4. Start from `assets/Debugfile.md`. Preserve valid existing entries, write references rather than copied private documentation, and keep credential values out of the file.
5. Validate the result. Resolve schema errors and likely inline secrets; report missing paths and unverified external references as warnings.
6. Summarize discovered facts, user decisions, configured gaps, and the exact validation performed.
