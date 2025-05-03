import sys
sys.stdin = open(r"billboard.in", "r")
sys.stdout = open(r"billboard.out", "w")

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())


wx1 = max(ax1, bx1)
wx2 = min(ax2, bx2)
hy1 = max(ay1, by1)
hy2 = min(ay2, by2)
width = max(0, wx2 - wx1)
height = max(0, hy2 - hy1)

intersection = width * height

if width == (ax2 - ax1) and (hy1 == ay1 or hy2 == ay2):
    print((ax2 - ax1) * ((ay2 - ay1)) - intersection)
elif height == (ay2 - ay1) and (wx1 == ax1 or wx2 == ax2):
    print((ax2 - ax1) * ((ay2 - ay1)) - intersection)
else:
    print((ax2 - ax1) * ((ay2 - ay1)))