from itertools import permutations
with open(r"hps.in", 'r') as infile, \
     open(r"hps.out", 'w') as outfile:
    
    N = int(infile.readline())
    data = [(x.strip()) for x in infile.readlines()]

    prefix_sum = {
        'P' : [0],
        'H' : [0],
        'S' : [0],
    }

    what_win = {
        'P' : 'H',
        'H' : 'S',
        'S' : 'P'
    }

    result = 0
    john_input = ['P', 'H', 'S']

    for i in range(N):
        prefix_sum['P'].append(prefix_sum['P'][-1])
        prefix_sum['H'].append(prefix_sum['H'][-1])
        prefix_sum['S'].append(prefix_sum['S'][-1])

        if data[i] == 'P':
            prefix_sum['P'][-1] += 1
        elif data[i] == 'H':
            prefix_sum['H'][-1] += 1
        else:
            prefix_sum['S'][-1] += 1

    combos = list(permutations(john_input, 2))
    for i in range(0,N):
        if i == N-1:
            pass
        
        for j in combos:
            before = j[0]
            after = j[1]

            wins_before_transition = prefix_sum[what_win[before]][i]
            wins_after_transition = prefix_sum[what_win[after]][-1] - prefix_sum[what_win[after]][i]

            result = max(result, wins_before_transition + wins_after_transition)

    
    print(result, file=outfile)
