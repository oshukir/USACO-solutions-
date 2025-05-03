N = int(input())
data = [int(x) for x in input().split()]

data.sort()

mediana_value = data[len(data) // 2]
result = 0

for i in data:
    result += abs(i - mediana_value)

print(result)