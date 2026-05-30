---
title: Architecture
description: Planned image tree, build pipeline, and helper layout for agent-images.
sidebar:
  order: 2
---

> Placeholder for the agent-images platform architecture. The image tree and build pipeline land in follow-up commits.

## Image tree (planned)

```text
agent-images/base-mise
  └─ agent-images/software-agent-polyglot
       ├─ agent-images/node-agent-dev
       ├─ agent-images/python-agent-dev
       ├─ agent-images/jvm-agent-dev
       ├─ agent-images/infra-agent-dev
       └─ agent-images/security-agent-dev
```

`base-mise` lands the OS, mise, and core CLI tools. `software-agent-polyglot` adds polyglot runtimes and the agent harness (claude-code, opencode-ai, Context7 MCP). Each `*-agent-dev` family layer adds the lint/typecheck/test toolchain for its ecosystem and the standard `mise run af-validate-fast` / `af-validate-ci` task contract.

## Build pipeline (planned)

- `docker-bake.hcl` orchestrates the tree.
- BuildKit registry cache (`type=registry,mode=max`) for cache reuse across CI and dev.
- ARM64 default for AgentCore-bound images, multi-arch matrix later.
- Per-image smoke harness — tool smoke (`mise run *-smoke`) + runtime smoke (real JSON-RPC over Context7 stdio MCP, plus an end-to-end agent loop against a fixture).
- Image manifest YAML registered in the catalog with `mise_config_digest`, image digest, and capabilities.

## Repo helpers

`src/agent_images/` will house the small Python helpers that glue the pipeline together: mise TOML merger, image-manifest renderer, smoke-harness runner.
