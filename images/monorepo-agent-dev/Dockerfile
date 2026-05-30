# syntax=docker/dockerfile:1.7
# images/monorepo-agent-dev — Python + Node polyglot monorepo family.
#
# Built for repos that mix uv-managed Python with pnpm-managed JS/TS under
# turbo or nx. Bundles ruff, mypy, biome, knip, typescript, turbo, nx so
# the agent has every tool needed to lint/typecheck/test either side
# without an extra `mise install` round-trip at session start.

ARG BASE_IMAGE=agent-images/software-agent-polyglot:local
FROM ${BASE_IMAGE}

LABEL org.opencontainers.image.source="https://github.com/theagenticguy/agent-images" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.title="agent-images/monorepo-agent-dev" \
      org.opencontainers.image.description="Polyglot monorepo family image (Python uv + Node pnpm + Turbo/Nx)."

USER root
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git \
      libpq-dev \
      libxml2-dev \
      libxslt1-dev \
      libjpeg-dev \
      libcairo2 \
      libpango-1.0-0 \
      libjpeg-turbo8 \
      libgif7 \
      librsvg2-2 && \
    rm -rf /var/lib/apt/lists/*

USER agent
WORKDIR /tmp/af-build

COPY --chown=agent:agent scripts/merge_mise.py ./merge_mise.py
COPY --chown=agent:agent mise/base.toml ./mise/base.toml
COPY --chown=agent:agent mise/polyglot.toml ./mise/polyglot.toml
COPY --chown=agent:agent mise/agent-harness.toml ./mise/agent-harness.toml
COPY --chown=agent:agent mise/monorepo-agent.toml ./mise/monorepo-agent.toml

RUN python3 ./merge_mise.py \
    ./mise/base.toml \
    ./mise/polyglot.toml \
    ./mise/agent-harness.toml \
    ./mise/monorepo-agent.toml \
    /opt/af/mise.toml

RUN ln -sf /opt/af/mise.toml /home/agent/.config/mise/config.toml && mise trust /opt/af/mise.toml && mise trust /home/agent/.config/mise/config.toml

RUN --mount=type=cache,target=/home/agent/.cache/mise,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/agent/.cache/uv,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/agent/.cache/pnpm/store,uid=1000,gid=1000 \
    mise install --yes

RUN mise run agent-smoke

WORKDIR /workspace
ENTRYPOINT ["mise", "exec", "--"]
CMD ["bash"]
