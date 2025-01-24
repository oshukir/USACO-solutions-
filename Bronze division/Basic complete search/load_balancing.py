inpath = r"balancing.in"
outpath = r"balancing.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    N, B = map(int, infile.readline().split())
    cows = [tuple(map(int, infile.readline().split())) for _ in range(N)]


    x_coords = sorted(set(x+1 for x,y in cows if (x+1) % 2 == 0))
    y_coords = sorted(set(y+1 for x,y in cows if (y+1) % 2 == 0))

    min_M = N

    for x_fence in x_coords:
        for y_fence in y_coords:

            q1 = q2 = q3 = q4 = 0
            for x, y in cows:
                if x > x_fence and y > y_fence:
                    q1 += 1
                elif x > x_fence and y < y_fence:
                    q2 += 1
                elif x < x_fence and y < y_fence:
                    q3 += 1
                elif x < x_fence and y > y_fence:
                    q4 += 1

            M = max(q1,q2,q3,q4)
            min_M = min(min_M, M)

    print(min_M, file=outfile)