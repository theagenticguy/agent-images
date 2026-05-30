---
title: Getting Started
description: Clone, build the image tree locally, and run the smoke harness.
sidebar:
  order: 1
---

> Placeholder. Step-by-step quick start lands when the image tree commits in.

## Prerequisites

- Docker 28+ with BuildKit and the `buildx` plugin
- mise 2026.5+
- AWS CLI v2 (only required to push to ECR)

## Clone

```bash
git clone https://github.com/theagenticguy/agent-images.git
cd agent-images
mise install
mise run install
```

## Build the tree

```bash
docker buildx create --name af-builder --use
docker buildx bake
```

## Smoke test

```bash
mise run image-smoke
```
