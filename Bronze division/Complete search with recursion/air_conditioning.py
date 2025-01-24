n, m = list(map(int, input().split()))
cows = [list(map(int,input().split())) for _ in range(n)]
airc = [list(map(int,input().split())) for _ in range(m)]
interval = [0] * 101
for l, r, c in cows:
    for j in range(l, r+1):
        interval[j] = c


def get_air_set(n: int):
    all_sets = []
    subset = []

    def traverse(k: int):
        if k == n:
            all_sets.append(subset.copy())
        else:
            traverse(k+1)
            subset.append(airc[k])
            traverse(k+1)
            subset.pop()

    traverse(0)
    return all_sets

def validate(data: list):
    check = interval.copy()
    cost = 0
    for l, r, c, m in data:
        for j in range(l, r+1):
            check[j] -= c
        cost += m

    for l, r, c in cows:
        for j in range(l, r+1):
            if check[j] > 0:
                return -1
    
    return cost

result = 1e6
subsets = get_air_set(m)

for i in subsets:
    poss_cost = validate(i)
    if poss_cost != -1:
        result = min(result, poss_cost)

print(result)




    
    
