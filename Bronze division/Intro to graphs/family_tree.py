import sys
sys.stdin = open(r"family.in", "r")
sys.stdout = open(r"family.out", 'w')

def go_to_root(node: str, mom_figlia):
    result = []
    while(True):
        if not node in mom_figlia:
            break
        result.append(mom_figlia[node])
        node = mom_figlia[node]
    
    return result

def find_common_ancestor(a_ancestor, b_ancestor):
    
    for i in range(len(a_ancestor)):
        if b_ancestor.count(a_ancestor[i]):
            return (i, b_ancestor.index(a_ancestor[i]))
        
    return False

n, a, b = input().split()
n = int(n)
mom_figlia = dict()

for _ in range(n):
    m, d = input().split()
    mom_figlia[d] = m


a_ancestor = [a] + go_to_root(a, mom_figlia)
b_ancestor = [b] + go_to_root(b, mom_figlia)

common_ancestor = find_common_ancestor(a_ancestor, b_ancestor)

if common_ancestor != False:
    da = common_ancestor[0]
    db = common_ancestor[1]

    if da == 1 and db == 1:
        print("SIBLINGS")
        sys.exit()
    elif da > 1 and db > 1:
        print("COUSINS")
        sys.exit()
    else:
        if da > db:
            da, db = db, da
            b, a = a, b
        print(a, "is the ", end="")

        for _ in range(db-2):
            print("great-", end="")
        if da == 0 and db > 1:
            print("grand-", end="")
        if da == 0:
            print("mother ", end="")
        else:
            print("aunt ", end="")
        print("of", b)

else:
    print("NOT RELATED")