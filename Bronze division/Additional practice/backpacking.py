from collections import deque
from typing import List, Tuple

def main():
    N, K = map(int, input().split())
    D = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    pq: deque[Tuple[int, int]] = deque()
    in_backpack = 0
    ans = 0

    def do_pop(n: int):
        nonlocal in_backpack, ans
        while n > 0:
            assert pq
            c, cnt = pq[0]
            num = min(cnt, n)
            n -= num
            in_backpack -= num
            ans += c * num
            cnt -= num
            if cnt == 0:
                pq.popleft()
            else:
                pq[0] = (c, cnt)

    for i in range(N-1):
        c = C[i]
        while pq and pq[-1][0] >= c:
            in_backpack -= pq[-1][1]
            pq.pop()
        pq.append((c, K - in_backpack))
        in_backpack = K
        do_pop(D[i])
    
    print(ans)

if __name__ == "__main__":
    main()