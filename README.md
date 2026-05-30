# erpaval

> **E**xplore · **R**esearch · **P**lan · **A**ct · **Val**idate — an adaptive methodology for autonomous software development with coding agents.

[![CI](https://github.com/lalsaado/erpaval/actions/workflows/ci.yml/badge.svg)](https://github.com/lalsaado/erpaval/actions/workflows/ci.yml)
[![Security](https://github.com/lalsaado/erpaval/actions/workflows/security.yml/badge.svg)](https://github.com/lalsaado/erpaval/actions/workflows/security.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/lalsaado/erpaval/badge)](https://securityscorecards.dev/viewer/?uri=github.com/lalsaado/erpaval)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Quick start

```bash
git clone https://github.com/lalsaado/erpaval.git
cd erpaval
mise install        # installs python, uv, lefthook, gitleaks, etc.
mise run install    # uv sync + lefthook install
mise run validate   # full local quality gate
```

## What's in the box

| Surface | Tool | Why |
|---|---|---|
| Toolchain pin | [mise](https://mise.jdx.dev) | One source of truth for tool versions |
| Package manager | [uv](https://docs.astral.sh/uv/) | Fast, deterministic Python packaging |
| Lint + format | [ruff](https://docs.astral.sh/ruff/) | Single tool replaces flake8 + black + isort |
| Typecheck | [ty](https://github.com/astral-sh/ty) | Astral's typechecker, py3.13-aware |
| Tests | pytest + hypothesis + coverage | 80% coverage gate, strict warnings |
| Git hooks | [lefthook](https://github.com/evilmartians/lefthook) | Parallel pre-commit, commit-msg, pre-push |
| Commit format | Conventional Commits 1.0.0 | Enforced via commit-msg hook |
| Secret scanning | [gitleaks](https://github.com/gitleaks/gitleaks) | Pre-commit + CI + history scan |
| Dep audit | [osv-scanner](https://google.github.io/osv-scanner/) | OSV.dev vuln database |
| SAST | semgrep + CodeQL | Layered static analysis |
| Supply chain | [OpenSSF Scorecard](https://scorecards.dev) | Continuous posture scoring |
| Auto-updates | Dependabot | Weekly grouped PRs for uv + actions |

## Layout

```text
erpaval/
├── src/erpaval/        # Package source
├── tests/              # Pytest suite
├── docs/               # Long-form documentation
├── scripts/            # Repo automation (commit-msg validator, etc.)
├── .github/            # Workflows, templates, CODEOWNERS, dependabot
├── mise.toml           # Tool versions + tasks
├── pyproject.toml      # Package + tool config
├── lefthook.yml        # Git hooks
├── .gitleaks.toml      # Secret scan rules
└── .editorconfig       # Editor normalization
```

## Daily commands

```bash
mise run install      # install deps + git hooks
mise run format       # auto-fix formatting
mise run lint         # ruff + markdownlint
mise run typecheck    # ty
mise run test         # pytest with coverage
mise run security     # gitleaks + osv-scanner
mise run validate     # everything CI runs
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All commits must follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — the commit-msg hook enforces it.

## Security

See [SECURITY.md](SECURITY.md) for the disclosure policy. Use GitHub Security Advisories to report vulnerabilities privately.

## License

[Apache 2.0](LICENSE).
