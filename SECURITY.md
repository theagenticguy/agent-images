# Security Policy

## Reporting a vulnerability

Use **[GitHub Security Advisories](https://github.com/lalsaado/erpaval/security/advisories/new)** to report security issues privately. Do **not** open a public issue.

We aim to acknowledge reports within 2 business days and ship a fix or mitigation within 30 days for high-severity issues.

When reporting, please include:

- A description of the issue and its impact.
- Steps to reproduce.
- Affected versions.
- Suggested mitigation, if any.

## Supported versions

The latest release on `main` is supported. Older versions are best-effort.

| Version | Supported |
|---|---|
| Latest `main` | Yes |
| Previous releases | Best-effort |

## Posture

This repo runs the following continuous controls:

- **Secret scanning** on every commit, push, and history (gitleaks pre-commit, pre-push, and CI).
- **Dependency vulnerability scanning** via OSV-Scanner on every PR and daily on `main`.
- **Static analysis** via Semgrep and GitHub CodeQL with `security-extended` queries.
- **Supply-chain posture scoring** via OpenSSF Scorecard.
- **Pinned tool versions** via mise; pinned action SHAs via Dependabot updates.
- **Branch protection** on `main` requiring code-owner review and green status checks.
- **Step Security harden-runner** on every workflow job.

## Cryptographic signing

Releases (when published) are signed with [Sigstore](https://www.sigstore.dev/). Verification instructions ship with each release.

## Out of scope

- Vulnerabilities in third-party dependencies that are already patched upstream — please file with the upstream project.
- Issues requiring physical access to a developer's machine.
- Social engineering of maintainers.
