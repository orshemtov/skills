# Working in this repository

This is a personal library of portable Agent Skills.

- Keep every first-party skill in a root-level `<skill-name>/SKILL.md` directory. Do not group skills under category directories. <!-- user-specified -->
- Give every skill valid YAML frontmatter with a lowercase, hyphenated `name`.
- Write the frontmatter `description` only for routing and activation: state when the skill should be used. Keep workflow, rationale, and output details in the skill body or bundled resources. <!-- user-specified -->
- Treat each skill directory as a self-contained installable unit. Do not require files outside the skill directory at runtime.
- Keep `SKILL.md` focused on triggering, decisions, workflow, boundaries, and routing to bundled resources.
- Put detailed knowledge in `references/`, deterministic or repeated operations in `scripts/`, reusable output material in `assets/`, and behavioral verification in `evals/`.
- Start drafts thin. Add bundled resources only when they earn their maintenance cost.
- Preserve portability: avoid agent-specific instructions unless the skill explicitly needs them.
- Keep third-party sources under `vendor/` as git submodules. Do not copy vendor content into first-party skills without recording its source and license.
- Do not change or update vendored submodules without explicit approval.

Before committing a new or changed skill, ensure its `SKILL.md` is valid and that the described workflow matches the repository's development principles.
