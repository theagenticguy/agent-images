# agent-images

> Container image platform for coding agents. Base, polyglot, and per-family dev images, built with mise-pinned toolchains and BuildKit registry cache.

[![CI](https://github.com/theagenticguy/agent-images/actions/workflows/ci.yml/badge.svg)](https://github.com/theagenticguy/agent-images/actions/workflows/ci.yml)
[![Security](https://github.com/theagenticguy/agent-images/actions/workflows/security.yml/badge.svg)](https://github.com/theagenticguy/agent-images/actions/workflows/security.yml)
[![Documentation](https://github.com/theagenticguy/agent-images/actions/workflows/docs.yml/badge.svg)](https://github.com/theagenticguy/agent-images/actions/workflows/docs.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/theagenticguy/agent-images/badge)](https://securityscorecards.dev/viewer/?uri=github.com/theagenticguy/agent-images)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

**Docs:** <https://theagenticguy.github.io/agent-images/>

## Quick start

```bash
git clone https://github.com/theagenticguy/agent-images.git
cd agent-images
mise install        # installs python, uv, node, pnpm, lefthook, gitleaks, etc.
mise run install    # uv sync + pnpm install + lefthook install
mise run validate   # full local quality gate (incl. docs build)
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
| Docs | [Astro Starlight](https://starlight.astro.build) | Static site, AI-friendly, deployed to GitHub Pages |

## Layout

```text
agent-images/
├── src/agent_images/   # Build helpers, manifest renderers, smoke harness
├── tests/              # Pytest suite
├── docs/               # Astro Starlight site (deploys to GitHub Pages)
│   ├── astro.config.mjs
│   ├── package.json
│   └── src/content/docs/
├── scripts/            # Repo automation (commit-msg validator, etc.)
├── .github/            # Workflows, templates, CODEOWNERS, dependabot
├── mise.toml           # Tool versions + tasks
├── pyproject.toml      # Package + tool config
├── lefthook.yml        # Git hooks
├── .gitleaks.toml      # Secret scan rules
└── .editorconfig       # Editor normalization
```

The image tree itself (`images/base-mise/`, `images/software-agent-polyglot/`, etc.) and the `docker-bake.hcl` pipeline land in follow-up commits — see the [architecture page](https://theagenticguy.github.io/agent-images/reference/architecture/) for the planned layout.

## Daily commands

```bash
mise run install        # install deps + git hooks
mise run format         # auto-fix formatting
mise run lint           # ruff + markdownlint
mise run typecheck      # ty
mise run test           # pytest with coverage
mise run security       # gitleaks + osv-scanner
mise run docs-dev       # local docs server
mise run docs-build     # build the docs site
mise run validate       # everything CI runs (incl. docs build)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All commits must follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — the commit-msg hook enforces it.

## Security

See [SECURITY.md](SECURITY.md) for the disclosure policy. Use GitHub Security Advisories to report vulnerabilities privately.

## License

[Apache 2.0](LICENSE).
