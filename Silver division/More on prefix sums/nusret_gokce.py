n, m = map(int, input().split())
s = list(map(int, input().split()))
t = s[:]

# Left to right: can't go down too steeply
for i in range(1, n):
    t[i] = max(t[i], t[i - 1] - m)

# Right to left: can't go down too steeply
for i in range(n - 2, -1, -1):
    t[i] = max(t[i], t[i + 1] - m)

print(*t)
