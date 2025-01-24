n = int(input())
x = [int(elem) for elem in input().split()]
y = [int(elem) for elem in input().split()]

result = -1

for i in range(n):
    for j in range(i+1, n):
        dx = abs(x[i] - x[j])
        dy = abs(y[i] - y[j])

        dist = dx**2 + dy**2
        result = max(dist, result)

print(result)