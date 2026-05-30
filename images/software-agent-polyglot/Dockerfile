# syntax=docker/dockerfile:1.7
# images/software-agent-polyglot — polyglot runtimes + agent harness.
# Inherits base-mise. Adds Python/Node/JVM/Go/Rust + claude-code, opencode-ai,
# and the Context7 MCP server. Renders /opt/af/mise.toml from the merged
# source TOMLs so every downstream image has one canonical config.

ARG BASE_IMAGE=agent-images/base-mise:local
FROM ${BASE_IMAGE}

USER root
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git-lfs \
      make \
      cmake \
      ninja-build \
      libssl-dev \
      zlib1g-dev \
      libffi-dev \
      libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

USER agent
WORKDIR /tmp/af-build

COPY --chown=agent:agent scripts/merge_mise.py ./merge_mise.py
COPY --chown=agent:agent mise/base.toml ./mise/base.toml
COPY --chown=agent:agent mise/polyglot.toml ./mise/polyglot.toml
COPY --chown=agent:agent mise/agent-harness.toml ./mise/agent-harness.toml

# Place a default Context7 MCP config so claude-code / opencode-ai pick it up
# at session start. The CONTEXT7_API_KEY env var is injected at session start
# from the SessionPlan and is NOT baked here.
COPY --chown=agent:agent images/software-agent-polyglot/mcp /opt/af/agent-runtime/mcp

# Stub agent-runtime; real package lands in a follow-up commit.
RUN mkdir -p /opt/af/agent-runtime && \
    printf '[project]\nname = "af-agent-runtime"\nversion = "0.0.0"\nrequires-python = ">=3.13"\ndependencies = []\n' \
      > /opt/af/agent-runtime/pyproject.toml

RUN python3 -m pip install --user --no-cache-dir 'tomli-w==1.2.0' && \
    python3 ./merge_mise.py \
      ./mise/base.toml \
      ./mise/polyglot.toml \
      ./mise/agent-harness.toml \
      /opt/af/mise.toml

RUN mise trust /opt/af/mise.toml

RUN --mount=type=cache,target=/home/agent/.cache/mise,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/agent/.cache/uv,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/agent/.cache/pnpm/store,uid=1000,gid=1000 \
    mise --config /opt/af/mise.toml install --yes

# Smoke checks: tools resolve and MCP server responds to initialize.
RUN mise --config /opt/af/mise.toml run base-smoke && \
    mise --config /opt/af/mise.toml run polyglot-smoke && \
    mise --config /opt/af/mise.toml run agent-smoke

WORKDIR /workspace
ENTRYPOINT ["mise", "--config", "/opt/af/mise.toml", "exec", "--"]
CMD ["bash"]
