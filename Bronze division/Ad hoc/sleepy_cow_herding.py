import sys

sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

data = list(map(int, input().split()))
data.sort()

if data[1] - data[0] == 1 and data[2] - data[1] == 1:
    print(0, 0, sep='\n')
    sys.exit(0)


if data[1] - data[0] == 2 or data[2] - data[1] == 2:
    print(1)
else:
    print(2)

print(max(data[2]- data[1], data[1] - data[0]) - 1)

