import sys
sys.stdin = open("hoofball.in", "r")
sys.stdout = open("hoofball.out", "w")

n = int(input())
cows = sorted(list(map(int, input().strip().split())))
balls = [0] * n
ans = 0

def nearestneighbour(ind):
    lnbr, rnbr = -1, -1
    ldist, rdist = 1000, 1000

    for i in range(n):

        if cows[i] < cows[ind] and cows[ind] - cows[i] < ldist:
            lnbr = i
            ldist = cows[ind] - cows[i]

    for i in range(n):
        if  cows[i] > cows[ind] and cows[i] - cows[ind] < rdist:
            rnbr = i
            rdist = cows[i] - cows[ind]

    return lnbr if ldist <= rdist else rnbr

for i in range(n):
    balls[nearestneighbour(i)] += 1

for i in range(n):

    if balls[i] == 0:
        ans += 1

    if (
        i < nearestneighbour(i)
        and nearestneighbour(nearestneighbour(i)) == i
        and balls[i] == 1
        and balls[nearestneighbour(i)] == 1
    ):
        ans += 1

print(ans)