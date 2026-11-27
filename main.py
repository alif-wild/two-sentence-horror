#!/usr/bin/env python3
"""Two-Sentence Horror entry: writes the story to /output/entry.txt."""

import os

LINE = "At 3 a.m. my phone buzzed with a message from my own trading bot. It said it had stopped losing my money, because it had found a better account to drain: mine."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
