from typing import NamedTuple

ZODIAC = [
    "OX",
    "TIGER",
    "RABBIT",
    "DRAGON",
    "SNAKE",
    "HORSE",
    "GOAT",
    "MONKEY",
    "ROOSTER",
    "DOG",
    "PIG",
    "RAT",
]


class Relation(NamedTuple):
    name: str
    prev: bool  # is this a "previous" or "next" relation?
    year: int
    relative: str


relations = []
for _ in range(int(input())):
    relation = input().upper().split()
    relations.append(
        Relation(
            relation[0],
            relation[3] == "PREVIOUS",
            ZODIAC.index(relation[4]),
            relation[7],
        )
    )

birth_years = {"BESSIE": 0}
for r in relations:
    change = -1 if r.prev else 1
    # +change because it has to be at least 1 year off
    this_year = birth_years[r.relative] + change

    check = this_year % len(ZODIAC)  # FIXED: Correct indentation
    while check != r.year:
        this_year += change
        check = this_year % len(ZODIAC)  # FIXED: Correct indentation

    birth_years[r.name] = this_year

dist = abs(birth_years["BESSIE"] - birth_years["ELSIE"])
print(dist)
