n, q = map(int, input().split())
a = list(map(int, input().split()))

freq = [0] * (n+2)

for _ in range(q):
    l, r = map(int, input().split())
    freq[l] += 1
    freq[r+1] -= 1

for i in range(1, n+1):
    freq[i] += freq[i-1]

freq = freq[1:n+1]
a.sort()
freq.sort()

res = sum(ai * fi for ai, fi in zip(a, freq))
print(res)