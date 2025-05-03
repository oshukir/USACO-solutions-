inpath = r"outofplace.in"
outpath = r"outofplace.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    cow_num = int(infile.readline())
    cows = [int(infile.readline()) for _ in range(cow_num)]

    sorted_order = sorted(cows)

    count = 0
    for i in range(len(cows)):
        if cows[i] != sorted_order[i]:
            count+=1
    
    print(max(0, count-1), file=outfile)