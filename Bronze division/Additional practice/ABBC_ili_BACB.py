n = int(input())

for i in range(n):
    line = input() + 'K'

    count_B = 0 if line[0] == 'A' else 1
    min_count_A = float("inf")
    count_fila_A = 0
    count_A = 0 if line[0] == 'B' else 1

    result = 0

    for j in range(1, len(line)):
        if line[j] == 'A':
            if count_A == 0:
                count_A = 1
            
            if line[j-1] == 'A':
                count_A += 1
        else:
            if count_A > 0:
                min_count_A = min(min_count_A, count_A)
                result += count_A
                count_fila_A += 1
                count_A = 0
            
            if line[j] == 'B':
                count_B += 1
    
    if count_B < count_fila_A:
        print(result - min_count_A)
    else:
        print(result)

