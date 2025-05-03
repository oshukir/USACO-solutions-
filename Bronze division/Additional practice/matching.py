for _ in range(int(input())):
    input()
    arr = [int(i) for i in input().split()]

    groups: dict[int, list] = {}
    for i in range(len(arr)):
        id_ = i - arr[i]
        if id_ not in groups:
            groups[id_] = []
        groups[id_].append(arr[i])

    total = 0
    for comp in groups.values():
        comp.sort(reverse=True)
        for i in range(0, len(comp) - 1, 2):
            weight = comp[i] + comp[i+1]
            if weight > 0:
                total += weight
    
    print(total)
