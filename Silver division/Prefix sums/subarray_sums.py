import random

RANDOM = random.randrange(2**62)

def Wrapper(x):
    return x ^ RANDOM

def main():
    N, X = map(int, input().split())
    prefix, res = 0, 0
    mp = {Wrapper(0): 1}

    for x in input().split():
        prefix += int(x)
        res += mp.get(Wrapper(prefix - X), 0)
        mp[Wrapper(prefix)] = mp.get(Wrapper(prefix), 0) + 1

    print(res)

# Вызов основной функции
if __name__ == "__main__":
    main()