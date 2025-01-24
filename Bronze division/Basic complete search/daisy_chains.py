n = int(input())
flowers = list(map(int, input().split()))

result = 0

for i in range(n):
    result+=1
    sub_sum = flowers[i]
    temp_dict = {flowers[i]:1}

    for j in range(i+1, n):
        sub_sum += flowers[j]
        temp_dict[flowers[j]] = 1


        average = sub_sum // (j-i+1)

        if sub_sum % (j-i+1):
            continue
        elif average in temp_dict:
            result += 1

print(result)

        


############# Shorter solution ################
n = int(input())
flowers = [int(x) for x in input().split()]
count = 0
for j in range(1, n+1):
   for i in range(0,n-(j-1)):
       sub = flowers[i:i+j]
       if sum(sub)/len(sub) in sub:
           count +=1
print(count)