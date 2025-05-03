import sys
sys.stdin = open(r"factory.in", 'r')
sys.stdout = open(r"factory.out", 'w')


n = int(input())
adj = [[] for _ in range(n)]
for j in range(n-1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    adj[b].append(a)

left = [True] * n
for j in range(n):
    if len(adj[j]):
        for i in adj[j]:
            left[i] = False

counter = left.count(True)
print(-1 if counter > 1 else left.index(True)+1)



###USACO simplified solution:
# n = int(input())
# outgoing = [0 for _ in range(n)]
# for _ in range(n-1):
#     a, b = [int(i) - 1 for i in input().split()]
#     outgoing[a] += 1

# no_outs = []
# for s in range(n):
#     if outgoing[s] == 0:
#         no_outs.append(s+1)

# root = no_outs[0] if len(no_outs) == 1 else -1
# print(root)