mystr = input()

def get_perms(mystr):
    all_perms = set()
    perm = []
    chosen = [False] * len(mystr)

    def recursive():
        if len(perm) == len(mystr):
            all_perms.add("".join(perm.copy()))
            return 
        else:
            for i in range(len(mystr)):
                if chosen[i]:
                    continue
                chosen[i] = True
                perm.append(mystr[i])
                recursive()
                chosen[i] = False
                perm.pop()

    recursive()
    return all_perms

result = get_perms(mystr)
k = len(result)

print(k)
print("\n".join(sorted(result)))