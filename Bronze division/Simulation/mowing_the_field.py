inpath = r"mowing.in"
outpath = r"mowing.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n = int(infile.readline().strip())

    visited = {}
    time = 0
    res = float('inf')
    x, y = 0, 0
    directions = {'N' : (-1,0), 'S': (1,0), 'W': (0, -1), 'E': (0,1)}

    for _ in range(n):
        line = infile.readline().strip().split()
        d = directions[line[0].upper()]
        s = int(line[1])

        for _ in range(s):
            x += d[0]
            y += d[1]
            time += 1

            if (x,y) in visited:
                res = min(res, time - visited[(x,y)])
            
            visited[(x,y)] = time
    # Output result
    outfile.write(f"{res if res != float('inf') else -1}\n")
