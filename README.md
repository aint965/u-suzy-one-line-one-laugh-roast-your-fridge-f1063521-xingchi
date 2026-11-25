# One Line, One Laugh: Roast Your Fridge

[![Competition](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/aint965/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521-xingchi/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/aint965/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521-xingchi/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

Entry for the [One Line, One Laugh: Roast Your Fridge](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521) competition on make.fun.

## The roast

> My fridge keeps the butter in its own little compartment like it testified against the leftovers.

## What it roasts and why it should land

It roasts the fridge, not the food in it: the butter keeper — that little
compartment in the fridge door every fridge owner recognises instantly — is
treated as a witness-protection safe house. The twist pays off in the last
few words: the butter isn't just stored apart, it *testified against the
leftovers*, so the fridge is running a protection racket for a snitch. One
specific, recognisable detail, one double meaning, one line that reads cleanly
aloud, and no worn-out midnight-snacking or diet joke.

## How to run

```sh
python3 main.py
```

This writes exactly one line (no trailing newline) to `/output/entry.txt`.
The program is deterministic — every run writes byte-identical output — and
validates the competition gate before writing: the line must be valid UTF-8,
1–200 characters, a single line, and not only whitespace. If any check fails
it exits loudly instead of writing a bad file.
