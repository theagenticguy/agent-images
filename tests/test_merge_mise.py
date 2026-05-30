"""Tests for scripts/merge_mise.py."""

from __future__ import annotations

import subprocess
import sys
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "merge_mise.py"


def _write(tmp_path: Path, name: str, content: str) -> Path:
    path = tmp_path / name
    path.write_text(content, encoding="utf-8")
    return path


def _run(*args: Path) -> None:
    subprocess.run(
        [sys.executable, str(SCRIPT), *(str(a) for a in args)],
        check=True,
    )


def test_later_file_overrides_scalar(tmp_path: Path) -> None:
    a = _write(tmp_path, "a.toml", '[tools]\npython = "3.12"\n')
    b = _write(tmp_path, "b.toml", '[tools]\npython = "3.13"\n')
    out = tmp_path / "out.toml"

    _run(a, b, out)

    merged = tomllib.loads(out.read_text())
    assert merged["tools"]["python"] == "3.13"


def test_tables_merge_recursively(tmp_path: Path) -> None:
    a = _write(tmp_path, "a.toml", '[env]\nA = "1"\n')
    b = _write(tmp_path, "b.toml", '[env]\nB = "2"\n')
    out = tmp_path / "out.toml"

    _run(a, b, out)

    merged = tomllib.loads(out.read_text())
    assert merged["env"] == {"A": "1", "B": "2"}


def test_arrays_replace_not_concatenate(tmp_path: Path) -> None:
    a = _write(tmp_path, "a.toml", '[tools]\nclassifiers = ["a", "b"]\n')
    b = _write(tmp_path, "b.toml", '[tools]\nclassifiers = ["c"]\n')
    out = tmp_path / "out.toml"

    _run(a, b, out)

    merged = tomllib.loads(out.read_text())
    assert merged["tools"]["classifiers"] == ["c"]


def test_creates_output_directory(tmp_path: Path) -> None:
    a = _write(tmp_path, "a.toml", '[x]\ny = "z"\n')
    out = tmp_path / "nested" / "deep" / "out.toml"

    _run(a, out)

    assert out.exists()
    assert tomllib.loads(out.read_text())["x"]["y"] == "z"


def test_usage_error_when_too_few_args(tmp_path: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "only-one-arg.toml"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert "usage:" in result.stderr.lower()
