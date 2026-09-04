---
name: debug
description: Diagnose software bugs, incidents, and performance regressions with root-cause analysis, or create and update a repository Debugfile.md. Use project context and configured evidence channels to reproduce safely, test hypotheses, and, when authorized, implement and verify a regression-safe fix.
---

# Debug

Find the causal chain behind the reported behavior. Treat a plausible code path or correlated event as a hypothesis until a discriminating probe supports it.

## Choose the mode

| Request | Mode |
| --- | --- |
| Asks to create or update debugging configuration | Setup |
| Reports broken, incorrect, failing, flaky, or slow behavior | Diagnose |

Both modes use [references/debugfile.md](references/debugfile.md). Read its Setup section and use [assets/Debugfile.md](assets/Debugfile.md) only in Setup mode; otherwise read the discovery, routing, and safety sections as needed.

## Diagnose

1. **Frame.** Record expected behavior, observed behavior, scope, environment, time window, and affected version. Keep facts, reports, and assumptions distinct.
2. **Map.** Find the nearest `Debugfile.md` by searching from the working directory toward the repository root. Validate it with `scripts/validate_debugfile.py`. Load only the context sources and channels relevant to the symptom. Without a Debugfile, continue with discoverable local evidence and report the missing project map.
3. **Reproduce.** Invoke `diagnosing-bugs` when available for its tight-loop discipline. Build the safest pass/fail loop that asserts the exact symptom. Prefer local or isolated environments. For a flaky bug, raise and measure the reproduction rate. If reproduction is unavailable, use captured artifacts or read-only runtime evidence and state the limitation.
4. **Correlate.** Build a timeline across the relevant architecture, request or job identifiers, deployments, logs, traces, metrics, dependencies, and source changes. Documentation describes intended behavior; executable configuration and runtime evidence establish current behavior.
5. **Probe.** Rank 3–5 falsifiable hypotheses. For each, state the prediction and choose the smallest probe that distinguishes it. Change one variable at a time and preserve the evidence.
6. **Conclude.** State the causal chain from trigger through faulty behavior to the user-visible symptom. Classify it as `confirmed`, `probable`, or `unresolved`, with supporting and conflicting evidence.
7. **Correct.** When the request authorizes changes, turn the minimized reproduction into a failing behavior test at the owning seam, apply the smallest coherent fix, and make the test pass. Otherwise stop after the RCA and proposed fix.
8. **Verify.** Re-run the original reproduction, focused checks, then broader risk-appropriate checks. When deployment and live observation are in scope, use the Debugfile's recovery signal and observation window. Record material or recurring bugs at the configured destination.

## Provider adapters

When a Debugfile names both a skill and a CLI, invoke the skill for provider-specific guidance and use the CLI for operations. Prefer established CLIs such as `gh` for GitHub and `acli` for Jira or Confluence; keep their changing command syntax out of this skill. Use read-only operations by default, redact sensitive data before reporting it, and obtain authorization immediately before any external mutation.

## Report

Lead with the current conclusion, then include:

- symptom and impact;
- reproduction or evidence loop;
- causal timeline and root-cause confidence;
- fix and regression coverage, when authorized;
- verification performed and residual uncertainty;
- follow-up observation or bug record, when applicable.
