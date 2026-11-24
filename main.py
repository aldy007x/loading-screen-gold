#!/usr/bin/env python3
"""Loading Screen Gold — make.fun bounty entry.

Writes a single original loading-screen tip line to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (defaults to "output").

The tip speaks to stressed developers and the AI coding agents working
alongside them, mid-build.
"""

import os
import sys

TIP = (
    "Loading\u2026 while your AI agent confidently rewrites the code you wrote "
    "an hour ago \u2014 faster, cleaner, and wrong in a brand-new way. "
    "Read the diff before you merge it."
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Runtime self-check: exactly one non-blank line, 1-200 characters.
    lines = TIP.splitlines()
    if len(lines) != 1 or not TIP.strip():
        print("error: entry must be exactly one non-blank line", file=sys.stderr)
        return 1
    if not 1 <= len(TIP) <= MAX_CHARS:
        print(
            f"error: entry is {len(TIP)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(TIP + "\n")

    # Verify the round-trip: what we wrote must read back identical.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TIP + "\n":
        print("error: written entry does not match the tip", file=sys.stderr)
        return 1
    if written.count("\n") != 1 or len(written.rstrip("\n")) != len(TIP):
        print("error: written entry is not exactly one line", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(TIP)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
