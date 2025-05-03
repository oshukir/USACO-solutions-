for _ in range(int(input())):

    N = int(input())
    
    prefix_sum = 0
    result = 0
    a = input()
    d = {0: 1}

    for i in range(N):
        prefix_sum += int(a[i])
        x = prefix_sum - (i+1)

        if not x in d:
            d[x] = 0
        d[x] += 1

        result += d[x] - 1

    print(result)