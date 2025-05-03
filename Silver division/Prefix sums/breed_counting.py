# import sys
# sys.stdin = open("bcount.in", 'r')
# sys.stdout = open("bcount.out", 'w')

# N, Q = map(int, input().split())
# prefix_sums = [[0,0,0]]

# for i in range(N):
#     cow = int(input())
    
#     to_add = prefix_sums[-1].copy()
#     to_add[cow-1] += 1

#     prefix_sums.append(to_add)

# for i in range(Q):
#     a, b = map(int, input().split())

#     result = [x-y for x, y in zip(prefix_sums[b], prefix_sums[a-1])]
#     print(result[0], result[1], result[2])


#More efficient solution:
with open("bcount.in") as read:
	cow_num, query_num = [int(i) for i in read.readline().split()]
	holsteins = [0]
	guernseys = [0]
	jerseys = [0]
	for _ in range(cow_num):
		holsteins.append(holsteins[-1])
		guernseys.append(guernseys[-1])
		jerseys.append(jerseys[-1])

		cow = int(read.readline())
		if cow == 1:
			holsteins[-1] += 1
		elif cow == 2:
			guernseys[-1] += 1
		elif cow == 3:
			jerseys[-1] += 1

	with open("bcount.out", "w") as written:
		for _ in range(query_num):
			start, end = [int(i) for i in read.readline().split()]
			holstein = holsteins[end] - holsteins[start - 1]
			guernsey = guernseys[end] - guernseys[start - 1]
			jersey = jerseys[end] - jerseys[start - 1]
			written.write(f"{holstein} {guernsey} {jersey}\n")