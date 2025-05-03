

N, a, b = input(), input(), input()
s = [(x == y) for x, y in zip(a, b)] + [True]

print(sum(1 if not x and y else 0 for x, y in zip(s, s[1:])))