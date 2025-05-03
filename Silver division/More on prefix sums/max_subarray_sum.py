N = int(input())
data = [int(x) for x in input().split()]

prefix_sum = [0]
min_prefix = [0]

max_subarray = -float("inf")

for index, i in enumerate(data):
    prefix_sum.append(prefix_sum[-1] + i)

    max_subarray = max(max_subarray, prefix_sum[-1] - min_prefix[-1])

    min_prefix.append(min(min_prefix[-1], prefix_sum[-1]))


print(max_subarray)