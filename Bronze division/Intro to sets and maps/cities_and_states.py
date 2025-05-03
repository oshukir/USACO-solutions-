import sys
from collections import defaultdict

inpath = r"citystate.in"
outpath = r"citystate.out"


with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    pairs = []

    for _ in range(int(infile.readline())):
        city, state = infile.readline().strip().split()
        city = city[:2]
        pairs.append((city, state))

    seen = defaultdict(int)
    total = 0

    for c, s in pairs:
        if c != s:
            total += seen[s + c]
        seen[c+s] += 1

    print(total, file=outfile)







# with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
#     n = int(infile.readline())
#     data = [line.split() for line in infile.readlines()]

#     data_dict = {}
#     for i in data:
#         key, value = i[0][:2], i[1]
#         element = (key,value)

#         if not element in data_dict:
#             data_dict[element] = 0
#         data_dict[element] += 1

#     res = 0
#     for i in data:
#         if (i[1], i[0][:2]) in data_dict and i[1] != i[0][:2]:
#             res += data_dict[(i[1], i[0][:2])]

    
#     print(res//2, file=outfile)



