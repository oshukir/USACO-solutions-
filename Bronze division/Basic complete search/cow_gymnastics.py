inpath = r"gymnastics.in"
outpath = r"gymnastics.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    k, n = list(map(int, infile.readline().split()))

    n_cow = [[] for elem in range(n)]

    for i in range(k):
        line = infile.readline().split()

        for index, j in enumerate(line):
            n_cow[int(j)-1].append(n-index)

    result = 0
        
    for i in range(n):
        for j in range(i+1, n):
            
            total = 0
            for c in range(k):
                if n_cow[i][c] > n_cow[j][c]:
                    total += 1
            
            if total == 0 or total == k:
                result += 1

    print(result, file=outfile)


    