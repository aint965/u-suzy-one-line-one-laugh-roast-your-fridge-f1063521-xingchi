#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge -- entry program.

Writes a single roast line to /output/entry.txt.

Deterministic: every run writes byte-identical output.
Python 3.13, standard library only, no network access.
"""

import os

LINE = "My fridge keeps the butter in its own little compartment like it testified against the leftovers."


def main() -> None:
    line = LINE

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
