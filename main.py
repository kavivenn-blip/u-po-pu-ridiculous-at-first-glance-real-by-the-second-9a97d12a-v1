#!/usr/bin/env python3
"""Write one sentence pitching a bizarre startup idea to /output/entry.txt.

The pitch (167 characters, one sentence): a second sunset, sold to a
rooftop bar. Mirrors on a hilltop bounce the dusk back after it sets, and
the bar pays per night because a second sunset sells a second round of
drinks. Deterministic, offline, standard library only.
"""

import os

ENTRY = (
    "We sell a second sunset: mirrors on a hilltop bounce the dusk back "
    "to a rooftop bar, and the bar pays per night because a second sunset "
    "sells a second round of drinks."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    # The gate counts characters (code points): 1 to 200, not only white
    # space. Refuse to write an entry that would fail it.
    if not 1 <= len(ENTRY) <= MAX_CHARS or not ENTRY.strip():
        raise ValueError("entry does not satisfy the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    os.chmod(os.path.dirname(OUTPUT_PATH), 0o755)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
