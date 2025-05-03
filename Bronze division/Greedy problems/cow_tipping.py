import sys
from typing import List

sys.stdin = open(r"cowtip.in", 'r')
sys.stdout = open(r"cowtip.out", 'w')

Tipped = "0"
n = int(input())
data = [[(Tipped != x) for x in input()] for _ in range(n)]

def flip(r: int, c: int, cows: List[List[int]]) -> bool:
    if cows[r][c]:
        for ri in range(r+1):
            for ci in range(c+1):
                cows[ri][ci] = not cows[ri][ci]

        return True
    return False


min_flips = 0
x = n - 1
y = n - 1
while x >= 0 and y >= 0:
    min_flips += flip(x, y, data)

    if x != y:
        min_flips += flip(y, x, data)

    if x > 0:
        x -= 1
    else:
        y -= 1
        x = y

print(min_flips)