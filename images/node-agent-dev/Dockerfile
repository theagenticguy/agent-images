# syntax=docker/dockerfile:1.7
# images/node-agent-dev — JavaScript/TypeScript family.

ARG BASE_IMAGE=agent-images/software-agent-polyglot:local
FROM ${BASE_IMAGE}

LABEL org.opencontainers.image.source="https://github.com/theagenticguy/agent-images" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.title="agent-images/node-agent-dev" \
      org.opencontainers.image.description="Node/TypeScript family image."

USER root
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git \
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
COPY --chown=agent:agent mise/node-agent.toml ./mise/node-agent.toml

RUN python3 ./merge_mise.py \
    ./mise/base.toml \
    ./mise/polyglot.toml \
    ./mise/agent-harness.toml \
    ./mise/node-agent.toml \
    /opt/af/mise.toml

RUN mise trust /opt/af/mise.toml

RUN --mount=type=cache,target=/home/agent/.cache/mise,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/agent/.cache/pnpm/store,uid=1000,gid=1000 \
    mise --config /opt/af/mise.toml install --yes

RUN mise --config /opt/af/mise.toml run agent-smoke

WORKDIR /workspace
ENTRYPOINT ["mise", "--config", "/opt/af/mise.toml", "exec", "--"]
CMD ["bash"]
