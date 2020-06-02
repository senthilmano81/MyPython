def Sort(arr): 
    if len(arr) == 1 or len(arr) ==0: 
        return arr 
    mid  = len(arr) // 2 
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    Sort(arr1)
    Sort(arr2)
    merge(arr,arr1,arr2)
    
def merge(arr,arr1,arr2): 
    
    i = 0 
    j = 0 
    k = 0 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            k = k + 1
            i = i + 1
        else: 
            arr[k] = arr2[j]
            k = k + 1
            j = j + 1

    while i < len(arr1): 
        arr[k] = arr1[i]
        k = k + 1
        i = i + 1
        
    while j < len(arr2): 
        arr[k] = arr2[j]
        k = k + 1
        j = j + 1

arr = [int(x) for x in input().split()]
Sort(arr)
print(*arr)