MOD = 2019
string = input()

count = [0] * 2019
count[0] = 1

cur_num = 0
power = 1

for c in reversed(string):
    cur_num = (int(c) * power + cur_num) % MOD
    power = (power * 10) % MOD

    count[cur_num] += 1

ans = 0
for rep in count:
    ans += (rep * (rep-1)) // 2

print(ans)