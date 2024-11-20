# inpath = "blist.in"
# outpath = "blist.out"

# from math import log2, floor, ceil

# with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
#     n = int(infile.readline().strip())

#     cows = [[int(j) for j in i.split()] for i in infile.readlines()]

#     intervals = []
#     for _ in range(n):
#         cow_interval = [0] * 1010
#         for i in range(cows[_][0], cows[_][1]+1):
#             cow_interval[i] = cows[_][2]
#         intervals.append(cow_interval)

#     result = 0
#     for i in range(n):
#         index = cows[i][0]
#         using_now = 0
#         for j in range(n):
#             using_now += intervals[j][index]

#         if using_now > result:
#             result += (using_now-result)
        
#     print(result, file=outfile, end="")



#USACO first solution (Brute force)
inpath = "blist.in"
outpath = "blist.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n = int(infile.readline().strip())

    cows = [[int(j) for j in i.split()] for i in infile.readlines()]

    result = 0
    
    for t in range(1, 1001):
        curr_buckets = 0
        for c in cows:
            if c[0] <= t <= c[1]:
                curr_buckets += c[2]
        result = max(result, curr_buckets)

        
    print(result, file=outfile, end="")