####My code

import sys


sys.stdin = open(r"race.in", "r")
sys.stdout = open(r"race.out", 'w')


k, n = list(map(int, input().split()))  # Read the first line
data = [int(input().strip()) for _ in range(n)]  # Read the next k lines


prefix_sum = [0]
for i in range(n):

    result = 0
    flag = False
    j = 1
    sum = 0

    diff = 0

    while sum < k:
        if len(prefix_sum) <= j:
            prefix_sum.append(j + prefix_sum[j-1])
        
        rising = k - prefix_sum[j]
        falling = 0

        if j > data[i]:
            falling = prefix_sum[j-1] - prefix_sum[data[i]-1]

        if rising - falling < 0 and abs(rising - falling) >= data[i]:
            flag = True
            break

        sum = prefix_sum[j]
        diff = rising - falling
        j+=1
    
    if flag:
        result = (j-1) + ((diff) // j) + (j - data[i])
    else:
        result = j-1
    
    print(result)





####USACO code
# import sys


# sys.stdin = open(r"C:\Users\ACER\Desktop\USACO\Bronze division\Greedy problems\race.in", "r")
# sys.stdout = open(r"C:\Users\ACER\Desktop\USACO\Bronze division\Greedy problems\race.out", 'w')

# def S(n: int):
#     return n * (n+1) // 2

# def sum_(A: int, B: int):
#     return S(B) - S(A-1) if A <= B else 0

# def ok(S: int, X: int, L: int):
#     if S <= X:
#         return True
#     need = sum_(X+1, S-1) + 1
#     return need <= L


# k, n = [int(v) for v in input().split()]
# X = [int(input().strip()) for _ in range(n)]


# def solve(k, x):
#     speed = 0
#     left = k
#     t = 0

#     while left > 0:
#         if ok(speed+1, x, left - (speed+1)):
#             speed += 1
#         elif ok(speed, x, left - speed):
#             pass
#         else:
#             assert ok(speed-1, x, left-(speed-1))
#             speed -= 1
        
#         assert speed >= 1
#         left -= speed
#         t += 1
#     return t

# for x in X:
#     print(solve(k,x))




####Due to pythons slow speed, both of solutions approach (they are approx the same) face time limit test cases