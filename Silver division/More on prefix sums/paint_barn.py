import sys

sys.stdin = open(r"paintbarn.in", 'r')
sys.stdout = open(r"paintbarn.out", 'w')

WIDTH = 1000
barn = [[0 for _ in range(WIDTH+1)] for _ in range(WIDTH+1)]

N, K = map(int, input().split())
for _ in range(N):
    sx, sy, ex, ey = map(int, input().split())
    barn[sx][sy] += 1
    barn[ex][ey] += 1
    barn[sx][ey] -= 1
    barn[ex][sy] -= 1

valid_area = 0
for x in range(WIDTH+1):
    for y in range(WIDTH+1):

        if x > 0:
            barn[x][y] += barn[x-1][y]
        if y > 0:
            barn[x][y] += barn[x][y-1]
        if x > 0 and y > 0:
            barn[x][y] -= barn[x-1][y-1]

        valid_area += barn[x][y] == K

print(valid_area)