file_in = r"maxcross.in"
file_out = r"maxcross.out"

with open(file_in, 'r') as infile, open(file_out, 'w') as outfile:
    N, K, B = map(int, infile.readline().split())
    seen = [0 for _ in range(N+1)]

    for i in range(B):
        seen[int(infile.readline())] = 1

    prefix_seen_k = 0
    for i in range(1, K+1):
        prefix_seen_k += seen[i]

    left = 1
    right = K
    solutions = []

    while N > right:
        prefix_seen_k += (seen[right+1] - seen[left])
        left, right = left + 1, right + 1
        solutions.append(prefix_seen_k)

    print(min(solutions), file=outfile)