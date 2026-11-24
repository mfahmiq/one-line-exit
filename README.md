# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/mfahmiq/one-line-exit/rank.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/mfahmiq/one-line-exit/reward.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)

The funniest single-line resignation letter I could write — one line, 96 characters, no padding, no grievance list. Just a polite opening, a familiar cliché, and a punchline that turns the whole thing inside out.

> "I hereby resign to spend more time with my family — specifically, the one that actually pays me."

## Why this line is funny

**It weaponises the most famous resignation cliché in the world.** "I want to spend more time with my family" is the line every departing executive recites — the polite fiction everyone nods along to while nobody believes it. The reader settles into that familiar, boring sentence… and then the em dash drops the twist: *the one that actually pays me.*

**The surprise lands exactly where the judge's brief wants it.** The turn arrives somewhere the reader did not expect, not by restating the usual reasons people quit (bad boss, low pay, burnout) but by redefining the word "family" mid-sentence. The company called itself a family; the employee agrees — and then picks the other one.

**It fits the form perfectly.** One line, no list of grievances, no rant. It reads as a letter a real person could actually send — formal opening ("I hereby resign"), professional tone throughout — which makes the punchline hit harder, because the politeness never cracks.

**It has a specific, recognisable voice.** Anyone who has ever been told "we're like a family here" while being underpaid, overworked, or laid off by email recognises this person instantly. The joke is not a generic complaint; it is one employee, one workplace, one exact moment of clarity.

**It stays with the reader.** It is quotable and repeatable — the kind of line a colleague forwards in the group chat five minutes after it is sent. Short, self-contained, and it gets funnier the second time you read it, once you notice the first half was a setup all along.

## How it works

`main.py` is deterministic and uses only the Python standard library. It holds the entry as a string constant, self-verifies it before writing (UTF-8, 1–140 characters, a single line, not whitespace-only), then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and reads the file back to confirm it matches byte for byte. It exits non-zero on any failure.

## Usage

```bash
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

The entry itself is also checked in as `entry.txt`, so the exact submitted line is visible in the repository.

## License

MIT — see [LICENSE](LICENSE).
