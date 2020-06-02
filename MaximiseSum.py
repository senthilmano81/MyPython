n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]

finalsum  = 0 
sum1 = 0 
sum2 = 0 
i = 0 
j = 0 

while i < len(arr1) and j < len(arr2): 
    if arr1[i] < arr2[j]:
        sum1 = sum1 + arr1[i]
        i = i + 1
    elif arr1[i] > arr2[j]: 
        sum2 = sum2 + arr2[j]
        j = j + 1
    else: 
        sum1 = sum1 + arr1[i]
        sum2 = sum2 + arr2[j]
        finalsum = finalsum + max(sum1,sum2)
        sum1 = 0
        sum2 = 0 
        i = i + 1
        j = j + 1
                
while i < len(arr1): 
    sum1 = sum1 + arr1[i]
    i = i + 1

while j < len(arr2): 
    sum2 = sum2 + arr2[j]
    j = j + 1

finalsum = finalsum + max(sum1,sum2)
       
print(finalsum)