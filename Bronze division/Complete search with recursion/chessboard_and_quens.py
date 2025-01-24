reserved = [[True for __ in range(8)] for _ in range(8)]
for i in range(8):
    line = input()
    for index,j in enumerate(line):
        if j == '*':
            reserved[i][index] = False

def get_result(n: int):
    count = 0
    column = [False] * n
    diagn1 = [False] * (2*n-1)
    diagn2 = [False] * (2*n-1)

    def f(y: int= 0):
        if y == n:
            nonlocal count
            count+=1
            return
        else:
            for i in range(n):
                if reserved[y][i] == False or column[i] or diagn1[i+y] or diagn2[i-y+n-1]:
                    continue
                else:
                    column[i] = diagn1[i+y] = diagn2[i-y+n-1] = True
                    f(y+1)
                    column[i] = diagn1[i+y] = diagn2[i-y+n-1] = False
    
    f()
    return count

print(get_result(8))
    
    

