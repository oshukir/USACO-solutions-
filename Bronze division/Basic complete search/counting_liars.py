n = int(input())

data = []

for i in range(n):
    line = [elem for elem in input().split()]
    data.append((line[0], int(line[1])))

result = 1e6

for i in range(0,n):
    cow_position = data[i][1]
    truth = 0

    for j in range(0, n):
        if data[j][0] == 'L' and data[j][1] >= cow_position:
            truth += 1
        elif data[j][0] == 'G' and data[j][1] <= cow_position:
            truth += 1

    result = min(result, n-truth)

print(result)