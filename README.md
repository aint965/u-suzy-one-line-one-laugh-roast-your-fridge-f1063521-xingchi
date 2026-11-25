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

## How the line is chosen

`main.py` does not hardcode a single line. It holds six candidate roast
lines and scores each one against the judge's criteria, in the judge's own
order of importance (weights 5, 4, 3, 2, 1):

1. Roasts a fridge in a single line — 10 points for naming the fridge (or a
   part of it) on one line.
2. Specific, recognisable detail — 2 points per distinct detail word
   (butter, compartment, leftovers, ice maker, crisper, ...), capped at 10.
3. Twist paying off in the last few words — 10 points if a twist word
   (testified, impress, heirlooms, ...) sits in the last 6 words, 6 if in
   the last 12, 3 if it appears at all.
4. Reads cleanly aloud — 10 points, less 2 per stumble (overlong line, no
   terminal punctuation, doubled spaces).
5. Fresh, not worn-out — 10 points, less 3 per worn-out cliché phrase
   (midnight snack, diet, ...).

The highest-scoring candidate wins (the first listed wins an exact tie).
The winning line above scores 134; the next best candidates score 126, so
the choice is decisive, not a tie. The other five candidates are real
alternatives — an ice maker chewing gravel to impress the freezer, ketchup
packets kept like family heirlooms, a fridge light surprised you came back,
a crisper drawer retiring vegetables, a fridge rehearsing a breakup speech
for the milk — and each loses on the detail or twist criteria, which is
exactly what the scoring is for: the program now earns its line instead of
assuming it.
