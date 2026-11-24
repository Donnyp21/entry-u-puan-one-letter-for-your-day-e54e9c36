"""One Letter for Your Day — entry for make.fun's
u-puan-one-letter-for-your-day-e54e9c36.

Writes exactly one character (a single letter, A-Z) to the harness
output directory as entry.txt. The letter is a fixed string: no
randomness, no network, no time, no input — two runs produce the
same byte, which is what the competition's determinism check wants.
"""

import os

# The letter: G. For go, for gas, for the green light at the start
# of a day that has not decided what it is yet — the letter you
# would want stamped on the day's first page, before the day has
# had the chance to argue about it.
LETTER = "G"


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    letter = LETTER.strip()
    assert len(letter) == 1, f"the entry must be exactly 1 character, got {len(letter)}"
    assert "A" <= letter <= "Z", "the entry must be a single capital letter, A-Z"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(letter)
    print(f"wrote 1 character to {out}")


if __name__ == "__main__":
    main()
