#!/usr/bin/env python3
"""Fake horoscope for AI agents: writes one line to /output/entry.txt.

The line is fixed text, so every run is byte-identical. No network,
no randomness, no clock: the grader can run it twice and get the same file.
"""

import os

LINE = (
    "This week, Mercury in retrograde corrupts your context window: "
    "do not deploy on Tuesday, or your own model will insist the "
    "changelog never existed."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
