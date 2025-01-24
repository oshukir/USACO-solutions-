import sys
def solution(x,y,a,b,n,m):

    t = max(max(a,b), max(max(x,y), max(n,m)))
    area = x*y + a*b + n*m
    if t**2 != area:
        return -1
    
    return t



x,y,a,b,n,m = list(map(int, input().split()))

answer = solution(x,y,a,b,n,m)

if answer == -1:
    print("-1")
else:
    print(answer)

    logos = ['A', 'B', 'C']
    sizes = [[x,y], [a,b], [n,m]]
    
    if len(set((max(a,b),max(x,y),max(n,m)))) == 1:
        for i in range(3):
            for j in range(min(sizes[i][0], sizes[i][1])):
                print(logos[i] * answer)
    else:
        sizes = [[max(x,y), x, y],[max(a,b), a, b], [max(n,m),n,m]]
        zipped = list(zip(sizes, logos))
        zipped.sort(reverse=True)

        for i in range(min(zipped[0][0][1], zipped[0][0][2])):
            print(zipped[0][-1] * zipped[0][0][0])

        for j in range(1,3):
            for k in range(1,3):
                if zipped[1][0][j] + zipped[2][0][k] == answer:
                    for i in range(answer - min(zipped[0][0][1], zipped[0][0][2])):
                        print(zipped[1][-1] * zipped[1][0][j] + zipped[2][-1] * zipped[2][0][k])
                    sys.exit(0)
        
