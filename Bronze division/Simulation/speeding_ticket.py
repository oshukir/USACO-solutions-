inpath = "speeding.in"
outpath = "speeding.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n, m = map(int, infile.readline().split())

    limit = [list(map(int, infile.readline().split())) for _ in range(n)]
    besii = [list(map(int, infile.readline().split())) for _ in range(m)]

    result = 0


    
    lb_besi = 0
    for i in range(m):
        ub_besi = lb_besi + besii[i][0]
        lb_road = 0

        for j in range(n):
            ub_road = lb_road + limit[j][0]

            if lb_besi < ub_road and ub_besi > lb_road:
                result = max(result, besii[i][1] - limit[j][1])

            lb_road = ub_road
        
        lb_besi = ub_besi
    
    print(result, file=outfile, end="")
            
            

    