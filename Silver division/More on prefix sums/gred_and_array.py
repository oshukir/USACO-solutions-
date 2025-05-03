N, M, K = map(int, input().split())
array = [int(x) for x in input().split()]
command = [0] + [list(map(int, input().split())) for _ in range(M)]

s = [0] * (M+2)
add = [0] * (N+2)

for _ in range(K):
    x, y = map(int, input().split())
    s[x] += 1
    s[y+1] -= 1

for i in range(1, M+1):
    s[i] += s[i-1]

    add[command[i][0]] += s[i] * command[i][2]
    add[command[i][1] + 1] -= s[i] * command[i][2]

for i in range(1, N+1):
    add[i] += add[i-1]
    print(add[i] + array[i-1], end=" ")

