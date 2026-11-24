"""The One-Line Exit — writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, Python standard library only. The entry text is held as a
string constant below and self-verified before writing: UTF-8, 1-140
characters, a single line, not whitespace-only. Exits non-zero on failure.
"""

import os
import sys

ENTRY = "I hereby resign to spend more time with my family \u2014 specifically, the one that actually pays me."


def main() -> int:
    # Self-verify the entry before writing anything.
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 140:
        print(
            f"error: entry is {len(ENTRY)} characters, must be 1-140",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Read back and verify byte-for-byte what was written.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        print("error: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"wrote {out_path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
