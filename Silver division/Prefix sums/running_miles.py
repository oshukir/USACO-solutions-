for _ in range(int(input())):
    N = int(input())
    b = [int(x) for x in input().split()]

    #bleft + bmiddle + bright - (right - left) -> main formula
    #bleft and bright determine the left and right vars's values
    #Notice, we can rewrite the above formula to next: bmiddle + (bleft + left) + (bright - right)
    #Now, we can independently iterate all bmiddles using prefix and suffix results for bleft and bright accordingly

    prefix = [0 for _ in range(N)]
    suffix = [0 for _ in range(N)]

    for i in range(N):
        prefix[i] = b[i] + i
        suffix[i] = b[i] - i

    for i in range(1, N):
        prefix[i] = max(prefix[i], prefix[i-1])

    for i in range(N-2, -1, -1):
        suffix[i] = max(suffix[i], suffix[i+1])

    answer = 0
    for i in range(1, N-1):
        answer = max(answer, prefix[i-1] + b[i] + suffix[i+1])

    print(answer)