n, k = map(int, input().split())
data = [int(x) for x in input().split()]

data.sort()

l = 0
r = len(data) - 1

result = 0

while l <= r:
    if data[l] + data[r] > k:
        r -= 1
    else:
        l += 1
        r -= 1
        
    result += 1

print(result)
    
