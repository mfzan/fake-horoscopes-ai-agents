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
    # The scorer only judges a 1-200 character single line: refuse to
    # emit anything outside that gate instead of shipping a bad file.
    assert 1 <= len(LINE) <= 200, "horoscope must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "horoscope must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
