n, m, k = map(int, input().split())

desires = [int(x) for x in input().split()]
casi = [int(x) for x in input().split()]

desires.sort()
casi.sort()

l1 = 0
l2 = 0
result = 0


while l1 < len(casi):

    while l2 < len(desires):

        while l2+1 < len(desires) and casi[l1] - desires[l2] > 0 and abs(casi[l1] - desires[l2]) > k:
            l2 += 1

        
        if abs(casi[l1] - desires[l2]) <= k:
            result+=1
            l2 += 1
            

        break

    l1+=1

print(result)

    

#USACO solution:
# n, m, tolerance = map(int, input().split())
# applicants = list(map(int, input().split()))
# apartments = list(map(int, input().split()))
# applicants.sort()
# apartments.sort()

# i = 0
# j = 0
# ans = 0
# while i < n and j < m:
#     applicant = applicants[i]
#     apartment = apartments[j]

#     if apartment < applicant - tolerance:
#         j += 1
#     elif apartment > applicant + tolerance:
#         i += 1
#     else:
#         ans += 1
#         i += 1
#         j += 1
# print(ans)