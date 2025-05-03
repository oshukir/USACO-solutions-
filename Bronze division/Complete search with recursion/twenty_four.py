import operator

def custom_truediv(a, b):
    if b == 0 or a % b != 0:
        return float("-inf")
    
    return a // b

operation = [operator.add, operator.sub, operator.mul, custom_truediv]

def get_permutation(data: list):

    all_perms = set()
    perm = []
    chosen = [False] * len(data)

    def recursion(k: int = 0):
        if len(perm) == 4:
            all_perms.add(tuple(perm.copy()))
            return
        
        for i in range(4):
            if chosen[i] == True:
                continue

            perm.append(data[i])
            chosen[i] = True

            recursion(k+1)

            chosen[i] = False
            perm.pop()


    recursion()
    return all_perms



def calculation1(A,B,C,D):
    ans = float("-inf")
    for q in range(4):
        for w in range(4):
            for e in range(4):

                try:
                    first = operation[q](A, B)
                    # If the operation is invalid, continue;
                    if first == float("-inf"):
                        continue

                    second = operation[w](first,C)
                    if second == float("-inf"):
                        continue

                    third = operation[e](second,D)
                    if third == float("-inf"):
                        continue

                    if third <= 24:
                        ans = max(ans, third)
                except ZeroDivisionError as z:
                    pass

    return int(ans)

def calculation2(A,B,C,D):
    ans = float("-inf")
    for q in range(4):
        for w in range(4):
            for e in range(4):
                try:
                    first = operation[q](A,B)
                    if first == float("-inf"):
                        continue

                    second = operation[w](C,D)
                    if second == float("-inf"):
                        continue

                    third = operation[e](first,second)
                    if third == float("-inf"):
                        continue

                    if third <= 24:
                        ans = max(ans, third)   
                except ZeroDivisionError as z:
                    pass
    return int(ans)


def solution(data: list):
    result = []

    for i in range(len(data)):
        all_perms = get_permutation(data[i])
        answer = float("-inf")
        for t in all_perms:
            A = t[0]
            B = t[1]
            C = t[2]
            D = t[3]

            answer = max(answer,calculation1(A,B,C,D))
            answer = max(answer,calculation2(A,B,C,D))
            
        
        result.append(str(answer))

    return "\n".join(result)
                        

N = int(input())
data = [[int(input()) for __ in range(4)] for _ in range(N)]

print(solution(data))

