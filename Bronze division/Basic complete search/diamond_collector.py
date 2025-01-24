inpath = "diamond.in"
outpath = "diamond.out"

from math import log2, floor, ceil

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n, k = map(int, infile.readline().split())
    data = []
    for i in infile.readlines():
        line = i
        line.replace("/n", "")
        data.append(int(line))

    most = 0
    for x in data:
        fittable = 0
        for y in data:
            if x <= y <= x + k:
                fittable += 1
        
        most = max(most, fittable)

    print(most, file=outfile)

        
    

    