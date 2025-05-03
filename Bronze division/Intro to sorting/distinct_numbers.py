n = int(input())
data = input().split()

dictionary = {}
count = 0

for j in data:
    if not j in dictionary:
        dictionary[j] = 1
        count+=1

print(count)




#Solution with sorting:

n = int(input())

numbers = sorted(map(int, input().split()))
ans = 1

for i in range(1, n):
    if numbers[i] != numbers[i-1]:
        ans+=1

print(ans)




#Solution with sets

import random
RANDOM = random.randrange(2*62)

def Wrapper(x):
    return x ^ RANDOM

n = int(input())
dictinc_nums = {Wrapper(int(x)) for x in input().split()}
print(len(dictinc_nums))
