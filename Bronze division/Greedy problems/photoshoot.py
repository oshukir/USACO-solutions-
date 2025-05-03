cow_num = int(input())
cows = input()

flips = 0
for c in range(cow_num-2, -1, -2):
    sub = cows[c : c+2]
    if sub[0] == sub[1]:
        continue
    if (sub == "GH" and flips % 2 == 0) or (sub == "HG" and flips % 2 == 1):
        flips += 1
    
print(flips)

### Look youtube explanation (the same approach)
### https://www.youtube.com/watch?v=rkcC_oKfIrU
