with open(r"div7.in", 'r') as infile, \
     open(r"div7.out", 'w') as outfile:
    
    N = int(infile.readline())
    data = [int(x.strip()) for x in infile.readlines()]

    first_occur = [-1 for _ in range(7)]
    first_occur[0] = 0

    prefix_mod = 0
    best_photo = 0

    for index, c in enumerate(data):
        prefix_mod = (prefix_mod + c) % 7

        if first_occur[prefix_mod] == -1:
            first_occur[prefix_mod] = index+1
        else:
            best_photo = max(best_photo, index + 1 - first_occur[prefix_mod])

    print(best_photo, file=outfile)