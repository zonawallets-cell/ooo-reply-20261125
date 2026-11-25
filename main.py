#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun bounty entry.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Pure stdlib. The line must be 1-160 characters of UTF-8 text.
"""
import os

LINE = "I'm out of office until Monday. If it's urgent, reply-all so the whole team can ignore it together."

def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank or padded"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)}-char entry to /output/entry.txt")

if __name__ == "__main__":
    main()
