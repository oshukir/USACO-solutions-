n = input()
data = [int(x) for x in input().split()]

even = 0
odd = 0
for i in data:
    if i % 2:
        odd+=1
    else:
        even+=1


if even >= odd:
    print(min(odd+1, even) + odd)
else:
    odd -= even

    if odd % 3 == 0:
        print((odd//3)*2 + even*2)
    elif odd % 3 == 2:
        print((odd//3)*2+1 + even*2)
    elif odd % 3 == 1:
        print((odd//3)*2-1 + even*2)



#USACO solution: less eficient but more readable and logical
# n = int(input())
# even, odd = 0, 0

# cows = [int(i) for i in input().split()]
# for c in cows:
# 	if c % 2 == 0:
# 		even += 1
# 	else:
# 		odd += 1

# # Pair up odd cows so that there aren't too many of them.
# while odd > even:
# 	odd -= 2
# 	# Two odd cows together are effectively an even cow.
# 	even += 1

# # Group even cows so that there aren't too many evens either.
# if even > odd + 1:
# 	even = odd + 1

# print(even + odd)
    

