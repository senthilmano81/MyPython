 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
# While Loop 
n = int(input())
i = 1
p = 1
while (i<=n):
    j = 1    
    while (j<=i):
        print(p,end="")
        p = p + 1
        j = j + 1
    print()
    i= i + 1
    
"""
"""
# Character Pattern + ASCII conversions
n = int(input())
i = 1 

while(i<=n): 
    p = ord('A')
    j = 1
    while (j<=n): 
        print(chr(p+j-1),end='')
        j = j + 1
    print()
    i = i + 1
"""
"""
# Character Pattern + ASCII conversions
n = int(input())
i = 1 
k = ord('A')
while(i<=n): 
    p = k + i - 1   
    j = 1
    while (j<=n): 
        print(chr(p+j-1),end='')
        j = j + 1
    print()
    i = i + 1
"""

def func(arr,*args): 
    arr.append(args)
    return arr[-1] 

arr = []
a,b=func(arr,1,2)
a,b=func(arr,1,3)
a,b=func(arr,2,1)
a,b=func(arr,2,3)
print(a,b)
print(arr[0][1])
print(*arr)









  