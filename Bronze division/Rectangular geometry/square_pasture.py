import sys
sys.stdin = open(r"square.in", "r")
sys.stdout = open(r"square.out", "w")

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

width = abs(min(ax1, bx1) - max(ax2, bx2))
height = abs(min(ay1, by1) - max(ay2, by2))

result = max(width, height) ** 2
print(result)