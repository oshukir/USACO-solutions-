import sys
N, K = map(int, input().split())

data = [int(x) for x  in input().split()]
data.sort()

result = 0
for i in data:
    if K < i:
        break
    K -= i
    result+=1

print(result)
