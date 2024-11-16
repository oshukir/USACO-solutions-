#https://usaco.org/index.php?page=viewproblem2&cpid=891


#MY SOLUTION
# file = open(r"C:\Users\ACER\Desktop\USACO\Bronze division\Simulation\shell.in", 'r')

# n = int(file.readline())
# data = [list(map(int, file.readline().split())) for _ in range(n)]
# file.close()

# def simulate(start_position):
#     game = [0,0,0,0]
#     game[start_position] = 1
#     guesses = 0

#     for a, b, g in data:
#         game[a], game[b] = game[b], game[a]

#         if game[g] == 1:
#             guesses += 1

#     return guesses

# max_score = 0
# for start in range(1, 4):
#     max_score = max(max_score, simulate(start))

# with open(r"C:\Users\ACER\Desktop\USACO\Bronze division\Simulation\shell.out", 'w') as file:
#     file.write(str(max_score))



#USACO solution

read = open("shell.in")
n = int(read.readline)

shell_at_poss = [i for i in range(3)]

counter = [0 for _ in range(3)]

for _ in range(n):
    a, b, g = [int(i) - 1 for i in read.readline().split()]

    shell_at_poss[a], shell_at_poss[b] = shell_at_poss[b], shell_at_poss[a]

    counter[shell_at_poss[g]] += 1

print(max(counter), file=open("shell.out", "w"))