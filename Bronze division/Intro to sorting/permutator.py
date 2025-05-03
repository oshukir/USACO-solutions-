import operator

n = int(input())
a, b = [[int(elem) for elem in input().split()] for _ in range(2)]

to_add = n - 2
coefficent = [n] * (n)
for i in range(1, n):
    coefficent[i] = coefficent[i-1] + to_add
    to_add -= 2

new_a = list(map(operator.mul, a, coefficent))
new_a.sort()
b.sort(reverse=True)


result = sum(map(operator.mul, new_a, b))
print(result)