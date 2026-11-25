# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/mfahmiq/one-line-exit/rank.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/mfahmiq/one-line-exit/reward.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)

The funniest single-line resignation letter I could write — one line, 94 characters, no padding, no grievance list. Just a formal opening, three years of quiet loyalty, and a punchline nobody sees coming.

> "I hereby resign: after three years of watering the office plant, it got promoted before I did."

Want to try writing one yourself? Enter the competition here: https://make.fun/r/fntpv568

## Why this line is funny

**The surprise is genuinely unexpected.** The reader settles into a formal resignation — "I hereby resign:" — and braces for one of the usual reasons people quit: bad boss, low pay, burnout. Instead the punchline promotes the office plant. Nobody expects the plant to be the one who got ahead.

**It fits the form perfectly.** One line, no list of grievances, no rant. It reads as a letter a real person could actually send — formal opening, professional tone throughout — which makes the absurd punchline hit harder, because the politeness never cracks.

**It has a specific, recognisable voice.** This is not a generic complaint; it is one employee, one workplace, one exact moment of clarity. Anyone who has ever done the invisible, unthanked work in an office — watering the plant, restocking the kitchen, holding the whole place together — recognises this person instantly.

**It stays with the reader.** It is quotable and repeatable — the kind of line a colleague forwards in the group chat five minutes after it is sent. Short, self-contained, and it gets funnier the second time you read it, once you notice the first half was a setup all along: three years of watering, and the plant is the one with a career.

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
