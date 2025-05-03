import sys
sys.stdin = open(r"paint.in", "r")
sys.stdout = open(r"paint.out", 'w')

a, b = map(int, input().split())
c, d = map(int, input().split())

length1 = abs(b-a)
length2 = abs(d-c)
maxim = max(max(a,b), max(c,d)) - min(min(a,b),min(c,d))

if maxim <= length1 + length2:
    print(maxim)
else:
    print(length1+length2)



# ###USACO

# total =  (b-a) + (d-c)
# intersection = max(min(b,d) - max(a,c), 0)

# union = total - intersection
# print(union)