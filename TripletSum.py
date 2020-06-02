def tripletSum(arr,x): 
    mergeSort(arr)
    for i in range(len(arr)-1):  
        si = i + 1 
        pairSum(arr,x-arr[i],arr[i],si)

def pairSum(arr,x,ele,si): 
    left  = si 
    right = len(arr) - 1
    while left < right: 
        sum = arr[left] + arr[right]
        if sum < x: 
            left = left + 1
        elif sum > x: 
            right = right - 1 
        else: 
            for j in range(right,left,-1): 
                if (arr[left] + arr[j]) == x: 
                    print(ele,arr[left],arr[right])
                else: 
                    break 
            left = left + 1  

def mergeSort(arr): 
    if len(arr) == 0 or len(arr) == 1: 
        pass 
    else: 
        mid = len(arr) // 2 
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        mergeSort(arr1)
        mergeSort(arr2)
        merge(arr1,arr2,arr)

def merge(arr1, arr2, arr): 
    i = 0 
    j = 0 
    k = 0 
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] <= arr2[j]:
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


# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
tripletSum(arr, sum)
