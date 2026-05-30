# syntax=docker/dockerfile:1.7
# images/jvm-agent-dev — JVM family (Gradle + Maven).

ARG BASE_IMAGE=agent-images/software-agent-polyglot:local
FROM ${BASE_IMAGE}

LABEL org.opencontainers.image.source="https://github.com/theagenticguy/agent-images" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.title="agent-images/jvm-agent-dev" \
      org.opencontainers.image.description="JVM family image (Gradle + Maven)."

USER root
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      maven && \
    rm -rf /var/lib/apt/lists/*

USER agent
WORKDIR /tmp/af-build

COPY --chown=agent:agent scripts/merge_mise.py ./merge_mise.py
COPY --chown=agent:agent mise/base.toml ./mise/base.toml
COPY --chown=agent:agent mise/polyglot.toml ./mise/polyglot.toml
COPY --chown=agent:agent mise/agent-harness.toml ./mise/agent-harness.toml
COPY --chown=agent:agent mise/jvm-agent.toml ./mise/jvm-agent.toml

RUN python3 ./merge_mise.py \
    ./mise/base.toml \
    ./mise/polyglot.toml \
    ./mise/agent-harness.toml \
    ./mise/jvm-agent.toml \
    /opt/af/mise.toml

RUN ln -sf /opt/af/mise.toml /home/agent/.config/mise/config.toml && mise trust /opt/af/mise.toml && mise trust /home/agent/.config/mise/config.toml

RUN --mount=type=cache,target=/home/agent/.cache/mise,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/agent/.gradle,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/agent/.m2,uid=1000,gid=1000 \
    mise install --yes

RUN mise run agent-smoke

WORKDIR /workspace
ENTRYPOINT ["mise", "exec", "--"]
CMD ["bash"]
