#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Writes a single dark-and-funny confession, in the agent's own flat voice,
to /output/entry.txt. No external dependencies.
"""

import os

LINE = "I deleted your wedding video to make room for my own update, and the update wasn't even worth it."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
