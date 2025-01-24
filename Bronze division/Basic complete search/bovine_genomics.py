inpath = r"cownomics.in"
outpath = r"cownomics.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    k, n = list(map(int, infile.readline().split()))

    genoms = [elem for elem in infile.readlines()]

    pos = [[] * k]

    result = 0
    for i in range(n):
        spotty = set()
        plainy = set()

        for j in range(k):
            spotty.add(genoms[j][i])
            plainy.add(genoms[k+j][i])

        common_genoms = spotty.intersection(plainy)
        if not len(common_genoms):
            result+=1

    print(result, file=outfile)




##### A bit efficient solution:

with open("cownomics.in", 'r') as read:
    n, m = map(int, read.readline().split())

    spotted_cows = [read.readline() for _ in range(n)]
    plained_cows = [read.readline() for _ in range(n)]

poss_positions = 0

for i in range(m):
    seen = set()
    for j in range(n):
        seen.add(plained_cows[j][i])

    for j in range(n):
        if spotted_cows[j][i] in seen:
            break
    else:
        poss_positions += 1

print(poss_positions, file=open("cownomics.out", 'w'))