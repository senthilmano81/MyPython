def pairsum(arr,x): 
    arr.sort()
    left  = 0 
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
                    print(arr[left],arr[right])
                else: 
                    break 
            left = left + 1 


arr = [int(x) for x in input().split()]
n   = int(input('Enter the sum:  '))
pairsum(arr,n)

b = set()
b.add(2)
print(b)
if 2 in b: 
    print('yes')
else: 
    print('No')

arr = set()
arr.add(3)
arr.add(2)
arr.add(2)
arr.add(5)
arr.add(4)
arr.add(0)
print(arr[1])
