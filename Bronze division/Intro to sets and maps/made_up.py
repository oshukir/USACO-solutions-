from collections import Counter

N = int(input())
A, B, C = [[int(x) for x in input().split()] for _ in range(3)]
ALLOWED_B = [B[x-1] for x in C]

occurence = {
    'A' : dict(Counter(A)),
    'B' : dict(Counter(ALLOWED_B))
}

res = 0
for key, value in occurence['A'].items():
    res += value * occurence['B'].get(key, 0)

print(res)