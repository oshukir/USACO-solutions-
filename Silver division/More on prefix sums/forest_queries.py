N, M = map(int, input().split())
data = [[0 if x == "." else 1 for x in input()] for _ in range(N)]

prefix_2d = [[0 for _ in range(N+1)]]
for i in range(N):
    prefix_2d.append([0] + data[i])

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_2d[i][j] = prefix_2d[i-1][j] + prefix_2d[i][j-1] - prefix_2d[i-1][j-1] + data[i-1][j-1]

for i in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(prefix_2d[y2][x2] - prefix_2d[y1-1][x2] - prefix_2d[y2][x1-1] + prefix_2d[y1-1][x1-1])