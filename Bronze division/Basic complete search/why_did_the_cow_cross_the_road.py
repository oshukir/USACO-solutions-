inpath = r"circlecross.in"
outpath = r"circlecross.out"
import string

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    data = infile.readline()

    letter_enters = {}
    for i in range(52):
        if not data[i] in letter_enters:
            letter_enters[data[i]] = []
        letter_enters[data[i]].append(i)

    alph = string.ascii_uppercase
    pair_number = 0
    for i in alph:
        left = letter_enters[i][0]
        right = letter_enters[i][1]

        inner_enters = {}
        for j in range(left+1, right):
            if not data[j] in inner_enters:
                inner_enters[data[j]] = 0
            inner_enters[data[j]]+=1

        for key, value in inner_enters.items():
            if value == 1:
                pair_number+=1
        
    
    print(pair_number//2, file=outfile)






#more effictive solution:

with open("circlecross.in") as read:
    crossings = read.readline().strip()

start = [-1 for _ in range(26)]
end = [-1 for _ in range(26)]
for v, c in enumerate(crossings):
    c_id = ord(c) - ord("A")

    if start[c_id] == -1:
        start[c_id] = v
    else:
        end[c_id] = v

crossing_pairs = 0

for i in range(26):
    for j in range(26):
        crossing_pairs += start[i] < start[j] and start[j] < end[i] and end[i] < end[j]

print(crossing_pairs, file=open("circlecross.out", "w"))
