# #https://usaco.org/index.php?page=viewproblem2&cpid=665

# #MY SOLUTION

with open('cowsignal.in') as f:
    m, n, k = map(int, f.readline().split())

    maze = []

    for _ in range(m):
        row = f.readline()
        row = row.replace('\n', "")
        maze.append(row)

with open('cowsignal.out', mode='w') as f:
    for row in maze:
        k_row = ""
        for char in row:
            k_row += char*k
        
        k_row = (k_row + '\n')*k
        print(k_row, file=f, end="")





#USACO solution
with open("cowsignal.in", "r") as infile, open("cowsignal.out", "w") as outfile:

    r, c, k = map(int, infile.readline().split())
    
    for _ in range(r):
        curr_row = infile.readline().strip()

        for _ in range(k):
            expanded_row = ''.join(char * k for char in curr_row)
            outfile.write(expanded_row + '\n')