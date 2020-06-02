def pairSum(arr, x):
    # Please add your code here
    mergeSort(arr)
    i = 0 
    j = len(arr) - 1
    k = 0 
    while i<j and i < len(arr): 
        sum = arr[i] + arr[j]
        if sum < x:
            if (i+1) < len(arr):         
                if arr[i] == arr[i+1]: 
                    j = j + k 
            i = i + 1
            k = 0 
        elif sum > x: 
            j = j - 1
            k = 0 
        else: 
            print(arr[i],arr[j])            
            if (j-1) > i : 
                k = k + 1 
                j = j - 1
            else: 
                if (i + 1) < len(arr): 
                    if arr[i] == arr[i+1]: 
                        j = j + k 
                k = 0 
                i = i + 1                                        


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
pairSum(arr, sum)
