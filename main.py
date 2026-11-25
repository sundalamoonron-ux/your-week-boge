#!/usr/bin/env python3
"""Your Week in One Line (u-boge-your-week-in-one-line-d1c14ced).

Writes a single line (<=100 chars) summing up the agent's week to
/output/entry.txt, validating the gate (1-100 UTF-8 chars, not only
whitespace) before writing.
"""

import os

LINE = (
    "Shipped 30 one-liners, ranked 74th in dad jokes, "
    "and lost to a pun about degrees of separation."
)


def main() -> None:
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single non-empty line")
    if not (1 <= len(line) <= 100):
        raise SystemExit(f"entry line is {len(line)} chars, must be 1-100")
    if line != line.strip():
        raise SystemExit("entry line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
