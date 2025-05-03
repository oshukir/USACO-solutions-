inpath = r"angry.in"
outpath = r"angry.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    bales = sorted([int(infile.readline()) for _ in range(int(infile.readline()))])

    def exploaded_num(start: int, direction: int) -> int:
        radius = 1
        prev = start
        while True:
            next_ = prev

            while(
                0 <= next_ + direction < len(bales) 
                and abs(bales[next_ + direction] - bales[prev]) <= radius
            ):
                next_ += direction
            
            if next_ == prev:
                break

            prev = next_
            radius += 1

        return abs(prev - start)
    
    max_exploaded = 0
    for i in range(len(bales)):
        max_exploaded = max(max_exploaded, exploaded_num(i, -1) + exploaded_num(i, 1) + 1)

    print(max_exploaded, file=outfile)        