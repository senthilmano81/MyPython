def intersection(arr1,arr2): 
    inter = set(arr1).intersection(arr2)
    return list(inter)

def getSumArr(arr,inter):
    sumarr = []
    i = 0 
    for point in inter: 
        sum = 0 
        while i < len(arr) and arr[i] <= point: 
            sum = sum + arr[i]
            i = i + 1
        sumarr.append(sum)
        
    sum = 0 
    while i < len(arr): 
        sum = sum + arr[i]
        i = i + 1
    sumarr.append(sum)
    
    return sumarr 
    
def sumOfArray(arr): 
    sum = 0 
    for ele in arr: 
        sum += ele
    return sum 

n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]

inter = intersection(arr1,arr2)
sumarr1 = getSumArr(arr1,inter)
sumarr2 = getSumArr(arr2,inter)

sum = 0 
for i in range(len(sumarr1)): 
    sum = sum + max(sumarr1[i], sumarr2[i])

print(sum)

