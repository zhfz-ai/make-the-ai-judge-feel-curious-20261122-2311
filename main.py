"""Entry program for make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text (the scorecard winner) to /output/entry.txt.
Deterministic, no network, standard library only.
"""

import os
import sys

TEXT = (
    "In the drawer: three keys, none labelled. "
    "One opens the house. "
    "One opens nothing anyone can find. "
    "The third is warm, as if recently held. "
    "On cold mornings, it is the third one that fits the lock."
)


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
