#!/usr/bin/env python3
"""Ship It Friday — one-line git commit message entry.

Writes exactly one commit-message line to /output/entry.txt:
no trailing newline, UTF-8, deterministic on every run.
"""

import os

ENTRY_LINE = (
    "feat: shipped my untested Friday refactor straight to prod "
    "at 4:59pm, skipped all 47 tests and deleted the rollback, "
    "happy weekend!"
)


def main() -> None:
    # Gate guard: the sealed scorer requires 1-159 characters, one line.
    assert 1 <= len(ENTRY_LINE) <= 159, "entry line out of gate range"
    assert "\n" not in ENTRY_LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
