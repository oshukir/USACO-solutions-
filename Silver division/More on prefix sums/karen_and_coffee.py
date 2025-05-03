N, K, Q = map(int, input().split())
MAX = 200000

diff = [0] * (MAX + 2)
for i in range(N):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r+1] -= 1

for i in range(1, MAX+1):
    diff[i] += diff[i-1]

for i in range(1, MAX+1):
    diff[i] = (diff[i] >= K) + diff[i-1]

for i in range(Q):
    l, r = map(int, input().split())
    print(diff[r] - diff[l-1])
