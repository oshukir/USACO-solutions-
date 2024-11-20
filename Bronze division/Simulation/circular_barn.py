inpath = "cbarn.in"
outpath = "cbarn.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n = int(infile.readline().strip())

    r = [int("".join(line)) for line in infile.readlines()]
    
    result = float('inf')
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += (j * r[(i+j) % n])
        
        result = min(result, sum)

    print(result, file=outfile, end="")



