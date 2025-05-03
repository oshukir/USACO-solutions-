import sys

inpath = r"tttt.in"
outpath = r"tttt.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    lines = [line.strip() for line in infile.readlines()]

    all_commands = []
    all_commands.extend(lines)
    for i in range(len(lines)):
        vertical = ""
        for j in range(3):
            vertical += lines[j][i]
        all_commands.append(vertical)
    all_commands.append(lines[0][0] + lines[1][1] + lines[2][2])
    all_commands.append(lines[0][2] + lines[1][1] + lines[2][0])

    result = {
        1: set(),
        2: set(),
        3: set()
    }
    for i in all_commands:
        result[len(set(i))].add("".join(sorted(list(set(i)))))

    for i in result:
        if i != 3:
            print(len(result[i]), file=outfile)


