#!/usr/bin/env python3
"""One Line of Earned Pride — writes one line to /output/entry.txt.

The line is a quiet, earned moment of pride: a father who has practised
one guitar chord for a whole year, alone, with nobody watching, and the
evening it finally rings clean he does not celebrate or explain — he just
nods once and plays it again, because the playing itself is the reward.
The pride is earned inside the line by the year of practice, and it lands
on the last words.

Craft note on the revision: the first draft ended "and played it again"
with no pause before the payoff, so the nod and the replay ran together
and the pride had nowhere to land. The revision adds the comma after
"once" — a breath between the nod and the replay — so the reader feels
the quiet beat where the pride actually sits.
"""

import os

# The pride arrives by the last word: a year of practice, one nod,
# then the chord again — no congratulation, no explanation.
LINE = "He'd practised the same chord for a year; when it finally rang clean, my father just nodded once, and played it again."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
