inpath = "shuffle.in"
outpath = "shuffle.out"

from math import log2, floor, ceil

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    x = int(infile.readline().strip())

    shuffle = [(int(i)-1) for i in infile.readline().split()]
    ids = [int(i) for i in infile.readline().split()]

    for i in range(3):
        temp_list = [0] * x
        
        for j in range(0, x):
            temp_list[j] = ids[shuffle[j]]

        ids = temp_list.copy()

    for i in range(x):
        print(str(ids[i])+'\n' if i < x-1 else ids[i], file=outfile, end="")