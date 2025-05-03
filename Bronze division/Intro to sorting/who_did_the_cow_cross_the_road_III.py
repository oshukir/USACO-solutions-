inpath = r"cowqueue.in"
outpath = r"cowqueue.out"



with open(inpath, "r") as infile, open(outpath, "w") as outfile:

    n = int(infile.readline())
    data = [tuple(map(int, line.split())) for line in infile.readlines()]

    data.sort()

    index = -1

    for i in data:
        time, duration = i

        index = max(index, time)
        index += duration

    print(index, file=outfile)

