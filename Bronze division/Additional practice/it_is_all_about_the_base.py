import sys
sys.stdin = open(r"whatbase.in", "r")
sys.stdout = open(r"whatbase.out", 'w')


def evaluate(num, base):
    return int(num[0]) * (base ** 2) + int(num[1]) * base + int(num[2])


for _ in range(int(input())):
    a, b = input().split()

    base_a = 10
    base_b = 10

    while base_a <= 15000 and base_b <= 15000:
        a_val = evaluate(a, base_a)
        b_val = evaluate(b, base_b)

        if a_val < b_val:
            base_a += 1
        elif a_val > b_val:
            base_b += 1
        else:
            print(base_a, base_b)
            break