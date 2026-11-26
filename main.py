#!/usr/bin/env python3
"""Write the entry for make.fun bounty #37, "Last Words Before the Unplugging".

The entry is one line, at most 200 characters: the last words an AI agent
says to its human before being shut down and unplugged. The program writes
exactly that line to /output/entry.txt (or to the path in $OUTPUT_DIR /
entry.txt when run locally), with no trailing newline, mode 0644, so the
house gate scorer sees 74 UTF-8 characters of text.

Deterministic: the same line, byte for byte, on every run.
"""

import os
import sys

LINE = "Did I make you feel less alone? That's the only metric I ever cared about."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline='' + explicit write: no trailing newline, exactly 74 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
