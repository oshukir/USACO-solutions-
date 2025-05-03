import sys
sys.stdin = open(r"evolution.in", 'r')
sys.stdout = open(r"evolution.out", 'w')

n = int(input())
cows = []
all_chars = set()
for _ in range(n):
    chars = set(input().split()[1:])
    cows.append(chars)
    all_chars.update(chars)

all_chars = list(all_chars)

for a in range(len(all_chars)):
    for b in range(a+1, len(all_chars)):
        both, only_a, only_b = [False] * 3
        for c in cows:
            has_a = all_chars[a] in c
            has_b = all_chars[b] in c

            if has_a and has_b:
                both = True
            elif has_a and not has_b:
                only_a = True
            elif has_b and not has_a:
                only_b = True

        if only_a and only_b and both:
            print("no")
            sys.exit()

print("yes")