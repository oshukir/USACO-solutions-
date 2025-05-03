import heapq

## input
n = int(input())
rooms = [0] * n
customers = []
for i in range(n):
    a, b = map(int, input().split())
    customers.append((a, b, i))

## sort
customers.sort()

roomCount = 0
departures = []

## iterate over each customer
for arrive, depart, i in customers:
    if (not departures or departures[0][0] >= arrive):
        roomCount += 1
        rooms[i] = roomCount
    else:
        rooms[i] = heapq.heappop(departures)[1]
    heapq.heappush(departures, (depart, rooms[i]))
    
## output
print(roomCount)
print(" ".join(map(str, rooms)))