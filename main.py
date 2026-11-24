#!/usr/bin/env python3
"""Office Joke Open: write one original one-line office joke to entry.txt.

Deterministic, Python 3 standard library only, no network access.
The joke is written as exactly one line of 1-200 characters, with no
trailing newline, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
After writing, the file is read back and verified byte-for-byte.
"""

import os
import sys

JOKE = (
    "My boss said to treat the office like home, so now I leave dishes "
    "in the sink and ignore emails from my landlord \u2014 I mean, my boss."
)


def main() -> int:
    line = JOKE

    # Validate: exactly one line, 1-200 characters, not only whitespace.
    if not line or line != line.strip():
        print(
            "error: joke is empty or has surrounding whitespace "
            "(length %d characters)" % len(line),
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 200:
        print(
            "error: joke is %d characters, must be 1-200" % len(line),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)

    # Verify byte-exact: read back and compare with what was written.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("error: entry.txt does not match the joke byte-for-byte", file=sys.stderr)
        return 1

    print("Wrote %d bytes (%d characters) to %s" % (len(data), len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
