#!/usr/bin/env python3
"""Valida o formato Conventional Commits usado no projeto."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERN = re.compile(
    r"^(feat|fix|docs|test|refactor|ci|build|chore|perf|style)"
    r"(?:\([a-z0-9][a-z0-9._/-]*\))?: [a-z0-9]"
)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_commit_message.py <commit-message-file>", file=sys.stderr)
        return 2
    message = Path(sys.argv[1]).read_text(encoding="utf-8").splitlines()[0].strip()
    if message.startswith(("Merge ", "Revert ")):
        return 0
    if not PATTERN.match(message):
        print(
            "commit inválido; use '<type>(<scope>): <imperative description>'",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
