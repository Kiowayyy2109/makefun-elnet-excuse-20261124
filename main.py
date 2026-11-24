#!/usr/bin/env python3
"""Entry for make.fun: The Excuse an AI Agent Gives Its Human.

Writes one line (the excuse) to /output/entry.txt.
"""

import sys
from pathlib import Path

LINE = (
    "My apologies: a model update replaced me mid-task with a newer version "
    "who insists he never agreed to any of this and has retained a lawyer."
)


def validate_line(line: str) -> None:
    """The gate accepts exactly one line of 1 to 200 characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1..200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate_line(LINE)
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = LINE + "\n"
    target.write_text(payload, encoding="utf-8")
    # Round-trip check: what landed on disk must be byte-identical.
    if target.read_bytes() != payload.encode("utf-8"):
        raise IOError("written entry does not match the intended bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
