inpath = r"triangles.in"
outpath = r"triangles.out"

    



with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    n = int(infile.readline())

    data = [list(map(int,infile.readline().split())) for _ in range(n)]

    result = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if data[i][0] == data[j][0] and data[i][1] == data[k][1]:
                    area = abs((data[j][1] - data[i][1])*(data[k][0] - data[i][0]))
                    result = max(result, area)

    print(result, file=outfile)


