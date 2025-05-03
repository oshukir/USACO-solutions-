import sys

sys.stdin = open(r"planting.in", "r")
sys.stdout = open(r"planting.out", 'w')


n = int(input())
adjacent = [[] for _ in range(n)]
for i in range(n-1):
    a, b = list(map(int, input().split()))
    a-=1
    b-=1
    adjacent[a].append(b)
    adjacent[b].append(a)

result = 0
for i in range(n):
    result = max(result, len(adjacent[i]))

print(result+1)