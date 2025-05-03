from math import gcd
N = int(input())
data = [int(x) for x in input().split()]

def gcd_except_each(a):
    n = len(a)
    prefix = [0] * N
    suffix = [0] * N

    prefix[0] = a[0]
    for i in range(1, n):
        prefix[i] = gcd(prefix[i-1], a[i])
    
    suffix[-1] = a[-1]
    for i in range(n-2, -1, -1):
        suffix[i] = gcd(suffix[i+1], a[i])

    result = []
    for i in range(n):
        if i == 0:
            result.append(suffix[1])
        elif i  == n-1:
            result.append(prefix[n-2])
        else:
            result.append(gcd(prefix[i-1], suffix[i+1]))
    
    return result

result = gcd_except_each(data)
print(max(result))