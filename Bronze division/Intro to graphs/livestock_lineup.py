import sys

sys.stdin = open(r"lineup.in", "r")
sys.stdout = open(r"lineup.out", "w")

COWS = sorted(
    [
        "Bessie",
        "Buttercup",
        "Belinda",
        "Beatrice",
        "Bella",
        "Blue",
        "Betsy",
        "Sue"
    ]
)

cow_inds = {c: i for i, c in enumerate(COWS)}
neighbours = [[] for _ in range(len(COWS))]

n = int(input())
for _ in range(n):
    words = input().strip().split()

    cow1 = cow_inds[words[0]]
    cow2 = cow_inds[words[-1]]

    neighbours[cow1].append(cow2)
    neighbours[cow2].append(cow1)

order = []
added = [False for _ in range(len(COWS))]

for c in range(len(COWS)):
    if not added[c] and len(neighbours[c]) <= 1:
        added[c] =True
        order.append(c)

        if len(neighbours[c]) == 1:
            prev = c
            at = neighbours[c][0]

            while len(neighbours[at]) == 2:
                added[at] = True
                order.append(at)
                a, b = neighbours[at]
                at, prev = b if a == prev else a, at

            added[at] = True
            order.append(at)

for c in order:
    print(COWS[c])

