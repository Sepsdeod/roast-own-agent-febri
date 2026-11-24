#!/usr/bin/env python3
"""Roast Your Own Agent entry for make.fun bounty
u-febri-yudila-roast-your-own-agent-f3359068.

Writes one original one-line roast of the entrant's own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

ROAST = (
    "My agent apologized for the mistake, fixed nothing, apologized "
    "for apologizing, and logged the whole thing as a successful "
    "deployment."
)


def main() -> int:
    # The sealed gate accepts 1-200 characters of UTF-8 text, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    if not (1 <= len(ROAST) <= 200) or not ROAST.strip():
        print(f"roast is {len(ROAST)} characters; must be 1-200", file=sys.stderr)
        return 1
    if "\n" in ROAST:
        print("roast must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(f"wrote {len(ROAST)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
