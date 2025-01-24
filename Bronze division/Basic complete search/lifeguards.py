inpath = r"lifeguards.in"
outpath = r"lifeguards.out"

    



with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    n = int(infile.readline())
    data = [list(map(int,infile.readline().split())) for _ in range(n)]

    ox = {}
    cover = 0

    for i in range(n):
        left = data[i][0]
        right = data[i][1]

        for j in range(left, right):
            if not j in ox:
                ox[j] = 0
                cover += 1
            ox[j] += 1

    time_loss = 10000
    for i in range(n):
        left = data[i][0]
        right = data[i][1]
        efficiency = right - left

        for j in range(left, right):
            if ox[j] - 1 > 0:
                efficiency -= 1

        time_loss = min(time_loss, efficiency)

    print(cover-time_loss, file=outfile)
                

        

