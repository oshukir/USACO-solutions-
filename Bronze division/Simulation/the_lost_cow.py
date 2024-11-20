#https://usaco.org/index.php?page=viewproblem2&cpid=735

inpath = "lostcow.in"
outpath = "lostcow.out"

from math import log2, floor, ceil

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    x, y = map(int, infile.readline().split())
    result = 0

    if x == y:
        print(0, file=outfile)
    else:
        i = 0
        current_position = x

        while True:
            target = x + ((-1) ** i) * (2 ** i)

            if (x < y <= target) or (x > y >= target):
                result += abs(current_position - y)
                break
            else:
                result += abs(current_position - target)
                current_position = target

            i += 1
    
    print(result, file=outfile, end="")
            



#USACO SOLUTION
inpath = "lostcow.in"
outpath = "lostcow.out"

from math import log2, floor, ceil

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    x, y = map(int, infile.readline().split())
    
    ans = 0
    by = 1
    direction = 1

    while True:
        if (direction == 1 and x <= y < x + by) or (direction == -1 and x - by <= y <= x):
            ans += abs(y-x)

            print(ans, file=outfile)
            break
        else:
            ans += by * 2
            by *= 2

            direction *= -1
    
    
            
            

    
            

    