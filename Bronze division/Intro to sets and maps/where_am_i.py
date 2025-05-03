import sys

inpath = r"whereami.in"
outpath = r"whereami.out"

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    n = int(infile.readline())
    mails = infile.readline()

    lengths_to_unique = {}

    for i in range(1, len(mails)+1):
        lengths_to_unique[i] = set()
        for j in range(0, len(mails) - i + 1):
            if not mails[j:j+i] in lengths_to_unique[i]:
                lengths_to_unique[i].add(mails[j:j+i])

    for i in range(1, len(mails)+1):
        if len(lengths_to_unique[i]) == len(mails) - i + 1:
            print(i, file=outfile)
            sys.exit(0)




#USACO solution:
# Take in input using Python file i/o system
file_in = open("whereami.in")
data = file_in.read().strip().split("\n")
n = int(data[0])
mailboxes = data[1]

# Set the answer initially to n, as we know n is always a possible answer
ans = n

# We can iterate through lengths of sequences to find the smallest length
for l in range(1, n + 1):
	# Store the substrings in a set
	sequences = set()
	for i in range(n - l + 1):
		sequences.add(mailboxes[i : i + l])
	# Check if all substrings are unique
	if len(sequences) == (n - l + 1):
		ans = l
		# We can exit the loop as this will be the smallest working length
		break

print(ans, file=open("whereami.out", "w"))