# syntax=docker/dockerfile:1.7
# images/base-mise — OS, mise, core CLI tools.

ARG UBUNTU_VERSION=26.04
FROM ubuntu:${UBUNTU_VERSION}

LABEL org.opencontainers.image.source="https://github.com/theagenticguy/agent-images" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.title="agent-images/base-mise" \
      org.opencontainers.image.description="Ubuntu LTS + mise + core CLI tools."

ARG USERNAME=agent
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Use bash with pipefail for any RUN that pipes — hadolint DL4006.
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# hadolint ignore=DL3008,DL3009
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      bash \
      ca-certificates \
      curl \
      git \
      gnupg \
      jq \
      less \
      locales \
      openssh-client \
      procps \
      sudo \
      tar \
      unzip \
      xz-utils \
      zip \
      build-essential \
      pkg-config \
      python3 \
      python3-pip \
      python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Ubuntu 24.04+ ships with a default `ubuntu:1000` user. Reuse uid/gid 1000
# by deleting that user first, then create our `agent` user at the same ids
# so cache mounts and Dockerfile uid/gid args stay consistent.
RUN if id -u 1000 >/dev/null 2>&1; then userdel -r "$(id -un 1000)" 2>/dev/null || true; fi && \
    if getent group 1000 >/dev/null 2>&1; then groupdel "$(getent group 1000 | cut -d: -f1)" 2>/dev/null || true; fi && \
    groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m -s /bin/bash ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
WORKDIR /home/${USERNAME}

ENV MISE_DATA_DIR=/home/${USERNAME}/.local/share/mise
ENV MISE_CONFIG_DIR=/home/${USERNAME}/.config/mise
ENV MISE_CACHE_DIR=/home/${USERNAME}/.cache/mise
ENV PATH=/home/${USERNAME}/.local/bin:/home/${USERNAME}/.local/share/mise/shims:${PATH}

# Pin mise to a known-good version. Bump deliberately when mise's CLI shifts.
ARG MISE_VERSION=v2026.5.16
RUN curl -fsSL "https://mise.run" | MISE_VERSION="${MISE_VERSION}" sh

USER root
RUN mkdir -p /opt/af /workspace /evidence && \
    chown -R ${USERNAME}:${USERNAME} /opt/af /workspace /evidence

USER ${USERNAME}
WORKDIR /workspace

ENTRYPOINT ["mise", "exec", "--"]
CMD ["bash"]
