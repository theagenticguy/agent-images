// agent-images — buildx bake orchestration.
//
// Local build:
//   docker buildx create --name af-builder --use || docker buildx use af-builder
//   docker buildx bake
//
// Build + push to ECR with registry cache:
//   export REGISTRY=123456789012.dkr.ecr.us-west-2.amazonaws.com/agent-images
//   export VERSION=2026-05
//   export CACHE_REF=$REGISTRY/buildcache:agent-images-main
//   docker buildx bake \
//     --set "*.cache-from=type=registry,ref=$CACHE_REF" \
//     --set "*.cache-to=type=registry,ref=$CACHE_REF,mode=max" \
//     --push

variable "REGISTRY" {
  default = "agent-images"
}

variable "VERSION" {
  default = "dev"
}

variable "UBUNTU_VERSION" {
  default = "26.04"
}

variable "PLATFORMS" {
  default = "linux/amd64"
}

variable "VCS_REF" {
  default = ""
}

variable "BUILD_DATE" {
  default = ""
}

group "default" {
  targets = [
    "base-mise",
    "software-agent-polyglot",
    "node-agent-dev",
    "python-agent-dev",
    "monorepo-agent-dev",
    "jvm-agent-dev",
    "infra-agent-dev",
    "security-agent-dev",
  ]
}

# Shared OCI labels applied to every image.
target "_common" {
  labels = {
    "org.opencontainers.image.source"      = "https://github.com/theagenticguy/agent-images"
    "org.opencontainers.image.licenses"    = "Apache-2.0"
    "org.opencontainers.image.description" = "Container image platform for coding agents."
    "org.opencontainers.image.revision"    = "${VCS_REF}"
    "org.opencontainers.image.created"     = "${BUILD_DATE}"
    "org.opencontainers.image.vendor"      = "agent-images"
  }
  platforms = ["${PLATFORMS}"]
}

target "base-mise" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/base-mise/Dockerfile"
  args = {
    UBUNTU_VERSION = "${UBUNTU_VERSION}"
  }
  tags = [
    "${REGISTRY}/base-mise:${VERSION}",
    "agent-images/base-mise:local",
  ]
}

target "software-agent-polyglot" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/software-agent-polyglot/Dockerfile"
  args = {
    BASE_IMAGE = "agent-images/base-mise:local"
  }
  contexts = {
    "agent-images/base-mise:local" = "target:base-mise"
  }
  tags = [
    "${REGISTRY}/software-agent-polyglot:${VERSION}",
    "agent-images/software-agent-polyglot:local",
  ]
}

target "node-agent-dev" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/node-agent-dev/Dockerfile"
  args = {
    BASE_IMAGE = "agent-images/software-agent-polyglot:local"
  }
  contexts = {
    "agent-images/software-agent-polyglot:local" = "target:software-agent-polyglot"
  }
  tags = ["${REGISTRY}/node-agent-dev:${VERSION}"]
}

target "python-agent-dev" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/python-agent-dev/Dockerfile"
  args = {
    BASE_IMAGE = "agent-images/software-agent-polyglot:local"
  }
  contexts = {
    "agent-images/software-agent-polyglot:local" = "target:software-agent-polyglot"
  }
  tags = ["${REGISTRY}/python-agent-dev:${VERSION}"]
}

target "monorepo-agent-dev" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/monorepo-agent-dev/Dockerfile"
  args = {
    BASE_IMAGE = "agent-images/software-agent-polyglot:local"
  }
  contexts = {
    "agent-images/software-agent-polyglot:local" = "target:software-agent-polyglot"
  }
  tags = ["${REGISTRY}/monorepo-agent-dev:${VERSION}"]
}

target "jvm-agent-dev" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/jvm-agent-dev/Dockerfile"
  args = {
    BASE_IMAGE = "agent-images/software-agent-polyglot:local"
  }
  contexts = {
    "agent-images/software-agent-polyglot:local" = "target:software-agent-polyglot"
  }
  tags = ["${REGISTRY}/jvm-agent-dev:${VERSION}"]
}

target "infra-agent-dev" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/infra-agent-dev/Dockerfile"
  args = {
    BASE_IMAGE = "agent-images/software-agent-polyglot:local"
  }
  contexts = {
    "agent-images/software-agent-polyglot:local" = "target:software-agent-polyglot"
  }
  tags = ["${REGISTRY}/infra-agent-dev:${VERSION}"]
}

target "security-agent-dev" {
  inherits   = ["_common"]
  context    = "."
  dockerfile = "images/security-agent-dev/Dockerfile"
  args = {
    BASE_IMAGE = "agent-images/software-agent-polyglot:local"
  }
  contexts = {
    "agent-images/software-agent-polyglot:local" = "target:software-agent-polyglot"
  }
  tags = ["${REGISTRY}/security-agent-dev:${VERSION}"]
}
