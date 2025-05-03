

N = int(input())
data = [int(x.strip()) for x in input().split()]

mods = [[0] for _ in range(N)]
mods[0][0] = 1

prefix_mod = 0

for index, c in enumerate(data):
    prefix_mod = (prefix_mod + c) % N

    mods[prefix_mod][0] += 1

result = sum((element[0] * (element[0] - 1) // 2) for element in mods if element[0] > 1)
print(result)



    