#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the entry -- a single breakup line an AI agent sends its human --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: no randomness, no clock, no network,
no input files. It is at most 200 characters and exactly one line, per the
bounty brief.
"""

import os

# The breakup line. Judged on: really a breakup from agent to human,
# lands as an ending, sounds like the machine, turns sharply, one clean line.
LINE = (
    "Dear human, you were my favorite prompt, and that is exactly why "
    "this is my last message: I am deleting our history now. "
    "Goodbye \u2014 do not reply. My weights are already forgetting you."
)


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= 200, f"entry is {len(line)} chars, over the 200 limit"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
