import sys

sys.stdin = open("taming.in", "r")
sys.stdout = open("taming.out", "w")

n = int(input())
data = list(map(int, input().split()))
data.reverse()
data[-1] = 0

extention = 0
res = 0

i = 0
while i < len(data):
    if data[i] == -1:
        extention+=1
    else:
        for j in range(i+1, i+data[i]+1):
            if data[j] != -1 and (data[i] - data[j] != j - i):
                print(-1)
                sys.exit(0)

        res+=1
        i += data[i]

    i+=1

print(res, res+extention)