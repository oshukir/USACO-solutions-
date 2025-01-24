
inpath = r"lineup.in"
outpath = r"lineup.out"

def get_permutation(cows:list):

    all_perms = []
    current = []
    chosen = [False] * 8

    def permutation():
        if len(current) == 8:
            all_perms.append(current.copy())
            return
        else:
            for i in range(len(cows)):
                if chosen[i]:
                    continue
                chosen[i] = True
                current.append(cows[i])
                permutation()
                chosen[i] = False
                current.pop()

    permutation()
    return all_perms 

def check(cows:list, retrieved:list):
    for first, second in retrieved:
        if abs(cows.index(first) - cows.index(second)) != 1:
            return False
    return True

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n = int(infile.readline())
    data = [infile.readline().split() for _ in range(n)]
    cows = ["Bessie","Buttercup","Belinda","Beatrice","Bella","Blue","Betsy","Sue"]
    retrieved = [[data[i][0], data[i][-1]]for i in range(n)]

    all_perms = get_permutation(cows)
    filtered = []

    for i in all_perms:
        if check(i, retrieved):
            filtered.append(i)
    
    filtered.sort()
    print("\n".join(filtered[0]), file=outfile)



