inpath = r"backforth.in"
outpath = r"backforth.out"

def get_permutation(barn):
    all_perms = set()
    perm = []

    def recursion(barn, order):
        
        if len(perm) == 4:
            all_perms.add(sum(perm))
            return
        
        for i in range(len(barn[order%2])):
            perm.append((-1) ** ((order+1)%2) * barn[order%2][i])
            barn[(order+1)%2].append(barn[order%2][i])
            barn[order%2].pop(i)

            recursion(barn, order+1)

            perm.pop()
            barn[order%2].insert(i, barn[(order+1)%2][-1])
            barn[(order+1)%2].pop()
        

    recursion(barn, 0)
    return len(all_perms)

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    barn = [[int(bucket) for bucket in infile.readline().split()] for _ in range(2)]

    n = get_permutation(barn)

    print(n, file=outfile)