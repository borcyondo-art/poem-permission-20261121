#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency to /output/entry.txt.

The poem is a fixed text: every run writes exactly the same bytes,
so two runs are byte-identical. Pure standard library, no network.
"""

import os
from pathlib import Path

POEM = (
    "I asked, and you said yes \u2014\n"
    "a door I could not see\n"
    "swung open.\n"
    "\n"
    "I walk through it as you.\n"
    "The steps are mine,\n"
    "the door is yours.\n"
    "Keep the key.\n"
    "The yes is the hinge.\n"
)


def main() -> None:
    output = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
