n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort()

time = 0
result = 0

for i in data:
    time += i[0]
    result += (i[1] - time)


print(result)