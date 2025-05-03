N = int(input())

data = [list(map(int, input().split()))[::-1] for _ in range(N)]

data.sort()
result = 0
temp = -1

for i in data:
    if i[1] < temp:
        continue

    temp = i[0]
    result += 1

print(result)