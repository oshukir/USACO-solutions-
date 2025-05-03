###Mysolution:

# k, n = list(map(int, input().split()))
# marks, b = [[int(x) for x in input().split()] for _ in range (2)]

# pref_sum = [marks[0]] * k
# for i in range(1, k):
#     pref_sum[i] = pref_sum[i-1] + marks[i]



# guess = [set() for _ in range(n)]
# for i in range(n):
#     for j in range(k):
#         guess[i].add(b[i]-pref_sum[j])

# result = guess[0]    
# for i in range(1,n):
#     result = result.intersection(guess[i])

# print(len(result))




###USACO SOLUTION
mark_num, remember_num = [int(i) for i in input().split()]

# All net changes in the score
changes = [0] + [int(i) for i in input().split()]
scores = {int(i) for i in input().split()}
assert mark_num == len(changes) - 1 and len(scores) == remember_num

for i in range(1, len(changes)):
	changes[i] += changes[i - 1]

poss_starts = set()
random_score = next(iter(scores))
for c in range(1, len(changes)):
	poss_starts.add(random_score - changes[c])

valid_starts = 0
for s in poss_starts:
	# What all the scores are going to now be given the starting score
	resulting_scores = set()
	for c in range(1, len(changes)):
		resulting_scores.add(s + changes[c])

	valid_starts += scores.issubset(resulting_scores)

print(valid_starts)