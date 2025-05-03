from typing import List
import sys

def reverse_segment(lst: List[int], start: int, end: int):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

sys.stdin = open(r"swap.in", 'r')
sys.stdout = open(r"swap.out", 'w')

n, k = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

cows = list(range(1, n+1))

visited = set()
visited.add(tuple(cows))
while True:
    reverse_segment(cows, a1-1, a2-1)
    reverse_segment(cows, b1-1, b2-1)
    if tuple(cows) in visited:
        break
    visited.add(tuple(cows))

cycle_len = len(visited)
swaps_left = k % cycle_len
for _ in range(swaps_left):
    reverse_segment(cows, a1-1, a2-1)
    reverse_segment(cows, b1-1, b2-1)

print(*cows, sep="\n")