import sys

sys.stdin = open(r"revegetate.in", "r")
sys.stdout = open(r"revegetate.out", "w")

n, k = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(k):
    i, j = map(int, input().split())
    adj[i-1].append(j-1)
    adj[j-1].append(i-1)

options = [[1,2,3,4] for _ in range(n)]
for i in range(n):
    print(options[i][0], end="")

    for j in adj[i]:
        if options[i][0] in options[j]:
            options[j].remove(options[i][0])


