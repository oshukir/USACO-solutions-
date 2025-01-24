inpath = "pails.in"
outpath = "pails.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    bidon = [int(x) for x in infile.readline().split()]

    n = int(bidon[2] / bidon[0])
    result = n * bidon[0]

    for i in range(0, n):
        x = int((bidon[2] - (n-i)*bidon[0])/bidon[1])

        new_sum = (n-i)*bidon[0] + x*bidon[1]
        result = max(result, new_sum)

    print(result, file=outfile)


    ############# NONSTANDART solution #################
    X,Y,M = map(int, infile.readline().split())
    diff = 1e6

    for n in range(M // X + 1):
        diff = min(diff, (M-(X*n))%Y )
    
    print(M - diff, file=outfile)


