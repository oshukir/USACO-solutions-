n = int(input())
data = [int(number) for number in input().split()]

data.sort(reverse=True)

revenue = 0
price = float("inf")
for i in range(len(data)):
    if i == len(data) - 1 or data[i+1] != data[i]:
        iter_rev = data[i] * (i+1)
        if revenue <= iter_rev:
            revenue = iter_rev
            price = min(price, data[i])

print(revenue, price)