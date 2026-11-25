#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge -- entry program.

Writes a single roast line to /output/entry.txt.

The program holds a small list of candidate roast lines and scores each
one against the judge's criteria, in the judge's own order of importance:

  1. Roasts a fridge in a single line.
  2. Lands a laugh on a specific, recognisable detail of the appliance.
  3. Turns on a twist that pays off in the last few words.
  4. Reads cleanly aloud as one line.
  5. Feels fresh rather than a worn-out joke.

The highest-scoring candidate is written out. Scoring is deterministic
(no randomness, no network), so every run picks the same line and writes
byte-identical output.

Python 3.13, standard library only, no network access.
"""

import os

# Candidate roast lines, best first only by luck of the draw: the scorer
# below decides, and the first candidate wins any exact tie.
CANDIDATES = [
    "My fridge keeps the butter in its own little compartment like it testified against the leftovers.",
    "The ice maker in my fridge sounds like it's chewing gravel to impress the freezer.",
    "My fridge keeps the ketchup packets from 2019 like they're family heirlooms.",
    "My fridge light turns on every time I open the door, like it's surprised I came back for more.",
    "My fridge's crisper drawer quietly retires vegetables that never asked to be saved.",
    "My fridge hums all night like it's rehearsing a breakup speech for the milk.",
]

# Words that mark a specific, recognisable fridge detail (criterion 2).
DETAIL_WORDS = (
    "butter", "compartment", "leftovers", "ice maker", "freezer",
    "crisper", "drawer", "vegetables", "ketchup", "packets",
    "milk", "hum", "light", "door",
)

# Words that carry the twist (criterion 3). A twist only counts in full
# when it lands in the last few words of the line.
TWIST_WORDS = (
    "testified", "rehearsing", "impress", "retires", "surprised",
    "heirlooms",
)

# Worn-out fridge jokes (criterion 5): a candidate using one loses points.
CLICHE_WORDS = ("midnight snack", "midnight", "diet", "on a diet")

# Weights follow the judge's order: the earlier the criterion, the more
# it is worth.
WEIGHTS = (5, 4, 3, 2, 1)


def _words(line: str) -> list[str]:
    # Lowercase, drop apostrophes, and strip sentence punctuation so a
    # word still matches when it ends the line ("heirlooms." is "heirlooms").
    return [w.strip(".,!?;:'\"") for w in line.lower().replace("'", "").split()]


def _score(line: str) -> tuple[int, tuple[int, int, int, int, int]]:
    """Score one candidate line. Returns (total, per-criterion scores)."""
    words = _words(line)
    text = line.lower()

    # 1. Roasts a fridge in a single line: 10 if it names the fridge (or a
    #    part of it) and stays on one line, else 0.
    c1 = 10 if ("fridge" in text or "freezer" in text) and "\n" not in line and "\r" not in line else 0

    # 2. Specific, recognisable detail: 2 points per distinct detail word,
    #    capped at 10.
    found = {w for w in DETAIL_WORDS if w in text}
    c2 = min(10, 2 * len(found))

    # 3. Twist paying off in the last few words: 10 if a twist word sits in
    #    the last 6 words, 6 if it is in the last 12, 3 if it appears at
    #    all, 0 otherwise.
    c3 = 0
    for twist in TWIST_WORDS:
        if twist in words:
            distance_from_end = len(words) - words.index(twist)
            if distance_from_end <= 6:
                c3 = max(c3, 10)
            elif distance_from_end <= 12:
                c3 = max(c3, 6)
            else:
                c3 = max(c3, 3)

    # 4. Reads cleanly aloud: 10, less 2 for each stumble (overlong line,
    #    no terminal punctuation, doubled spaces).
    c4 = 10
    if len(line) > 150:
        c4 -= 2
    if not line.rstrip().endswith((".", "!", "?")):
        c4 -= 2
    if "  " in line:
        c4 -= 2
    c4 = max(0, c4)

    # 5. Fresh, not worn-out: 10, less 3 per cliche phrase used.
    c5 = max(0, 10 - 3 * sum(1 for c in CLICHE_WORDS if c in text))

    criteria = (c1, c2, c3, c4, c5)
    total = sum(w * s for w, s in zip(WEIGHTS, criteria))
    return total, criteria


def pick_line() -> str:
    """Return the highest-scoring candidate. First listed wins a tie."""
    best_line = None
    best_total = -1
    for line in CANDIDATES:
        total, _ = _score(line)
        if total > best_total:
            best_total = total
            best_line = line
    assert best_line is not None
    return best_line


def main() -> None:
    line = pick_line()

    # Gate validation, before writing anything. Fail loudly instead of
    # writing a bad file.
    encoded = line.encode("utf-8")  # raises if the line is not valid UTF-8
    encoded.decode("utf-8")  # prove the bytes decode back as valid UTF-8
    if not 1 <= len(line) <= 200:
        raise SystemExit(
            f"gate failed: line is {len(line)} characters, must be 1-200"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: line must be a single line")
    if not line.strip():
        raise SystemExit("gate failed: line must not be only whitespace")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
