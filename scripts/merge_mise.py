"""Deep-merge ordered mise TOML files into one effective config.

Usage:
    merge_mise.py <input.toml>... <output.toml>

The first input is the base; each subsequent file is overlaid in order.
On key conflicts, the later file wins. Tables are merged recursively;
arrays and scalars are replaced (not concatenated).
"""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path
from typing import Any

import tomli_w


def deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    """Return a new dict where overlay's keys are merged into base recursively."""
    result = dict(base)
    for key, overlay_value in overlay.items():
        base_value = result.get(key)
        if isinstance(base_value, dict) and isinstance(overlay_value, dict):
            result[key] = deep_merge(base_value, overlay_value)
        else:
            result[key] = overlay_value
    return result


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("usage: merge_mise.py <input.toml>... <output.toml>", file=sys.stderr)
        return 2

    *input_files, output_file = argv[1:]
    merged: dict[str, Any] = {}

    for input_file in input_files:
        with Path(input_file).open("rb") as f:
            data = tomllib.load(f)
        merged = deep_merge(merged, data)

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(tomli_w.dumps(merged))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
