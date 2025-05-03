n = int(input())
data = [int(elem) for elem in input().split()]

data.sort()



result = float("inf")
for i in range(len(data)):
    for j in range(i+1, len(data)):
        temp = data.copy()
        temp.pop(i)
        temp.pop(j-1)

        instability = 0

        for k in range(0,len(temp), 2):
            instability += abs(temp[k] - temp[k+1])

        result = min(result, instability)

print(result)
        