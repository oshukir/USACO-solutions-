for _ in range(int(input())):
    W, H = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w2, h2 = map(int, input().split())

    w1, h1 = (x2-x1), (y2-y1)

    result = float("inf")
    if w1 + w2 <= W:
        result = min(max(0, w2-x1), max(0, x2 - (W-w2)))
    if h1 + h2 <= H:
        result = min(result, min(max(0, h2-y1), max(0, y2 - (H-h2))))

    print(-1 if result == float("inf") else result)

    
    


