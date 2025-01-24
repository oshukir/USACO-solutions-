inpath = r"tttt.in"
outpath = r"tttt.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    r = [line.strip() for line in infile.readlines()]
    
    result = [0,0,0]
    
    team_dict = {}

    def process(line: str):
        line = "".join(sorted(set(line)))
        if not team_dict.get(line, 0):
            team_dict[line] = 1
            result[len(line)-1] += 1
    
    for k in range(2):
        for i in range(3):
            line = ""
            for j in range(3):
                line += r[i][j] if k == 0 else r[j][i]
            process(line)

            
    process(r[0][0] + r[1][1] + r[2][2])
    process(r[0][2] + r[1][1] + r[2][0])


    print(result[0], file=outfile)
    print(result[1], file=outfile)