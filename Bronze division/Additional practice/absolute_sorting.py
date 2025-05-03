import math
def solution():
    n = int(input())
    data = [int(x) for x in input().split()]

    global_l = 0
    global_r = float("inf")


    for i in range(1, len(data)):
        ceiled_av = (abs(data[i] + data[i-1]) / 2)

        l = 0
        r = float("inf")
        if data[i-1] < data[i]:
            r = math.floor(ceiled_av)
        elif data[i] < data[i-1]:
            l = math.ceil(ceiled_av)
        else:
            continue

        if min(r, global_r) - max(l, global_l) < 0:
            return -1
        else:
            global_r = min(r, global_r)
            global_l = max(l, global_l)
    
    return global_l
        


for _ in range(int(input())):
    print(solution())
            


