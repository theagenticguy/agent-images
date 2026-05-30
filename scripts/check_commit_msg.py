"""Conventional Commits 1.0.0 validator. Reads the commit-msg file path from argv[1]."""

from __future__ import annotations

import re
import sys
from pathlib import Path

PATTERN = re.compile(
    r"^(?P<type>build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)"
    r"(?P<scope>\([\w\-./]+\))?"
    r"(?P<breaking>!)?"
    r": "
    r"(?P<subject>.{1,100})$",
)

MAX_SUBJECT = 100


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_commit_msg.py <path-to-commit-msg>", file=sys.stderr)
        return 2

    msg_path = Path(sys.argv[1])
    raw = msg_path.read_text(encoding="utf-8")

    lines = [line for line in raw.splitlines() if not line.startswith("#")]
    if not lines:
        print("commit message is empty", file=sys.stderr)
        return 1

    subject = lines[0].rstrip()

    # Allow merge / revert / fixup commits to pass.
    if subject.startswith(("Merge ", "Revert ", "fixup!", "squash!")):
        return 0

    if len(subject) > MAX_SUBJECT:
        print(
            f"subject line too long ({len(subject)} > {MAX_SUBJECT}): {subject!r}",
            file=sys.stderr,
        )
        return 1

    if not PATTERN.match(subject):
        print(
            "commit subject does not match Conventional Commits 1.0.0:\n"
            f"  got:      {subject!r}\n"
            "  expected: <type>(<scope>)?!?: <subject>\n"
            "  types:    build, chore, ci, docs, feat, fix, perf, refactor, "
            "revert, style, test",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
