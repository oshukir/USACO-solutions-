from itertools import combinations

inpath = r"C:\Users\ACER\Desktop\USACO\Bronze division\Basic complete search\cownomics.in"
outpath = r"C:\Users\ACER\Desktop\USACO\Bronze division\Basic complete search\cownomics.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    N,M = map(int, infile.readline().split())
    genomes = [line.strip() for line in infile.readlines()]
    spotty_genomes = genomes[:N]
    plain_genomes = genomes[N:]

    spotty_tupples = [{(genome[i], genome[j], genome[k]) for genome in spotty_genomes} for i,j,k in combinations(range(M), 3)]
    plain_tupples = [{(genome[i], genome[j], genome[k]) for genome in plain_genomes} for i,j,k in combinations(range(M), 3)]

    result = sum(1 for s_set, p_set in zip(spotty_tupples, plain_genomes) if s_set.isdisjoint(p_set))

    print(result, file=outfile)





#my code (less eficient):
inpath = r"cownomics.in"
outpath = r"cownomics.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    k, n = list(map(int, infile.readline().split()))

    genoms = [elem for elem in infile.readlines()]
    result = 0

    for i in range(n):
        for j in range(i+1,n):
            for z in range(j+1, n):

                spotty = set()
                plainy = set()

                # Collect the tuples of characters at positions i, j, z
                for cow in range(k):
                    spotty.add((genoms[cow][i], genoms[cow][j], genoms[cow][z]))
                    plainy.add((genoms[cow + k][i], genoms[cow + k][j], genoms[cow + k][z]))

                # Check if the sets are disjoint
                if not spotty.intersection(plainy):
                    result += 1
    
    print(result, file=outfile)

                




