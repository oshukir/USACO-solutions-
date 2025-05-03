import heapq

n, m = map(int, input().split())

# Adjacency list of (neighbour, edge weight)
graph = [[] for _ in range(n)]
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a - 1].append((b - 1, c))

#graph[0] -> (2, 6), (3, 4), (3, 2)
#graph[2] -> []


# Initially set all distances to infinity
dist = [float("inf") for _ in range(n)]

# Dijkstra's algorithm
pq = []

start = 0
heapq.heappush(pq, (0, start))
dist[start] = 0  # The shortest path from a node to itself is 0
while pq:
	cdist, node = heapq.heappop(pq)
	if cdist > dist[node]:
		continue
	for i in graph[node]:
		# If we can reach a neighbouring node faster,
		# we update its minimum distance
		if cdist + i[1] < dist[i[0]]:
			dist[i[0]] = cdist + i[1]
			heapq.heappush(pq, (dist[i[0]], i[0]))

print(*dist)