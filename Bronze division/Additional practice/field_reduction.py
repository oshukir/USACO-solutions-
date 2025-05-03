import sys

sys.stdin = open(r"reduce.in", "r")
sys.stdout = open(r"reduce.out", "w")



n = int(input())
cows = []
for _ in range(n): 
    coord = [int(i) for i in input().split()]
    cows.append(coord)

x_coords = sorted([cows[i][0] for i in range(n)])
y_coords = sorted([cows[i][1] for i in range(n)])
area = (max(x_coords) - min(x_coords)) * (max(y_coords) - min(y_coords))
x_min = x_coords[:4:]
x_max = x_coords[n:n-5:-1]
y_min = y_coords[:4:]
y_max = y_coords[n:n-5:-1]

for i in x_min:
    for j in x_max:
        if i >= j:
            continue
        
        for k in y_min:
            for l in y_max:
                if k >= l:
                    continue
                out = 0

                for x, y in cows:
                    if x < i or x > j or y < k or y > l:
                        out += 1
                    if out > 3:
                        break

                if out <= 3:
                    area_temp = (j-i) * (l-k)
                    if area_temp < area:
                        area = area_temp

print(area)