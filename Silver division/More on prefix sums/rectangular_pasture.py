N = int(input())
cows = [tuple(map(int, input().split())) for _ in range(N)]

# Coordinate compression
sorted_x = sorted(set(x for x, y in cows))
sorted_y = sorted(set(y for x, y in cows))

x_map = {x: i for i, x in enumerate(sorted_x)}
y_map = {y: i for i, y in enumerate(sorted_y)}

cows = [(x_map[x], y_map[y]) for x, y in cows]
cows.sort()  # sort by x

# Prefix sums
lt_y = [[0] * (N + 1) for _ in range(N)]
gt_y = [[0] * (N + 1) for _ in range(N)]

for y in range(N):
    for x in range(1, N + 1):
        lt_y[y][x] = lt_y[y][x - 1] + (cows[x - 1][1] < y)
        gt_y[y][x] = gt_y[y][x - 1] + (cows[x - 1][1] > y)

# Count subsets
total = 0
for i in range(N):
    for j in range(i + 1, N):
        y1 = cows[i][1]
        y2 = cows[j][1]
        bottom, top = min(y1, y2), max(y1, y2)

        bottom_total = 1 + lt_y[bottom][j + 1] - lt_y[bottom][i]
        top_total = 1 + gt_y[top][j + 1] - gt_y[top][i]

        total += bottom_total * top_total

# Add single cow and empty subset
total += N + 1

print(total)
