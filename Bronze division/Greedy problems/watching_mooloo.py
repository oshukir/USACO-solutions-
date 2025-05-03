# n, k = map(int, input().split())
# data = [int(x) for x in input().split()]

# count = 0
# group = [data[0]]
# for i in range(1, len(data)):
#     if (k + 1) + (k + group[-1] - group[0] + 1) > data[i] - group[0] + 1 + k:
#         group.append(data[i])
#     else:
#         count += group[-1] - group[0]  + 1 + k
#         group = [data[i]]

# if len(group):
#     count += group[-1] - group[0] + 1 + k

# print(count)



#USACO solution (same concept, but better):
n, k = map(int, input().split())
days = list(map(int, input().split()))

last_day = days[0]
cost = k + 1  # Start the first subscription

for d in days:
	# Should Bessie extend the most recent subscription?
	if d - last_day < k + 1:
		cost += d - last_day
	else:
		# Or just start a new one entirely?
		cost += k + 1

	# Store the date of the last subscription
	last_day = d

print(cost)