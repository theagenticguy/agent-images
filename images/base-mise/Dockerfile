# syntax=docker/dockerfile:1.7
# images/base-mise — OS, mise, core CLI tools.

ARG UBUNTU_VERSION=26.04
FROM ubuntu:${UBUNTU_VERSION}

ARG USERNAME=agent
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

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

RUN groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m -s /bin/bash ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
WORKDIR /home/${USERNAME}

ENV MISE_DATA_DIR=/home/${USERNAME}/.local/share/mise
ENV MISE_CONFIG_DIR=/home/${USERNAME}/.config/mise
ENV MISE_CACHE_DIR=/home/${USERNAME}/.cache/mise
ENV PATH=/home/${USERNAME}/.local/bin:/home/${USERNAME}/.local/share/mise/shims:${PATH}

# hadolint ignore=DL4006
RUN curl -fsSL https://mise.run | sh

USER root
RUN mkdir -p /opt/af /workspace /evidence && \
    chown -R ${USERNAME}:${USERNAME} /opt/af /workspace /evidence

USER ${USERNAME}
WORKDIR /workspace

ENTRYPOINT ["mise", "exec", "--"]
CMD ["bash"]
