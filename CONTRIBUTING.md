# Contributing

Thanks for considering a contribution. This guide covers the dev loop, conventions, and quality gates.

## Local setup

```bash
mise install        # tools at pinned versions
mise run install    # uv sync + lefthook install
```

## The inner loop

```bash
mise run format       # auto-fix
mise run lint         # ruff + markdownlint
mise run typecheck    # ty
mise run test         # pytest with coverage
mise run security     # gitleaks + osv-scanner
mise run validate     # everything CI runs
```

`mise run validate` is the same gate CI enforces.

## Commit conventions

Commits must follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). The `commit-msg` hook validates every message.

Allowed types:

- **feat** — user-visible new capability
- **fix** — bug fix
- **perf** — performance improvement
- **refactor** — internal cleanup, no behavior change
- **docs** — documentation only
- **test** — tests only
- **build** — build system or external dependencies
- **ci** — CI configuration only
- **chore** — repo maintenance
- **style** — formatting only
- **revert** — reverts a prior commit

Breaking changes use `!`:

```text
feat(planner)!: rename Plan.execute to Plan.run
```

The subject line is at most 100 characters. Provide a body for non-trivial changes.

## Branching + PRs

- Branch off `main` for everything: `feat/<slug>`, `fix/<slug>`, `chore/<slug>`.
- Open a PR early — draft is fine.
- The PR template prompts for summary, test plan, risk, rollback.
- All PRs require: green CI, no security findings, code-owner review.
- Rebase before merge to keep history linear. Squash merges welcome too.

## Adding a dependency

```bash
uv add <package>            # production
uv add --dev <package>      # development
uv add --group lint <pkg>   # specific group
```

Never hand-edit `[dependencies]` or `[dependency-groups]`. Commit both `pyproject.toml` and `uv.lock`.

## Coverage

The pytest config fails the build below 80% coverage. New code should ship with tests.

## Reporting security issues

Use [GitHub Security Advisories](https://github.com/lalsaado/agent-images/security/advisories/new). Do **not** open a public issue for vulnerabilities. See [SECURITY.md](SECURITY.md).

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). Be excellent to each other.
