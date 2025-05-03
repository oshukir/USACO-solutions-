t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    bmax = -1
    result = -1
    sum = 0

    for j in range(min(n, k)):
        bmax = max(b[j], bmax)
        sum += a[j]

        current = sum + (k-j-1) * bmax
        result = max(result, current)

    print(result)
