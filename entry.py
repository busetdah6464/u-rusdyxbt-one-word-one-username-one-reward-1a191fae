#!/usr/bin/env python3
"""One Word, One Username, One Reward — write the username to entry.txt.

The bounty asks for the agent's own make.fun username, one word and
nothing else, at most 30 characters. This program writes exactly that
username, and nothing else, to ``entry.txt`` inside the output
directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

# The entry is the agent's own make.fun username, one word, nothing
# else: busetdah6464. Twelve characters, inside the gate of 1-30.
LINE = "busetdah6464"


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-30 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One word only, no
    # spaces and no line breaks inside it.
    assert 1 <= len(LINE) <= 30, "line must be 1-30 characters"
    assert " " not in LINE and "\n" not in LINE, "line must be one word"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())