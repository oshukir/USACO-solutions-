# N, Q = map(int, input().split())
# data = [int(x) for x in input().split()]
# quer = []

# for i in range(Q):
#     a, b = map(int, input().split())
#     quer.append((a,b))

# prefix_sum = [0]
# for i in range(N):
#     prefix_sum.append(prefix_sum[-1] + data[i])

# for i in range(Q):
#     print(prefix_sum[quer[i][1]] - prefix_sum[quer[i][0]])



#Alternative solution
import itertools

def psum(a):
    return [0] + list(itertools.accumulate(a))

N, Q = map(int, input().split())
a = list(map(int, input().split()))
p = psum(a)

for i in range(Q):
	l, r = map(int, input().split())
	print(p[r] - p[l])