def triangle_area(base: int, height: int) -> int:
    return base*h / 2

def trapezoid_area(a, b, h):
    return (a+b) * h / 2

k = int(input())
while(k):
    n, d, h = map(int, input().split())
    data = [int(x) for x in input().split()]
    data.append(data[-1] + h + 1)

    result = 0
    for i in range(0,len(data)-1):
        if data[i] + h <= data[i+1]:
            result += triangle_area(d, h)
        else:
            a = d
            height = (data[i+1] - data[i])
            b = (h - height) * a / h
            
            result += trapezoid_area(a, b, height)
    
    k-=1

    print("{:.7f}".format(result))