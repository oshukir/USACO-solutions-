from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    char_freq = Counter(input())

    num_pairs = 0
    num_odd = 0
    for c in char_freq.values():
        num_pairs += c // 2
        num_odd += c%2

    res = 2 * (num_pairs // k)
    num_odd += 2 * (num_pairs % k)

    res += num_odd >= k
    print(res)