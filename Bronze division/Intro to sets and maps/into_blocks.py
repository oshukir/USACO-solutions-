####MY SOLUTION

n, q = list(map(int, input().split()))
data = [x for x in input().split()]

num_range = {}
for i in range(len(data)):
    if not data[i] in num_range:
        num_range[data[i]] = [i,i]
    else:
        num_range[data[i]][1] = i
    
result = 0


i = 0
while i < n:
    left = i
    valid_right = num_range[data[i]][1]
    k = left
    while k < valid_right + 1:
        valid_right = max(valid_right, num_range[data[k]][1])
        k += 1

    occured = {}
    local_max = 0
    for j in range(left, valid_right+1):
        if not data[j] in occured:
            occured[data[j]] = 0
        occured[data[j]] += 1
        local_max = max(local_max, occured[data[j]])

    i = valid_right + 1
    result += (valid_right - left + 1) - local_max

print(result)





#Мне очень понравилась идея с блоками (аналог моего расширения в правую сторону, как с valid_right в моем коде)
'''Approach:
Instead of finding the elements which we should change to get a nice sequence it is much easier
to find which all elements will not change in a give sequence. 
Finally subtracting the these constants from total number of elements will give our answer 

1.we can divide the given sequence into differernt blocks and we need to find the number of constant
element in each block
2. the number of constant element in each block will be the count of maximum occuring element within the block

eg. [1,1,3,1,4,5,4]
here we can take [1,1,3,1] as first block and [4,5,4] as the second block 
a block continst the first occurence and last occurence of each element within it

the count of max occuring element ib block1 is :3  (number of 1s)
the count of max occuring element in block2 is :2  (number of 4s)

so 3 elements from block 1 will not change and 2 elements from block 2 remain constant give a total of 5 constants
therefore, the total number of changes/difficulty of the sequence is 7-5=2  (7 is total number of element is sequence)


I couldn't find any solution for this question , so hopefully this  will help someone 


'''
n,q=map(int,input().split())   #input n and q values
sequence=list(map(int,input().split()))   #take the input sequence as a list

#we can use dictionary to keep track of elements of sequence 

dict_first_occur={} #To keep track of INDEX of first occurence of each element of sequence
                    # is of the form {element : index}
dict_last_occur={}  #To keep track of INDEX of last occurence of each element of sequence
                    # is of the form {element : index}
dict_count={}       #To keep track of total number of occurence of each element in sequence 

for i in range(n):
    if sequence[i] not in dict_first_occur:
        dict_first_occur[sequence[i]]=i

    dict_last_occur[sequence[i]]=i

    if sequence[i] not in dict_count:
        dict_count[sequence[i]]=0
    dict_count[sequence[i]]+=1

block=0
max_count=0
constants=0
for i in range(n):
    if i==dict_first_occur[sequence[i]]:
        block+=1
    if i==dict_last_occur[sequence[i]]:
        block-=1
    max_count=max(max_count,dict_count[sequence[i]])
    if block==0:  #if block value become 0 then it can be taken as a single block (can be separated from the sequence) 
        constants+=max_count  #count the blocks individually 
        max_count=0
print(n-constants)
