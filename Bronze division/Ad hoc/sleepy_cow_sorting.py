import sys

sys.stdin = open("sleepy.in", "r")
sys.stdout = open("sleepy.out", "w")

n = int(input())
data = list(map(int, input().split()))

data.reverse()
first_sorted_number = 1
for i in range(1, len(data)):
    if data[i] < data[i-1]:
        first_sorted_number+=1
    else:
        break

print(n - first_sorted_number)