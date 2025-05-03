import sys

# Open correct input and output files
sys.stdin = open("art.in", "r")
sys.stdout = open("art.out", "w")

n = int(input())
data = [[int(i) for i in input()] for _ in range(n)]


colors = []
color_stats = {}
for i in range(n):
    for j in range(n):
        if data[i][j] == 0:
            continue

        if not data[i][j] in color_stats:
            color_stats[data[i][j]] = [1e9, -1, 1e9, -1]
            colors.append(data[i][j])

        color_stats[data[i][j]][0] = min(color_stats[data[i][j]][0], j)
        color_stats[data[i][j]][1] = max(color_stats[data[i][j]][1], j)
        color_stats[data[i][j]][2] = min(color_stats[data[i][j]][2], i)
        color_stats[data[i][j]][3] = max(color_stats[data[i][j]][3], i)

for k in colors.copy():
    for i in range(color_stats[k][2], color_stats[k][3]+1):
        for j in range(color_stats[k][0], color_stats[k][1]+1):
            if data[i][j] in colors and data[i][j] != k:
                colors.remove(data[i][j])

print(len(colors))