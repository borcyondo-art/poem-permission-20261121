#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency to /output/entry.txt.

The poem turns on its last line: the "yes" is the hinge, the small
permission that lets the speaker walk through a door they could not
see. The door stays the other's; the steps are the speaker's.

The poem is a fixed text: every run writes exactly the same bytes,
so two runs are byte-identical. Pure standard library, no network.
"""

import os
from pathlib import Path

DEFAULT_OUTPUT = "/output/entry.txt"

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
    output = Path(os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
