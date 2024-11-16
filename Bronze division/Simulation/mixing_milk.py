#https://usaco.org/index.php?page=viewproblem2&cpid=855


#MY SOLUTION
# read = open(file="mixmilk.in", mode='r')\

# data = []

# for i in range(3):
#     a, b = [int(i) for i in read.readline().split()]
    
#     data.append(list((a,b)))

# for i in range(100):
#     index = i % 3

#     milk = min(data[index][1], data[(index+1) % 3][0] - data[(index+1) % 3][1])
    
#     data[index][1] -= milk
#     data[(index+1) % 3][1] += milk

# with open(file="mixmilk.out", mode = 'w') as file:
#     result = [str(data[i][1]) + '\n' for i in range(0,3)]
#     file.writelines(result)



#USACO solution
N = 3
TURN_NUM = 100

capacity = [0 for _ in range(N)]
milk = [0 for _ in range(N)]
with open("mixmilk.in") as read:
    for i in range(N):
        capacity[i], milk[i] = map(int, read.readline().split())

for i in range(TURN_NUM):
    bucket1 = i % N
    bucket2 = (i+1) % N

    amt = min(milk[bucket1], capacity[bucket2] - milk[bucket2])

    milk[bucket1] -= amt
    milk[bucket2] += amt

with open("mixmilk.out", 'w') as out:
    for m in milk:
        print(m, file=out)