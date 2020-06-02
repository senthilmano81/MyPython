# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Sun Jul 21 09:32:28 2019)---
python3
python
print("HelloWorld")
print('HelloWorld')
print(HelloWorld)
if False and True or False: 
    print("in IF")
else: 
    print("in Else")
if True and False or True: 
    print("in IF")
else: 
    print("in Else")
if True or True:
    if False and True or False: 
        print("A")
    elif False and False or True and True: 
        print("B")
    else: 
        print("C")
else: 
    print("D")
if True and False or True and True: 
    print("in IF")
else: 
    print("in ELSE")
n = int(input())
i = 2 
flag = False 
while (i<n): 
    if (n%i == 0 ): 
        flag = True
    i = i + 1

if flag: 
    print("not prime")
else: 
    print("prime")
"""
n = int(input())
i = 2 
flag = False 
while (i<n): 
    if (n%i == 0 ): 
        flag = True
    i = i + 1

if flag: 
    print("not prime")
else: 
    print("prime")
n = int(input())
i = 2 
flag = False 
while (i<n): 
    if (n%i == 0 ): 
        flag = True
    i = i + 1

if flag: 
    print("not prime")
else: 
    print("prime")
n = int(input())
i = 2 
flag = False 
while (i<n and not flag): 
    if (n%i == 0 ): 
        flag = True
    i = i + 1

if flag: 
    print("not prime")
else: 
    print("prime")
n = int(input())
i = 2 
flag = False 
while (i<n and not flag): 
    print(i)
    if (n%i == 0 ): 
        flag = True
    i = i + 1

if flag: 
    print("not prime")
else: 
    print("prime")
s = int(input())
e = int(input())
w = int(input())

f = s 
while(f<=e):
    c = (f-32)*5/9
    print(f+'\t'+c)
    F = F + W
s = int(input())
e = int(input())
w = int(input())

f = s 
while(f<=e):
    c = (f-32)*5/9
    print(f+'\t'+c)
    f = f + w
s = int(input())
e = int(input())
w = int(input())

f = s 
while(f<=e):
    c = (f-32)*5/9
    print(f '\t' c)
    f = f + w
s = int(input())
e = int(input())
w = int(input())

f = s 
while(f<=e):
    c = (f-32)*5/9
    print(f, '\t', c)
    f = f + w
s = int(input())
e = int(input())
w = int(input())

f = s 
while(f<=e):
    c = (f-32)*5//9
    print(f, '\t', c)
    f = f + w
flag = True
while flag: 
   c = int(input())
   a = int(input())
   b = int(input())
   if (c == 1): 
        out = a + b
        flag = False 
    elif (c == 2): 
        out = a - b
        flag = False 
    elif (c == 3): 
        out = a * b
        flag = False 
    elif (c == 4):
        out = a // b 
        flag = False 
    elif (c == 5):
        out = a % b
        flag = False 
    elif (c == 6): 
        flag = False
    else: 
        print("Invalid Operation")


if (c != 6):
    print(out)
flag = True
while flag: 
   c = int(input())
   a = int(input())
   b = int(input())
   if (c == 1): 
        out = a + b
        flag = False 
   elif (c == 2): 
        out = a - b
        flag = False 
   elif (c == 3): 
        out = a * b
        flag = False 
   elif (c == 4):
        out = a // b 
        flag = False 
   elif (c == 5):
        out = a % b
        flag = False 
   elif (c == 6): 
        flag = False
   else: 
        print("Invalid Operation")


if (c != 6):
    print(out)
6
7
u
8
7
flag = True
while flag: 
   operation = int(input())
   a = int(input())
   b = int(input())
   if (operation == 1): 
        print(a + b)        
   elif (operation == 2): 
        print(a - b)
   elif (operation == 3): 
        print(a * b)    
   elif (operation == 4):
        print(a // b)         
   elif (operation == 5):
        print(a % b)        
   elif (operation == 6): 
        flag = False
   else: 
        print("Invalid Operation")
flag = True
while flag: 
   operation = int(input())
   a = int(input())
   b = int(input())
   if (operation == 1): 
        print(a + b)        
   elif (operation == 2): 
        print(a - b)
   elif (operation == 3): 
        print(a * b)    
   elif (operation == 4):
        print(a // b)         
   elif (operation == 5):
        print(a % b)        
   elif (operation == 6): 
        print("value is 6")
        flag = False
   else: 
        print("Invalid Operation")
flag = True
while flag: 
   operation = int(input())
   if (operation >=1 and operation <= 5):
       a = int(input())
       b = int(input())
   if (operation == 1): 
        print(a + b)        
   elif (operation == 2): 
        print(a - b)
   elif (operation == 3): 
        print(a * b)    
   elif (operation == 4):
        print(a // b)         
   elif (operation == 5):       
        print(a % b)        
   elif (operation == 6):         
        flag = False
   else: 
        print("Invalid Operation")
def reverse(n):

#Implement Your Code Here
	print(len(n))

n=int(input())
result = reverse(n)
print(result)
def reverse(n):

#Implement Your Code Here
	print(len(str(n)))

n=int(input())
result = reverse(n)
print(result)
def reverse(n):

#Implement Your Code Here
   flag = True 
   nlen = len(str(n)) - 1
   s = 0 
   while flag: 
       r = n % 10
       n = n // 10 
       s= s + r * (10**nlen) 
       print("s = " + str(s))
       nlen = nlen - 1 
       if (nlen < 0 ):
           flag = False

n=int(input())
result = reverse(n)
print(result)
def reverse(n):

#Implement Your Code Here
   flag = True 
   nlen = len(str(n)) - 1
   s = 0 
   while flag: 
       r = n % 10
       n = n // 10 
       s= s + r * (10**nlen) 
       print("s = " + str(s))
       nlen = nlen - 1 
       if (nlen < 0 ):
           flag = False
   return s

n=int(input())
result = reverse(n)
print(result)
1980
def reverse(n):

#Implement Your Code Here
   flag = True 
   nlen = len(str(n)) - 1
   s = 0 
   while flag: 
       r = n % 10
       n = n // 10 
       s= s + r * (10**nlen) 
       print("s = " + str(s))
       nlen = nlen - 1 
       if (nlen < 0 ):
           flag = False
   return s

n=int(input())
result = reverse(n)
print(result)
def reverse(n):

#Implement Your Code Here
   flag = True 
   nlen = len(str(n)) - 1
   s = 0 
   while flag: 
       s= s + (n%10) * (10**nlen) 
       n = n // 10        
       nlen = nlen - 1 
       if (nlen < 0 ):
           flag = False
   return s

n=int(input())
result = reverse(n)
print(result)
def reverse(n):

#Implement Your Code Here
   nlen = len(str(n)) - 1
   s = 0 
   while True: 
       s= s + (n%10) * (10**nlen) 
       n = n // 10        
       nlen = nlen - 1 
       if (nlen < 0 ):
           break
   return s

n=int(input())
result = reverse(n)
print(result)
ef reverse(n):
#Implement Your Code Here
   s = 0    
   while n > 0: 
       s= s*10 + (n%10)
       n = n // 10               
   return s

n=int(input())
result = reverse(n)
print(result)
def reverse(n):

#Implement Your Code Here
   s = 0    
   while n > 0: 
       s= s*10 + (n%10)
       n = n // 10               
   return s

n=int(input())
result = reverse(n)
print(result)
num = int(input())
oddsum = 0 
evensum = 0 
while (num > 0):
    digit  = num % 10 
    if (digit % 2 == 0): 
        evensum = evensum + digit 
    else: 
        oddsum = oddsum + digit 
    num = num // 10


print(evensum,' ',oddsum)
a = 0 
b = 1 
i = 2
print(a)
print(b)
while (i <=10):
    a = a + b
    print(a) 
    b = b + a
    print(b)
    i = i + 2
n = int(input())
a = 0 
b = 1 
if (n==1): 
    print(b)
else: 
    i = 2 
    while(i <= n): 
        c = b 
        b = a + b 
        a = c 
        print(b)
        i = i + 1
n = int(input())
a = 0 
b = 1 
print(b)
i = 2 
while(i <= n): 
    c = b 
    b = a + b 
    a = c 
    print(b)
    i = i + 1
n = int(input())
a = 0 
b = 1 
i = 2 
while(i <= n): 
    c = b 
    b = a + b 
    a = c 
    i = i + 1


print(b)
n = int(input())
i = 1
while (i<=n):
    j = 1
    while (j<=n):
        print('*')
        j = j + 1
    i= i + 1
n = int(input())
i = 1
while (i<=n):
    j = 1
    while (j<=n):
        print('*',end="")
        j = j + 1
    print()
    i= i + 1
n = int(input())
i = 1
while (i<=n):
    j = 1
    while (j<=n):
        print(i,end="")
        j = j + 1
    print()
    i= i + 1
n = int(input())
i = 1
while (i<=n):
    j = 1
    while (j<=n):
        print(j,end="")
        j = j + 1
    print()
    i= i + 1
n = int(input())
i = 1
while (i<=n):
    j = n
    while (j>=1):
        print(j,end="")
        j = j - 1
    print()
    i= i + 1
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input())
i = 1
while (i<=n):
    j = 1
    p = i
    while (j<=n):
        print(p,end="")
        p = p + 1
        j = j + 1
    print()
    i= i + 1
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input())
i = 1
while (i<=n):
    j = 1
    p = i
    while (j<=i):
        print(p,end="")
        p = p + 1
        j = j + 1
    print()
    i= i + 1
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input())
i = 1
while (i<=n):
    j = 1
    
    while (j<=i):
        print(j,end="")
        
        j = j + 1
    print()
    i= i + 1
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input())
i = 1
while (i<=n):
    j = 1
    p = i
    while (j<=i):
        print(p,end="")
        p = p + 1
        j = j + 1
    print()
    i= i + 1
"""
Spyder Editor

This is a temporary script file.
"""
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
n = int(input())
i = 1 

while(i<=n): 
    p = ord('A')
    j = 1
    while (j<=n): 
        print(chr(p+j-1),end='')
    i = i + 1
n = int(input())
i = 1 

while(i<=n): 
    p = ord('A')
    j = 1
    while (j<=n): 
        print(chr(p+j-1),end='')
        j = j + 1
    i = i + 1
while(i<=n): 
    p = ord('A')
    j = 1
    while (j<=n): 
        print(chr(p+j-1),end='')
        j = j + 1
    print()
    i = i + 1
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

""""
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

## ---(Fri Jul 26 03:15:30 2019)---
n = ()int(input()) // 2) + 1
i = 1 
# increasing pattern
while(i<=n): 
    #spaces
    spaces = 1 
    while(spaces <= (2*i - 3)): 
        print(' ',end='')
        spaces = spaces + 1
    #stars 
    stars = 1 
    while(stars <= i): 
        print('* ',end='')
        stars = stars + 1
    print()
    i = i + 1
n = (int(input()) // 2) + 1
i = 1 
# increasing pattern
while(i<=n): 
    #spaces
    spaces = 1 
    while(spaces <= (2*i - 3)): 
        print(' ',end='')
        spaces = spaces + 1
    #stars 
    stars = 1 
    while(stars <= i): 
        print('* ',end='')
        stars = stars + 1
    print()
    i = i + 1
def print_arrow(i): 
    spaces = 1 
    while(spaces <= (2*i - 3)): 
        print(' ',end='')
        spaces = spaces + 1
    #stars 
    stars = 1 
    while(stars <= i): 
        print('* ',end='')
        stars = stars + 1



n = (int(input()) // 2) + 1
i = 1 
# increasing pattern
while(i<=n): 
    print_arrow(i)
    print()
    i = i + 1
n = int(input())
k = (n // 2) + 1
for i in range(1,k+1): 
    for j in range(1,k-i+1): 
        print(' ',end='')
    for j in range(1,i+1): 
        print(' ',end='')
    print()
n = int(input())
k = (n // 2) + 1
for i in range(1,k+1): 
    for j in range(1,k-i+1): 
        print(' ',end='')
    for j in range(1,i+1): 
        print('*',end='')
    print()
n = int(input())
k = (n // 2) + 1
for i in range(1,k+1): 
    for j in range(1,k-i+1): 
        print(' ',end='')
    for j in range(1,2*i): 
        print('*',end='')
    print()
def print_star(i): 
    for j in range(1,k-i+1): 
        print(' ',end='')
    for j in range(1,2*i): 
        print('*',end='')
    print()



n = int(input())
k = (n // 2) + 1
for i in range(1,k+1): 
    print_star(i)

for i in range(k-1,0,-1): 
    print_star(i)
a = 1 > 2?"yes":"no"

## ---(Mon Jul 29 08:38:52 2019)---
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
""""
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


""""
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

""""
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
""""
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


""""
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

""""



a = 1

## ---(Wed Jul 31 09:29:08 2019)---
runfile('C:/Users/GGR0/.spyder-py3/temp.py', wdir='C:/Users/GGR0/.spyder-py3')
a
print(a)
runfile('C:/Users/GGR0/.spyder-py3/temp.py', wdir='C:/Users/GGR0/.spyder-py3')

## ---(Tue Aug  6 14:04:15 2019)---
a = 2 ^ 4
print(a)
a = -(2 ^ 4
print(a)
a = -(2 ^ 4)
print(a)
a = -(2 ** 4)
print(a)
arr = [0, 1, 2, 0, 2, 0, 1]
for i in range(len(arr)): 
    if arr[i] == 0: 
        arr.pop(i)
        arr.insert(0,0)
    elif arr[i] == 2: 
        arr.pop(i)
        arr.append(2)

print(*arr)
arr = [0, 1, 2, 0, 2, 0, 1]
i = 0 
count2 = 0
length = len(arr)
while i < length: 
    if arr[i] == 0: 
        arr.pop(i)
        arr.insert(0,0)
        i = i + 1
    elif arr[i] == 2: 
        arr.pop(i)
        arr.append(2)
        length = length - 1 
    elif arr[i] == 1: 
        i = i + 1


print(*arr)
arr = [0, 1, 2, 0, 2, 0, 1]
i = 0 
count2 = 0
length = len(arr)
while i < length: 
    if arr[i] == 0: 
        arr.pop(i)
        arr.insert(0,0)
    elif arr[i] == 2: 
        arr.pop(i)
        arr.append(2)
        length = length - 1 
        Continue  
    i = i + 1 

print(*arr)
arr = [0, 1, 2, 0, 2, 0, 1]
print(arr.remove(0))        
print(arr.remove(0))
print(arr.remove(0))
print(arr.remove(0))

## ---(Tue Aug 13 10:29:32 2019)---
Str1 = "Senthil"
Str1[3] = 'z'
print(Str1)
a = ['senthil', 'eswari', 'baargavi]
print(a)
b = *a
print(b)
a = ['senthil', 'eswari', 'baargavi']
print(a)
b = *a
print(b)
a = ['senthil', 'eswari', 'baargavi']
print(a)
b = a[0]*3
print(b)
a = ['senthil', 'eswari', 'baargavi']
print(a)
b = a[0]*3
print(b)
b = b/3
print(b)

## ---(Mon Aug 26 00:42:58 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/LearnClass.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Temp.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Class2.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Temp.py', wdir='C:/Data Backup/E Drive/Learning/Python')
"""
Created on Mon Aug 26 10:34:42 2019

@author: GGR0
"""

class Circle:
    def __init__(self,radius): 
        self.radius = radius


c = Circle()
print(c)
"""
Created on Mon Aug 26 10:34:42 2019

@author: GGR0
"""

class Circle:
    def __init__(self,radius): 
        self.radius = radius


c = Circle(4)
print(c)
"""
Created on Mon Aug 26 10:34:42 2019

@author: GGR0
"""

class Circle:
    def __init__(self,radius): 
        self.radius = radius


class Square: 
    def __init__(self,side): 
        self.side = side 
    def __str__(self): 
        return "This is a Square Class" 


c = Circle(4)
print(c)

s = Square(4)
print(s)
runfile('C:/Data Backup/E Drive/Learning/Python/MultipleInheritance.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/MultipleInheritance1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/OperatorOverloading.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/abstractclass.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/classmethod.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/abstractclass.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/ExceptionHandling.py', wdir='C:/Data Backup/E Drive/Learning/Python')
5
2
runfile('C:/Data Backup/E Drive/Learning/Python/ExceptionHandling.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/MergeSort.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/intersection.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Binary Search.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/intersection.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/FindUnique.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Binary Search.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/FindUnique.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Mon Sep  2 23:48:50 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/FindUnique.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/FindUnique1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/FindUnique2.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/FindDuplicate.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/CodePair.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Tue Sep  3 02:07:44 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/CodePair.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/FindUnique2.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/CodePair.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/TripletSum.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/LinkedList1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/samplenode.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/InsertLL - Iterative.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/DeleteNode - Recursion.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/LinearSearchLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/RotateLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/RemoveDuplicatesfromSortedLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/printReverseLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/checkPallindromeLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/createLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/checkPallindromeLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Temp.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/checkPallindromeLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/createLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Baargavi.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/ReverseLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Fri Sep  6 04:09:29 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/checkPallindromeLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/OddEvenLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/DeleteNNodesLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/SwapNodes.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/kreversell.txt', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/kreversell.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/bubbleSortLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Mon Sep  9 14:10:54 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/pairsum1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/TripletSum.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Tue Sep 10 10:51:08 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/bubbleSortLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
debugfile('C:/Data Backup/E Drive/Learning/Python/bubbleSortLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/array.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/arraystack.py', wdir='C:/Data Backup/E Drive/Learning/Python')
debugfile('C:/Data Backup/E Drive/Learning/Python/bubbleSortLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/arraystack.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/reverseStackLL.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Wed Sep 11 10:41:51 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/checkredundantbraces.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Users/GGR0/.spyder-py3/temp.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/stockspan.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/QueueUsingTwoStacks.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/InbuiltQueue.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/StackUsingTwoQueues.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/InbuiltQueue.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/StackUsingTwoQueues.py', wdir='C:/Users/GGR0/.spyder-py3')

## ---(Thu Sep 12 19:31:38 2019)---
runfile('C:/Users/GGR0/.spyder-py3/StackUsingTwoQueues.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/ReverseFirstKelements.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/printBinaryTree.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/binaryTreeLevelwiseInput.py', wdir='C:/Users/GGR0/.spyder-py3')
max(1,2) 
runfile('C:/Users/GGR0/.spyder-py3/PrintwithoutSibling.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Users/GGR0/.spyder-py3/ReverseFirstKelements.py', wdir='C:/Users/GGR0/.spyder-py3')
runfile('C:/Data Backup/E Drive/Learning/Python/NodesatDepthK.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Fri Sep 13 16:56:55 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/NodesatDepthK.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/CountNodesGreaterThanX.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Wed Sep 18 19:21:22 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/CheckBalanced.py', wdir='C:/Data Backup/E Drive/Learning/Python')
print(abs(1))
print(abs(-1))
runfile('C:/Data Backup/E Drive/Learning/Python/CheckBalanced1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/CheckBalanced1.py', wdir='C:/Data Backup/E Drive/Learning/Py
runfile('C:/Data Backup/E Drive/Learning/Python/CheckBalanced1.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Sat Sep 21 07:05:14 2019)---
arr = [1,2,3,4,5]
print(len(arr))
runfile('C:/Data Backup/E Drive/Learning/Python/ConstructBTusingPreandInorder.py', wdir='C:/Data Backup/E Drive/Learning/Python')
arr = [1, 2, 3, 4, 5]
idx = arr.index(6)
print(idx)
arr = [1, 2, 3, 4, 5]
idx = arr.index(3)
print(idx)
arr = [1, 2, 3, 4, 5]
idx = arr.index(1)
print(idx)
runfile('C:/Data Backup/E Drive/Learning/Python/ConstructBTusingPreandInorder.py', wdir='C:/Data Backup/E Drive/Learning/Python')

idx = arr.index(3)
print(idx)


runfile('C:/Data Backup/E Drive/Learning/Python/ConstructBTusingPreandInorder.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Sat Sep 21 08:33:54 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/ConstructBTusingPreandInorder.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/BuildBTFromPostOrder.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Sun Sep 22 05:04:36 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/InsertDuplicateNode.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/LeverOrderTraversal.py', wdir='C:/Data Backup/E Drive/Learning/Python')
a= queue.Queue()
a.put((1,2))
print(a.get())
a= queue.Queue()
a.put((BinaryTreeNode(1),2))
(curr,level) = a.get()
print('curr:',curr.data)
print(level)
runfile('C:/Data Backup/E Drive/Learning/Python/LeverOrderTraversal.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/test.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/PathSumToLeaf.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/printNodesatDistanceK.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/TopView.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/printNodesatDistanceK.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/SumOfDigits.py', wdir='C:/Data Backup/E Drive/Learning/Python')
a = 2 ** 4
print(a)
runfile('C:/Data Backup/E Drive/Learning/Python/SumOfDigits.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/ElementsbetweenK1K2BST.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/untitled8.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/FindPathBST.py', wdir='C:/Data Backup/E Drive/Learning/Python')
print(*path)
for ele in path[-1:-1]: 
    print(ele)
for ele in path[-1:]: 
    print(ele)
print(path[-1:])
print(path[-1:-3])
print(path[-1:-2])
print(path[-1::-1])
runfile('C:/Data Backup/E Drive/Learning/Python/untitled8.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/BSTClass.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Sat Oct  5 08:46:59 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/GenericTree.py', wdir='C:/Data Backup/E Drive/Learning/Python')
min(1,2)
runfile('C:/Data Backup/E Drive/Learning/Python/maxNodeGT.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Pytho
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
1
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
1
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
1
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
1
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
1
2
122
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
2
1
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
3
333
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Saswanth1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/printLevelWiseGT.py', wdir='C:/Data Backup/E Drive/Learning/Python')
a = True
b = False 
print(a&b)
a = False
b = False 
print(a&b)
a = True
b = False 
print(a&b)
a = False
b = True 
print(a&b)
a = True
b = True 
print(a&b)
a = False 
b = True 
print(a|b)
a = True
b = True 
print(a|b)
a = True
b = False 
print(a|b)
a = False
b = False 
print(a|b)
a = 1 
b = 2
print(a!=b)
runfile('C:/Data Backup/E Drive/Learning/Python/isIdenticalGT.py', wdir='C:/Data Backup/E Drive/Learning/Python')
d = {1:2, “abc”:5, “def”:7}
print(d[0])
d = {1:2, 'abc':5, 'def':7}
print(d[0])
d = {1:2, 'abc':5, 'def':7}
print(d[1])
d = {1:2, 'abc':5, 'def':7}
print(d['abc'])
d = {1:2, 'abc':5, 'def':7}
print(d[0])
d = {1:2, 'abc':5, 'def':7}
print(d.get(0,5))
d = {1:2, 'abc':5, 'def':7}
if 2 in d:
    print(‘Present’)
else:
    print(‘Not Present’)
d = {1:2, 'abc':5, 'def':7}
if 2 in d:
    print('Present')
else:
    print('Not Present')

## ---(Wed Oct  9 00:10:37 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/Dict_MaxFreq.py', wdir='C:/Data Backup/E Drive/Learning/Python')
b = {}
b.add(2)
print(b)
b = set()
b.add(2)
print(b)
b = set()
b.add(2)
print(b)
if 2 in b: 
    print('yes')
else: 
    print('No')
str1= 'string1'
str2 = 'string2'
print(str1+str2)
str1= 'string1'
str2 = 'string2' 
str1 = str1+str2
print(str1)
str1= 'string1'
str2 = 'string2' 
str1 = str1||str2
print(str1)
arr = [1,2,3,4,5]
print(*arr)
arr.clear()
print(*arr)
arr = set()
arr.add(2)
arr.add(3)
arr.add(2)
arr = set()
arr.add(2)
arr.add(3)
arr.add(2)
print(arr)
arr = set()
arr.add(3)
arr.add(2)
arr.add(2)
print(arr)
arr = set()
arr.add(3)
arr.add(2)
arr.add(2)
for ele in arr: 
    print(ele)
arr = set()
arr.add(3)
arr.add(2)
arr.add(2)
arr.add(5)
arr.add(4)
arr.add(0)
print(arr[1:3])
print(arr[1])
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
map = dict.fromkeys(l,0)
runfile('C:/Data Backup/E Drive/Learning/Python/LongestConsecutiveSequence.py', wdir='C:/Data Backup/E Drive/Learning/Python')
l=list(int(i) for i in input().strip().split(' '))
map = dict.fromkeys(l,0)
print(map)
map.clear()
print(map)
runfile('C:/Data Backup/E Drive/Learning/Python/LongestConsecutiveSequence.py', wdir='C:/Data Backup/E Drive/Learning/Python')
arr = [4,4,4,4]
map = dict.fromkeys(arr)
print(map)
runfile('C:/Data Backup/E Drive/Learning/Python/PairwithDifferenceK.py', wdir='C:/Data Backup/E Drive/Learning/Python')
arr = [1,2,3,4,5]
for i in arr: 
    if i == 2: 
        continue
    print(i)
runfile('C:/Data Backup/E Drive/Learning/Python/PairwithDifferenceK.py', wdir='C:/Data Backup/E Drive/Learning/Python')
k = -1
print(abs(k))
runfile('C:/Data Backup/E Drive/Learning/Python/PairwithDifferenceK.py', wdir='C:/Data Backup/E Drive/Learning/Python')
map = {}
print(map[1])
runfile('C:/Data Backup/E Drive/Learning/Python/Test53.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Fri Oct 11 15:11:35 2019)---
map = {}
print(map[1])
runfile('C:/Data Backup/E Drive/Learning/Python/SubsetSum.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Tue Oct 15 14:14:02 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/Graph.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/Graph_DFS.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Tue Oct 15 17:07:04 2019)---
a, b = input().split()
print(a,b)
a = input().split()
print(a)
runfile('C:/Data Backup/E Drive/Learning/Python/Graph_BFS.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/GraphHasPath.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/GraphGetPath_BFS.py', wdir='C:/Data Backup/E Drive/Learning/Python')
arr1 = [1,2,3]
arr2 = arr1
arr2.append(5)
print(arr1)
runfile('C:/Data Backup/E Drive/Learning/Python/GraphGetPath_BFS.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Wed Oct 16 15:30:25 2019)---
runfile('C:/Users/GGR0/Test12.py', wdir='C:/Users/GGR0')
arr = [5,4,3,2,1]
arr.sort()
print(*arr)
arr = [5,4,3,2,1]
print(*arr.sort())
i=1
while i<3:
    j=0
    while j<5:
        j = j +1
        if j==3:
            continue
        print(j,end=” “)
    i = i +1
i=1
while i<3:
    j=0
    while j<5:
        j = j +1
        if j==3:
            continue
        print(j,end=' ')
    i = i +1
runfile('C:/Users/GGR0/EvenFibonacci.py', wdir='C:/Users/GGR0')
s = 'abcd'
s.upper()
print(s)
s = 'abcd'
print(len(s))
s = input()
slen = len(s) // 2 
s1   = s[:slen+1]
s2   = s[-1:-1*slen-1:-1]
if s1 == s2: 
    print('true')
else: 
    print('false')
s = input()
slen = len(s) // 2 
s1   = s[:slen+1]
print('s1=',s1)

s2   = s[-1:-1*slen-1:-1]
print('s2=',s2)
if s1 == s2: 
    print('true')
else: 
    print('false')
s = input()
slen = len(s) // 2 
s1   = s[:slen]
print('s1=',s1)

s2   = s[-1:-1*slen-1:-1]
print('s2=',s2)
if s1 == s2: 
    print('true')
else: 
    print('false')
instr = input()
for i in range(len(instr)): 
    for j in range(i,len(instr)): 
        print(s[i:j+1])
instr = input()
for i in range(len(instr)): 
    for j in range(i,len(instr)): 
        print(instr[i:j+1])
list1 = list()
list1 = list()
print(list)
list1 = list()
list1.append(1)
print(list)
list1 = list()
list1.append(1)
print(list1)
list1 = list()
print(list1)
list1 = list([1,2,3])
print(list1)
A = [[0, 10, 20],
       [30, 40, 50],
       [60, 70, 80]]

print(A[0:2][0])
a = [10,23,56,[78]]
b = list(a)
a[3][0] = 95
a[1] = 34
print(b)
points = [[1, 2], [3, 1.5], [0.5,7]]
points.sort()
print(points)
points = [[1, 2], [3, 1.5], [0.5,7]]
print(len(points))
dic = dict()
print(dic)
arr = [1,2,3,4,5,0]
print(any(i==0 for i in arr))
arr = [1,2,3,4,5]
print(any(i==0 for i in arr))
arr = [1,2,3,4,5]
print(all(i>0 for i in arr))
arr = [1,2,3,4,5,0]
print(all(i>0 for i in arr))
runfile('C:/Users/GGR0/MaximiseSum.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/MaximiseSum1.py', wdir='C:/Users/GGR0')
n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]

inter = set(arr1).intersection(arr2)
inter = list(inter)
print(inter)
runfile('C:/Users/GGR0/MaximiseSum1.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/MaximiseSum.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/Fibo_Recursion.py', wdir='C:/Users/GGR0')
n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]

inter = set(arr1).intersection(arr2)
inter = list(inter)
print(inter)`
runfile('C:/Users/GGR0/Fibo_Recursion.py', wdir='C:/Users/GGR0')
a = 1,2
b= (4,5)
d = a + b
print(d)
arr = []
if arr: 
    print('true')
else: 
    print('false')
arr1  = [5,7,6]
arr2  = [6,7,5]
if set(arr1) == set(arr2): 
    print('true')
else: 
    print('false')
class Student:
    def __init__(self,name,age):
        self.name = “Rohan”
        self.age = 20
    
    def print_student_details():
        print(self.name, end= “ “)
        print(self.age)

s = Student(“Parikh”,25)
s.print_student_details()
class Student:
    def __init__(self,name,age):
        self.name = 'Rohan'
        self.age = 20
    
    def print_student_details():
        print(self.name, end= ' ')
        print(self.age)

s = Student('Parikh',25)
s.print_student_details()

## ---(Fri Oct 18 11:30:18 2019)---
v,e  = input().split()
print(v)
print(e)
v,e  = (x for x in input().split())
print(v)
print(e)
v,e  = (int(x) for x in input().split())
print(v)
print(e)
print(v*e)
v,e  = input().split()
print(v)
print(e)


def mergeSort(arr): 
    if len(arr) == 1 or len(arr) ==0: 
        return arr 
    mid  = len(arr) // 2 
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    mergeSort(arr1)
    mergeSort(arr2)
    merge(arr,arr1,arr2)


def merge(arr,arr1,arr2): 
    
    i = 0 
    j = 0 
    k = 0 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            k = k + 1
            arr[k] = arr1[i]
            i = i + 1
        else: 
            k = k + 1
            arr[k] = arr2[j]
            j = j + 1
    
    while i < len(arr1): 
        k = k + 1
        arr[k] = arr1[i]
        i = i + 1
    
    while j < len(arr2): 
        k = k + 1
        arr[k] = arr2[j]
        j = j + 1


arr = [int(x) for x in input().split()]
mergeSort(arr)
print(*arr)
runfile('C:/Users/GGR0/mergeSort.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/EdgeSort.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/Kruskal\'s Algorithm.py', wdir='C:/Users/GGR0/Kruskal')
runfile('C:/Users/GGR0/Kruskal.py', wdir='C:/Users/GGR0')
arr = [0,1,2,3,5,-1]
print(min(arr))
arr = [1,2,3,4,5]
dic = dict.fromkeys(arr,0)
print(dic)
runfile('C:/Users/GGR0/PrimAlgorithm.py', wdir='C:/Users/GGR0')
print('Enter the marks of the Student')
marks = int(input())
runfile('C:/Users/GGR0/Grader.py', wdir='C:/Users/GGR0')
square = lambda a: a + 2
print(square(5))
square = lambda a: a ** 2
print(square(5))
square = lambda a: a ** 0.5
print(square(2))
runfile('C:/Users/GGR0/PrimAlgorithm.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/prim1.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/Lambda.Sort.py', wdir='C:/Users/GGR0')
runfile('C:/Users/GGR0/Dijkstra.py', wdir='C:/Users/GGR0')
4
runfile('C:/Users/GGR0/Dijkstra.py', wdir='C:/Users/GGR0')
arr = OrderedDict([('year',2017),('Age',28)])
arr = Dict([('year',2017),('Age',28)])
arr = [('year',2017),('Age',28)]
arr = [('year',2017),('Age',28)]
arr['year']
arr = [('year',2017),('Age',28)]
print(dict(arr))
def func1(a,*more): 
    print('a=',a)
    print('more=',more)


func1(1,2,3,4,5,6)
str1 = 'Senthil Manoharan'
if 'Mano' in str1: 
    print('true')
else: 
    print('false' )
a = 'Senthil Manoharan'
print(a.upper())
a = 'Senthil Manoharan'
a.upper()
print(a)
li = ['Jan','Feb','Mar']
dic = dict.fromkeys(li,0)
print(dic)
arr1 = [1,2,3,4,5]
print(max(arr1))
dic = {'January':907,'February':790,'March':13}
max_value = max(dic,key=lambda month:dic[month])
print(max_value)
dic = {'January':907,'February':790,'March':9913}
max_value = max(dic,key=lambda month:dic[month])
print(max_value,dic[max_value])
runfile('C:/Users/GGR0/LinkedList.py', wdir='C:/Users/GGR0')

## ---(Fri Nov  1 18:16:39 2019)---
qual = 'BS in India for Java'
if 'BS' in qual: 
    print('yes')
qual = 'BS in India for Java'
if 'Java' in qual: 
    print('yes')
lang = 'Java program for developers'
if 'developer' in lang: 
    print('yes')
else: 
    print('no')
lang = 'Java program for developers'
if 'senthil' not in lang: 
    print('yes')
else: 
    print('no')
lang = 'Java program for developers'
if 'deve' not in lang: 
    print('yes')
else: 
    print('no')
ing = ['IN,KA,Bangalore','US,CA,Los Angeles']
country = ing[0].split(',')[0]
print(country)

## ---(Mon Nov  4 03:51:06 2019)---
arr = [1,2,3,4]
print(arr.pop())
print(arr)
runfile('C:/Users/GGR0/PriorityQueue.py', wdir='C:/Users/GGR0')

## ---(Wed Nov  6 18:39:31 2019)---
import numpy as np
a = [1,2,3,4,5]
b = np.array(a)
print(b)
import numpy as np
a = [1,2,3,4,5]
b = np.array(a)
print(a)
print(b)
import numpy as np
a = [1,2,3,4,5]
b = np.array(a)
print(a)
print(*b)
import numpy as np
a = [1,2,3,4,5]
b = np.array(a,dtype=float)
print(a)
print(b)
import numpy as np
a = [1,2,3.4,4,5]
b = np.array(a,dtype=float)
print(a)
print(b)
import numpy as np
a = [1,2,3.4,4,5]
b = np.array(a,dtype=int)
print(a)
print(b)
import numpy as np
a = [1,2,3.4,4,5]
b = np.array(a)
print(a)
print(b)
import numpy as np
a = [1,2,3.4,'a',5]
b = np.array(a)
print(a)
print(b)
a = 'hi'
print(a*3)
import numpy as np
a = [1,2,3.4,'a',5]
print(a*3)
b = np.array(a)
print(a)
print(b)
print(np.ones(5))
print(np.zeros(6))
print(np.empty(7))
print(np.full(5))
print(np.full(5,'a'))
a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
b.append([10,11,12])
a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
b[2][2] = 10 
print(b)
print(np.ones(5))
print(np.zeros(6))
print(np.empty(7))
print(np.full(5,'a'))

a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
b[2][2] = 10 
print(b)

## ---(Wed Nov 20 18:42:33 2019)---
print(np.full(5,'a'))
import numpy as np
print(np.full(5,'a'))
print(np.full(3,5))
print(np.full((3,3),5))
print(np.linspace(2,10,5))
print(np.linspace(2,14,5))
print(np.linspace(2,14,5,dtype=int))
print(np.linspace(2,14,5,dtype=int,endpoint=False))
print(np.identity())
print(np.identity(3))
print(np.identity(3),dtype=int)
print(np.identity(3))
print(np.eye(3))
a=np.array([0,1,2,3])
a.shape
a=np.array([0,1,2,3],[4,5,6,7])
a.shape
a=np.array([[0,1,2,3],[4,5,6,7]])
a.shape
print(a)
print(np.random.rand(10,4))
print(np.random.randint(10,4))
print(np.random.randint(4,10))
a = np.linspace(0,5,9)
for i in a: 
    print(i)
a = np.linspace(0,5,9)
for i in a: 
    print("(0:.2f)",format(i))
a = np.linspace(0,5,9)
for i in a: 
    print("(0:.2f)".format(i))
a = np.linspace(0,5,9)
for i in a: 
    print("{0:.2f}".format(i))
a = np.linspace(0,5,8,endpoint=False)
for i in a: 
    print("{0:.2f}".format(i))
a = np.linspace(0,5,9,endpoint=False)
for i in range(1,len(a)): 
    print("{0:.2f}".format(a[i]))
input_=np.arange(1,21,1)
input_=input_.reshape(4,5)
arr1 = input_[2,:3]
arr2 = input_[1:,3]
arr3 = input_[2:,:5]
arr4 = input_[1:3,1:3]
print(*arr1)
print(*arr2)
print(*arr3)
print(*arr4)
input_=np.arange(1,21,1)
input_=input_.reshape(4,5)
arr1 = input_[2,:3]
arr2 = input_[1:,3]
arr3 = input_[2:,:5]
arr4 = input_[1:3,1:3]
print(*arr1)
print(*arr2)
for ele in arr3: 
    print(*ele)

for ele in arr4:
    print(*ele)
input_=np.arange(1,21,1)
input_=input_.reshape(4,5)
arr1 = input_[2,:3]
arr2 = input_[1:,3]
arr3 = input_[2:,:5]
arr4 = input_[1:3,1:3]
print(*arr1)
print(*arr2)
for ele in arr3: 
    print(*ele,end='')
    print(' ',end='')

print()
for ele in arr4:
    print(*ele,end='')
    print(' ',end='')

## ---(Fri Nov 22 14:27:31 2019)---
import numpy as np
a = [1,2,3.4,'a',5]
print(a*3)
b = np.array(a)
print(a)
print(b)

print(np.ones(5))
print(np.zeros(6))
print(np.empty(7))
print(np.full(5,'a'))

a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
b[2][2] = 10 
print(b)


a = np.array([1,2,3,4,5])
a = a + 1
print(a)
a = np.array([1,2,3,4,5])
a = a * 4
print(a)
import numpy as np
a = [1,2,3.4,'a',5]
print(a*3)
b = np.array(a)
print(a)
print(b)

print(np.ones(5))
print(np.zeros(6))
print(np.empty(7))
print(np.full(5,'a'))

a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
b[2][2] = 10 
print(b)


a = np.array([1,2,3,4,5])
a = a * 4
print(a)
a = [1,2,3,4,5]
a = a * 4
print(a)
a = [1,2,3,4,5]
a = a * 4
print(a)
print(max(a))
print(sum(a))
a = [1,2,3,4,5]
print(a)
print(max(a))
print(min(a))
a = [1,2,3,4,5]
print(a)
print(max(a))
print(min(a))
print(suma(a))
a = [1,2,3,4,5]
print(a)
print(max(a))
print(min(a))
print(sum(a))
a = np.array([1,2,3,4,5])
bool_ar = a > 2; 
print(bool_ar)
new_ar = a[bool_ar]
print(new_ar)
print(np.where(a>2))
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(ind)
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(**ind)
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(*ind)
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(*(*ind))
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
for ele in ind: 
    print(ind,end=' ')
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
for ele in *ind: 
    print(ind,end=' ')
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print([ind])
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(array(ind))
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
pritn(*ind)
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
b = *ind
print(b)
li = [1,2,3,4,5]
if any(li) > 0: 
    print('yes')
li = [1,2,3,4,5]
if any(li) > 5: 
    print('yes')
else: 
    print('no')
if any(li) > 4: 
    print('yes')
else: 
    print('no')
if any(li) > 3: 
    print('yes')
else: 
    print('no')
if any(li) > 1: 
    print('yes')
else: 
    print('no')
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(ind)
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(np.ind)
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(np.array(ind))
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(ind[0])
a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(*ind[0])
import numpy as np
arr1 = np.arange(1,21,2)
print(arr1)
arr1 = np.arange(1,21,2)
print(arr1)
ind = np.where(arr1%3==0)
print(ind)
arr1 = np.arange(1,21,2)
print(arr1)
ind = np.where(arr1%3==0)
print(*ind[0])
arr1 = np.arange(1,11)
arr1[arr1>=3 and arr2<=8] = -1*arr1[arr1>=3 and arr2<=8]
print(*arr1)
arr1 = np.arange(1,11)
arr1[arr1>=3 & arr2<=8] = -1*arr1
print(*arr1)
arr1 = np.arange(1,11)
arr1[arr1>=3 & arr1<=8] = -1*arr1
print(*arr1)
arr1 = np.arange(1,11)
arr1[arr1>=3 && arr1<=8] = -1*arr1
print(*arr1)
arr1 = np.arange(1,11)
arr1[arr1>=3 & arr1<=8] = -1*arr1
print(*arr1)
arr1 = np.arange(1,11)
arr1[(arr1>=3) & (arr1<=8)] = -1*arr1
print(*arr1)
arr1 = np.arange(1,11)
arr1[(arr1>=3) & (arr1<=8)] = -1*arr1[(arr1>=3) & (arr1<=8)]
print(*arr1)
arr1 = np.arange(1,11)
arr1[(arr1>=3) & (arr1<=8)] = -1*arr1[(arr1>=3) & (arr1<=8)]
print(arr1.length())
print(len(arr1))
age=np.array([15,17,19,20,14,21,16,19,13,20,22,23,21,16,18,19,20,15,17,18])
height=np.array([156,144,180,162,152,157,154,155,151,150,158,179,126,182,183,154,159,160,172,149])
ind = np.where(height>155)
ind
age=np.array([15,17,19,20,14,21,16,19,13,20,22,23,21,16,18,19,20,15,17,18])
height=np.array([156,144,180,162,152,157,154,155,151,150,158,179,126,182,183,154,159,160,172,149])
ind = np.where(height>155)

for i in range(len(ind[0])): 
    print(age[ind[0][i]],height[ind[0][i]])
a = np.array([5,4,1,3,2])
print(a.sort())
a = np.array([5,4,1,3,2])
print(a.sorted())
a = [5,4,1,3,2]
print(a.sorted())
a = [5,4,1,3,2]
print(a.sort())
a = [5,4,1,3,2]
a.sorted()
a = [5,4,1,3,2]
a.sort()
print(a)
a = np.array([5,4,1,3,2])
a.sort()
print(a)
a = np.array([5,4,1,3,2])
np.sort(a)
print(a)
a = np.array([5,4,1,3,2])
a = np.sort(a)
print(a)
a = [5,4,1,3,2]
b = a.sort()
print(b)
arr1 = np.arange(21,1,-1)
print(arr1)
arr1 = np.arange(21,1,-1)
arr1.reshape(4,5)
print(arr1)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr1 = np.arange(21,1,-1).reshape(4,5)
print(arr1)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = np.sort(arr1,1)
print(arr2)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = np.sort(arr1,:1)
print(arr2)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = np.sort(arr1,key=lambda row:row[1])
print(arr2)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = np.argsort(arr1[:,1])
print(arr2)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = np.argsort(arr1[:1])
print(arr2)
print(arr1[:,1])
print(arr1[,1])
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
print(arr1[:,1])
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = arr1[arr1[1].argsort(),:]
print(arr2)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = arr1[:,arr1[1].argsort()]
print(arr2)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = arr1[:,arr1[:,1].argsort()]
print(arr2)
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = arr1[arr1[:,1].argsort()]
print(arr2)
arr1 = np.array([[1,2],[3,4]])
print(arr1)
arr1 = np.array([[1,2],[3,4]])
print(arr1)
arr2 = np.array([8,9])
print(arr2)
arr1 = np.array([[1,2],[3,4]])
print(arr1)
arr2 = np.array([8,9])
print(arr2)
print(arr1+arr2)
arr1 = np.array([[1,2],[3,4]])
print(arr1)
arr2 = np.array([8,9,10])
print(arr2)
print(arr1+arr2)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
print(arr1.resize(3,2))
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr1.resize(2,3)
print(arr1)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr1.reshape(2,3)
print(arr1)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr2 = arr1.reshape(2,3)
print(arr2)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr2 = arr1.reshape(6,6)
print(arr2)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr1.resize(6,6)
print(arr1)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr1.resize(2,2)
print(arr1)
import numpy as np 
import csv
with open('terrorismData.csv') as file_obj: 
    file_data = csv.DictReader(file_obj, skipinitialspace=True)
    for row in file_data: 
        print(row)
runfile('C:/Data Backup/E Drive/Learning/Python/numpy_ex1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
a = 5.0
print(int(a))
runfile('C:/Data Backup/E Drive/Learning/Python/numpy_ex1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
a = np.array([1,2,3,4,5,6,7])
bool_arr = [a >=3 & a<=6]
print(bool_arr)
a = np.array([1,2,3,4,5,6,7])
bool_arr = [(a >=3) & (a<=6)]
print(bool_arr)
a = np.array([1,2,3,4,5,6,7])
bool_arr = [(a >=3) & (a<=6)]
print(bool_arr)
print(a[bool_arr])
a = np.array([1,2,3,4,5,6,7])
bool_arr = (a >=3) & (a<=6)
print(bool_arr)
print(a[bool_arr])
a = np.array([1,2,3,4,5])
b= np.array([6,7,8,9,10])
c = np.array([a, b])
print(c)
a = np.array([5,3,2,4,1])
b= np.array([10,9,7,6,8])
c = np.array([a, b])
print(c)
a = np.array([5,3,2,4,1])
b= np.array([10,9,7,6,8])
c = np.array([a, b])
a.sort()
print(a)
a = np.array([5,3,2,4,1])
b= np.array([10,9,7,6,8])
c = np.array([a, b])
a =np.sort(a)
print(a)
a = np.array([5,3,2,4,1])
b= np.array([10,9,7,6,8])
c = np.array([a, b])
ind = a.argsort()
print(ind)
a = np.array([5,3,2,4,1])
b= np.array([10,9,7,6,8])
c = np.array([a, b])
ind = a.argsort()
print(ind)
print(b[ind])
a = np.array([5,5,3,2,4,5,1])
b= np.array([10,9,7,6,8])
a.unique()
print(a)
a = np.array([5,5,3,2,4,5,1])
b= np.array([10,9,7,6,8])
print(a)
c = np.unique(a)
print(c)
a = np.array([5,5,3,2,4,5,1])
b= np.array([10,9,7,6,8])
print(a)
c = np.unique(a)
print(c)
print(np.sum(c))
a = np.array([5,5,3,2,4,5,1])
b= np.array([10,9,7,6,8])
print(a)
c = np.unique(a)
print(c)

print(c.sum())
a = np.array([5,5,3,2,4,5,1])
b= np.array([10,9,7,6,8])
print(a)
c = np.unique(a)
print(c)

print(c.argmax())
runfile('C:/Data Backup/E Drive/Learning/Python/numpy_ex1.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
file_data = pd.read_csv('C:\Data Backup\E Drive\Learning\Python\terrorismData.csv')
print(type(file_data))
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(file_data)
print(type(file_data))
a = [1,2,3]
b= a
b[1] = 5
print(a)
a = [1,2,3]
b= a*2
b[1] = 5
print(a)
a = [1,2,3]
b= a
b[1] = 5
print(a)
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
df = file_data.copy()
print(df.head())
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
print(file_data.head())
df = file_data.copy()
print(df.head())
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
print(file_data)
print(file_data.head())
df = file_data.copy()
print(df.head())
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
df = file_data.copy()
print(df.head())
print(df.shape())
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
df = file_data.copy()
print(df.head())
print(df.shape
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
df = file_data.copy()
print(df.head())
print(df.shape)
print(df.dtypes)
runfile('C:/Data Backup/E Drive/Learning/Python/pandasExample.py', wdir='C:/Data Backup/E Drive/Learning/Python')

## ---(Fri Nov 29 09:03:43 2019)---
print('Hi Priya')

## ---(Fri Nov 29 09:25:07 2019)---
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
df = file_data.copy()
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe)
import pandas as pd
file_data = pd.read_csv('C:/Data Backup/E Drive/Learning/Python/terrorismData.csv')
print(type(file_data))
df = file_data.copy()
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe())
print(df.Month == 5)
print(df.Month == 1)
print(df.Month == 0)
df(df.Month == 0)
df[df.Month == 0]
x = [int(i) for i in input().split()]
print(x)
runfile('C:/Data Backup/E Drive/Learning/Python/pandasExample.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
iris = pd.read_csv("iris.data")
df = iris.copy()
df.columns = ['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
print(df)
import pandas as pd
iris = pd.read_csv("iris.data")
df = iris.copy()
print(df)
df.columns = ['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
print(df)
runfile('C:/Data Backup/E Drive/Learning/Python/pandasExample.py', wdir='C:/Data Backup/E Drive/Learning/Python')
df.columns
import pandas as pd
iris = pd.read_csv("iris.data")
df = iris.copy()
print(df.shape)
df.columns = ['sl', 'sw', 'pl', 'pw', 'flower_type']
print(df.shape)
print(df.dtypes)
import pandas as pd
iris = pd.read_csv("iris.data")
df = iris.copy()
print(df.shape)
df.columns = ['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
print(df.shape)
print(df.dtypes)

print(df['Species'].value_counts())
runfile('C:/Data Backup/E Drive/Learning/Python/pandasExample.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()
print(df.head())
print(df.shape)

out = df['Species'].value_counts()
print(out)
runfile('C:/Data Backup/E Drive/Learning/Python/pandasExample.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()
fo ri in 
print(df.head())
print(df.shape)

out = df['Species'].value_counts()
out.columns = ['Unique Values', 'Counts']
print(out)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

out = df['Species'].value_counts()
out.columns = ['Unique Values', 'Counts']
print(out)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

out = pd.DataFrame(df['Species'].value_counts())
print(out)
runfile('C:/Data Backup/E Drive/Learning/Python/pandasExample.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

out = pd.DataFrame(df['Species'].value_counts())
out.index.name = 'Species'
out.columns = 'count'
print(out)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

out = pd.DataFrame(df['Species'].value_counts())
out.index.name = 'Species'
out.columns = ['count']
print(out)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

out = pd.DataFrame(df['Species'].value_counts())
for i in out: 
    print(i)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

out = pd.DataFrame(df['Species'].value_counts())
for i in out: 
    print(out[i])
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

out = df['Species'].value_counts().tolist()
print(out)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

keys = df['Species'].value_counts().keys().tolist()
out = df['Species'].value_counts().tolist()
print(keys)
print(out)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

keys = df['Species'].value_counts().keys().tolist()
count = df['Species'].value_counts().tolist()
print(keys)
print(count)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[df['Species'] == 'Iris-virginica' & df[df['PetalLength'] > 1.5 ]]
print(iris_v_df)
df.describe()
df.dtypes
iris_v_df= df[df['Species'] == 'Iris-virginica']
print(iris_v_df)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PetalWidth'] > 1.5)]
print(iris_v_df)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PetalWidth'] > 1.5)]
print(iris_v_df.tolist())
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PetalWidth'] > 1.5)]
for i in iris_v_df: 
    print(i)
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PetalWidth'] > 1.5)]
print(iris_v_df[1])
import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PetalWidth'] > 1.5)]
print(iris_v_df(0))
import pandas as pd
cols =['SL','SW','PL','PL','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PetalWidth'] > 1.5)]
for i in range(len(iris_v_df)): 
    print(iris_v_df.loc[i, 'SL'], iris_v_df.loc[i, 'SW'], iris_v_df.loc[i, 'PL'], iris_v_df.loc[i, 'PW'], iris_v_df.loc[i, 'Species'])
import pandas as pd
cols =['SL','SW','PL','PL','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PW'] > 1.5)]
for i in range(len(iris_v_df)): 
    print(iris_v_df.loc[i, 'SL'], iris_v_df.loc[i, 'SW'], iris_v_df.loc[i, 'PL'], iris_v_df.loc[i, 'PW'], iris_v_df.loc[i, 'Species'])
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PW'] > 1.5)]
for i in range(len(iris_v_df)): 
    print(iris_v_df.loc[i, 'SL'], iris_v_df.loc[i, 'SW'], iris_v_df.loc[i, 'PL'], iris_v_df.loc[i, 'PW'], iris_v_df.loc[i, 'Species'])
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PW'] > 1.5)]
print(iris_v_df)
##for i in range(len(iris_v_df)):     
##    print(iris_v_df.loc[i, 'SL'], iris_v_df.loc[i, 'SW'], iris_v_df.loc[i, 'PL'], iris_v_df.loc[i, 'PW'], iris_v_df.loc[i, 'Species'])
print(iris_v_df)
print(iris_v_df.index)
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PW'] > 1.5)]
print(iris_v_df)
print(iris_v_df.index)
for i in iris_v_df.index:     
    print(i)


##    print(iris_v_df.loc[i, 'SL'], iris_v_df.loc[i, 'SW'], iris_v_df.loc[i, 'PL'], iris_v_df.loc[i, 'PW'], iris_v_df.loc[i, 'Species'])
runfile('C:/Data Backup/E Drive/Learning/Python/pandasIris-virginica.py', wdir='C:/Data Backup/E Drive/Learning/Python')
a= 'Senthil' 
b = ' Manoharan'
c = a + b
print(c)
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index()
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index()
print(df1)
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index(drop=True)
print(df1)
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index(drop=True)
df2 = df[(df['Species']=='Iris-versicolor')].reset_index(drop=True)
df3 = df[(df['Species']=='Iris-virginica')].reset_index(drop=True)
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index(drop=True)
df2 = df[(df['Species']=='Iris-versicolor')].reset_index(drop=True)
df3 = df[(df['Species']=='Iris-virginica')].reset_index(drop=True)

new = pd.DataFrame(df1.describe())
print(new)
print(df1['SL'])
print(df1['SL'].min())
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index(drop=True)
df2 = df[(df['Species']=='Iris-versicolor')].reset_index(drop=True)
df3 = df[(df['Species']=='Iris-virginica')].reset_index(drop=True)

print(df1['SL'].min(), df1['SW'].min(), df1['PL'].min(),df1['PW'].min(), 'Iris-setosa')
print(df1['SL'].max(), df1['SW'].max(), df1['PL'].max(),df1['PW'].max(), 'Iris-setosa')
print(df1['SL'].average())
print(df1['SL'].avg())
print(df1['SL'].mean())
print('%.1f'%(df1['SL'].mean()))
runfile('C:/Data Backup/E Drive/Learning/Python/pandasIrisValues.py', wdir='C:/Data Backup/E Drive/Learning/Python')
print(df1.describe())
df4 = pd.DataFrame(df1.describe()))
print(df4)
df4 = pd.DataFrame(df1.describe())
print(df4)
print(df4.index)
print(df4.loc['min', 'SL'])
print(df4.loc['min', 'SL'], df4.loc['mean','SL'])
print(df1['SL'].mean(), df1['SW'].mean(),(df1['PL'].mean(),%(df1['PW'].mean(),'Iris-setosa')
print(df1['SL'].mean(), df1['SW'].mean(),df1['PL'].mean(),%(df1['PW'].mean(),'Iris-setosa')
print(df1['SL'].mean(), df1['SW'].mean(),df1['PL'].mean(),df1['PW'].mean(),'Iris-setosa')
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index(drop=True)
df2 = df[(df['Species']=='Iris-versicolor')].reset_index(drop=True)
df3 = df[(df['Species']=='Iris-virginica')].reset_index(drop=True)

print(df1['SL'].min(), df1['SW'].min(), df1['PL'].min(),df1['PW'].min(), 'Iris-setosa')
print(df1['SL'].max(), df1['SW'].max(), df1['PL'].max(),df1['PW'].max(), 'Iris-setosa')
print(df1['SL'].mean(), df1['SW'].mean(),df1['PL'].mean(),df1['PW'].mean(),'Iris-setosa')

print(df2['SL'].min(), df2['SW'].min(), df2['PL'].min(),df2['PW'].min(), 'Iris-versicolor')
print(df2['SL'].max(), df2['SW'].max(), df2['PL'].max(),df2['PW'].max(), 'Iris-versicolor')
print(df2['SL'].mean(), df2['SW'].mean(),df2['PL'].mean(), df2['PW'].mean(),'Iris-versicolor')

print(df3['SL'].min(), df3['SW'].min(), df3['PL'].min(),df3['PW'].min(), 'Iris-virginica')
print(df3['SL'].max(), df3['SW'].max(), df3['PL'].max(),df3['PW'].max(), 'Iris-virginica')
print(df3['SL'].mean(), df3['SW'].mean(),df3['PL'].mean(),df3['PW'].mean(),'Iris-virginica')
print('%.2f'%(df1['SL'].min()), '%.2f'%(df1['SW'].min()), '%.2f'%(df1['PL'].min()),'%.2f'%(df1['PW'].min()), 'Iris-setosa')
print('%.2f'%(df1['SL'].max()), '%.2f'%(df1['SW'].max()), '%.2f'%(df1['PL'].max()),'%.2f'%(df1['PW'].max()), 'Iris-setosa')
print('%.2f'%(df1['SL'].mean()), '%.2f'%(df1['SW'].mean()),'%.2f'%(df1['PL'].mean()),'%.2f'%(df1['PW'].mean()),'Iris-setosa')
print('%.2f'%(df2['SL'].min()), '%.2f'%(df2['SW'].min()), '%.2f'%(df2['PL'].min()),'%.2f'%(df2['PW'].min()), 'Iris-versicolor')
print('%.2f'%(df2['SL'].max()), '%.2f'%(df2['SW'].max()), '%.2f'%(df2['PL'].max()),'%.2f'%(df2['PW'].max()), 'Iris-versicolor')
print('%.2f'%(df2['SL'].mean()), '%.2f'%(df2['SW'].mean()),'%.2f'%(df2['PL'].mean()),'%.2f'%(df2['PW'].mean()),'Iris-versicolor')
print('%.2f'%(df3['SL'].min()), '%.2f'%(df3['SW'].min()), '%.2f'%(df3['PL'].min()),'%.2f'%(df3['PW'].min()), 'Iris-virginica')
print('%.2f'%(df3['SL'].max()), '%.2f'%(df3['SW'].max()), '%.2f'%(df3['PL'].max()),'%.2f'%(df3['PW'].max()), 'Iris-virginica')
print('%.2f'%(df3['SL'].mean()), '%.2f'%(df3['SW'].mean()),'%.2f'%(df3['PL'].mean()),'%.2f'%(df3['PW'].mean()),'Iris-virginica')
runfile('C:/Data Backup/E Drive/Learning/Python/pandasIrisValues.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/pandasExample2.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv('iris.data',names=cols)
df = iris.copy()
print(df.SL.mean())

## ---(Mon Dec  2 09:20:54 2019)---
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
print(gender)
a = [1,2,3,4,5,6,7]
print(sum(a))
print(a.sum())
a = [1,2,3,4,5,6,7]
print(a.sum())
print(gender)
print(sum(gender,lambda g: 1 if g=='M' else 0))
print(sum(gender,lambda g: 1)
print(sum(gender,lambda g: 1))
def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(2)

print(mydoubler(11))
def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(3)

print(mydoubler(11))
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
print(gender)
print(sum(gender,lambda g: 1 if (g=='M') else 0)
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
print(gender)
print(sum(gender,lambda g: 1 if (g=='M') else 0))
print(sortgender,lambda g: 1 if (g=='M') else 0))
print(sort(gender))
print(gender.sort())
gender.sort()
gender
sort(gender)
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
print(gender)
gender.sort(gender,key=lambda g:0 if (g=='M') else 1)
gender
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
print(gender)
gender.sort(gender,key=lambda g:0 if (g=='M') else 1))
gender
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
print(gender)
gender.sort(gender,key=lambda g:0 if (g=='M') else 1)
gender
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
print(gender)
gender.sort(key=lambda g:0 if (g=='M') else 1)
gender
max(gender)
max(gender,key=lambda g:0 if (g=='M') else 1)
min(gender,key=lambda g:0 if (g=='M') else 1)
a.sum()
sum(a)
gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
a = [1,2,3,4,5,6]
sum(gender,key=lambda g:1 if (g=='M') else 0)
import pandas as pd
terdata = pd.read_csv('terrorismData.csv')
df = terdata.copy()
import pandas as pd
terdata = pd.read_csv('terrorismData')
df = terdata.copy()
import pandas as pd
terData = pd.read_csv("terrorismData.csv")
df = terData.copy()
runfile('C:/Data Backup/E Drive/Learning/Python/pandasTerrorCity.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
print(df.head())
print(df.Year)
print(df.describe())
des_df = pd.Dataframe(df.describe())
des_df = pd.DataFrame(df.describe())
print(des_df)
print(des_df['count']['Year'])
print(des_df['count'])
print(des_df)
print(des_df['Year'])
print(des_df['Year']['count'])
new_df = df[(df['State'] == 'Jammu and Kashmir')]
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
new_df = df[(df['State'] == 'Jammu and Kashmir')] 
print(new_df)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
new_df = df[(df['State'] == 'Jammu and Kashmir') & df['Group'] ! = 'Unknown'] 
print(new_df)
new_df = df[(df['State'] == 'Jammu and Kashmir') & (df['Group'] ! = 'Unknown')]
new_df = df[(df['State'] == 'Jammu and Kashmir') & (df['Group'] != 'Unknown')]
print(new_df)
new_df['City'].value_counts
new_df['City'].value_counts()
a = [1,2,3,4,5,6,7]
print(a.max())
print(city_count)
print(city_count['srinagar'])
new_df = df[(df['State'] == 'Jammu and Kashmir') & (df['Group'] != 'Unknown')] 
city_count = new_df['City'].value_counts()
print(city_count['srinagar'])
city_count = new_df['City'].value_counts()
print(city_count)
print(city_count['Srinagar'])
city_count = new_df['City'].value_counts(descending=True)
city_count = new_df['City'].value_counts(asscending=True)
city_count = new_df['City'].value_counts(ascending=True)
city_count = new_df['City'].value_counts(ascending=True)
print(city_count)
print(city_count[-1])
for city in city_count: 
    print(city)
for city in city_count.keys(): 
    print(city)
city_count = new_df['City'].value_counts()
print(city_count[-1],city_count.keys()[-1])
new_df = df[(df['State'] == 'Jammu and Kashmir') & (df['Group'] != 'Unknown')] 
city_count = new_df['City'].value_counts()
print(city_count[-1],city_count.keys()[-1])
new_df = df[(df['State'] == 'Jammu and Kashmir') & (df['Group'] != 'Unknown')] 
city_count = new_df['City'].value_counts()
print(city_count[0],city_count.keys()[0])
city_df = new_df[new_df.City=='Srinagar']
city_df = new_df[new_df.City=='Srinagar']
print(city_df)
print(grp_count)
city_df = new_df[new_df.City=='Srinagar']
grp_count  = city_df['Group'].value_counts()
print(grp_count)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
new_df = df[(df['State'] == 'Jammu and Kashmir') & (df['Group'] != 'Unknown')] 
city_count = new_df['City'].value_counts()


city_df = new_df[new_df.City=='Srinagar']
grp_count  = city_df['Group'].value_counts()
print(city_count.keys()[0],city_count[0],grp_count.keys()[0])
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
new_df = df[(df['State'] == 'Jammu and Kashmir') & (df['Group'] != 'Unknown')] 
city_group = new_df['City'].value_counts()
city_name  = city_group.keys()[0]
city_attacks = city_group[0]

city_df = new_df[new_df.City==city_name]
grp_group  = city_df['Group'].value_counts()
print(city_name, city_attacks,grp_group.keys()[0])
print(city_name, city_attacks,grp_group.keys()[0],grp_group[0]
print(city_name, city_attacks,grp_group.keys()[0],grp_group[0])
pritn(grp_group)
print(grp_group)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
new_df = df[(df['State'] == 'Jammu and Kashmir')] 
city_group = new_df['City'].value_counts()
city_name  = city_group.keys()[0]
city_attacks = city_group[0]

city_df = new_df[new_df.City==city_name]
grp_group  = city_df['Group'].value_counts()
print(grp_group)
print(city_name, city_attacks,grp_group.keys()[0],grp_group[0])
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
new_df = df[(df['State'] == 'Jammu and Kashmir')] 
city_group = new_df['City'].value_counts()
city_name  = city_group.keys()[0]
city_attacks = city_group[0]

city_df = new_df[(new_df.City==city_name) & new_df.Group != 'Unknown']
grp_group  = city_df['Group'].value_counts()
print(grp_group)
print(city_name, city_attacks,grp_group.keys()[0],grp_group[0])
city_df = new_df[(new_df.City==city_name) & (new_df.Group != 'Unknown')]
grp_group  = city_df['Group'].value_counts()
print(grp_group)
print(city_name, city_attacks,grp_group.keys()[0],grp_group[0])
runfile('C:/Data Backup/E Drive/Learning/Python/pandasTerrorAttack.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/pandasDeadliest.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df[(df['Killed'] == '')] = 0 

print(df['Killed'].max())
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df[(df['Year'] == 1970] = 1971

print(df['Killed'].max())
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df[(df['Year'] == 1970)] = 1971

print(df['Killed'].max())
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df[(df['Year'] == 1970)] = 1971
runfile('C:/Data Backup/E Drive/Learning/Python/pandasDeadliest.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
print(df['Killed'].idxmax())
runfile('C:/Data Backup/E Drive/Learning/Python/pandasDeadliest.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
print(df['Killed'].max())
ind = df['Killed'].idxmax()
print(df['Country'][ind], int(df['Killed'][ind]), df['Group'][ind])
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
print(df['Killed'].max())
ind = df['Killed'].idxmax()
print(df['Country'][ind], int(df['Killed'][ind]), df.Group[ind])
runfile('C:/Data Backup/E Drive/Learning/Python/pandasDeadliest.py', wdir='C:/Data Backup/E Drive/Learning/Python')
x = lambda a: a*2

print(x(2))
x = lambda a: a*2 if (a > 5) else a/2

print(x(2))
print(x(2))
print(x(6))
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df = df[df.Country=='India']
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df = df[(df.Country=='India') & (df.Year >= 2014)]
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0) & (df.Month != '')]
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
gov_df['YearMonth']
gov_df.YearMonth['count']
gov_df.YearMonth.count()
attacks   = gov_df.count()
attacks
attacks   = gov_df.YearMonth.count()
attacks
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
att_counts = gov_df['Group'].value_counts()
act_group  = att_counts.keys()[0]
attacks   = gov_df.YearMonth.count()
print(act_group)
print(attacks)
print(act_group, att_counts[0])
print(act_group, att_counts[1])
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
att_counts = gov_df['Group'].value_counts()
act_group  = att_counts.keys()[1]
attacks   = gov_df.YearMonth.count()
print(act_group, att_counts[1])
print(attacks)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys(): 
    if group != 'Unknown': 
        act_group = group 
        break 

attacks   = gov_df.YearMonth.count()
print(act_group)
print(attacks)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys(): 
    if group != 'Unknown': 
        act_group = group 
        break 

attacks   = gov_df.YearMonth.count()
print(attacks, act_group)
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys(): 
    if group != 'Unknown': 
        act_group = group 
        break 

attacks   = gov_df.YearMonth.count()
print(int(attacks), act_group)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= '20140526')]
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys(): 
    if group != 'Unknown': 
        act_group = group 
        break 

attacks   = gov_df.YearMonth.count()
print(int(attacks), act_group)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= 20140526)]
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys(): 
    if group != 'Unknown': 
        act_group = group 
        break 

attacks   = gov_df.YearMonth.count()
print(int(attacks), act_group)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= 20140526)]
att_counts = gov_df['Group'].value_counts()
attacks   = gov_df.YearMonth.count()
act_group = att_counts.keys()[0]
print(int(attacks), a)
act_group = att_counts.keys()
act_group
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= 20140526)]
att_counts = gov_df['Group'].value_counts()
att_counts
gov_df
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 100 + gov_df.Month + gov_df.Day
print(gov_df)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 10000 + gov_df.Month*100 + gov_df.Day
print(gov_df)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 10000 + gov_df.Month*100 + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= 20140526)]
att_counts = gov_df['Group'].value_counts()
att_counts
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 10000 + gov_df.Month*100 + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= 20140526)]
attacks   = gov_df.YearMonth.count()
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys(): 
    if group != 'Unknown': 
        act_group = group 
        break 

print(int(attacks), act_group)
print(att_counts)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 10000 + gov_df.Month*100 + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= 20140526)]
attacks   = gov_df.YearMonth.count()
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys(): 
    if group != 'Unknown': 
        act_group = group 
        break 

print(int(attacks), act_group)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.State == 'Jammu and Kashmir' | df.state == 'Jharkhand')]
print(gov_df.State)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.State == 'Jammu and Kashmir' | df.State == 'Jharkhand')]
print(gov_df.State)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & ((df.State == 'Jammu and Kashmir') | (df.State == 'Jharkhand'))]
print(gov_df.State)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
red_states = ['Jammu and Kashmir', 'Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
print(gov_df.State)
gov_df['Casualty'] = gov_df.Killed + gov_df.Wounded
print(gov_df.Casualty)
gov_df['Casualty'] = int(gov_df.Killed + gov_df.Wounded)
print(gov_df.Casualty)
years = gov_df.Year.max() - gov_df.Year.min()
years = gov_df.Year.max() - gov_df.Year.min()
years

## ---(Mon Dec  2 20:01:20 2019)---
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
red_states = ['Jammu and Kashmir', 'Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
gov_df.Killed.fillna(0,inplace=True)
gov_df.Wounded.fillna(0,inplace=True)
gov_df['Casualty'] = gov_df.Killed + gov_df.Wounded
years = gov_df.Year.max() - gov_df.Year.min() + 1
years
runfile('C:/Data Backup/E Drive/Learning/Python/pandasTerrorFrequency.py', wdir='C:/Data Backup/E Drive/Learning/Python')
years
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
red_states = ['Jammu and Kashmir', 'Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
gov_df.Killed.fillna(0,inplace=True)
gov_df.Wounded.fillna(0,inplace=True)
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
gov_df.Killed.fillna(0,inplace=True)
gov_df.Wounded.fillna(0,inplace=True)
gov_df['Casualty'] = gov_df.Killed + gov_df.Wounded
years = gov_df.Year.max() - gov_df.Year.min() + 1
years
gov_df.Year.count()
total_count = gov_df.Year.count()
kashmir_count = gov_df[(gov_df.State == 'Jammu and Kashmir')].count()
kasmir_count
kashmir_count
kashmir_count = gov_df[(gov_df.State == 'Jammu and Kashmir')].Year.count()
kashmir_count
gov_df[(gov_df.State.isin(red_states))].Year.count()
totalcount
total_count
kashmir_freq = kashmir_count / years 
kashmir_freq
red_count = gov_df[(gov_df.State != 'Jammu and Kashmir')].Year.count()
red_count
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
red_states = ['Jammu and Kashmir', 'Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
gov_df.Killed.fillna(0,inplace=True)
gov_df.Wounded.fillna(0,inplace=True)
gov_df['Casualty'] = gov_df.Killed + gov_df.Wounded
years = gov_df.Year.max() - gov_df.Year.min() + 1
total_count = gov_df.Year.count()
kashmir_count = gov_df[(gov_df.State == 'Jammu and Kashmir')].Year.count()
kashmir_freq = kashmir_count / years 
red_count = gov_df[(gov_df.State != 'Jammu and Kashmir')].Year.count()
red_freq   = red_count / years 
print(kashmir_freq, red_freq)
kashmir_count = gov_df[(gov_df.State == 'Jammu and Kashmir')].Casualty.count()
kashmir_count = gov_df[(gov_df.State == 'Jammu and Kashmir')].Casualty.sum()
print(kashmir_count)
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
red_states = ['Jammu and Kashmir', 'Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
gov_df.Killed.fillna(0,inplace=True)
gov_df.Wounded.fillna(0,inplace=True)
gov_df['Casualty'] = gov_df.Killed + gov_df.Wounded
years = gov_df.Year.max() - gov_df.Year.min() + 1
total_count = gov_df.Year.count()
kashmir_count = gov_df[(gov_df.State == 'Jammu and Kashmir')].Casualty.sum()
kashmir_freq = kashmir_count / years 
red_count = gov_df[(gov_df.State != 'Jammu and Kashmir')].Casualty.sum()
red_freq   = red_count / years 
print(int(kashmir_freq), int(red_freq))

## ---(Tue Dec  3 10:02:17 2019)---
import matplotlib.pyplot as plt
x = [1,2,3]
y = 2*x
print(y)
import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,6]
plt.scatter(x,y)
plt.show()
plt.plot(x,y)
plt.show()
import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,6]
plt.scatter(x,y)
plt.show()
plt.plot(x,y)
plt.show()
plt.scatter(x,y)
plt.plot(x,y)
plt.show()
x2= [1,2,3]
y2 = [3,6,9]
plt.scatter(x,y)
plt.scatter(x2,y2)
plt.plot(x,y)
plt.plot(x2,y2)
plt.show()
print(y)
print(x)
import matplotlib.pyplot as plt
import numpy as np 
x = np.array([1,2,3,4])
print(x)
y = x**3
print(y)
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotExample2.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,4,0.01)
print(x)
y = x**3
plt.scatter(x,y)
plt.plot(x,y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,4,0.01)
print(x)
plt.plot(x,y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,4,0.01)
y=x**3
plt.plot(x,y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,4,0.1)
y=x**3
plt.plot(x,y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,4,0.1)
y=x**3
plt.plot(x,y,'bp')
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,4,0.1)
y=x**3
plt.plot(x,y,'rp')
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,4,0.1)
y=x**3
plt.plot(x,y,'gp')
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,40,2)
y = 2*x
print(y)
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(0,40,2)
y = 2**x
print(y)
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotCustomization.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2')
plt.ylabel('Y')
plt.xlabel('X')
plt.axis([0,10,0,200])
plt.title('Pyplot Demo')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2')
plt.ylabel('Y')
plt.xlabel('X')
#plt.axis([0,10,0,200])
plt.grid()
plt.title('Pyplot Demo')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2')
plt.ylabel('Y')
plt.xlabel('X')
#plt.axis([0,10,0,200])
plt.grid()
plt.text(2,80,'Test')
plt.title('Pyplot Demo')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2')
plt.ylabel('Y')
plt.xlabel('X')
#plt.axis([0,10,0,200])
plt.grid()
plt.text(2,80,'Test',fontsize=12)
plt.title('Pyplot Demo')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2',alpha=0.5)
plt.ylabel('Y')
plt.xlabel('X')
#plt.axis([0,10,0,200])
plt.grid()
plt.text(2,80,'Test',fontsize=12)
plt.title('Pyplot Demo')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2',alpha=0.1)
plt.ylabel('Y')
plt.xlabel('X')
#plt.axis([0,10,0,200])
plt.grid()
plt.text(2,80,'Test',fontsize=12)
plt.title('Pyplot Demo')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
# alpha = 1 denotes completely opaque, alpha closer to zero is much more transparent 
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2',alpha=0.5)
plt.ylabel('Y')
plt.xlabel('X')
#plt.axis([0,10,0,200])
plt.grid()
plt.text(2,80,'Test',fontsize=12)
plt.title('Pyplot Demo')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
# Open and read data file as specified in the question
# Print the required output in given format
employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]

plt.scatter(year,revenue,size=employees)
import matplotlib.pyplot as plt
# Open and read data file as specified in the question
# Print the required output in given format
employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]

plt.scatter(year,revenue,s=employees)
import matplotlib.pyplot as plt
# Open and read data file as specified in the question
# Print the required output in given format
employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]

plt.scatter(year,revenue,s=employees)
plt.grid()
plt.show()
import matplotlib.pyplot as plt
# Open and read data file as specified in the question
# Print the required output in given format
employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]

plt.scatter(year,revenue,s=employees)
plt.title('Microsoft Statistics')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.grid()
plt.show()
import matplotlib.pyplot as plt
# Open and read data file as specified in the question
# Print the required output in given format
employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]

colors = range(len(year))
plt.scatter(year,revenue,s=employees,c=colors)
plt.title('Microsoft Statistics')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.grid()
plt.show()

## ---(Tue Dec  3 16:42:30 2019)---
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
plt.pie(sizes)
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
plt.pie(sizes)
plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs)
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels)
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels)
plt.title("Pie Sample")
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels,autopct='%.1f')
plt.title("Pie Sample")
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels,autopct='%.1f')
plt.title("Pie Sample")
plt.axis("equal")
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels,autopct='%.1f%%')
plt.title("Pie Sample")
plt.axis("equal")
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
expld = [0.1,0,0,0]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels,autopct='%.1f%%',explode=expld)

plt.title("Pie Sample")
plt.axis("equal")
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
plt.pie(sold,labels=company)
import matplotlib.pyplot as plt
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
plt.pie(sold,labels=company,autopct='%.1f')
import matplotlib.pyplot as plt
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
plt.axis("equal")
plt.pie(sold,labels=company,autopct='%.1f')
total = sold.sum()
total = sum(sold)
import matplotlib.pyplot as plt
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
plt.axis("equal")
plt.pie(sold,labels=company,autopct='%.1f')
total = sum(sold)
for i in range(len(sold)): 
    print(company[i],'%.1f'%(sold[i]/total))
import matplotlib.pyplot as plt
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
plt.axis("equal")
plt.pie(sold,labels=company,autopct='%.1f')
total = sum(sold)
for i in range(len(sold)): 
    print(company[i],'%.1f'%(sold[i]/total*100))
import matplotlib.pyplot as plt
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
plt.axis("equal")
plt.pie(sold,labels=company,autopct='%.1f')
plt.show()
total = sum(sold)
for i in range(len(sold)): 
    print(company[i],'%.1f'%(sold[i]/total*100))
import matplotlib.pyplot as plt
a = [3,6,4, 1,2,10,8,7]
plt.hist(a)
plt.show()
import matplotlib.pyplot as plt
a = [1,2,1,2,1,1,3,3,3,4]
plt.hist(a)
plt.show()
import matplotlib.pyplot as plt
a = [1,2,1,2,1,1,3,3,3,4]
plt.hist(a,edgecolor='black')
plt.show()
import matplotlib.pyplot as plt
a = [1,2,1,2,2,1,1,3,3,3,4]
plt.hist(a,edgecolor='black')
plt.show()
import matplotlib.pyplot as plt
sizes = [3,4,6,2]
expld = [0.1,0,0,0]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels,autopct='%.1f%%',explode=expld)

plt.title("Pie Sample")
plt.axis("equal")
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()
import matplotlib.pylot as plt 

height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
import matplotlib.pyplot as plt 

height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
import matplotlib.pyplot as plt 

height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
plt.hist(height,bins=5,edgecolor='black')
plt.show()

plt.hist(weight,bins=5,edgecolor='black')
plt.show()
import matplotlib.pyplot as plt 

height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
plt.hist(height,bins=5,edgecolor='black')
plt.grid()
plt.show()

plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.show()
bin = max(height) - min(height) /5
print(bin)
bin = (max(height) - min(height)) /5 
print(bin)
heightmin = min(height)
heightmax = max(height)
hdelta = (heightmax - heightmin) /5 
print(hdelta)

print(*range(heightmin,heightmax+1,hdelta))
heightmin = min(height)
heightmax = max(height)
hdelta = (heightmax - heightmin) /5 
print(hdelta)

print(range(heightmin,heightmax+1,hdelta))
heightmin = min(height)
heightmax = max(height)
hdelta = (heightmax - heightmin) /5 
print(hdelta)

a = range(heightmin,heightmax+1,hdelta))
heightmin = min(height)
heightmax = max(height)
hdelta = (heightmax - heightmin) /5 
print(hdelta)

a = range(heightmin,heightmax+1,hdelta)
heightmin = int(min(height))
heightmax = int(max(height))
hdelta = (heightmax - heightmin) /5 
print(hdelta)

a = range(heightmin,heightmax+1,hdelta)
heightmin = int(min(height))
heightmax = int(max(height))
hdelta = (heightmax - heightmin) /5 
print(hdelta)
print(heightmin)
print(heightmax)
a = heightmin + hdelta
print(a)
a = range(heightmin,heightmax+1,int(hdelta))
heightmin = int(min(height))
heightmax = int(max(height))
hdelta = (heightmax - heightmin) /5 
print(hdelta)
print(heightmin)
print(heightmax)

a = range(heightmin,heightmax+1,int(hdelta))
print(a)
a = [x for x in range(heightmin,heightmax,int(hdelta))]
print(a)
plt.hist(height,bins=5,edgecolor='black')
plt.grid()
plt.show()
weightmin = int(min(weight))
weightmax = int(max(weight))
wdelta = (weightmax - weightmin) /5 
print(wdelta)
print(weightmin)
print(weightmax)
weightmin = float(min(weight))
weightmax = float(max(weight))
wdelta = (weightmax - weightmin) /5 
print(wdelta)
print(weightmin)
print(weightmax)
a = [x for x in range(weightmin,weightmax,wdelta)]
print(a)
a = np.arange(weightmin,weightmax,wdelta)
a
import matplotlib.pyplot as plt 
import numpy as np 
height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]

heightmin = int(min(height))
heightmax = int(max(height))
hdelta = (heightmax - heightmin) /5 
print(hdelta)
print(heightmin)
print(heightmax)
a = [x for x in range(heightmin,heightmax,int(hdelta))]
print(a)


weightmin = float(min(weight))
weightmax = float(max(weight))
wdelta = (weightmax - weightmin) /5 
print(wdelta)
print(weightmin)
print(weightmax)
a = np.arange(weightmin,weightmax,wdelta)
a
plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.show()
plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.xticks(5)
plt.show()
plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.xticks([140,145,150])
plt.show()
plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.xticks([80,85,90,145,150])
plt.show()
plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.xticks([80,85,90,100,110])
plt.show()
plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.show()
plt.bar(year,population,width=0.6)
plt.xticks(rotation=40)
plt.show()
import matplotlib.pyplot as plt

year = ['year-2012','year-2013','year-2014','year-2015', 'year-2016', 'year-2017']
salary = [12,13,14,17,19,20]
population = [100,120,180,250,300,370]

plt.bar(year,population,width=0.6)
plt.xticks(rotation=40)
plt.show()
import matplotlib.pyplot as plt

year = ['year-2012','year-2013','year-2014','year-2015', 'year-2016', 'year-2017']
salary = [12,13,14,17,19,20]
population = [100,120,180,250,300,370]


plt.bar(year,population,width=0.6)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Bar Graph Demo")
plt.xticks(rotation=40)
plt.show()
import matplotlib.pyplot as plt

year = ['year-2012','year-2013','year-2014','year-2015', 'year-2016', 'year-2017']
salary = [12,13,14,17,19,20]
population = [100,120,180,250,300,370]


plt.bar(year,population,edgecolor='black',width=0.6)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Bar Graph Demo")
plt.xticks(rotation=40)
plt.show()
import matplotlib.pyplot as plt

year = ['year-2012','year-2013','year-2014','year-2015', 'year-2016', 'year-2017']
salary = [12,13,14,17,19,20]
population = [100,120,180,250,300,370]


plt.bar(year,population,edgecolor='red',width=0.6)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Bar Graph Demo")
plt.xticks(rotation=40)
plt.show()
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
red_states = ['Jammu and Kashmir', 'Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
gov_df.Killed.fillna(0,inplace=True)
gov_df.Wounded.fillna(0,inplace=True)
gov_df['Casualty'] = gov_df.Killed + gov_df.Wounded
years = gov_df.Year.max() - gov_df.Year.min() + 1
runfile('C:/Data Backup/E Drive/Learning/Python/pandasTerrorFrequency.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
red_states = ['Jammu and Kashmir', 'Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
gov_df = df[(df.Country=='India') & (df.State.isin(red_states))]
gov_df.Killed.fillna(0,inplace=True)
gov_df.Wounded.fillna(0,inplace=True)
gov_df['Casualty'] = gov_df.Killed + gov_df.Wounded
years = gov_df.Year.max() - gov_df.Year.min() + 1
years
gov_df.Year.max()
gov_df.Year.min()
years = df.Year.max() - df.Year.min() + 1
years
runfile('C:/Data Backup/E Drive/Learning/Python/pandasTerrorFrequency.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
#gov_df.Killed.fillna(0,inplace=True)
#gov_df.Wounded.fillna(0,inplace=True)
df['Casualty'] = gov_df.Killed + gov_df.Wounded
kashmir_count = df[(df.Country=='India') & (df.State == 'Jammu and Kashmir')].Casualty.sum()
kashmir_freq = kashmir_count / years
kashmir_freq
red_states = [Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
red_states = ['Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
red_count = df[(df.Country=='India') & (df.State.isin(red_states))].Casualty.sum()
red_freq   = red_count / years
red_freq
round(kashmir_freq)
int(round(kashmir_freq))
int(round(red_freq))
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
#gov_df.Killed.fillna(0,inplace=True)
#gov_df.Wounded.fillna(0,inplace=True)
red_states = ['Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
df['Casualty'] = df.Killed + df.Wounded
years = df.Year.max() - df.Year.min() + 1
kashmir_count = df[(df.Country=='India') & (df.State == 'Jammu and Kashmir')].Casualty.sum()
kashmir_freq = kashmir_count / years
red_count = df[(df.Country=='India') & (df.State.isin(red_states))].Casualty.sum()
red_freq   = red_count / years
int(round(red_freq))
int(round(kashmir_freq))
print(int(red_freq), int(kashmir_freq))
import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
#gov_df.Killed.fillna(0,inplace=True)
#gov_df.Wounded.fillna(0,inplace=True)
red_states = ['Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
df['Casualty'] = df.Killed + df.Wounded
years = df.Year.max() - df.Year.min() + 1
kashmir_count = df[(df.Country=='India') & (df.State == 'Jammu and Kashmir')].Casualty.sum()
kashmir_freq = kashmir_count / years
red_count = df[(df.Country=='India') & (df.State.isin(red_states))].Casualty.sum()
red_freq   = red_count / years
print(int(round(red_freq)), int(round(kashmir_freq)))
import pandas as pd 
jobs = read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
print(df.head())
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotJob_Year.py', wdir='C:/Data Backup/E Drive/Learning/Python')
print(df)
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
print(df.describe())
print(df.Title)
print(df.Posting_date)
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
for i in df.Posting_date: 
    print(i)
for i in df.Posting_date: 
    print(i[-4:])
df['Year'] = df.Posting_date[-4:]
print(df.Year)
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = []
for date in df.Posting_date: 
    years.append(date[-4:])

df['Year'] = years
print(df.Year)
print(df.count())
print(year_counts)
year_counts = df.Year.value_counts()
print(year_counts)
print(year_counts['2018'])
print(year_counts[0])
year_counts = df.Year.value_counts(ascending=True)
print(year_counts[0])
year_counts = df.Year.value_counts().sort_index()
print(year_counts)
job_year = df.Year.value_counts().sort_index()
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = []
for date in df.Posting_date: 
    years.append(date[-4:])

df['Year'] = years
job_year = df.Year.value_counts().sort_index()
for year in job_year: 
    print(year)
for year in job_year.keys(): 
    print(year)
for year in job_year.keys(): 
    print(year, job_year[year])
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = []
for date in df.Posting_date: 
    years.append(date[-4:])

df['Year'] = years
job_year = df.Year.value_counts().sort_index()
plt.plot(job_year.keys(),job_year)
plt.show()
for year in job_year.keys(): 
    print(year, job_year[year])
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = []
for date in df.Posting_date: 
    years.append(date[-4:])

df['Year'] = years
job_year = df.Year.value_counts().sort_index()
years     = job_year.keys().tolist()
jobs      = job_year.tolist()
plt.plot(years,jobs)
plt.show()
for year in job_year.keys(): 
    print(year, job_year[year])
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = []
for date in df.Posting_date: 
    years.append(date[-4:])

df['Year'] = years
job_year = df.Year.value_counts().sort_index()
years     = job_year.keys().tolist()
jobs      = job_year.tolist()
plt.plot(years,jobs)
plt.xlabel('Year')
plt.ylabel('Jobs')
plt.title('Jobs Vs Year')
plt.show()
for year in job_year.keys(): 
    print(year, job_year[year])
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotJob_Year.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotMonthJob.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
ind_df = df[(df.Country=='India')]

colrs = range(ind_df.City.count())
plt.pie(ind_df.City,labels=ind_df.City,colors=colrs,autopct=True)
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotCity_Job.py', wdir='C:/Data Backup/E Drive/Learning/Python')
a = 'CA,'
b = a.split(',')
print(b[-1])
a = 'CA,'
b = a.split(',')
print(b[0])
a = 'CA'
b = a.split(',')
print(b[0])
a = 'CA'
b = a.split(',')
print(b[-1])
print(loc)
for loc in df.location: 
    print(loc)
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
obj_slice = slice(1,3,1)
df['Country'] == df.location[obj_slice]
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
obj_slice = slice(1,3,1)
df['Country'] = df.location[obj_slice]
print(df.Coutnry)
print(df.Country)
a = 'Senthil'
a.partition(5)
a = 'Senthil'
a.partition('Sent')
a = 'Senthil'
substr(a,1,4)
def substr(string,start,end): 
    return string[start:end:1]
a = 'Senthil'
substr(a,1,4)
a = 'Senthil'
substr(a,0,4)
def substr(string): 
    return string[0:2]
a= 'Senthil'
print(substr(a))
df['Country'] = df.location.apply(substr)
print(df.Country)
ind_df = df[(df.Coutnry=='IN')]
ind_df = df[(df.Country=='IN')]
ind_df
ind_df = df[(df.location.apply(substr)=='IN')]
ind_df
del ind_df.Country
del ind_df['Country']
print(ind_df)
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotCity_Job.py', wdir='C:/Data Backup/E Drive/Learning/Python')
plt.pie(ind_df.City)
plt.show()
a = [1,1,1,2,3,2,2,4,4,4,4,4,4,4,4]
plt.pie(a)
plt.show()
a = ind_df.City.tolist()
print(a)
plt.pie(ind_df.City.tolist())
job_city = ind_df.City.value_counts()
plt.pie(job_city,labels=job_city.keys())
plt.show()
plt.pie(job_city,labels=job_city.keys())
plt.axis("equal")
plt.show()
plt.pie(job_city,labels=job_city.keys(),autopct=True)
plt.axis("equal")
plt.show()
plt.pie(job_city,labels=job_city.keys())
plt.axis("equal")
plt.show()
plt.pie(job_city,labels=job_city.keys(),autopct='%.1f%%')
plt.axis("equal")
plt.show()
job_city.sum()
total_jobs = job_city.sum()
for city in job_city.keys(): 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f'%(curpct))
for city in job_city.keys()[-1::-1]: 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f'%(curpct))
for city in job_city.keys()[-1::]: 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f'%(curpct))
plt.hist(ind_df.City)
import matplotlib.pyplot as plt
import pandas as pd 

def substr(string): 
    return string[0:2]


def getCity(location): 
    loc = location.split(',')
    return loc[-1]


jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
df['Country'] = df.location.apply(substr)
ind_df = df[(df.Country=='IN')]
del ind_df['Country']
ind_df['City'] = ind_df.location.apply(getCity)
job_city = ind_df.City.value_counts()
plt.pie(job_city,labels=job_city.keys(),autopct='%.2f%%')
plt.axis("equal")
plt.show()

total_jobs = job_city.sum()
for city in job_city.keys()[-1::]: 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f'%(curpct))
import matplotlib.pyplot as plt
import pandas as pd 

def substr(string): 
    return string[0:2]


def getCity(location): 
    loc = location.split(',')
    return loc[-1]


jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
df['Country'] = df.location.apply(substr)
ind_df = df[(df.Country=='IN')]
del ind_df['Country']
ind_df['City'] = ind_df.location.apply(getCity)
job_city = ind_df.City.value_counts()
plt.pie(job_city,labels=job_city.keys(),autopct='%.2f%%')
plt.axis("equal")
plt.show()

total_jobs = job_city.sum()
for city in job_city.keys(): 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f'%(curpct))
total_jobs = job_city.sum()
for city in job_city.keys(): 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f%%'%(curpct,2))
total_jobs = job_city.sum()
for city in job_city.keys(): 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f%%'%(curpct))
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
data = pd.read_csv('amazon_jobs_dataset.csv')
location = data['location'].str.split(', ',expand=True)
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotJob_CitySolution.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
data = pd.read_csv('amazon_jobs_dataset.csv')
location = data['location'].str.split(', ',expand=True)
location
location = data['location'].str.split(', ',expand=False)
location
location = data['location'].str.split(', ',expand=True)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
data = pd.read_csv('amazon_jobs_dataset.csv')
location = data['location'].str.split(', ',expand=True)
arr = location[0] == 'IN'
india_city = location[arr][2]
freq = india_city.value_counts()
plt.axis('equal')
x = freq.index
plt.pie(freq,labels=x,autopct='%.2f%%')
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotJob_CitySolution.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = df.Posting_date.str.split(',',expand=True)
print(years)
years = df.Posting_date.str.split(',')[1]
print(years)
years = df.Posting_date.str.split(',',expand=True)
print(years)
years = years.iloc[:,1]
print(years)
years = df.Posting_date.str.split(',',expand=True).iloc[:,1]

print(years)
arr   = df['BASIC QUALIFICATIONS']
arr
years = df.Posting_date.str.split(',',expand=True).iloc[:,1]
arr   = ('Java' in df['BASIC QUALIFICATIONS'].str) | ('java' in df['BASIC QUALIFICATIONS'].str)
arr
a.index('Senthil')
find(a,'Senthil')
a.find('Sent')
a  = 'Senthil'
'Sent' in a
a.find('Sent')
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java')) | (df['BASIC QUALIFICATIONS'].str.find('java'))
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java'))
arr
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java') >= 0 )
arr
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java') >= 0 )  | (df['BASIC QUALIFICATIONS'].str.find('java') >= 0 ) 
arr
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = df.Posting_date.str.split(',',expand=True).iloc[:,1]
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java') >= 0 )  | (df['BASIC QUALIFICATIONS'].str.find('java') >= 0 ) 
java_years = years[arr]
freq = java_years.value_counts(ascending=True)
print(freq)
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = df.Posting_date.str.split(',',expand=True).iloc[:,1]
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java') >= 0 )  | (df['BASIC QUALIFICATIONS'].str.find('java') >= 0 ) 
valid_years = years[arr]
java_years = valid_years.value_counts(ascending=True)
for year in java_years.keys(): 
    print(year,java_years[year])
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('amazon_jobs_dataset.csv')
year = data['Posting_date'].str.split(', ',expand=True)[1]
basic_qualification=data['BASIC QUALIFICATIONS']
array=np.array(list(zip(year,basic_qualification)))
for i in range(len(array)): 
    if 'Java' in array[i][1] or 'java' in array[i][1]:
        array[i][1] = 1 
    else: 
        array[i][1] = 0

array = array[array[:,1]=='1']
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('amazon_jobs_dataset.csv')
year = data['Posting_date'].str.split(', ',expand=True)[1]
basic_qualification=data['BASIC QUALIFICATIONS']
array=np.array(list(zip(year,basic_qualification)))
for i in range(len(array)): 
    if 'Java' in array[i][1] or 'java' in array[i][1]:
        array[i][1] = 1 
    else: 
        array[i][1] = 0

array = array[array[:,1]=='1']
array = array[:,0]
year=np.unique(array)
job=[]
for i in year: 
    job.append(len(array[array==i]))

plt.scatter(year,job,edgecolor='black',s=100)
plt.grid()
plt.show()
for i in range(len(year)): 
    print(year[i],job[i])
runfile('C:/Data Backup/E Drive/Learning/Python/pyplotJobJava.py', wdir='C:/Data Backup/E Drive/Learning/Python')
arr
import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = df.Posting_date.str.split(',',expand=True).iloc[:,1]
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java') >= 0 )  | (df['BASIC QUALIFICATIONS'].str.find('java') >= 0 ) 
valid_years = years[arr]
java_years = valid_years.value_counts().sort_index()
plt.scatter(java_years.keys().tolist(),java_years.tolist(),edgecolor='black',s=100)
plt.grid()
plt.show()
for year in java_years.keys(): 
    print(year,java_years[year])
import matplotlib.pylot as plt
import numpy as np 
import pandas as pd
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
year = df.Date.str.split('/',expand=True).iloc[:,-1]
print(year)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
year = df.Date.str.split('/',expand=True).iloc[:,-1]
print(year)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
year = df.Date.str.split('/',expand=True)
print(year)
a = '22/01//2015'
b= a.split('/')
b
 = '22/01/2015'
b= a.split('/')
b
a = '22/01/2015'
b= a.split('/')
b
a = '22/01/2015 '
b= a.split('/')
b
a = '22/01/2015'
a.apply(getYear)
runfile('C:/Data Backup/E Drive/Learning/Python/CS-1-Startup Funding.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getYear(String): 
    return String[-4:]


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
year = df.Date(getYear)
print(year)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getYear(String): 
    return String[-4:]


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['Year'] = df.Date(getYear)
print(year)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getYear(String): 
    return String[-4:]


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
year = df.Date.apply(getYear)
print(year)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getYear(String): 
    return String[-4:]


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
year = df.Date.apply(getYear)

fund_year = year.value_counts().sort_index()
plt.plot(fund_year.keys(),fund_year)
plt.grid()
plt.xlabel('Year')
plt.ylabel('Fund')
plt.title('Fundings per year')

for year in fund_year.keys(): 
    print(year,fund_year[year])
a.title(a)
a = 'senthil'
a.title(a)
a = 'senthil'
a.title()
a = 'DELHI'
print(a.title())
a = 'NEW DELHI'
a.title()
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

city = df.CityLocation.apply(getCity)
print(city)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

city = df.CityLocation.str.apply(getCity)
print(city)
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopIndianCities.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

city = df.CityLocation.apply(getCity)
print(city)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)
freq = city.value_counts()
for city in freq.keys(): 
    print(city,freq[city])
cities = df.CityLocation.apply(getCity)
cities.dropna(inplace=True)
cities = df.CityLocation.apply(getCity)
cities.dropna(inplace=True)
freq = city.value_counts()
for city in freq.keys(): 
    print(city,freq[city])
cities = df.CityLocation.apply(getCity)
cities.dropna(inplace=True)
freq = cities.value_counts()
for city in freq.keys(): 
    print(city,freq[city])
cities = df.CityLocation.apply(getCity)
cities = cities.dropna(inplace=True)

freq = cities.value_counts()
cities = df.CityLocation.apply(getCity)
cities = cities.dropna(inplace=True)

freq = cities.value_counts()
for city in freq.keys(): 
    print(city,freq[city])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)
cities = cities.dropna(inplace=True)

freq = cities.value_counts()
for city in freq.keys(): 
    print(city,freq[city])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)

freq = cities.value_counts()
for city in freq.keys(): 
    print(city,freq[city])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)

freq = cities.value_counts(dropna=True)
for city in freq.keys(): 
    print(city,freq[city])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)

freq = cities.value_counts(dropna=True)
for city in freq.keys(): 
    if city == 'Nan': 
        continue 
    print(city,freq[city])
cities = df.CityLocation.apply(getCity)
cities
cities.dropna(inplace=True)
cities
cities = df.CityLocation.apply(getCity)
new_cities = cities.dropna()
new_cities
cities = df.CityLocation.apply(getCity)
new_cities = cities.CityLocation.dropna()
new_cities
cities = df.CityLocation.apply(getCity)
new_cities = cities.CityLocation
new_cities
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopIndianCities.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)

freq = cities.value_counts(dropna=True)
for city in freq.keys(): 
    if city == 'Nan': 
        continue 
    print(city,freq[city])
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopIndianCities.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)

freq = cities.value_counts(dropna=True)
i = 0 
top_city = []
top_count = []
for city in freq.keys(): 
    if city == 'Nan': 
        continue
    if i >= 10: 
        break 
    
    top_city.append(city)
    top_count.append(freq[city])
    i = i + 1


plt.pie(top_count,labels=top_city,autopct='%.2f%%')
plt.axis("equal")
plt.show()

for i in range(10): 
    print(top_city[i],top_count[i])
cities
cities[678]
cities[cities=='Bangalore']
cities.index
for i in cities.index: 
    print(i)
cities = df.CityLocation.apply(getCity)
for i in cities[cities=='Bangalore'].index: 
    print(i)
a.strip()
a = 'Senthil'
a.strip()
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)
cities
cities = df.CityLocation.apply(getCity)
cities[cities=='Bangalore']
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopIndianCities.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation[df.CityLocation!=''].apply(getCity)
cities
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation[df.CityLocation!=Nan].apply(getCity)
cities
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation[df.CityLocation!=np.nan].apply(getCity)
cities
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

cities = df.CityLocation.apply(getCity)
cities
freq = cities.value_counts(dropna=True)
i = 0 
top_city = []
top_count = []
for city in freq.keys(): 
    #if city == 'Nan': 
    #    continue
    if i >= 10: 
        break 
    
    top_city.append(city)
    top_count.append(freq[city])
    i = i + 1


plt.pie(top_count,labels=top_city,autopct='%.2f%%')
plt.axis("equal")
plt.show()

for i in range(10): 
    print(top_city[i],top_count[i])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df[2342]
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df[:,2342]
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df.iloc[2342,]
df.CityLocation.iloc[2342,]
np.isnan(df.CityLocation.iloc[2342,])
df.CityLocation.iloc[2342,] ==np.nan
df.CityLocation.iloc[2342,] ==np.NaN
df.CityLocation.iloc[2342,] == np.NAN
np.isnan(df.CityLocation.iloc[2342,])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    if np.isnan(location): 
        return 'blank'
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()


cities = df.CityLocation.apply(getCity)
cities
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
data = pd.read_csv('startup_funding.csv')
df   = data.copy()


cities = df.CityLocation.apply(getCity)
cities
cities = df.CityLocation.apply(getCity)
cities.dropna(inplace=True)
cities
groupcols = df.groupby(['City']).AmountInUSD.sum()
df
df.City
df['City'] = df.CityLocation.apply(getCity)
df.City
groupcols = df.groupby(['City']).AmountInUSD.sum()
groupcols = df.groupby(['City'])
groupcols
groupcols.describe()
df.AmoundInUSD
df.AmountInUSD
df[df.AmountInUSD==NaN] = 0
df[df.AmountInUSD=='NaN'] = 0
df.AmountInUSD
df[df.AmountInUSD==np.NaN] = 0
df.AmountInUSD
df[np.isnan(df.AmountInUSD)] = 0
df.AmountInUSD
df.AmountInUSD
df.AmountInUSD.fillna(inplace=True)
df.AmountInUSD
df.AmountInUSD.fillna(0,inplace=True)
df.AmountInUSD
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['City'] = df.CityLocation.apply(getCity)
df[np.isnan(df.AmountInUSD)] = 0
df.AmountInUSD.fillna(0,inplace=True)

groupcols = df.groupby(['City'])['AmountInUSD'].sum()
groupcols.describe()
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['City'] = df.CityLocation.apply(getCity)
df.AmountInUSD.fillna(0,inplace=True)

groupcols = df.groupby(['City'])['AmountInUSD'].sum()
groupcols.describe()
groupcols = df.groupby(['City'])['AmountInUSD']
groupcols.describe()
groupcols = df.groupby(['City'])['AmountInUSD'].sum()
df.AmountInUSD.sum()
print(df.AmountInUSD.sum())
print(df.AmountInUSD)
df['AmountInUSD'] = int(df['AmountInUSD'].replace(',',''))
def str2int(string): 
    return int(string.replace(',',''))
df['AmountInUSD'] = df.AmoutInUSD.apply(str2int)
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['City'] = df.CityLocation.apply(getCity)
df.AmountInUSD.fillna(0,inplace=True)
df['AmountInUSD'] = df.AmoutInUSD.apply(str2int)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['City'] = df.CityLocation.apply(getCity)
df.AmountInUSD.fillna("0.0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['City'] = df.CityLocation.apply(getCity)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
groupcols = df.groupby(['City'])['AmountInUSD'].sum()
groupcols.describe()
groupcols
print(groupcols[0])
print(groupcols.index)
for city in groupcols: 
    print(city,groupcols[city])
groupcols['Agra']
for city in groupcols.keys(): 
    print(city,groupcols[city])
sort(groupcols)
groupcols.sort()
groupcols.sorted()
groupcols.sort_values()
groupcols.sort_values(descending=True)
groupcols.sort_values()
groupcols.sort_values(axis=0)
groupcols.sort_values(axis=1)
groupcols.sort_values(axis='City')
groupcols.sort_values()
groupcols
groupcols = df.groupby(['City'])['AmountInUSD'].sum().sort_values()
groupcols
groupcols = groupcols.sort_values()
groupcols
groupcols = df.groupby(['City'])['AmountInUSD'].sum()
groupcols = groupcols.sort_index()
groupcols
groupcols = df.groupby(['City'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
groupcols
len(groupcols)
for i in range(len(groupcols)-1,len(groupcols)-1-10,-1): 
    print(groupcols.keys()[i],groupcols[i])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()


def str2int(string): 
    return int(string.replace(',',''))


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['City'] = df.CityLocation.apply(getCity)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
groupcols = df.groupby(['City'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()

for i in range(len(groupcols)-1,len(groupcols)-1-10,-1): 
    print(groupcols.keys()[i],groupcols[i])
total = sum(fund)
cities = []
fund   = []
for i in range(len(groupcols)-1,len(groupcols)-1-10,-1): 
    cities.append(groupcols.keys()[i])
    fund.append(groupcols[i])


total = sum(fund)
total
total = sum(fund)
for i in range(len(cities)): 
    print(city[i],'%.2f'%(fund[i]/total*100))
total = sum(fund)
for i in range(len(cities)): 
    print(cities[i],'%.2f'%(fund[i]/total*100))
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopIndianCities.py', wdir='C:/Data Backup/E Drive/Learning/Python')
df.InvestmentType
a = 'Senthil Manoharan'
a.space()
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestmentType
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType[df.InvestmentType=='blank]
df.InvestmentType[df.InvestmentType=='blank']
a = 'A'
a.isupper()
a = 'a'
a.isupper()
def checkSpell(String):
    outStr = ''
    char ='a'
    for char in String: 
        if char.isupper(): 
            outStr = outStr + ' ' + char
        else:
            outStr = outStr + char
        
        return outStr.strip()
a ='CrowdFunding'
checkSpell(a)
def checkSpell(String):
    outStr = ''
    char ='a'
    for char in String: 
        if char.isupper(): 
            outStr = outStr + ' ' + char
        else:
            outStr = outStr + char
        
        return outStr
a ='CrowdFunding'
checkSpell(a)
def checkSpell(String):
    outStr = ''
    char ='a'
    for char in String: 
        if char.isupper(): 
            outStr = outStr + ' ' + char
        else:
            outStr = outStr + char
    
    return outStr
def checkSpell(String):
    outStr = ''
    char ='a'
    for char in String: 
        if char.isupper(): 
            outStr = outStr + ' ' + char
        else:
            outStr = outStr + char
    
    return outStr.strip()
a ='CrowdFunding'
checkSpell(a)
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.InvestmentType[0]
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    if prevchar != ' ': 
        for char in String: 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char
            prevchar = char 
    else: 
        outStr = outStr + char
    return outStr.strip()      


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.InvestmentType[0]
a = 'CrowdFunding'
a = checkSpell(a)
print(a)
a = checkSpell(a)
print(a)
def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    if prevchar != ' ': 
        for char in String: 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char
            prevchar = char 
    else: 
        outStr = outStr + char
    return outStr.strip()
a = 'CrowdFunding'
a = checkSpell(a)
print(a)
a = checkSpell(a)
print(a)
def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip()
a = 'CrowdFunding'
a = checkSpell(a)
print(a)
a = checkSpell(a)
print(a)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip()      


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.InvestmentType[0]
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip()      


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
print(df.InvestmentType[0])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip()      


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df.groupby(['InvestmentType'])['AmountInUSD'].sum()
groupcols = df[df.InvestmentType !='blank'].groupby(['InvestmentType'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
groupocols
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    String = String.title()
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip()      


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df.InvestmentType !='blank'].groupby(['InvestmentType'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip().title()


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df.InvestmentType !='blank'].groupby(['InvestmentType'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip().title()


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df.InvestmentType !='Blank'].groupby(['InvestmentType'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
groupcols
total = groupcols.sum()
print(total)
plt.pie(groupcols,labels=groupcols.keys())
plt.axis("equal")
plt.pie(groupcols,labels=groupcols.keys(),autopct='%.2f%%')

plt.show()
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip().title()


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df.InvestmentType !='Blank'].groupby(['InvestmentType'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
total = groupcols.sum()

plt.axis("equal")
plt.pie(groupcols,labels=groupcols.keys(),autopct='%.2f%%')
plt.show()

for i in range(len(groupcols)-1,-1,-1):
    print(groupcols.keys()[i],'%.2f'%(groupcols[i]/total*100))
groupcols = groupcols.sort_values()
groupcols
a = 'Senthil'
upper(a)
a = 'Senthil'
a.upper()
a = 'Senthil'
a.upper()
a.lower()
a = 'Senthil'
a.upper()
a.lower()
a
a = 'Senthil-Manoharan'
a.replace('-','')
a = 'e-Commerce of the world' 
words = a.split()
word[0] = 'Ecommerce'
word[0] + word[1:]
a = 'e-Commerce of the world' 
words = a.split()
words[0] = 'Ecommerce'
words[0] + words[1:]
a = 'e-Commerce of the world' 
words = a.split()
words[0] = 'Ecommerce'
*words
a = 'e-Commerce of the world' 
words = a.split()
words[0] = 'Ecommerce'
print(*words)
a = 'e-Commerce World of fun' 
print(checkSpell(a))
def checkSpell(String):
    word = String.split()[0]
    pos  = len(word) 
    if word.replace('-','').lower() = 'ecommerce': 
        word = 'Ecommerce'
    return word+ String[pos:]
a = 'e-Commerce World of fun' 
print(checkSpell(a))
def checkSpell(String):
    word = String.split()[0]
    pos  = len(word) 
    temp = word.replace('-','').lower()
    if temp == 'ecommerce': 
        word = 'Ecommerce'
    return word+ String[pos:]
a = 'e-Commerce World of fun' 
print(checkSpell(a))
a = 'E-commerce World of fun' 
print(checkSpell(a))
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    word = String.split()[0]
    pos  = len(word) 
    temp = word.replace('-','').lower()
    if temp == 'ecommerce': 
        word = 'Ecommerce'
    return word+ String[pos:]


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['Industry/Vertical'].fillna('blank',inplace=True)
df['Industry/Vertical'] = df['Industry/Vertical'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df['Industry/Vertical'] !='blank'].groupby(['Industry/Vertical'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
df['Industry/Vertical'].fillna('blank',inplace=True)
df.describe()
df.head()
df['Industry/Vertical']
df['IndustryVertical']
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    word = String.split()[0]
    pos  = len(word) 
    temp = word.replace('-','').lower()
    if temp == 'ecommerce': 
        word = 'Ecommerce'
    return word+ String[pos:]


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['IndustryVertical']

# Handle NaN and convert String to Number 
df['IndustryVertical'].fillna('blank',inplace=True)
df['IndustryVertical'] = df['IndustryVertical'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df['IndustryVertical'] !='blank'].groupby(['IndustryVertical'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
total = groupcols.sum()
groupcols
a[-1::-1][:5]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a[-1::-1][:5]
industry = []
fund     = []
for ind in groupcols.keys()[-1::-1][:5]:
    industry.append(ind)
    fund.append(groupcols[ind])
industry
fund
total =  sum(fund)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    word = String.split()[0]
    pos  = len(word) 
    temp = word.replace('-','').lower()
    if temp == 'ecommerce': 
        word = 'Ecommerce'
    return word+ String[pos:]


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['IndustryVertical']

# Handle NaN and convert String to Number 
df['IndustryVertical'].fillna('blank',inplace=True)
df['IndustryVertical'] = df['IndustryVertical'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df['IndustryVertical'] !='blank'].groupby(['IndustryVertical'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
total = groupcols.sum()

industry = []
fund     = []
for ind in groupcols.keys()[-1::-1][:5]:
    industry.append(ind)
    fund.append(groupcols[ind])


total =  sum(fund)

for i in range(len(industry)): 
    print(industry[i],'%.2f'%(fund[i]/total*100))
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopIndustries.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    word = String.split()[0]
    pos  = len(word) 
    temp = word.replace('-','').lower()
    if temp == 'ecommerce': 
        word = 'Ecommerce'
        return word
    return word+ String[pos:]


def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['IndustryVertical'].fillna('blank',inplace=True)
df['IndustryVertical'] = df['IndustryVertical'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df['IndustryVertical'] !='blank'].groupby(['IndustryVertical'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
total = groupcols.sum()

industry = []
fund     = []
for ind in groupcols.keys()[-1::-1][:5]:
    industry.append(ind)
    fund.append(groupcols[ind])


total =  sum(fund)

for i in range(len(industry)): 
    print(industry[i],'%.2f'%(fund[i]/total*100))
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartUpName'].fillna('blank',inplace=True)
df['StartUpName'] = df['StartUpName'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df['StartUpName'] !='blank'].groupby(['StartUpName'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df['StartupName'] !='blank'].groupby(['StartupName'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)

groupcols = df[df['StartupName'] !='blank'].groupby(['StartupName'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()

for startup in groupcols.keys()[-1::-1][:5]: 
    print(startup)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
groupcols = df.StartupName.value_counts()
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
groupcols = df.StartupName.value_counts()

for startup in groupcols.keys()[-1::-1][:5]: 
    print(startup)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
groupcols = df.StartupName.value_counts()

for startup in groupcols.keys(): 
    print(startup)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
groupcols = df.StartupName.value_counts()

for startup in groupcols.keys()[:5]: 
    print(startup)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
groupcols = df.StartupName.value_counts()

for startup in groupcols.keys()[:5]: 
    print(startup,groupcols[startup])
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df.InvestorName.fillna('blank',inplace=True)
groupcols = df.InvestorName.value_counts()

for startup in groupcols.keys()[:5]: 
    print(startup,groupcols[startup])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

data = pd.read_csv('startup_funding.csv')
df   = data.copy()

# Handle NaN and convert String to Number 
df.InvestorsName.fillna('blank',inplace=True)
groupcols = df.InvestorsName.value_counts()

for startup in groupcols.keys()[:5]: 
    print(startup,groupcols[startup])
df.InvestorsName.fillna('blank',inplace=True)
investors = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorName != 'Undisclosed investors')]
investors = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]
groupcols = investors.value_counts()
groupcols
groupcols[0]
print(groupcols.keys()[0],groupcols[0])
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

# Handle NaN and convert String to Number 
def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]
for investor in df.InvestorsName: 
    print(investor)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

# Handle NaN and convert String to Number 
def getInvestor(investor):
    
    outarr = []
    arr1 = investor.split(',')
    for ele in arr1: 
        arr2 = ele.split('&')
        for com in arr2: 
            outarr.append(com.strip())
    return outarr 



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        investors.append(ele)

print(investors)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

# Handle NaN and convert String to Number 
def getInvestor(investor):
    investor = str(investor)
    outarr = []
    arr1 = investor.split(',')
    for ele in arr1: 
        arr2 = ele.split('&')
        for com in arr2: 
            outarr.append(com.strip())
    return outarr 



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        investors.append(ele)

print(investors)
print(pd.DataFrame(investors))
print(pd.DataFrame(investors),names=['InvestorsName'])
inv_df = pd.DataFrame(investors,columns=['InvestorName'])
inv_df
groupcols = inv_df.InvestorName.value_counts()
groupcols
a = lower('Senthil')
a
investors = []
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        temp = ele.lower()
        if ele != ' ' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele)

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
groupcols
investors = []
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        temp = ele.strip().lower()
        if temp != ' ' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele)

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
groupcols
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

# Handle NaN and convert String to Number 
def getInvestor(investor):
    investor = str(investor)
    outarr = []
    arr1 = investor.split(',')
    for ele in arr1: 
        arr2 = ele.split('&')
        for com in arr2: 
            outarr.append(com.strip())
    return outarr 



data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        temp = ele.strip().lower()
        if temp != ' ' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele)

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()

for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
a = [1,2,3]
b = [4,5,6]
zip(a,b)
dict(zip)
dict(zip(a,b))
a =[(1,4),(2,5),(3,6)]
b= dict(a)
a =[(1,4),(2,5),(3,6)]
b= dict(a)
b
dict_arr  = [] 
dict_arr.append("Accel Partner","Accel Partners")
dict_arr
dict_arr  = [] 
dict_arr.append(("Accel Partner","Accel Partners"))
dict_arr
a = 'Senthil and Manoharan'
b  = a.split('and')
b
a = 'Senthil and Manoharan'
b  = a.split(' and')
b
a = 'Senthil and Manoharan'
b  = a.split(' and ')
b
out = []
out.append(x) for x in range(5)
out
out = []
for x in range(5)  out.append(x) 

out
a = [1,2,3]
b = [4,5,6]
a.append(b)
a
a = [1,2,3]
b = [4,5,6]
a.extend(b)
a
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = inp.pop()          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele,inv_map)
        temp = ele.strip().lower()
        if temp != ' ' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()

for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = inp.pop()          
            arr1 = inStr.split(str(spchar))
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele,inv_map)
        temp = ele.strip().lower()
        if temp != ' ' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()

for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])




groupcols = investors.value_counts()
groupcols
print(groupcols.keys()[0],groupcols[0])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = inp.pop()          
            print(spchar)
            arr1 = inStr.split(str(spchar))
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele,inv_map)
        temp = ele.strip().lower()
        if temp != ' ' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()

for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])




groupcols = investors.value_counts()
groupcols
print(groupcols.keys()[0],groupcols[0])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            print(spchar)
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele,inv_map)
        temp = ele.strip().lower()
        if temp != ' ' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()

for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            print(spchar)
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele,inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()

for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopInvestor.py', wdir='C:/Data Backup/E Drive/Learning/Python')
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele,inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
groupcols
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
groupcols
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
groupcols
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])

## ---(Fri Dec  6 08:24:59 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopInvestor.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ##ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
groupcols
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
groupcols
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopInvestor.py', wdir='C:/Data Backup/E Drive/Learning/Python')
investors
if 'Accel' in investors: 
    print('yes')
if 'accel' in investors: 
    print('yes')
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopInvestor.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append((" Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Â  Accel Partners India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

if 'accel' in investors: 
    print('yes')

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Â  Accel Partners India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

if 'accel' in investors: 
    print('yes')

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Â  Accel Partners India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

if 'accel' in investors: 
    print('yes')

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    #dict_arr.append(("Â  Accel Partners India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())

if 'accel' in investors: 
    print('yes')

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]
data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName[1590]
df.InvestorsName[1591]
df.InvestorsName[1592]
df.InvestorsName[1590]
df.InvestorsName[1591]
getInvestor(df.InvestorsName[1591])
resolveInvestor(getInvestor(df.InvestorsName[1591]),inv_map)
resolveInvestor(getInvestor(df.InvestorsName[1591][1]),inv_map)
b= getInvestor(df.InvestorsName[1591][1])
b
b= getInvestor(df.InvestorsName[1591])
b
b= getInvestor(df.InvestorsName[1591])[1]
b
resolveInvestor(b,inv_map)
inv_map   = getInvestorMap()
b= getInvestor(df.InvestorsName[1591])[1]
resolveInvestor(b,inv_map)
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp
b= getInvestor(df.InvestorsName[1591])
b
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("\xa0 Accel Partners India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners")
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("\xa0 Accel Partners India","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]


investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
b = getInvestor(df.InvestorsName[1591])
b
b = getInvestor(df.InvestorsName[1591])
c = []
for ele in b:
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())

c
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    #dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    #dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
df.InvestorsName[2071]
investor = df.InvestorsName[2071]
c = []
for ele in getInvestor(investor):
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())
c
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel US","Accel Partners))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]
c = []
for ele in getInvestor(investor):
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())


df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]
c = []
for ele in getInvestor(investor):
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())


df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopInvestor.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    #dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2071]

df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
investor = df.InvestorsName[2146]
c = []
for ele in getInvestor(investor):
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())
c
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2146]
c = []
for ele in getInvestor(investor):
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())


df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
c
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
investor = df.InvestorsName[2146]
c = []
for ele in getInvestor(investor):
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())


df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
c
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopInvestor.py', wdir='C:/Data Backup/E Drive/Learning/Python')
c
investor = df.InvestorsName[2146]
investor
def getInvestor(investor):
    parse = [',','&',' and ','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp
investor = df.InvestorsName[2146]
investor
c = []
for ele in getInvestor(investor):
    ele = resolveInvestor(ele.strip(),inv_map)
    temp = ele.strip().lower()
    if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
        c.append(ele.strip())
c
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
a = "senthil"
b = []
b.append(a.title())
b
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    #dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip()


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    #dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getInvestorMap():
    dict_arr  = [] 
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    #dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    #dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor,inv_map): 
    
    if investor in inv_map: 
        return inv_map[investor]
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip().title())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:10]:
    print(investor,groupcols[investor])

## ---(Sat Dec  7 07:36:32 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/inPlaceHeapSort.py', wdir='C:/Data Backup/E Drive/Learning/Python')
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq[self.getSize()+1] = newPqNode
        self.upSize()
        self.__percolateUp()
    
    def __percolateUp(self): 
        child = self.getSize() - 1
        while child > 0: 
            parent = (child - 1) // 2 
            child1 = parent*2 + 1
            child2 = parent*2 + 2
            if self.pq[child].priority < self.pq[child].priority: 
                child = child1
            else: 
                child = child2
            if self.pq[parent].priority > self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child], self.pq[parent]
                child = parent 
            else: 
                break                
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pq.ele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()






arr = [int(x) for x in input().split()]
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        self.__percolateUp()
    
    def __percolateUp(self): 
        child = self.getSize() - 1
        while child > 0: 
            parent = (child - 1) // 2 
            child1 = parent*2 + 1
            child2 = parent*2 + 2
            if self.pq[child].priority < self.pq[child].priority: 
                child = child1
            else: 
                child = child2
            if self.pq[parent].priority > self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child], self.pq[parent]
                child = parent 
            else: 
                break                
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pq.ele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()






arr = [int(x) for x in input().split()]
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        self.__percolateUp()
    
    def __percolateUp(self): 
        child = self.getSize() - 1
        print('Bfr:', child, self.pq[child].priority)
        while child > 0: 
            parent = (child - 1) // 2 
            print('Aft:', parent)
            print('Aft:', self.pq[parent].priority)
            child1 = parent*2 + 1
            child2 = parent*2 + 2
            if self.pq[child].priority < self.pq[child].priority: 
                child = child1
            else: 
                child = child2
            print('Aft:', child)
            print('Aft:, self.pq[child].priority)
            if self.pq[parent].priority > self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child], self.pq[parent]
                child = parent 
            else: 
                break                
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pq.ele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()






arr = [int(x) for x in input().split()]
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        self.__percolateUp()
    
    def __percolateUp(self): 
        child = self.getSize() - 1
        print('Bfr:', child, self.pq[child].priority)
        while child > 0: 
            parent = (child - 1) // 2 
            print('Aft:', parent)
            print('Aft:', self.pq[parent].priority)
            child1 = parent*2 + 1
            child2 = parent*2 + 2
            if self.pq[child].priority < self.pq[child].priority: 
                child = child1
            else: 
                child = child2
            print('Aft:', child)
            print('Aft:', self.pq[child].priority)
            if self.pq[parent].priority > self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child], self.pq[parent]
                child = parent 
            else: 
                break                
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pq.ele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()






arr = [int(x) for x in input().split()]
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        self.__percolateUp()
    
    def __percolateUp(self): 
        child = self.getSize() - 1
        while child > 0: 
            parent = (child - 1) // 2 
            if self.pq[parent].priority > self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child], self.pq[parent]
                child = parent 
            else: 
                break                
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pq.ele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        self.__percolateUp()
    
    def __percolateUp(self): 
        child = self.getSize() - 1
        while child > 0: 
            parent = (child - 1) // 2 
            if self.pq[parent].priority > self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child], self.pq[parent]
                child = parent 
            else: 
                break                
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = (self.getSize() - 1) // 2 
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[parent].priority < self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = (self.getSize() - 1) // 2 
        for parent in range(nonLeafL,-1,-1): 
            print(parent,self.pq[parent].priority)
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[parent].priority < self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            print(parent,self.pq[parent].priority)
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[parent].priority < self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        print(parent,self.pq[parent].priority)
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[parent].priority < self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
runfile('C:/Data Backup/E Drive/Learning/Python/inPlaceHeapSort.py', wdir='C:/Data Backup/E Drive/Learning/Python')
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        print('Bfr:', parent,self.pq[parent].priority)
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print('Aftr child:', child,self.pq[child].priority)
            if self.pq[parent].priority < self.pq[child].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        print('Bfr:', parent,self.pq[parent].priority)
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print('Aftr child:', child,self.pq[child].priority)
            if self.pq[parent].priority < self.pq[child].priority:
                print('yes')
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        print('Bfr:', parent,self.pq[parent].priority)
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print('Aftr child:', child,self.pq[child].priority)
            if self.pq[child].priority < self.pq[parent].priority:
                print('yes')
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
            self.printPq()
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
            self.printPq()
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            last = self.getSize() - 1 
            self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
            self.downSize()
            self.__percolateDown(self,0)
        self.setSize()
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
    
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
            self.printPq()
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            last = self.getSize() - 1 
            self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
            self.downSize()
            self.__percolateDown(0)
        self.setSize()
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            last = self.getSize() - 1 
            self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
            self.downSize()
            self.__percolateDown(0)
        self.setSize()
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
print(arr)
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            last = self.getSize() - 1 
            self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
            self.downSize()
            self.__percolateDown(0)
        self.setSize()
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.printPq()
PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            last = self.getSize() - 1 
            self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
            self.downSize()
            self.__percolateDown(0)
        self.setSize()
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            last = self.getSize() - 1 
            self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
            self.downSize()
            self.__percolateDown(0)
        self.setSize()
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
print('Final')
PriQ.heap_sort()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            print('size: ', self.getSize())
            self.printPq()
            last = self.getSize() - 1 
            self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
            self.downSize()
            self.__percolateDown(0)
        self.setSize()
    
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
print('Final')
PriQ.heap_sort()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            print('size: ', self.getSize())
            self.remove_min()            
        self.setSize()
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.remove_min()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            print(parent)
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print(child)
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            print('size: ', self.getSize())
            self.remove_min()            
        self.setSize()
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.remove_min()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            print('parent: ',parent)
            child1 = parent*2 + 1 
            child2 = parent*2+ 1
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print('child : ', child)
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            print('size: ', self.getSize())
            self.remove_min()            
        self.setSize()
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.remove_min()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            print('parent: ',parent)
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print('child : ', child)
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            print('size: ', self.getSize())
            self.remove_min()            
        self.setSize()
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.remove_min()
PriQ.printPq()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            print('parent: ',parent)
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print('child : ', child)
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 1: 
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            print('parent: ',parent)
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            print('child : ', child)
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() >= 0: 
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            self.printPq()
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 2) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if self.pq[child1].priority < self.pq[child2].priority:
                child = child1
            else: 
                child = child2 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            print(self.getSize(), end=' :  ')
            self.printPq()
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 1) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if child2 <= (self.getSize() - 1):
                if self.pq[child1].priority < self.pq[child2].priority:
                    child = child1
                else: 
                    child = child2 
            else: 
                child = child1 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            print(self.getSize(), end=' :  ')
            self.printPq()
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.printPq()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 1) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if child2 <= (self.getSize() - 1):
                if self.pq[child1].priority < self.pq[child2].priority:
                    child = child1
                else: 
                    child = child2 
            else: 
                child = child1 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            self.printPq()
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 1) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if child2 <= (self.getSize() - 1):
                if self.pq[child1].priority < self.pq[child2].priority:
                    child = child1
                else: 
                    child = child2 
            else: 
                child = child1 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 
    
    def printReverse(self): 
        for pqele in self.pq[-1::-1]: 
            print(pqele.priority,end=' ')
        print()
        return             


arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.heap_sort()
PriQ.printReverse()
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele 
        self.priority = priority



class priorityQ: 
    def __init__(self): 
        self.pq = []
        self.start  = 0 
        self.length = 0 
        return 
    
    def setSize(self): 
        self.length = len(self.pq)
        return 
    
    def upSize(self): 
        self.length += 1
        return 
    
    def downSize(self): 
        self.length -= 1
        return 
    
    def getSize(self): 
        return self.length 
    
    def insert(self,ele,priority): 
        newPqNode = pqNode(ele,priority)
        self.pq.append(newPqNode)
        self.upSize()
        return 
    
    def heapify(self): 
        nonLeafL = ((self.getSize() - 1) // 2) - 1  
        for parent in range(nonLeafL,-1,-1): 
            self.__percolateDown(parent)
        return 
    
    def __percolateDown(self,parent): 
        while (parent*2 + 1) <= (self.getSize() - 1) : 
            child1 = parent*2 + 1 
            child2 = parent*2 + 2
            if child2 <= (self.getSize() - 1):
                if self.pq[child1].priority < self.pq[child2].priority:
                    child = child1
                else: 
                    child = child2 
            else: 
                child = child1 
            
            if self.pq[child].priority < self.pq[parent].priority:
                self.pq[parent],self.pq[child] = self.pq[child],self.pq[parent]
                parent = child 
            else: 
                break 
        return 
    
    def heap_sort(self):     
        while self.getSize() > 0: 
            self.remove_min()            
        return 
    
    def remove_min(self):
        last = self.getSize() - 1 
        self.pq[last],self.pq[0] = self.pq[0],self.pq[last]
        self.downSize()
        self.__percolateDown(0)
        return 
    
    def printPq(self): 
        for pqele in self.pq: 
            print(pqele.priority,end=' ')
        print()
        
        return 



arr = [int(x) for x in input().split()]
PriQ = priorityQ()
for ele in arr:
    PriQ.insert(ele,ele)

PriQ.heapify()
PriQ.heap_sort()
PriQ.printPq()
arr.sort()
arr.sort()
print(*arr)
arr = [int(x) for x in input().split()]
arr.sort(reverse=True)
print(arr)
import heapq
li = [1,5,4,8,7,9,11]
b = heapq.heapify(li)
print(li)
print(b)
import heapq
li = [1,5,4,8,7,9,11]
heapq.heapify(li)
print(li)
print(b)
import heapq
li = [1,5,4,8,7,9,11]
heapq.heappush(li)
print(li)
print(b)
import heapq

li = [10,5,11,2,3,7,12,1,6]
heapq.heapify(li)
print(li)
import heapq

li = [10,5,11,2,3,7,12,1,6]
heapq.heapify(li)
print(li)
heapq.heappush(li,4)
li
import heapq

li = [10,5,11,2,3,7,12,1,6]
heapq.heapify(li)
print(li)
heapq.heappush(li,13)
li
import heapq

li = [10,5,11,2,3,7,12,1,6]
heapq.heapify(li)
print(li)
heapq.heappush(li,8)
li
import heapq

li = [10,5,11,2,3,7,12,1,6]
heapq.heapify(li)
print(li)
heapq.heappush(li,4)
li

## ---(Sat Dec  7 14:29:11 2019)---
import heapq
def kSmallest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq.heaify_max(arr)
    for ele in lst[k:]:
        if ele < arr[0]: 
            heapq.heapreplaace_max(arr,ele)
    return arr 

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
print(*ans)
import heapq
def kSmallest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq.heapify_max(arr)
    for ele in lst[k:]:
        if ele < arr[0]: 
            heapq.heapreplaace_max(arr,ele)
    return arr 

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
print(*ans)
runfile('C:/Data Backup/E Drive/Learning/Python/heapmax-ksmallest-elements.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import heapq
def kSmallest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq._heapify_max
    heapq.heapify_max(arr)
    for ele in lst[k:]:
        if ele < arr[0]: 
            heapq._heapreplaace_max(arr,ele)
    return arr 

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
print(*ans)
import heapq
def kSmallest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq._heapify_max(arr)
    for ele in lst[k:]:
        if ele < arr[0]: 
            heapq._heapreplaace_max(arr,ele)
    return arr 

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
print(*ans)
import heapq
def kSmallest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq._heapify_max(arr)
    for ele in lst[k:]:
        if ele < arr[0]: 
            heapq._heapreplace_max(lst,ele)
    return arr 

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
print(*ans)
import heapq
def kSmallest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq._heapify_max(arr)
    for ele in lst[k:]:
        if ele < arr[0]: 
            heapq._heapreplace_max(arr,ele)
    return arr 

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
print(*ans)
runfile('C:/Data Backup/E Drive/Learning/Python/checkmaxHeap.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/heapKthLargestElement.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import heapq

n = int(input())
arr = [int(x) for x in input().split()]
uidx = int(input())

you  = arr[uidx]
heapq._heapfiy_max(arr)
time = 0 
out = -9999999
while out < you:
    out = heapq._heappop_max(arr)
    time = time + 1

print(time)
import heapq

n = int(input())
arr = [int(x) for x in input().split()]
uidx = int(input())

you  = arr[uidx]
heapq._heapify_max(arr)
time = 0 
out = -9999999
while out < you:
    out = heapq._heappop_max(arr)
    time = time + 1

print(time)
import heapq

n = int(input())
arr = [int(x) for x in input().split()]
uidx = int(input())

you  = arr[uidx]
heapq._heapify_max(arr)
time = 0 
out = -9999999
while out < you:
    out = heapq._heappop_max(arr)
    print(out)
    time = time + 1

print(time)
runfile('C:/Data Backup/E Drive/Learning/Python/untitled4.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/heapBuyTheTicket.py', wdir='C:/Data Backup/E Drive/Learning/Python')
you  = arr[uidx]
print(you)
import heapq

n = int(input())
arr = [int(x) for x in input().split()]
uidx = int(input())

you  = arr[uidx]
print('you=',you)
heapq._heapify_max(arr)
time = 0  
out = -9999999

while out < you:
    out = heapq._heappop_max(arr)
    print('out=',out)
    time = time + 1


print('time = ', time )
import heapq

n = int(input())
arr = [int(x) for x in input().split()]
uidx = int(input())

you  = arr[uidx]
print('you=',you)
heapq._heapify_max(arr)
time = 0  
out = -9999999

while out != you:
    out = heapq._heappop_max(arr)
    print('out=',out)
    time = time + 1


print('time = ', time )
import heapq
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele
        self.priority = priority
    
    def __gt__(self,other): 
        return self.priority > other.priority
    
    def __ge__(self,other): 
        return self.priority >= other.priority
    
    def __lt__(self,other): 
        return self.priority < other.priority
    
    def __le__(self,other): 
        return self.priority <= other.priority
    
    def __eq__(self,other): 
        return self.priority == other.priority
    
    def __ne__(self,other): 
        return self.priority != other.priority



n = int(input())
lst = [int(x) for x in input().split()]
uidx = int(input())

arr  = []
for i in range(len(lst)): 
    newNode = pqNode(i,lst[i])
    arr.append(newNode)


heapq._heapify_max(arr)
time = 0  
out = -9999999

while out.ele != uidx:
    out = heapq._heappop_max(arr)
    print('out.ele=',out.ele)
    print('out.ele=',out.priority)
    time = time + 1


print('time = ', time )
import heapq
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele
        self.priority = priority
    
    def __gt__(self,other): 
        return self.priority > other.priority
    
    def __ge__(self,other): 
        return self.priority >= other.priority
    
    def __lt__(self,other): 
        return self.priority < other.priority
    
    def __le__(self,other): 
        return self.priority <= other.priority
    
    def __eq__(self,other): 
        return self.priority == other.priority
    
    def __ne__(self,other): 
        return self.priority != other.priority



n = int(input())
lst = [int(x) for x in input().split()]
uidx = int(input())

arr  = []
for i in range(len(lst)): 
    newNode = pqNode(i,lst[i])
    arr.append(newNode)


heapq._heapify_max(arr)
time = 0  
out = -9999999

while out.ele != uidx:
    out = heapq._heappop_max(arr)
    print(out)
    print('out.ele=',out.ele)
    print('out.ele=',out.priority)
    time = time + 1


print('time = ', time )
import heapq
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele
        self.priority = priority
    
    def __gt__(self,other): 
        return self.priority > other.priority
    
    def __ge__(self,other): 
        return self.priority >= other.priority
    
    def __lt__(self,other): 
        return self.priority < other.priority
    
    def __le__(self,other): 
        return self.priority <= other.priority
    
    def __eq__(self,other): 
        return self.priority == other.priority
    
    def __ne__(self,other): 
        return self.priority != other.priority



n = int(input())
lst = [int(x) for x in input().split()]
uidx = int(input())

arr  = []
for i in range(len(lst)): 
    newNode = pqNode(i,lst[i])
    arr.append(newNode)


heapq._heapify_max(arr)
time = 0  
out = pqNode(-99999999,-99999999)

while out.ele != uidx:
    out = heapq._heappop_max(arr)
    print(out)
    print('out.ele=',out.ele)
    print('out.ele=',out.priority)
    time = time + 1


print('time = ', time )
import heapq
class pqNode: 
    def __init__(self,ele,priority): 
        self.ele = ele
        self.priority = priority
    
    def __gt__(self,other): 
        return self.priority > other.priority
    
    def __ge__(self,other): 
        return self.priority >= other.priority
    
    def __lt__(self,other): 
        return self.priority < other.priority
    
    def __le__(self,other): 
        return self.priority <= other.priority
    
    def __eq__(self,other): 
        return self.priority == other.priority
    
    def __ne__(self,other): 
        return self.priority != other.priority



n = int(input())
lst = [int(x) for x in input().split()]
uidx = int(input())

arr  = []
for i in range(len(lst)): 
    newNode = pqNode(i,lst[i])
    arr.append(newNode)


heapq._heapify_max(arr)
time = 0  
out = pqNode(-99999999,-99999999)

while out.ele != uidx:
    out = heapq._heappop_max(arr)
    time = time + 1


print(time )
runfile('C:/Data Backup/E Drive/Learning/Python/heapBuyTheTicket.py', wdir='C:/Data Backup/E Drive/Learning/Python')
def fibb(n): 
    if n == 1 or n==2: 
        return 1 
    
    
    return fibb(n-1) + fibb(n-2)



n= int(input())
print(fibb(n))
runfile('C:/Data Backup/E Drive/Learning/Python/Fibonacci.py', wdir='C:/Data Backup/E Drive/Learning/Python')
def fibb(n): 
    if n == 1 or n==2: 
        return 1 
    
    return fibb(n-1) + fibb(n-2)



n= int(input())
for i in range(1,n+1):
    print(i,',',fibb(i))
class fib_data: 
    def __init__(self): 
        fibmap = {1:1,2:1}
    
    def lookup(self,n):
        if n in self.fibmap:
            return fibmap[n]
        else:
            return -1
    
    def add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self.lookup(n-1)
        if fibb1 = -1: 
            fibb1 = fibb(n-1)
            self.add_new(n-1,fibb1)
        
        fibb2 =  self.lookup(n-1)
        if fibb2 = -1: 
            fibb2 = fibb(n-1)
            self.add_new(n-1,fibb2)
        
        return fibb1 + fibb2



n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))
class fib_data: 
    def __init__(self): 
        fibmap = {1:1,2:1}
    
    def lookup(self,n):
        if n in self.fibmap:
            return fibmap[n]
        else:
            return -1
    
    def add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self.lookup(n-1)
        if fibb1 == -1: 
            fibb1 = fibb(n-1)
            self.add_new(n-1,fibb1)
        
        fibb2 =  self.lookup(n-1)
        if fibb2 == -1: 
            fibb2 = fibb(n-1)
            self.add_new(n-1,fibb2)
        
        return fibb1 + fibb2



n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))
class fib_data: 
    def __init__(self): 
        fibmap = {1:1,2:1}
    
    def lookup(self,n):
        if n in self.fibmap:
            return fibmap[n]
        else:
            return -1
    
    def add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(self,n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self.lookup(n-1)
        if fibb1 == -1: 
            fibb1 = fibb(n-1)
            self.add_new(n-1,fibb1)
        
        fibb2 =  self.lookup(n-1)
        if fibb2 == -1: 
            fibb2 = fibb(n-1)
            self.add_new(n-1,fibb2)
        
        return fibb1 + fibb2



n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))
class fib_data: 
    def __init__(self): 
        self.fibmap = {1:1,2:1}
    
    def lookup(self,n):
        if n in self.fibmap:
            return self.fibmap[n]
        else:
            return -1
    
    def add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(self,n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self.lookup(n-1)
        if fibb1 == -1: 
            fibb1 = fibb(n-1)
            self.add_new(n-1,fibb1)
        
        fibb2 =  self.lookup(n-1)
        if fibb2 == -1: 
            fibb2 = fibb(n-1)
            self.add_new(n-1,fibb2)
        
        return fibb1 + fibb2



n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))
class fib_data: 
    def __init__(self): 
        self.fibmap = {1:1,2:1}
    
    def _lookup(self,n):
        if n in self.fibmap:
            return self.fibmap[n]
        else:
            return -1
    
    def _add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(self,n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self.lookup(n-1)
        if fibb1 == -1: 
            fibb1 = self.fibb(n-1)
            self.add_new(n-1,fibb1)
        
        fibb2 =  self.lookup(n-1)
        if fibb2 == -1: 
            fibb2 = self.fibb(n-1)
            self.add_new(n-1,fibb2)
        
        return fibb1 + fibb2



n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))
class fib_data: 
    def __init__(self): 
        self.fibmap = {1:1,2:1}
    
    def _lookup(self,n):
        if n in self.fibmap:
            return self.fibmap[n]
        else:
            return -1
    
    def _add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(self,n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self._lookup(n-1)
        if fibb1 == -1: 
            fibb1 = self.fibb(n-1)
            self._add_new(n-1,fibb1)
        
        fibb2 =  self._lookup(n-1)
        if fibb2 == -1: 
            fibb2 = self.fibb(n-1)
            self._add_new(n-1,fibb2)
        
        return fibb1 + fibb2



n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))
class fib_data: 
    def __init__(self): 
        self.fibmap = {1:1,2:1}
    
    def _lookup(self,n):
        if n in self.fibmap:
            return self.fibmap[n]
        else:
            return -1
    
    def _add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(self,n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self._lookup(n-1)
        if fibb1 == -1: 
            fibb1 = self.fibb(n-1)
            self._add_new(n-1,fibb1)
        
        fibb2 =  self._lookup(n-2)
        if fibb2 == -1: 
            fibb2 = self.fibb(n-2)
            self._add_new(n-2,fibb2)
        
        return fibb1 + fibb2



n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))
def minStepsTo1DP(n,dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    if (n-1) in dp: 
        ans = dp[n-1]
    else: 
        ans = minStepsTo1DP(n-1,dp)
        dp[n-1] = ans
    
    if n % 2 == 0: 
        if (n/2) in dp: 
            ans2 = dp[n/2]
        else: 
            ans2 = minStepsTo1DP(n/2,dp)
            dp[n/2] = ans2
        ans = min(ans,ans2)
    
    if n % 3 == 0: 
        if (n/3) in dp: 
            ans3 = dp[n/3]
        else: 
            ans3 = minStepsTo1DP(n/3,dp)
            dp[n/3] = ans3
        ans = min(ans,ans3)
    
    return 1 + ans 


# Main
n=int(input())
dp = {}
print(minStepsTo1DP(n,dp))

7
def minStepsTo1DP(n,dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    if (n-1) in dp: 
        ans = dp[n-1]
    else: 
        ans = minStepsTo1DP(n-1,dp)
        dp[n-1] = ans
    
    if n % 2 == 0: 
        if (n/2) in dp: 
            ans2 = dp[n/2]
        else: 
            ans2 = minStepsTo1DP(n/2,dp)
            dp[n/2] = ans2
        ans = min(ans,ans2)
    
    if n % 3 == 0: 
        if (n/3) in dp: 
            ans3 = dp[n/3]
        else: 
            ans3 = minStepsTo1DP(n/3,dp)
            dp[n/3] = ans3
        ans = min(ans,ans3)
    
    return 1 + ans 


# Main
n=int(input())
dp = {}
print(minStepsTo1DP(n,dp))
runfile('C:/Data Backup/E Drive/Learning/Python/minStepsto1DP.py', wdir='C:/Data Backup/E Drive/Learning/Python')
runfile('C:/Data Backup/E Drive/Learning/Python/minStepsiterativeDP.py', wdir='C:/Data Backup/E Drive/Learning/Python')
for n in range(2,15):
    print(minStepsTo1DP(n,dp))
def minStepsTo1DP(n,dp):
    ''' Return Mini35mum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    if (n-1) in dp: 
        ans = dp[n-1]
    else: 
        ans = minStepsTo1DP(n-1,dp)
        dp[n-1] = ans
    
    if n % 2 == 0: 
        if (n/2) in dp: 
            ans2 = dp[n/2]
        else: 
            ans2 = minStepsTo1DP(n/2,dp)
            dp[n/2] = ans2
        ans = min(ans,ans2)
    
    if n % 3 == 0: 
        if (n/3) in dp: 
            ans3 = dp[n/3]
        else: 
            ans3 = minStepsTo1DP(n/3,dp)
            dp[n/3] = ans3
        ans = min(ans,ans3)
    
    return 1 + ans 


# Main
n=int(input())
dp = {}
for n in range(2,15):
    print(n,',',minStepsTo1DP(n,dp))
def minStepsTo1DP(n,dp):
    ''' Return Mini35mum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    if (n-1) in dp: 
        ans = dp[n-1]
    else: 
        ans = minStepsTo1DP(n-1,dp)
        dp[n-1] = ans
    
    if n % 2 == 0: 
        if (n/2) in dp: 
            ans2 = dp[n/2]
        else: 
            ans2 = minStepsTo1DP(n/2,dp)
            dp[n/2] = ans2
        ans = min(ans,ans2)
    
    if n % 3 == 0: 
        if (n/3) in dp: 
            ans3 = dp[n/3]
        else: 
            ans3 = minStepsTo1DP(n/3,dp)
            dp[n/3] = ans3
        ans = min(ans,ans3)
    
    return 1 + ans 


# Main
n=int(input())
dp = {}
for i in range(2,n):
    print(i,',',minStepsTo1DP(i,dp))
runfile('C:/Data Backup/E Drive/Learning/Python/untitled9.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import sys
def minSquares(n,dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    ans = sys.maxsize 
    for m in range(1,n+1): 
        if m**2 > n: 
            break 
        if (n-m) in dp: 
            ans1 = dp[n-m]
        else: 
            ans1 = minSquares(n-m,dp)
            dp[n-m] = ans1
        ans = min(ans,ans1)
    
    return 1 + ans 


# Main
n=int(input())
dp = {}
print(minSquares(n,dp))
import sys
def minSquares(n,dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1 or n == 0 : 
        return 1 
    
    if n in dp: 
        return dp[n]
    
    ans = sys.maxsize 
    for m in range(1,n+1): 
        k = m**2 
        if k > n: 
            break
        if (n-k) in dp: 
            ans1 = dp[n-k]
        else: 
            ans1 = minSquares(n-k,dp)
            dp[n-k] = ans1
        ans = min(ans,ans1)
    
    return 1 + ans 


# Main
n=int(input())
dp = {}
print(minSquares(n,dp))
import sys
def minSquares(n,dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 0: 
        return 0 
    
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    ans = sys.maxsize 
    for m in range(1,n+1): 
        k = m**2 
        if k > n: 
            break
        if (n-k) in dp: 
            ans1 = dp[n-k]
        else: 
            ans1 = minSquares(n-k,dp)
            dp[n-k] = ans1
        ans = min(ans,ans1)
    
    return 1 + ans 


# Main
n=int(input())
dp = {}
print(minSquares(n,dp))

3
runfile('C:/Data Backup/E Drive/Learning/Python/minSquaresDP.py', wdir='C:/Data Backup/E Drive/Learning/Python')
arr = [int(x) for x in input().split()]
print(*arr)
runfile('C:/Data Backup/E Drive/Learning/Python/LIS-DP.py', wdir='C:/Data Backup/E Drive/Learning/Python')
def find_lis(arr,lis,st=0): 
    
    curlis = 0 
    for i in range(st+1,len(arr)+1): 
        print('i=',i,'st=',st)
        if arr[i] >= arr[st]: 
            if lis[i] > -1: 
                curlis = max(curlis,lis[i])
            else: 
                newlis = find_lis(arr,lis,i)
                curlis = max(curlis,newlis)
    
    lis[st] = 1 + curlis
    
    return lis[st]


arr = [int(x) for x in input().split()]
lis = [-1 for x in range(len(arr))]
x = find_lis(arr,lis)
print(max(lis))
runfile('C:/Data Backup/E Drive/Learning/Python/LIS-DP.py', wdir='C:/Data Backup/E Drive/Learning/Python')
b = 'SEnt'
if b.lower() in 'senthil': 
    print('yes')
runfile('C:/Data Backup/E Drive/Learning/Python/LIS-DP.py', wdir='C:/Data Backup/E Drive/Learning/Python')
b = 'SEnt'
if b.lower() in 'sent': 
    print('yes')
runfile('C:/Data Backup/E Drive/Learning/Python/CS - 1 - TopInvestor.py', wdir='C:/Data Backup/E Drive/Learning/Python')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    ncr_list = ['Delhi', 'New Delhi', 'Gurgaon', 'Noida']
    if location.title() in ncr_list:
        city = 'NCR'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df.CityLocation = df.CityLocation.apply(getCity)
ncr_list = ['Bangalore', 'Mumbai', 'NCR']
cities = df.CityLocation[df.CityLocation.isin(ncr_list)]
cities
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    ncr_list = ['Delhi', 'New Delhi', 'Gurgaon', 'Noida']
    if location.title() in ncr_list:
        city = 'NCR'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df.CityLocation = df.CityLocation.apply(getCity)
ncr_list = ['Bangalore', 'Mumbai', 'NCR']
cities = df.CityLocation[df.CityLocation.isin(ncr_list)]
cities[cities=='NCR']
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    ncr_list = ['Delhi', 'New Delhi', 'Gurgaon', 'Noida']
    if location.title() in ncr_list:
        city = 'NCR'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df.CityLocation = df.CityLocation.apply(getCity)
ncr_list = ['Bangalore', 'Mumbai', 'NCR']
cities = df.CityLocation[df.CityLocation.isin(ncr_list)]

city_grp = cities.value_counts(dropna=True)
for city in city_grp.keys():
    print(city, city_grp[city])



plt.pie(city_grp,labels=city_grp.keys(),autopct='%.2f%%')
plt.axis("equal")
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    ncr_list = ['Delhi', 'New Delhi', 'Gurgaon', 'Noida']
    if location.title() in ncr_list:
        print('yes')
        city = 'NCR'
    else: 
        city = location
    return city.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df.CityLocation = df.CityLocation.apply(getCity)
ncr_list = ['Bangalore', 'Mumbai', 'NCR']
cities = df.CityLocation[df.CityLocation.isin(ncr_list)]

city_grp = cities.value_counts(dropna=True)
for city in city_grp.keys():
    print(city, city_grp[city])



plt.pie(city_grp,labels=city_grp.keys(),autopct='%.2f%%')
plt.axis("equal")
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question1_Find_City.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')
plt.bar(city_grp,labels=citygrp.keys())
plt.bar(city_grp,labels=city_grp.keys())
plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor=black))
plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor=black)
plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor='black')
plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor='black')
plt.ylabel(C"Number of Fundings')
plt.xlabel('City')
plt.title('City Vs Number of Start up Funding')
plt.show()
plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor='black')
plt.ylabel(C'Number of Fundings')
plt.xlabel('City')
plt.title('City Vs Number of Start up Funding')
plt.show()
plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor='black')
plt.ylabel('Number of Fundings')
plt.xlabel('City')
plt.title('City Vs Number of Start up Funding')
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    ncr_list = ['Delhi', 'New Delhi', 'Gurgaon', 'Noida']
    if location.title() in ncr_list:
        city = 'NCR'
        return city
    else: 
        return location.strip().title()


data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df.CityLocation = df.CityLocation.apply(getCity)
ncr_list = ['Bangalore', 'Mumbai', 'NCR']
cities = df.CityLocation[df.CityLocation.isin(ncr_list)]

city_grp = cities.value_counts(dropna=True)
for city in city_grp.keys():
    print(city, city_grp[city])



plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor='black')
plt.ylabel('Number of Fundings')
plt.xlabel('Location')
plt.title('City Vs Number of Start up Funding')
plt.show()
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip().title())


inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question2_Find_Investor.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')

## ---(Fri Dec 13 13:35:36 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question2_Find_Investor.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')
df
df.iloc[1]['InvestorsName']
df.iloc['InvestorsName'][1]
df.iloc[1]['InvestorsName']
len(df)
df.InvestorsName[1]
len(df.InvestorsName)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
startups= []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip().title())
            startups.append(startUp)


inv_st_df = pd.DataFrame(investors,startups,columns['InvestorsName', 'StartUp'])
inv_st_df
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
startups= []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip().title())
            startups.append(startUp)


inv_st_df = pd.DataFrame(investors,startups,columns=['InvestorsName', 'StartUp'])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])



inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
inv_st_df
inv_st_df.iloc[1,:]
inv_st_df.describe()
inv_st_df.head()
groupcols = inv_st_df['StartUp'].groupby['InvestorsName'].size()
groupcols
groupcols = inv_st_df[['StartUp']].groupby['InvestorsName'].size()
groupcols = inv_st_df.groupby['InvestorsName'].size()
groupcols = inv_st_df.groupby['InvestorsName']
groupcols = inv_st_df['StartUp'].groupby(['InvestorsName']).sizer()
inv_st_def.keys()
inv_st_df.keys()
groupcols = inv_st_df['StartUp'].groupby(['InvestorsName']).size()
groupcols = inv_st_df['StartUp'].groupby('InvestorsName').size()
groupcols = inv_st_df.groupby(['InvestorsName'])
groupcols
groupcols.keys()
groupcols.size()
groupcols = inv_st_df.groupby(['InvestorsName']).size()
groupcols
groupcols = inv_st_df.groupby(['InvestorsName', 'StartUp'])
groupcols
groupcols.size()
groupcols.groupby(['InvestorsName']).size()
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = pd.DataFrame(inv_st_df.groupby(['InvestorsName', 'StartUp']))
groupcols
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName', 'StartUp'])
groupcols
groupcols.keys()
groupcols.index
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])



inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName', 'StartUp'])
print(groupcols)
groupcols.agg(['InvestorsName']).size())
groupcols.agg(['InvestorsName']).size()
groupcols.size()
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = pd.DataFrame(inv_st_df.groupby(['InvestorsName', 'StartUp']).size())
groupcols
groupcols.index
groupcols.keys()
groupcols.describe()
grouipcols.groupby(['InvestorsName']).size()
groupcols.groupby(['InvestorsName']).size()
groupcols.groupby(['InvestorsName']).value_counts()
groupcols.InvestorsName.value_counts()
groupcols.desribe()
groupcols.describe()
len(groupcols)
for i in range(len(groupcols)): 
    print(groupcols[i])
for i in range(len(groupcols)): 
    print(groupcols.iloc[i])
for i in range(len(groupcols)): 
    print(groupcols.iloc[i][0])
for i in range(len(groupcols)): 
    print(groupcols.iloc[i][1])
print(groupcols)
for i in range(5): 
    print(groupcols.iloc[i])
for i in range(5): 
    print(groupcols.iloc[i,1])
for i in range(5): 
    print(groupcols.iloc[i,0])
for i in range(5): 
    print(groupcols.iloc[i,1])
for i in range(5): 
    print(groupcols.iloc[1,i])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])



inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = pd.DataFrame(inv_st_df.groupby(['InvestorsName', 'StartUp']).size())
print(groupcols)
for i in range(5): 
    print(groupcols.iloc[1)
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])



inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = pd.DataFrame(inv_st_df.groupby(['InvestorsName', 'StartUp']).size())
print(groupcols)
for i in range(5): 
    print(groupcols.iloc[i])
for i in range(5): 
    print(groupcols.iloc[i].Name)
print(groupcols)
for i in range(5): 
    print(groupcols[i])
for i in range(5): 
    print(groupcols[i])
inv_st_df
inv_st_df.InvestorsName
inv_st_df.StartUp
df.unique(['InvestorsName','StartUp])
df.unique(['InvestorsName','StartUp'])
groupcols = pd.DataFrame(inv_st_df.groupby(['InvestorsName', 'StartUp']),columns=['Investor','StartUp','count'])
groupcols = pd.DataFrame(inv_st_df.groupby(['InvestorsName', 'StartUp']),columns=['Investor','StartUp'])
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = pd.DataFrame(inv_st_df.groupby(['InvestorsName', 'StartUp']).count())
groupcols
len(groupcols)
for i in range(5):
    print(groupcols[i])
for i in range(5):
    print(groupcols.iloc[i])
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
groupcols = groupcols.sort_values()
groupcols
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()

groupcols
for i in groupcols.keys(): 
    print(i)
groupcols.keys()
groupcols.value()
groupcols.values()
groupcols.index
for i in groupcols.index: 
    print(groupcols.iloc[i])
for group in groupcols: 
    print(group)
print(groupcols)
print(groupcols.head())
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
output    = pd.DataFrame({'count' : inv_st_df.groupby(['InvestorsName','StartUp']).count()})
print(output)
output    = pd.DataFrame({'count' : inv_st_df.groupby(['InvestorsName','StartUp']).count()}).reset_index()
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index(name='Count'))
df1.head()
df1 = pd.DataFrame(groupcols.reset_index()
df1.head()
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index()
df1.head()
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index()
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index())
df1.head()
final = df1.InvestorsName.value_counts()
final
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp'])
df1 = pd.DataFrame(groupcols.reset_index())
final = df1.InvestorsName.value_counts()
final
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index())
final = df1.InvestorsName.value_counts()
final
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question3_Find_Investor_By_Start_Up.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

## As the investors column has multiple investors, we are exploding it into multiple records.  
## For example, if one Startup has three investors it will be exploded into three rows. 
investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])

inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])

## Grouping the records by InvestorsName and Start Up to get the Unique List of Start UPs invested by 
## an Investor           
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index())
freq = df1.InvestorsName.value_counts()

for investor in freq.keys()[:5]:
    print(investor,freq[investor])

## ---(Fri Dec 13 16:56:34 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question3_Find_Investor_By_Start_Up.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question4_Find_Investor_By_InvestmentType.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 


def resolveInvestmentType(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip().title()



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if investor.lower() == 'indian angels network' or investor.lower() == 'indian angel network (ian)': 
        return 'Indian Angel Network'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()



df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(resolveInvestmentType)

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
undis_inv = ['Undisclosed Investor', 'Undisclosed Investors', 'Undisclosed investors']
df = df[not (df.InvestorsName.isin(undis_inv)) & (df.InvestorsName != 'Undisclosed investors') & ((df.InvestmentType == 'Crowd Funding') | (df.InvestmentType == 'Seed Funding'))]

## As the investors column has multiple investors, we are exploding it into multiple records.  
## For example, if one Startup has three investors it will be exploded into three rows. 
investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])

inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])

## Grouping the records by InvestorsName and Start Up to get the Unique List of Start UPs invested by 
## an Investor           
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index())
freq = df1.InvestorsName.value_counts()

for investor in freq.keys()[:5]:
    print(investor,freq[investor])
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs': 
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com': 
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit': 
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace': 
        String = 'Paytm'
    return String 


def resolveInvestmentType(String):
    outStr = ''
    char ='a'
    prevchar = ''
    
    for char in String: 
        if prevchar != ' ': 
            if char.isupper(): 
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char    
        else: 
            outStr = outStr + char
        prevchar = char 
    return outStr.strip().title()



def str2int(string): 
    return int(string.replace(',',''))



# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp


def resolveInvestor(investor):
    
    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if investor.lower() == 'indian angels network' or investor.lower() == 'indian angel network (ian)': 
        return 'Indian Angel Network'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 


data = pd.read_csv('startup_funding.csv')
df   = data.copy()



df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(resolveInvestmentType)

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df = df[(df.InvestorsName != 'Undisclosed Investor') & (df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors') & ((df.InvestmentType == 'Crowd Funding') | (df.InvestmentType == 'Seed Funding'))]

## As the investors column has multiple investors, we are exploding it into multiple records.  
## For example, if one Startup has three investors it will be exploded into three rows. 
investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])

inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])

## Grouping the records by InvestorsName and Start Up to get the Unique List of Start UPs invested by 
## an Investor           
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index())
freq = df1.InvestorsName.value_counts()

for investor in freq.keys()[:5]:
    print(investor,freq[investor])
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question5_Find_Investor_By_PrivateEquity.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/test.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')

## ---(Wed Dec 18 10:05:04 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/sqlite_example.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
import sqlite3 as sq
db  = sq.connect('IMDB.sqlite')
db
import sqlite3 as sq
db  = sq.connect('school.sqlite')
db
import sqlite3 as sq
db  = sq.connect('school.sqlite')
cur = db.cursor();
sql_query = 'create table Student (RollNumber int Primary key, Name text, Age int)'
cur.execute(sql_query)
ist_query = 'insert into Student Values(101,"Aman",20)'
cur.execute(ist_query)
import sqlite3 as sq
db  = sq.connect('school.sqlite')
cur = db.cursor();
sql_query = 'create table Student (RollNumber int Primary key, Name text, Age int)'
cur.execute(sql_query)
ist_query = 'insert into Student Values(101,"Aman",20)'
cur.execute(ist_query)
db.commit()
ist_query = 'insert into Student Values(101,"Aman",20)'
cur.execute(ist_query)
db.commit()
ist_query = 'insert into Student values(101,"Aman",20)'
cur.execute(ist_query)
db.commit()
db.commit()
ist_query = 'insert into Student values(101,"Aman",20)'
cur.execute(ist_query)

## ---(Wed Dec 18 10:58:27 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/sqlite_example.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
ist_query = 'insert into Student values(101,"Aman",20)'
cur.execute(ist_query)
db.commit()
ist_query = 'insert into Student values(102,"Amit",25)'
cur.execute(ist_query)
db.commit()
db.close()
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/sqlite_example.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
dlt = (26, )
dlt
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/sqlite_example1.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
ame=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
age=[25,27,25,24,30,26,23,26,25,26,29,24]
department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]


ist_qry = 'insert into Employee_Detail values(?,?,?,?,?)'
tup_list = [(employee_id[i],name[i],age[i],department[i],salary[i]) for i in range(len(employee_id))]
#
name=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
age=[25,27,25,24,30,26,23,26,25,26,29,24]
department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]


ist_qry = 'insert into Employee_Detail values(?,?,?,?,?)'
tup_list = [(employee_id[i],name[i],age[i],department[i],salary[i]) for i in range(len(employee_id))]
employee_id=[101,102,103,104,105,106,107,108,109,110,111,112,113]
name=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
age=[25,27,25,24,30,26,23,26,25,26,29,24]
department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]


ist_qry = 'insert into Employee_Detail values(?,?,?,?,?)'
tup_list = [(employee_id[i],name[i],age[i],department[i],salary[i]) for i in range(len(employee_id))]
print(len(employee_id),len(name), len(age), len(department),len(salary))
tup_list = [(employee_id[i],name[i],age[i],department[i],salary[i]) for i in range(len(name))]
import sqlite3 as sq
db = sq.connect('Company.sqlite')
cur = db.cursor()
dlt = (102, )
del_qry = 'delete from EmployeeDetail where employee_id = ?'
cur.execute(del_qry,dlt)
db.commit()
db.close()
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/updateSQL.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
tup_list
import sqlite3 as sq
db = sq.connect('Company.sqlite')
cur = db.cursor()
employee_id=[101,102,103,104,105,106,107,108,109,110,111,112,113]
name=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
age=[25,27,25,24,30,26,23,26,25,26,29,24]
department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]

print(len(employee_id),len(name), len(age), len(department),len(salary))

ist_qry = 'insert into EmployeeDetail values(?,?,?,?,?)'
tup_list = [(employee_id[i],name[i],age[i],department[i],salary[i]) for i in range(len(name))]
cur.execute(ist_qry,tup_list)

db.commit()
db.close()
tup_list
import sqlite3 as sq
db = sq.connect('Company.sqlite')
cur = db.cursor()
employee_id=[101,102,103,104,105,106,107,108,109,110,111,112,113]
name=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
age=[25,27,25,24,30,26,23,26,25,26,29,24]
department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]

print(len(employee_id),len(name), len(age), len(department),len(salary))

ist_qry = 'insert into EmployeeDetail values(?,?,?,?,?)'
tup_list = [(employee_id[i],name[i],age[i],department[i],salary[i]) for i in range(len(name))]
cur.executemany(ist_qry,tup_list)

db.commit()
db.close()
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/test.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
import sqlite3 as sq
db = sq.connect('Employee.sqlite')
cur= db.cursor()
fet_qry = 'select * from Employee_Detail where department =  "Finance"'
out = cur.fetchall()
print(out)
import sqlite3 as sq
db = sq.connect('Employee.sqlite')
cur= db.cursor()
fet_qry = 'select * from Employee_Detail where department =  "Finance"'
cur.execute(fet_qry)
out = cur.fetchall()
print(out)
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/groupBySQL.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
import sqlite as sq
db = sq.connect('school.sqlite')

## Create Faculty table with fields ID, Name, Course, Salary

fac_list = [[101,'Senthil','Science',10000],[102,'Eswari','Biology',20000],[103,'Baargavi','Psychology',3000000]]
data     = pd.DataFrame(fac_list,columns=['ID','Name','Course','Salary'])
pd.to_sql(data,db)
import sqlite3 as sq
db = sq.connect('school.sqlite')

## Create Faculty table with fields ID, Name, Course, Salary

fac_list = [[101,'Senthil','Science',10000],[102,'Eswari','Biology',20000],[103,'Baargavi','Psychology',3000000]]
data     = pd.DataFrame(fac_list,columns=['ID','Name','Course','Salary'])
pd.to_sql(data,db)
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/createTablefromPandas.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
data
import sqlite3 as sq
import pandas as pd
db = sq.connect('school.sqlite')

## Create Faculty table with fields ID, Name, Course, Salary

fac_list = [[101,'Senthil','Science',10000],[102,'Eswari','Biology',20000],[103,'Baargavi','Psychology',3000000]]
data     = pd.DataFrame(fac_list,columns=['ID','Name','Course','Salary'])
data.to_sql('Faculty',db)
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/groupbyGenreIMDB.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
for i in range(len(out)):
    x = out[i]
    print(x[0],x[1])
for i in range(len(out)):
    print(out[i][0],out[i][1])
import sqlite3 as sq
import pandas as pd
fet_qry = 'select * from earning'
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query(fet_qry,db)
data
data.total = data.Domestic + data.Worldwide
data
data['total'] = data.Domestic + data.Worldwide
data
max(data['total'])
data = data[data.Movie_id == max(data.total)]
data
data = data[data.total == max(data.total)]
import sqlite3 as sq
import pandas as pd
fet_qry = 'select * from earning'
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query(fet_qry,db)
data['total'] = data.Domestic + data.Worldwide
data = data[data.total == max(data.total)]
data
data.Movie_id
data.Movie_id.tolist()
import sqlite3 as sq
import pandas as pd
fet_qry = 'select * from earning'
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query(fet_qry,db)
data['total'] = data.Domestic + data.Worldwide
filter = data[data.total == max(data.total)]
filter.Movie_id.tolist()
int(filter.Movie_id.tolist()[0])
import sqlite3 as sq
import pandas as pd
fet_qry = 'select * from earning'
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query(fet_qry,db)
data['total'] = data.Domestic + data.Worldwide
filter = data[data.total == max(data.total)]
movie_id = int(filter.Movie_id.tolist()[0])
import sqlite3 as sq
import pandas as pd
fet_qry = 'select * from earning'
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query(fet_qry,db)
data['total'] = data.Domestic + data.Worldwide
filter = data[data.total == max(data.total)]
movie_id = int(filter.Movie_id.tolist()[0])
fet_qry = 'select Rating from IMDB where Movie_id = ?'
cur = db.cursor()
cur.execute(fet_qry,movie_id)
out = cur.fetchall()
print(out)
import sqlite3 as sq
import pandas as pd
fet_qry = 'select * from earning'
db = sq.connect('IMDB.sqlite')
data = pd.read_sql_query(fet_qry,db)
data['total'] = data.Domestic + data.Worldwide
filter = data[data.total == max(data.total)]
movie_id = filter.Movie_id.tolist()[0]
fet_qry = 'select Rating from IMDB where Movie_id = ?'
cur = db.cursor()
cur.execute(fet_qry,movie_id)
out = cur.fetchall()
print(out)
movie_id
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/highestGrosser.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
vote_db = data[data.TotalVotes == max(TotalVotes)]
print(vote_db)
data
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
vote_db = data[data.TotalVotes == max(data.TotalVotes)]
print(vote_db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Runtime == '']
data['Runtime'] = data['Runtime'].apply(lambda x: x.split()[0])
data.Runtime
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Runtime != '']
data['Runtime'] = data['Runtime'].apply(lambda x: x.split()[0])
data.Runtime
vote_db = data[data.Runtime == max(data.Runtime)]
print(vote_db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Runtime != '']
data['Runtime'] = data['Runtime'].apply(lambda x: x.split()[0])
data.Runtime
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Runtime != '']
data['Runtime'] = data['Runtime'].apply(lambda x: x.split()[0])
long_db = data[data.Runtime == max(data.Runtime)]
print(long_db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Runtime != '']
data['Runtime'] = data['Runtime'].apply(lambda x: x.split()[0])
long_db = data[data.Runtime == max(data.Runtime)]
print(long_db.Title, longdb.Runtime)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Runtime != '']
data['Runtime'] = data['Runtime'].apply(lambda x: x.split()[0])
long_db = data[data.Runtime == max(data.Runtime)]
print(long_db.Title, long_db.Runtime)
print(long_db.Runtime)
print(long_db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Runtime != '']
data['Runtime'] = data['Runtime'].apply(lambda x: int(x.split()[0]))
long_db = data[data.Runtime == max(data.Runtime)]
print(long_db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data['Profit'] = data['Worldwide'] + data['Domestic'] - data[['budget']
data.Profit
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data['Profit'] = data['Worldwide'] + data['Domestic'] - data[['budget']
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select * from IMDB'
data = pd.read_sql_query(fet_qry,db)
data['Profit'] = data['Worldwide'] + data['Domestic'] - data['budget']
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Title, (b.Worldwide+b.Domestic-a.Budget) as Profit  from IMDB a inner join earning b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
data
data.head()
profit_db = data[data.Profit == max(data.Profit)]
profit_db
profit_db.Profit
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (b.Worldwide+b.Domestic-a.Budget) as Profit  from IMDB a inner join earning b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
profit_db = data[data.Profit == max(data.Profit)]
profit_db.Profit
profit_db.Movie_id
profit_db.Title
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (b.Worldwide+b.Domestic-a.Budget) as Profit, a.Budget from IMDB a inner join earning b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
budget_db = data[data.Budget == min(data.Budget)]
budget_db
data.Budget
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (b.Worldwide+b.Domestic-a.Budget) as Profit, a.Budget from IMDB a inner join earning b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
data = data[data.Budget!=' ']
data.Budget = data.Budget.apply(lambda x:float(x))
data.Budget = data.Budget.apply(lambda x:int(x))
data = data[data.Budget!='']
data.Budget = data.Budget.apply(lambda x:int(x))
budget_db = data[data.Budget == min(data.Budget)]
budget_db
def getYear(title):
    year = title.trim()[-2:-6:-1]
    return year
string = 'Short Term 12 (2013)'
print(getYear(string))
def getYear(title):
    year = title.strip()[-2:-6:-1]
    return year
string = 'Short Term 12 (2013)'
print(getYear(string))
def getYear(title):
    year = title.strip()[-5:-1]
    return year
string = 'Short Term 12 (2013)'
print(getYear(string))
import sqlite3 as sq
import pandas as pd

def getYear(title):
    year = title.strip()[-5:-1]
    return int(year)



db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (b.Worldwide, b.Domestic) as Total from IMDB a inner join earning b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
data['Year'] = data.Title.apply(getYear)
data.Year
import sqlite3 as sq
import pandas as pd

def getYear(title):
    year = title.strip()[-5:-1]
    return int(year)



db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (b.Worldwide, b.Domestic) as gross_amt from IMDB a inner join earning b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
data['Year'] = data.Title.apply(getYear)
data.Year
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/IMDBYearTop.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
data.Year
data.gross_amt
year_db = data.groupby(['Year'])['gross_amt'].max()
year_db
year_db = data.groupby(['Year'])['gross_amt'].max().reset_index()
year_db
year_db.tolist()
for i in year_db: 
    print(year_db[i])
for i in year_db.keys(): 
    print(year_db[i])
for i in year_db.keys(): 
    print(i, year_db[i])
k = 0 
for i in year_db.keys(): 
    print(k)
    k = k + 1
    print(i, year_db[i])
out_db = pd.merge(year_db, data, how='left', left_on=['Year', 'gross_amt'], right_on =['Year', 'gross_amt'])
out_db
out_db.head()
out_db.columns()
out_db.Year
out_db.gross_amt
out_db.Title
print(out_db.Year)
print(out_db.Title)
q
import pandas as pd

def getBudget(budget):
    if budget.strip() == '': 
        budget = '0'
    
    return int(budget)



db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, a.Budget, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
data.Budget = data.Budget.apply(getBudget)
import sqlite3 as sq
import pandas as pd

def getBudget(budget):
    if budget.strip() == '': 
        budget = '0'
    
    return int(budget)



db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, a.Budget, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id'
data = pd.read_sql_query(fet_qry,db)
data.Budget = data.Budget.apply(getBudget)
a = 5.0 
print(dataype(a))
a = 5.0 
print(dtype(a))
a = 5.0 
print(type(a))
a = '5.0' 
print(type(a))
data.Budget[data.Budget==''] = 0.0
budget_db= data.groupby(['genre'])['Budget'].sum().reset_index()
budget_db
import sqlite3 as sq
import pandas as pd



db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, a.Budget, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id where b.genre > ""
data = pd.read_sql_query(fet_qry,db)
data.Budget[data.Budget==''] = 0.0
budget_db= data.groupby(['genre'])['Budget'].sum().reset_index()
budget_db

year_db = data.groupby(['Year'])['gross_amt'].max().reset_index()
import sqlite3 as sq
import pandas as pd



db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, a.Budget, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id where b.genre > ""'
data = pd.read_sql_query(fet_qry,db)
data.Budget[data.Budget==''] = 0.0
budget_db= data.groupby(['genre'])['Budget'].sum().reset_index()
budget_db
year_db.genre
year_db[0]
year_db.Budget
year_db
budget_db.genre
budget_db.genre.tolist()
for i in budget_db.genre: 
    print(i)
for i in len(budget_db.genre): 
    print(budget_db.genre.iloc[i])
for i in len(budget_db.genre): 
    print(budget_db.iloc[0,1]
print(budget_db.iloc[0,1])
print(budget_db.iloc[0,2])
print(budget_db.iloc[0,1])
print(budget_db.iloc[0,0)
print(budget_db.iloc[0,0])
print(budget_db.iloc[0,0], budget_db.iloc[0,1])
print(budget_db.iloc[1,0], budget_db.iloc[1,1])
budget_db.Budget.sum()
budget_db.genre.tolist()
budget_db.Budget.tolist()
total = budgets.sum()
genres = ['Action',  'Adventure',  'Animation',  'Biography',  'Comedy',  'Crime',  'Drama',  'Family',  'Fantasy',  'History',  'Horror',  'Music',  'Musical',  'Mystery',  'Romance',  'Sci-Fi',  'Sport',  'Thriller',  'War',  'Western']
budgets = [4332500000.0,  6046700000.0,  1845200000.0, 624500000.0, 1740100000.0, 426500000.0, 2614400000.0, 460000000.0, 1094000000.0, 173000000.0, 6600000.0, 37300000.0, 61000000.0, 469000000.0, 270900000.0, 2596000000.0, 110000000.0, 961500000.0, 87000000.0, 138000000.0]
total = budgets.sum()
total = sum(budgets)
len(genres)
len(budgets)
for i in range(len(genres)): 
    print(genres[i], (%.2f)%(budgets[i]/total))
for i in range(len(genres)): 
    print(genres[i], "%.2f"%(budgets[i]/total))
for i in range(len(genres)): 
    print(genres[i], "%.2f"%(budgets[i]/total*100))
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (c.Worldwide+c.Domestic) as gross_amt, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id inner join earning c on b.Movie_id = c.Movie_id where b.genre > ""'
data = pd.read_sql_query(fet_qry,db)
import sqlite3 as sq
import pandas as pd



db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, a.Budget, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id where b.genre > ""'
data = pd.read_sql_query(fet_qry,db)
data.Budget[data.Budget==''] = 0.0
budget_db= data.groupby(['genre'])['Budget'].sum().reset_index()

budget_db.genre.tolist()
budget_db.Budget.tolist()
total = budget_db.Budget.sum()

genres = ['Action',  'Adventure',  'Animation',  'Biography',  'Comedy',  'Crime',  'Drama',  'Family',  'Fantasy',  'History',  'Horror',  'Music',  'Musical',  'Mystery',  'Romance',  'Sci-Fi',  'Sport',  'Thriller',  'War',  'Western']
budgets = [4332500000.0,  6046700000.0,  1845200000.0, 624500000.0, 1740100000.0, 426500000.0, 2614400000.0, 460000000.0, 1094000000.0, 173000000.0, 6600000.0, 37300000.0, 61000000.0, 469000000.0, 270900000.0, 2596000000.0, 110000000.0, 961500000.0, 87000000.0, 138000000.0]
total = sum(budgets)
for i in range(len(genres)): 
    print(genres[i], "%.2f"%(budgets[i]/total*100))
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (c.Worldwide+c.Domestic) as gross_amt, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id inner join earning c on b.Movie_id = c.Movie_id where b.genre > ""'
data = pd.read_sql_query(fet_qry,db)
earning_db= data.groupby(['genre'])['gross_amt'].sum().reset_index()
earning_db.genre.tolist()
earning_db.gross_amt.tolist()
genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
earnings = [27885213953.0, 36692818946.0, 10536209978.0, 5323303470.0, 11974693315.0, 2411969301.0, 18616065573.0, 1633853910.0, 8022713254.0, 1625677156.0, 14705802.0, 675707163.0, 590619540.0, 3134103383.0, 2263643052.0, 15488406870.0, 505861100.0, 6881591415.0, 395710609.0, 1011693604.0]
len(genres)
len(earnings)
genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
earnings = [27885213953.0, 36692818946.0, 10536209978.0, 5323303470.0, 11974693315.0, 2411969301.0, 18616065573.0, 1633853910.0, 8022713254.0, 1625677156.0, 14705802.0, 675707163.0, 590619540.0, 3134103383.0, 2263643052.0, 15488406870.0, 505861100.0, 6881591415.0, 395710609.0, 1011693604.0]
total = sum(earnings)
for i in range(len(genres)): 
    print(genres[i], "%.2f"%(earnings[i]/total*100))
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.genre, b.Title, b.Rating from genre a inner join IMDB b on a.Movie_id = b.Movie_id where b.genre in ("Sci-Fi", "Mystery")'
genre_data = pd.read_sql_query(fet_qry,db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.genre, b.Title, b.Rating from genre a inner join IMDB b on a.Movie_id = b.Movie_id where a.genre in ("Sci-Fi", "Mystery")'
genre_data = pd.read_sql_query(fet_qry,db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.genre, b.Title, b.Rating from genre a inner join IMDB b on a.Movie_id = b.Movie_id where a.genre in ("Sci-Fi", "Mystery") and b.Rating >= 8.0'
genre_data = pd.read_sql_query(fet_qry,db)
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id from genre a inner join IMDB b on a.Movie_id = b.Movie_id where a.genre in ("Sci-Fi", "Mystery") and b.Rating >= 8.0 group by a.Movie_id having count(*) > 1'
genre_data = pd.read_sql_query(fet_qry,db)
genre_data
genre_data.iloc[0,0]
fet_qry = 'select Title from IMDB where Movie_id = ?'
cur = db.cursor()
cur.execute(fet_qry,(movie_id,))
out = cur.fetchall()
print(out)
movie_id = genre_data.iloc[0,0]
fet_qry = 'select Title from IMDB where Movie_id = ?'
cur = db.cursor()
cur.execute(fet_qry,(movie_id,))
out = cur.fetchall()
print(out)
runfile('C:/Data Backup/E Drive/Learning/Python/api/http_libraries.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
import requests
response = requests.get('https://codingninjas.in/api/v3/events')
print(response.status_code)
print(response.headers['content-type'])
print(response.text)
import requests
response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.status_code)
import requests
response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.status_code)
print(response.text)
print(response.headers['content-type'])
import json 
json_data = {"Student":"Senthil", "Age":38, "Occupation":'SDE2"}
python_data = json.loads(json_data)
print(python_data)
import json 
json_data = {"Student":"Senthil", "Age":38, "Occupation":"SDE2"}
python_data = json.loads(json_data)
print(python_data)
import json 
json_data = '{"Student":"Senthil", "Age":38, "Occupation":"SDE2"}'
python_data = json.loads(json_data)
print(python_data)
runfile('C:/Data Backup/E Drive/Learning/Python/api/HoundsubBreeds.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
a = {"name":"Senthil","Age":25,"location":"Madurai"}
print(a.keys())
a = {"name":"Senthil","Age":25,"location":"Madurai"}
for i in a: 
    print(i)
a = {"name":"Senthil","Age":25,"location":"Madurai"}
for i in a: 
    print(i,a[i])

## ---(Fri Dec 27 16:29:13 2019)---
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (c.Worldwide+c.Domestic) as gross_amt, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id inner join earning c on b.Movie_id = c.Movie_id where b.genre > ""'
data = pd.read_sql_query(fet_qry,db)
earning_db= data.groupby(['genre'])['gross_amt'].sum().reset_index()

earning_db.genre.tolist()
earning_db.gross_amt.tolist()
runfile('C:/Data Backup/E Drive/Learning/Python/sqlite/IMDBGenreEarning.py', wdir='C:/Data Backup/E Drive/Learning/Python/sqlite')
import sqlite3 as sq
import pandas as pd

db = sq.connect('IMDB.sqlite')
fet_qry = 'select a.Movie_id, a.Title, (c.Worldwide+c.Domestic) as gross_amt, b.genre from IMDB a inner join genre b on a.Movie_id = b.Movie_id inner join earning c on b.Movie_id = c.Movie_id where b.genre > ""'
data = pd.read_sql_query(fet_qry,db)
earning_db= data.groupby(['genre'])['gross_amt'].sum().reset_index()
earning_db.genre.tolist()
earning_db.gross_amt.tolist()

## ---(Sat Dec 28 18:08:07 2019)---
runfile('C:/Data Backup/E Drive/Learning/Python/api/httpAuth.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
python_data = {}
python_data['name'] = 'Senthil'
python_data['age'] = 38
python_data['language'] = ['Python','Java','COBOL', 'REXX']
python_data
import json
json_data = json.dumps(python_data)
print(json_data)
python_data = {}
python_data['name'] = 'Senthil'
python_data['age'] = 38
python_data['language'] = ['Python','Java','COBOL', 'REXX']
python_data['Married'] = None
python_data
json_data = json.dumps(python_data)
print(json_data)
runfile('C:/Data Backup/E Drive/Learning/Python/api/httpAuth.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
runfile('C:/Data Backup/E Drive/Learning/Python/api/reddit_api.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
import requests
import json 
data = {'client_id':'d8HMWp_QC0GI4w', 'response_type':'code','state':'random_123', 'redirect_uri':'https://www.google.com/','scope':'read'}
response = requests.get('https://www.reddit.com/api/v1/authorize',params=data)
print(response.status_code)
print(response.url)
data = {'grant_type':'authorization_code','code':'FV5xCxvNtJK2UdhG_BUMUmVFMIE',
        'redirect_uri':'https://www.google.com/'}
r  = response.post('https://www.reddit.com/api/v1/access_token',data=data,
                   auth=('Senthilmano81','hoLlZYOSWwyHG3AgAWM2_AxVJhM'),
                   headers={'User-agent':'senthilmano'})
print(r.text)
data = {'grant_type':'authorization_code','code':'FV5xCxvNtJK2UdhG_BUMUmVFMIE',
        'redirect_uri':'https://www.google.com/'}
r  = requests.post('https://www.reddit.com/api/v1/access_token',data=data,
                   auth=('Senthilmano81','hoLlZYOSWwyHG3AgAWM2_AxVJhM'),
                   headers={'User-agent':'senthilmano'})
print(r.text)
data = {'grant_type':'authorization_code','code':'FV5xCxvNtJK2UdhG_BUMUmVFMIE',
        'redirect_uri':'https://www.google.com/'}
r  = requests.post('https://www.reddit.com/api/v1/access_token',data=data,
                   auth=('Senthilmano81','hoLlZYOSWwyHG3AgAWM2_AxVJhM'),
                   headers={'User-agent':'xyzabc123'})
print(r.text)
import ssl
ssl.OPENSSL_VERSION
import ssl
data = {'grant_type':'authorization_code','code':'FV5xCxvNtJK2UdhG_BUMUmVFMIE',
        'redirect_uri':'https://www.google.com/'}
r  = requests.post('https://www.reddit.com/api/v1/access_token',data=data,
                   auth=('Senthilmano81','hoLlZYOSWwyHG3AgAWM2_AxVJhM'),
                   headers={'User-agent':'xyzabc123'})
print(r.text)
runfile('C:/Data Backup/E Drive/Learning/Python/api/reddit_api.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
data = {'grant_type':'authorization_code','code':'FV5xCxvNtJK2UdhG_BUMUmVFMIE',
        'redirect_uri':'https://www.google.com/'}
r  = requests.post('https://www.reddit.com/api/v1/access_token',verify=False,data=data,
                   auth=('Senthilmano81','hoLlZYOSWwyHG3AgAWM2_AxVJhM'),
                   headers={'User-agent':'xyzabc123'})
print(r.text)
r  = requests.post('https://www.reddit.com/api/v1/access_token',data=data,
                   auth=('Senthilmano81','hoLlZYOSWwyHG3AgAWM2_AxVJhM'),
                   headers={'User-agent':'xyzabc123'})
print(r.text)
import requests
import json 
r = requests.get('https://api.github.com/orgs/codingninjascodes/repos')
python_data = json.loads(r.text)
for i in range(len(python_data)): 
    data = python_data[i]
    if data['fork']!='true':
            print(data['name'],data['watchers'],data['forks'])
runfile('C:/Data Backup/E Drive/Learning/Python/api/api2-githuborganisationrepo.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
runfile('C:/Data Backup/E Drive/Learning/Python/api/createGitHubRepos_BasicAuth.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
import requests
import json 
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':'random_123','scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
runfile('C:/Data Backup/E Drive/Learning/Python/api/APIgitHUB-OAuth.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'006aaddad8ee7782edec','https://www.google.com','state':'random_123'}
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'006aaddad8ee7782edec','https://www.google.com'}
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'006aaddad8ee7782edec','https://www.google.com','state':'random_123'}
info = {'client_id':'9cc675d93b9bc2d21620'}
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6'}
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'006aaddad8ee7782edec'}
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'006aaddad8ee7782edec','redirect_uri':'https://www.google.com','state':'random_123'}
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'006aaddad8ee7782edec','redirect_uri':'https://www.google.com','state':'random_123'}
r =requests.post('https://github.com/login/oauth/access_token',data=info,
                 headers={'User-Agent':'SenthilMano'})
print(r.text)
import requests
import json 

## Getting Authorization Grant using CLient ID
## data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':'random_123','scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
## r = requests.get('https://github.com/login/oauth/authorize',params=data)
## print(r.status_code)
## print(r.url)

## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'006aaddad8ee7782edec','redirect_uri':'https://www.google.com','state':'random_123'}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
print(r.text)
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':'random_123','scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'135549bba8e9a36f3bb0','redirect_uri':'https://www.google.com','state':'random_123'}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
print(r.text)
python_data = r.text
access_string python_data.split('&')[0]
python_data = r.text
access_string = python_data.split('&')[0]
access_string
access_token = access_string.split('=')[1]
print(access_token)
info = {'name':'New_Repo','description':'Created via API Call1', 'auto_init':'true'}
r = requests.post('https://api.github.com/user/repos',auth=('Senthilmano81',access_token),
                  data = json.dumps(info))
print(r.status_code)
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'135549bba8e9a36f3bb0','redirect_uri':'https://www.google.com','state':'random_123'}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':'135549bba8e9a36f3bb0','redirect_uri':'https://www.google.com','state':'random_123'}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':'random_123','scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = 'b792c29fd25187d25faf'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':'random_123'}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
info = {'filter':'all', 'role':'all'}
r = requests.get('https://api.github.com/orgs/CodingNinjasCodes/members',auth=('Senthilmano81',access_token),
                  params = json.dumps(info))
print(r.status_code)
print(r.text)
python_data = r.text
for user in python_data:
    print(user)
    print('Next...')
python_data = json.loads(r.text)
for user in python_data: 
    print(user)
    print('Next...')
for user in python_data: 
    print(user['login'])
import requests
import json 

##Getting Authorization Grant using CLient ID
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':'random_123','scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
import requests
import json 

##Getting Authorization Grant using CLient ID
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':'random_124','scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = '9f13947670289f3a4c6f'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':'random_123'}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
info = {'filter':'all', 'role':'all'}
r = requests.get('https://api.github.com/repos/CodingNinjasCodes/JSNotes/stats/contributors',auth=('Senthilmano81',access_token),
                  params = json.dumps(info))
print(r.status_code)
print(r.text)
info = {'filter':'all', 'role':'all'}
r = requests.get('https://api.github.com/repos/CodingNinjasCodes/JSNotes/contributors',auth=('Senthilmano81',access_token),
                  params = json.dumps(info))
print(r.status_code)
print(r.text)
for contributor in data: 
    print(contributor['login'])
data = json.loads(r.text)
for contributor in data: 
    print(contributor['login'])
data[0]
for contributor in data: 
    print(contributor['login'],contributor['contributions'])
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':'random_125','scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = '5984da65d60ea3644348'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':'random_125'}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
r = requests.get('https://api.github.com/repos/CodingNinjasCodes/JSNotes/stats/contributors',auth=('Senthilmano81',access_token))
print(r.status_code)
data = json.loads(r.text)
data[0]
for contributor in data: 
    print(contributor['author'])
for contributor in data: 
    print(contributor['author']['login'])
data[1]
data[2]
for contributor in data: 
    print(contributor['author']['login'],contributor['total'])
import requests
import json 

##Getting Authorization Grant using CLient ID
state_code='random_126'
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':state_code,'scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = 'f6ee91a78a251c1becfc'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':state_code}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
r = requests.get('https://api.github.com/repos/google/clusterfuzz/topics',auth=('Senthilmano81',access_token))
print(r.status_code)
data = json.loads(r.text)
state_code='random_127'
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':state_code,'scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = '84970c6b4235e2d06948'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':state_code}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
header = {'Accept':'application/vnd.github.mercy-preview+json'}
r = requests.get('https://api.github.com/repos/google/clusterfuzz/topics',auth=('Senthilmano81',access_token),headers=header)
data = json.loads(r.text)
for topic in data['names']: 
    print(topic)
import requests
import json 

##Getting Authorization Grant using CLient ID
state_code='random_128'
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':state_code,'scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = '4cb39e4acdc5430a3d9b'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':state_code}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
header = {'Accept':'application/vnd.github.mercy-preview+json'}
r = requests.get('https://api.github.com/repos/CodingNinjasCodes/SmoothScrollJs/community/profile',auth=('Senthilmano81',access_token),headers=header)
data = json.loads(r.text)
print(data['health_percentage'])
print(data)
header = {'Accept':'application/vnd.github.mercy-preview+json'}
r = requests.get('https://api.github.com/repos/CodingNinjasCodes/SmoothScrollJs/community/profile',auth=('Senthilmano81',access_token),headers=header)
print(r.text)
header = {'Accept':'application/vnd.github.black-panther-preview+json'}
r = requests.get('https://api.github.com/repos/CodingNinjasCodes/SmoothScrollJs/community/profile',auth=('Senthilmano81',access_token),headers=header)
print(r.text)
data = json.loads(r.text)
print(data['health_percentage'])
import requests
import json 

##Getting Authorization Grant using CLient ID
state_code='random_129'
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':state_code,'scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = '45474d6370a1bb7fe261'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':state_code}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token))
data = json.loads(r.text)
data
data[0]
data = json.loads(r.text)
for repo in data: 
    print(repo['name'])
string = ""
for repo in data:
    if string=="":
        string="['"+repo['name']+"'"
    else: 
        string = string + ",'" + repo['name']+"'"

string = string + "]"
print(string)
for repo in data: 
    print(repo)
data[0]
for repo in data: 
    print(repo['name'])
data = {'type':'all'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',params=data)
data = json.loads(r.text)
data
print(len(data))
data = {'type':'forks'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',params=data)
data = json.loads(r.text)
print(len(data))
data = {'type':'sources'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',params=data)
data = json.loads(r.text)
print(len(data))
data = {'type':'member'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',params=data)
data = json.loads(r.text)
print(len(data))
import requests
import json 

##Getting Authorization Grant using CLient ID
state_code='random_130'
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':state_code,'scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = '2bad81f4b60ced12b868'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':state_code}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
data = {'type':'all'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
data = json.loads(r.text)
len(data)
data = {'type':'public'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
data = json.loads(r.text)
len(data)
data = {'type':'private'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
data = json.loads(r.text)
len(data)
state_code='random_131'
data ={'client_id':'9cc675d93b9bc2d21620','redirect_uri':'https://www.google.com','state':state_code,'scope':'public_repo','login':'Senthilmano81','allow_signup':'false'}
r = requests.get('https://github.com/login/oauth/authorize',params=data)
print(r.status_code)
print(r.url)
authorization_code = '1d479b06534e9020e702'
## Getting accessToken
info = {'client_id':'9cc675d93b9bc2d21620','client_secret':'0e1e3ff6ab514bac66203a061a5c198102e011b6','code':authorization_code,'redirect_uri':'https://www.google.com','state':state_code}
r =requests.post('https://github.com/login/oauth/access_token',data=info)
python_data = r.text
access_string = python_data.split('&')[0]
access_token = access_string.split('=')[1]
print(access_token)
data = {'type':'private'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
data = json.loads(r.text)
len(data)
for repo in data: 
    print(repo['name'])
len(data)
data = {'type':'all'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
data = json.loads(r.text)
len(data)
for repo in data: 
    print(repo['name'])
data = {'type':'internal'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
data = json.loads(r.text)
data = {'type':'internal'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
print(r.text)
data = {'type':'internal'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
print(r.status_code)
data = {'type':'all'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),params=data)
print(r.status_code)
header = {'Accept':'application/vnd.github.nebula-preview+json', 'type':'internal'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),headers=header)
r.status_code
data = json.loads(r.text)
len(data)
header = {'Accept':'application/vnd.github.nebula-preview+json', 'visibility':'internal'}
r = requests.get('https://api.github.com/orgs/fossasia/repos',auth=('Senthilmano81',access_token),headers=header)
data = json.loads(r.text)
len(data)
r.text
r.links
r = requests.get('https://api.github.com/organizations/6295529/repos?page=2')
r.links
r = requests.get('https://api.github.com/organizations/6295529/repos?page=8')
r.links
import requests
import json 
r = requests.get('https://api.github.com/orgs/fossasia/repos')
r.links
import requests
import json 
nxtFlg = True 
url    = 'https://api.github.com/orgs/fossasia/repos'
r= requests.get(url)
print(r.text)
data[0]['name']
import requests
import json 
nxtFlg = True 
url    = 'https://api.github.com/orgs/fossasia/repos'
repos = []
while nxtFlg: 
    r = requests.get(url)
    data = json.loads(r.text)
    for repository in data: 
        repos.append(repository['name'])
    nxtFlg = False 


for i in repos:
    print(i)
print(len(repos))
import requests
import json 
nxtFlg = True 
url    = 'https://api.github.com/orgs/fossasia/repos'
repos = []
while nxtFlg: 
    r = requests.get(url)
    data = json.loads(r.text)
    for repository in data: 
        repos.append(repository['name'])
    
    links = json.loads(r.links)
    if 'next' in links:
        url = links['next']['url']
    else: 
        nxtFlg = False 


print(len(repos))
import requests
import json 
nxtFlg = True 
url    = 'https://api.github.com/orgs/fossasia/repos'
repos = []
while nxtFlg: 
    r = requests.get(url)
    data = json.loads(r.text)
    for repository in data: 
        repos.append(repository['name'])
    
    links = r.links
    if 'next' in links:
        url = links['next']['url']
    else: 
        nxtFlg = False 


print(len(repos))
import requests
import json 
nxtFlg = True 
url    = 'https://api.github.com/orgs/fossasia/repos'
repos = []
while nxtFlg: 
    r = requests.get(url)
    data = json.loads(r.text)
    for repository in data: 
        repos.append(repository['name'])
    
    links = r.links
    if 'next' in links:
        url = links['next']['url']
    else: 
        nxtFlg = False 


for repo in repos: 
    print(repo)
runfile('C:/Data Backup/E Drive/Learning/Python/api/api2-github-allrepositories.py', wdir='C:/Data Backup/E Drive/Learning/Python/api')
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 1 - Zomato/Zomato Cuisine 1.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 1 - Zomato')
res_arr = [(1,2,3),(2,3,6),(2,1,9)]
sort(res_arr)
res_arr = [(1,2,3),(2,3,6),(2,1,9)]
res_arr.sort(key=lambda x:x[2])
print(res_arr)
res_arr = [(1,2,3),(2,3,6),(2,1,9)]
out = res_arr.sort(key=lambda x:x[2])
print(out)
res_arr = [(1,2,7),(2,3,9),(2,1,1)]
res_arr.sort(key=lambda x:x[2])
print(res_arr)
res_arr = [(1,2,7),(2,3,9),(2,1,1)]
res_arr.sort(key=lambda x:x[2],reverse=True)
print(res_arr)
import pandas as pd
data = pd.read_csv('zomato.csv')
df = data.copy()
print(df)
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
data = pd.read_csv('zomato.csv')
df = data.copy()
df
df.head()
df = data.copy()
df
df.tail()
df['name']
df.describe()
data
data.head()
import pandas as pd
data = pd.read_csv('zomato.csv')
type(data)
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
runfile('C:/Data Backup/E Drive/Learning/Python/CaseStudy2/Question1_Find_City.py', wdir='C:/Data Backup/E Drive/Learning/Python/CaseStudy2')
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
type(df)
import pandas as pd
data = pd.read_csv('startup_funding.csv')
type(data)
data = pd.read_csv('zomato.csv')
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
data = pd.read_csv('zomato.csv')
import pandas as pd
data = pd.read_csv('zomato.csv')
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
data = pd.read_csv('zomato.csv')
import pandas as pd
data = pd.read_csv('zomato.csv')
type(data)

## ---(Wed Jan  1 18:18:47 2020)---
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
data = pd.read_csv('zomato.csv')
type(data)
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='utf-8')
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy
df = data.copy()
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df
df.head()
df.tail()
df.describe()
df.keys()
df.cols()
df.keys()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 1 - Zomato/Zomato Cuisine 1.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 1 - Zomato')
import requests
import json 

header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
r = requests.get('https://developers.zomato.com/api/v2.1/categories',headers=header)
print(r.status_code)
print(r.text)
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df.keys()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
df.keys()
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[df.City.isin(NCR_cities)]
df_NCR.City
df_ROI = df[!df.City.isin(NCR_cities)]
df_ROI = df[!(df.City.isin(NCR_cities))]
df_ROI = df[df.City.apply(lambda x: !(x in NCR_cities))]
df_ROI = df[df.City.apply(lambda x: x in NCR_cities)]
df_ROI
df_ROI.City
df_NCR.City
df_ROI = df[df.City.apply(lambda x: if x in NCR_cities True else False]
df_ROI = df[df.City.apply(lambda x: True if x in NCR_Cities else False]
df_ROI = df[df.City.apply(lambda x: True if x in NCR_Cities else False)]
df_ROI = df[df.City.apply(lambda x: True if x in NCR_cities else False)]
df_ROI.City
df_ROI = df[df.City.apply(lambda x: False if x in NCR_cities else True)]
df_ROI.City
df_ROI = df[df.City.apply(lambda x: False if x in NCR_cities else True) and df.Country == '1']
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) and (df.Country == '1')]
df_India = df[df.Country=='1']
df_India = df[df.country=='1']
df_India = df[df['Country Code']=='1']
df_India = df[df['Country Code']==1]
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[df.City.isin(NCR_cities) and df['Country Code'] == 1]
df_ROI = df[df.City.apply(lambda x: False if x in NCR_cities else True) and df['Country Code'] == 1]
df_ROI.City
df_NCR = df[df.City.isin(NCR_cities) and df['Country Code'] == 1]
NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[df.City.isin(NCR_cities) and df['Country Code'] == 1]
df_NCR = df[(df.City.isin(NCR_cities)) and (df['Country Code'] == 1)]
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_NCR.City
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]
df_ROI.City
df_ROI = df[df.City.apply(lambda x: False if x in NCR_cities else True) & df['Country Code'] == 1]
df_ROI.City
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]
df_ROI.City
import matplotlib.pyplot as plt
year = ['year-2012','year-2013','year-2014','year-2015', 'year-2016', 'year-2017']
salary = [12,13,14,17,19,20]
population = [100,120,180,250,300,370]


plt.bar(year,population,edgecolor='red',width=0.6)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Bar Graph Demo")
plt.xticks(rotation=40)
plt.show()
plt.bar(year,population,salary, edgecolor='red',width=0.6)
plt.bar(year,population,edgecolor='red',width=0.6)
plt.bar(year,[population,salary],edgecolor='red',width=0.6)
df_NCR.City.counts()
df_NCR.City.count()
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

reg_name =  ['Delhi NCR', 'Rest of India']
res_count = [df_NCR.count(),df_ROI.count()]
plt.bar(reg_name,res_count,edgecolor='black',width=0.6)
plt.title('Restaurants - Delhi NCR vs Rest of India')
plt.xlabel('Region')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=40)
plt.show()
reg_name
res_count
reg_name =  ['Delhi NCR', 'Rest of India']
res_count = [df_NCR.City.count(),df_ROI.City.count()]
plt.bar(reg_name,res_count,edgecolor='black',width=0.6)
plt.title('Restaurants - Delhi NCR vs Rest of India')
plt.xlabel('Region')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=40)
plt.show()
df_ROI.City.count()
df_NCR.City.count()
li = [1,2,3,4,5,1]
se = set(li)
se
li = [1,2,3,4,5,1]
se = set(li)
if 3 in se: 
    print('true')
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

for cuisine in df_NCR.Cuisines: 
    print(cuisine)
x.extend(y)
x = [1,2,3,4,5]
y = [6,7,8]
x.extend(y)
x = [1,2,3,4,5]
y = [6,7,8]
x.extend(y)
print(x)
x.extend(y)
print(x)
x = 'hi'
z = y.split(',')
print(z)
x = 'hi'
z = x.split(',')
print(z)
NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend(cuisine.split(','))
NCR_Cuisine_set = set(NCR_Cuisines)
NCR_Cuisines_set
NCR_Cuisine_Set = set(NCR_Cuisines)    
NCR_Cuisine_Set
ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend(cuisine.split(','))


ROI_Cuisine_Set = set(ROI_Cuisines)
ROI_Cuisine_Set
output = NCR_Cuisine_Set | ROI_Cuisine_Set
output
ROI_not_in_NCR = ROI_Cuisine_Set.difference(NCR_Cuisine_Set)   
ROI_not_in_NCR
for city in NCR_cities: 
    print(city,get_City_ID(city))
def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/categories',params=indata,headers=header)
    data  = json.loads(r.text)
    for city_info in data: 
        if city_info['country_name'] == 'India':
            return city_info['id']
    return 'NA'
for city in NCR_cities: 
    print(city,get_City_ID(city))
def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/categories',params=indata,headers=header)
    data  = json.loads(r.text)
    print(data[0])
    for city_info in data: 
        print(city_info)
    
    return 'NA'
for city in NCR_cities: 
    get_City_ID(city)
def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/categories',params=indata,headers=header)
    data  = json.loads(r.text)
    print(data)
    
    return 'NA'
get_City_ID(NCR_cities[0])
def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/cities',params=indata,headers=header)
    data  = json.loads(r.text)
    print(data)
    
    return 'NA'
get_City_ID(NCR_cities[0])
def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/cities',params=indata,headers=header)
    data  = json.loads(r.text)
    for city_info in data['location_suggestions']:
        print(city_info)
    
    return 'NA'
get_City_ID(NCR_cities[0])
def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/cities',params=indata,headers=header)
    data  = json.loads(r.text)
    for city_info in data['location_suggestions']:
        if city_info['country_id'] == 1:
            print(city_info['id'])
    
    return 'NA'
print(get_City_ID(NCR_cities[0]))
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
NCR_City_Id = []
for city in NCR_cities: 
    NCR_City_Id.append(get_City_ID(city))

NCR_City_id
NCR_City_Id
NCR_City_Id = []
for city in NCR_cities: 
    city_Id = get_City_ID(city
    if city_Id != 'NA':
        NCR_City_Id.append())

NCR_City_Id
NCR_City_Id = []
for city in NCR_cities: 
    city_Id = get_City_ID(city)
    if city_Id != 'NA':
        NCR_City_Id.append()

NCR_City_Id
NCR_City_Id = []
for city in NCR_cities: 
    city_Id = get_City_ID(city)
    if city_Id != 'NA':
        NCR_City_Id.append(city_Id)

NCR_City_Id

## ---(Fri Jan  3 01:47:58 2020)---
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import matplotlib.pyplot as plt
import pandas as pd
import requests
import json 

def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/cities',params=indata,headers=header)
    data  = json.loads(r.text)
    for city_info in data['location_suggestions']:
        if city_info['country_id'] == 1:
            return city_info['id']
    
    return 'NA'


def get_cuisines(city_id):
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata = {'city_id':city_id}
    r = requests.get('https://developers.zomato.com/api/v2.1/cuisines',params=indata,headers=header)
    data   = json.loads(r.text)
    cuisines = []
    for cuisine in data['cuisines']: 
        cuisines.append(cuisine['cuisine']['cuisine_name'])
    return cuisines


data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend(cuisine.split(','))


NCR_Cuisine_Set = set(NCR_Cuisines)    

ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend(cuisine.split(','))


ROI_Cuisine_Set = set(ROI_Cuisines)    

## Cuisines present in ROI but not in NCR 
ROI_not_in_NCR = ROI_Cuisine_Set.difference(NCR_Cuisine_Set)
ROI_not_in_NCR
NCR_cities
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
df_NCR_City.count()
df_NCR.City.count()
df_ROI.City.count()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
df_NCR_Cuisines
df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,namecols=['Cuisine'])
df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,names=['Cuisine'])
df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,cols=['Cuisine'])
df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
df_NCR_Cuisines.head()
import pandas as pd

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend(cuisine.split(','))

df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
df_NCR_Cuisines
new = df_NCR_Cuisines.groupby['Cuisine'].size().reset_index()
new = df_NCR_Cuisines.groupby['Cuisine'].count().reset_index()
new = df_NCR_Cuisines.groupby['Cuisine'].count()
new = df_NCR_Cuisines.groupby['Cuisine']
new = df_NCR_Cuisines.groupby(['Cuisine']).count().reset_index()
new
new = df_NCR_Cuisines.value_counts()
df_NCR_Cuisines.value_counts()
freq = df_NCR_Cuisines.Cuisine.value_counts()
freq
for cuisine in NCR_Cuisine_freq.keys(): 
    print(NCR_Cuisine_freq[cuisine])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
for cuisine in NCR_Cuisine_freq.keys(): 
    print(NCR_Cuisine_freq[cuisine])
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])
if ' Chinese' in NCR_Cuisines: 
    print('yes')

if 'Chinese' in NCR_Cuisines: 
    print('yes')
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
print(NCR_Cuisine_freq['Chinese'])
print(NCR_Cuisine_freq[' Chinese'])
NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])
print(NCR_Cuisine_freq[' Chinese'])
print(NCR_Cuisine_freq['Chinese'])
import pandas as pd

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])



ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend(cuisine.split(','))

df_ROI_Cuisines = pd.DataFrame(ROI_Cuisines,columns=['Cuisine'])
ROI_Cuisine_freq = df_ROI_Cuisines.Cuisine.value_counts()
for cuisine in ROI_Cuisine_freq.keys()[:10]:
    print(cuisine,ROI_Cuisine_freq[cuisine])
import pandas as pd

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
print('Top 10 NCR Cuisines:' )
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])



ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend([x.strip for x in cuisine.split(',')])

df_ROI_Cuisines = pd.DataFrame(ROI_Cuisines,columns=['Cuisine'])
ROI_Cuisine_freq = df_ROI_Cuisines.Cuisine.value_counts()
print()
print('Top 10 ROI Cuisines:' )
for cuisine in ROI_Cuisine_freq.keys()[:10]:
    print(cuisine,ROI_Cuisine_freq[cuisine])
import pandas as pd

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
print('Top 10 NCR Cuisines:' )
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])



ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_ROI_Cuisines = pd.DataFrame(ROI_Cuisines,columns=['Cuisine'])
ROI_Cuisine_freq = df_ROI_Cuisines.Cuisine.value_counts()
print()
print('Top 10 ROI Cuisines:' )
for cuisine in ROI_Cuisine_freq.keys()[:10]:
    print(cuisine,ROI_Cuisine_freq[cuisine])

## ---(Mon Jan  6 06:15:15 2020)---
import pandas as pd

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
print('Top 10 NCR Cuisines:' )
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])



ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_ROI_Cuisines = pd.DataFrame(ROI_Cuisines,columns=['Cuisine'])
ROI_Cuisine_freq = df_ROI_Cuisines.Cuisine.value_counts()
print()
print('Top 10 ROI Cuisines:' )
for cuisine in ROI_Cuisine_freq.keys()[:10]:
    print(cuisine,ROI_Cuisine_freq[cuisine])
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
plt.title('NCR Cuisines')
plt.pie(NCR_Cuisine_freq,labels=NCR_Cuisine_freq.keys(),autopct='%.1f%%')
plt.axis('equal')
plt.show()
plt.title('NCR Cuisines')
plt.pie(NCR_Cuisine_freq[:10],labels=NCR_Cuisine_freq.keys()[:10],autopct='%.1f%%')
plt.axis('equal')
plt.show()
plt.title('ROI Cuisines')
plt.pie(ROI_Cuisine_freq[:10],labels=ROI_Cuisine_freq.keys()[:10],autopct='%.1f%%')
plt.axis('equal')
plt.show()

## ---(Thu Jan 16 15:18:59 2020)---
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 1 - Zomato/Zomato Cuisine 1.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 1 - Zomato')
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
df
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt
import json 

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
plt.plot(df['Votes'],df['Aggregate rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.scatter()
import pandas as pd
import matplotlib.pyplot as plt
import json 

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
plt.plot(df['Votes'],df['Aggregate rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.scatter()
plt.show()
a = [1,2,3,4]
len(a)
df['CuisineCount'] = [df['Cuisines'].apply(lambda x: len(x.split(',')))
df['CuisineCount'] = [df['Cuisines'].apply(lambda x: len(x.split(','))
df['CuisineCount'] = [df['Cuisines'].apply(lambda x: x.split(','))
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
df.CuisineCount
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
plt.scatter(df['Votes'],df['Aggregate rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
plt.scatter(df['CuisineCount'],df['Aggregrate rating'])
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
plt.scatter(df['CuisineCount'],df['Aggregrate rating'])
import pandas as pd
import matplotlib.pyplot as plt
import json 

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
plt.scatter(df['CuisineCount'],df['Aggregrate rating'])
plt.scatter(df['CuisineCount'],df['Aggregate rating'])
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
plt.scatter(df['Votes'],df['Aggregate rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
x
x[0]
range(0,10,100)
for i in range(0,10,100): 
    pritn(i)
for i in range(0,10,100): 
    print(i)
x = [(x,x+100) for x in range(0,10000,100)]
x
x = [(x,x+99) for x in range(0,10000,100)]
x
plt.scatter(df['Votes'],df['Aggregate rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
x = [(x,x+99) for x in range(0,5000,100)]
x
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append(5000,20000)
limit_arr.append((5000,20000))
limit_arr
for limit in limit_arr: 
    lower = limit[0]
    upper = limit[1]
    print(lower,upper)
rating_arr = [(0,0) for x in range(0,5000,100)]]
rating_arr = [(0,0) for x in range(0,5000,100)]
rating_arr
df.Votes[0]
df.Votes.iloc[0]
len(df.Votes)
len(df['Aggregate raint'])
len(df['Aggregate rating'])
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)]
for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)]
for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            print('i=',i,'j=',j)
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break
len(rating_arr)
len(limit_arr)
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            print('i=',i,'j=',j)
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break
rating_arr
ave_rating = []
votes      = []
for i in len(rating_arr):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)
ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)
ave_rating
votes
plt.plot(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
plt.scatter(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

reg_name =  ['Delhi NCR', 'Rest of India']
res_count = [df_NCR.City.count(),df_ROI.City.count()]
plt.bar(reg_name,res_count,edgecolor='black',width=0.6)
plt.title('Restaurants - Delhi NCR vs Rest of India')
plt.xlabel('Region')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=40)
plt.show()
plt.scatter(df.Votes,df['Aggregate rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
plt.plot(df.Votes,df['Aggregate rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import json 

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


# find ranges for Votes 
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break

ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)



plt.scatter(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
plt.plot(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
plt.scatter(df['CuisineCount'],df['Aggregate rating'])
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt
import json 

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1


Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]
rating_arr
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.2.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1


Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]

plt.plot(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.3.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1


Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]

plt.plot(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
df['Average Cost for two'].min(
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

df['Average Cost for two'].min()
df['Average Cost for two'].max()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.3.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
plt.scatter(ave_cost, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Cost on Rating')
plt.show()
plt.plot(ave_cost, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Cost on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


Cuisine_dict = {}
for cuisines in df['Cuisines']:
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'],Cuisine_dict[cuisine][1]+1]

Cuisine_dict
for i in Cuisine_dict:
    print(i)
Cuisine_dict = {}
for cuisines in df['Cuisines']:
    cuis_arr = cuisines.split(',').strip()
    for cuisine in cuis_arr:
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'],Cuisine_dict[cuisine][1]+1]

for i in Cuisine_dict:
    print(i)
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for cuisines in df['Cuisines']:
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'],Cuisine_dict[cuisine][1]+1]

for i in Cuisine_dict:
    print(i)
Cuisine_dict = {}
for cuisines in df['Cuisines']:
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'],Cuisine_dict[cuisine][1]+1]

for i in Cuisine_dict:
    print(i)
for i in Cuisine_dict:
    print(i,Cuisine_dict[i])
for i in Cuisine_dict:
    print(i,Cuisine_dict[i][0],Cuisine_dict[i][1])
for i in Cuisine_dict:
    print(i)
    print(i,Cuisine_dict[i][0],Cuisine_dict[i][1])
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.3.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'].iloc[i],Cuisine_dict[cuisine][1]+1]

for i in Cuisine_dict:
    print(i,Cuisine_dict[i][0],Cuisine_dict[i][1])
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'].iloc[i],Cuisine_dict[cuisine][1]+1]
Cuisine_dict.keys()
Cuisine_dict.keys().tolist()
list(Cuisine_dict.keys())
Cuisine_list = list(Cuisine_dict.keys())
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][0] for cuisine in Cuisine_dict]
for i in Cuisine_dict:
    print(i,Cuisine_dict[i][0],Cuisine_dict[i][1])
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1] for cuisine in Cuisine_dict]
print(Cuisine_list)
print(rating_list)
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()
rating_list  = [[cuisine,Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1]] for cuisine in Cuisine_dict]
rating_list
arr.sort()
arr = [5,8,1,2]
arr.sort()
arr
arr = [5,8,1,2]
x = arr.sort()
x
arr = [5,8,1,2]
x = sort(arr)
cuisine_rating  = [[cuisine,Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1]] for cuisine in Cuisine_dict]
Cuisine_list = cuisine_rating[:][0]
Cuisine_list
Cuisine_list = list(Cuisine_dict.keys())
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1] for cuisine in Cuisine_dict]

plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()
Cuisine_rating = [[Cuisine_list[i]],rating_list[i]] for i in range(len(Cuisine_list)))]
Cuisine_rating = [i for i in range(len(Cuisine_list)))]
Cuisine_rating = [i for i in range(len(Cuisine_list))]
Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuising_rating
Cuisine_rating
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_rating
Cuisine_rating[:-10:-1]
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
rating_list  = [cuisinerate[1] for cuisinerate in Cuisine_rating[:-10:-1]]
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()
Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
rating_list  = [cuisinerate[1] for cuisinerate in Cuisine_rating[:-10:-1]]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.xticks(rotate=40)
plt.title('Rating of Specific Cuisines')
plt.show()
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.xticks(rotation=40)
plt.title('Rating of Specific Cuisines')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


# find ranges for Votes 
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break

ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)


plt.plot(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1


Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]

plt.plot(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'].iloc[i],Cuisine_dict[cuisine][1]+1]


Cuisine_list = list(Cuisine_dict.keys())
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1] for cuisine in Cuisine_dict]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()

Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
rating_list  = [cuisinerate[1] for cuisinerate in Cuisine_rating[:-10:-1]]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.xticks(rotation=40)
plt.title('Rating of Top rated Specific Cuisines')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


# find ranges for Votes 
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break

ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)


plt.plot(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1


Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]

plt.plot(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'].iloc[i],Cuisine_dict[cuisine][1]+1]


Cuisine_list = list(Cuisine_dict.keys())
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1] for cuisine in Cuisine_dict]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()

Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
rating_list  = [cuisinerate[1] for cuisinerate in Cuisine_rating[:-10:-1]]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.xticks(rotation=40)
plt.title('Rating of Top rated Specific Cuisines')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


# find ranges for Votes 
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    cost = df['Average Cost for two'].iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if  cost >= lower and cost <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break

ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)


plt.plot(votes, ave_rating)
plt.xlabel('Cost')
plt.ylabel('Rating')
plt.title('Effect of Cost on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


# find ranges for Votes 
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break

ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)


plt.plot(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1


Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]

plt.plot(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
plt.bar(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1


Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]

plt.bar(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'].iloc[i],Cuisine_dict[cuisine][1]+1]


Cuisine_list = list(Cuisine_dict.keys())
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1] for cuisine in Cuisine_dict]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()

Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
rating_list  = [cuisinerate[1] for cuisinerate in Cuisine_rating[:-10:-1]]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.xticks(rotation=40)
plt.title('Rating of Top rated Specific Cuisines')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


# find ranges for Votes 
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    cost = df['Average Cost for two'].iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if  cost >= lower and cost <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break

ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)


plt.plot(votes, ave_rating)
plt.xlabel('Cost')
plt.ylabel('Rating')
plt.title('Effect of Cost on Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'].iloc[i],Cuisine_dict[cuisine][1]+1]


Cuisine_list = list(Cuisine_dict.keys())
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1] for cuisine in Cuisine_dict]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()

Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
rating_list  = [cuisinerate[1] for cuisinerate in Cuisine_rating[:-10:-1]]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.xticks(rotation=40)
plt.title('Rating of Top rated Specific Cuisines')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
print('Top 10 NCR Cuisines:' )
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])

plt.title('NCR Cuisines')
plt.pie(NCR_Cuisine_freq[:10],labels=NCR_Cuisine_freq.keys()[:10],autopct='%.1f%%')
plt.axis('equal')
plt.show()

ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend([x.strip() for x in cuisine.split(',')])

df_ROI_Cuisines = pd.DataFrame(ROI_Cuisines,columns=['Cuisine'])
ROI_Cuisine_freq = df_ROI_Cuisines.Cuisine.value_counts()
print()
print('Top 10 ROI Cuisines:' )
for cuisine in ROI_Cuisine_freq.keys()[:10]:
    print(cuisine,ROI_Cuisine_freq[cuisine])


plt.title('ROI Cuisines')
plt.pie(ROI_Cuisine_freq[:10],labels=ROI_Cuisine_freq.keys()[:10],autopct='%.1f%%')
plt.axis('equal')
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import requests
import json 

def get_City_ID(city): 
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/cities',params=indata,headers=header)
    data  = json.loads(r.text)
    for city_info in data['location_suggestions']:
        if city_info['country_id'] == 1:
            return city_info['id']
    
    return 'NA'


def get_cuisines(city_id):
    header = {'user-key':'a0872ce198cd8c85d249e6188da90eb1'}
    indata = {'city_id':city_id}
    r = requests.get('https://developers.zomato.com/api/v2.1/cuisines',params=indata,headers=header)
    data   = json.loads(r.text)
    cuisines = []
    for cuisine in data['cuisines']: 
        cuisines.append(cuisine['cuisine']['cuisine_name'])
    return cuisines


data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend(cuisine.split(','))


NCR_Cuisine_Set = set(NCR_Cuisines)    

ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend(cuisine.split(','))


ROI_Cuisine_Set = set(ROI_Cuisines)    

## Cuisines present in ROI but not in NCR 
ROI_not_in_NCR = ROI_Cuisine_Set.difference(NCR_Cuisine_Set)   


## Check if the cuisines are really not present in NCR region
NCR_City_Id = []
for city in NCR_cities: 
    city_Id = get_City_ID(city)
    if city_Id != 'NA':
        NCR_City_Id.append(city_Id)


## get cuisines list of NCR region
NCR_Actual_Cuisines = []
for city_id in NCR_City_Id: 
    NCR_Actual_Cuisines.extend(get_cuisines(city_id))



print('as per dataset:')
print('      Cuisines in ROI but not present in NCR:',*ROI_not_in_NCR)
print()
print('As per zomato API:')
## Find cuisines that are actually not served in NCR: 
for ROI_Cuisine in ROI_not_in_NCR: 
    if ROI_Cuisine in NCR_Actual_Cuisines: 
        print(ROI_Cuisine)
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

out = df['Restaurant Name'].value_counts()
out
outlets = df['Restaurant Name'].value_counts()
for restaurant in outlets.keys():
    print(restaurant)
for restaurant in outlets.keys():
    print(restaurant,outlets[restaurant])
for restaurant in outlets.keys()[:16]:
    print(restaurant,outlets[restaurant])
for restaurant in outlets.keys()[:15]:
    print(restaurant,outlets[restaurant])
restaurants = outlets.keys()[:15].tolist()
restaurants
outlets     = outlet_dtl[:15].tolist()
outlet_dtl = df['Restaurant Name'].value_counts()
restaurants = outlet_dtl.keys()[:15].tolist()
outlets     = outlet_dtl[:15].tolist()
outlets
df['Restaurant Name'] = df['Restaurant Name'].apply(lambda x:'Giani' if x=="Giani's" else x)
outlet_dtl = df['Restaurant Name'].value_counts()
restaurants = outlet_dtl.keys()[:15].tolist()
outlets     = outlet_dtl[:15].tolist()
outlet_dtl[:15]
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.1.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

df['Restaurant Name'] = df['Restaurant Name'].apply(lambda x:'Giani' if x=="Giani's" else x)
outlet_dtl = df['Restaurant Name'].value_counts()
restaurants = outlet_dtl.keys()[:15].tolist()
outlets     = outlet_dtl[:15].tolist()

plt.bar(restaurants,outlets)
plt.xlabel('Restaurant')
plt.ylabel('outlets')
plt.xticks(rotation=90)
plt.title('Rating of Top rated Specific Cuisines')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

df['Restaurant Name'] = df['Restaurant Name'].apply(lambda x:'Giani' if x=="Giani's" else x)
outlet_dtl = df['Restaurant Name'].value_counts()
restaurants = outlet_dtl.keys()[:15].tolist()
outlets     = outlet_dtl[:15].tolist()

plt.bar(restaurants,outlets)
plt.xlabel('Restaurant')
plt.ylabel('outlets')
plt.xticks(rotation=90)
plt.title('Number of Outlets for Top Restaurants')
plt.show()
df.sort_values(by=['Votes'])
df.sort_values(by=['Votes'],ascending=False)
df.Votes
df = df.sort_values(by=['Votes'],ascending=False)
df.Votes
df1 = df.sort_values(by=['Votes'],ascending=False)[:10]
df1
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
df['Restaurant Name'] = df['Restaurant Name'].apply(lambda x:'Giani' if x=="Giani's" else x)

df1 = df.groupby['Restaurant Name']['Votes'].sum().reset_index()
df1 = df.groupby['Restaurant Name']['Votes'].sum()
df1 = df.groupby['Restaurant Name']['Votes'].count()
df1 = df.groupby['Restaurant Name']
df1 = df.groupby(['Restaurant Name'])['Votes'].sum().reset_index()
df1
df1 = df1.sort_values(by=['Votes'])
df1
df1 = df1.sort_values(by=['Votes'],ascending=False)
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
df['Restaurant Name'] = df['Restaurant Name'].apply(lambda x:'Giani' if x=="Giani's" else x)

df1 = df.groupby(['Restaurant Name'])['Votes'].sum().reset_index()
df1 = df1.sort_values(by=['Votes'],ascending=False)
df1
df1 = df1.sort_values(by=['Votes'],ascending=False)[:10]
df1
plt.bar(df1['Restaurant Name'],df1['Votes'])
plt.xlabel('Restaurant')
plt.ylabel('Votes')
plt.xticks(rotation=90)
plt.title('Number of Votes for Top Restaurants')
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.3.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
df1
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==126]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
df
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    print('c='cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.4.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    if cuisines is 'nan': 
        continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    if cuisines is None: 
        continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.4.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    if math.isnan(float(cuisines)):
        continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    if cuisines == np.nan:
        continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    if np.isnan(cuisines):
        continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
a = 'hi'
datatype(a)
a = 'hi'
dtype(a)
a = 'hi'
type(a)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    if type(cuisines) == 'str': 
        pass
    else: 
        if np.isnan(cuisines):
            continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    if type(cuisines) == 'str': 
        pass
    else: 
        continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
df
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==216]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    print(cuisines)
    if type(cuisines) == 'str': 
        pass
    else: 
        continue 
    print('c=',cuisines)
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==216]
df1 = df.Cuisines.dropna()

Cuisine_dict = {}
for i in range(len(df1['Cuisines'])):
    cuisines = df1.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==216]
df1 = df.Cuisines.dropna()
df1
df1 = df.Cuisines.dropna().reset_index()
df1
df1.Cuisines
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==216]
df1 = df.Cuisines.dropna().reset_index()

Cuisine_dict = {}
for i in range(len(df1['Cuisines'])):
    cuisines = df1.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 


Cuisine_dict
print(Cuisine_dict)
out = sorted(Cuisine_dict.items(),key=lambda x:x[1])
out
out = sorted(Cuisine_dict.items(),key=lambda x:x[1],ascending=False)
out
out = sorted(Cuisine_dict.items(),key=lambda x:x[1])[:-10]
out
out = sorted(Cuisine_dict.items(),key=lambda x:x[1])[:-10:-1]
out
out = sorted(Cuisine_dict.items(),key=lambda x:x[1])[:-11:-1]
out
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 1.3.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
Cuisine_dtl = sorted(Cuisine_dict.items(),key=lambda x:x[1])[:-11:-1]
restaurants = [cuisine[1] for cuisine in Cuisine_dtl] 
cuisines    = [cuisine[0] for cuisine in Cuisine_dtl]
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.4.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
plt.title('Top Cuisines in USA')
plt.pie(restaurants,explode=20,labels=cuisines,autopct='%.1f%%')
plt.axis('equal')
plt.show()
plt.pie(restaurants,labels=cuisines,autopct='%.1f%%')
plt.pie(restaurants,labels=cuisines,autopct='%.1f%%')
plt.axis('equal')
plt.show()
Cuisine_dtl
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==1]
len(df)
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==1]

City_dtl = {}
for i in range(len(df)):
    curCity = df.City.iloc[i]
    if curCity not in City_dtl:
        City_dtl[curCity] = [0,0,0]
    City_dtl[curCity][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    City_dtl[curCity][1] += df.Votes.iloc[i]
    City_dtl[curCity][2] += 1


cities = City_dtl.keys().tolist()
cities = City_dtl.keys()
cities
cities = list(City_dtl.keys())
cities
wt_rating = [citydtl[0]/citydtl[1] for citydtl in City_dtl]
wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
wt_rating
len(wt_rating)
len(cities)
cities    = list(City_dtl.keys())
wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
restaurants  [City_dtl[city][2] for city in City_dtl]
restaurants = [City_dtl[city][2] for city in City_dtl]
len(restaurants)
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==1]

City_dtl = {}
for i in range(len(df)):
    curCity = df.City.iloc[i]
    if curCity not in City_dtl:
        City_dtl[curCity] = [0,0,0]
    City_dtl[curCity][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    City_dtl[curCity][1] += df.Votes.iloc[i]
    City_dtl[curCity][2] += 1


cities    = list(City_dtl.keys())
wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
restaurants = [City_dtl[city][2] for city in City_dtl]

colors = range(len(cities))
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.ylabel('Number of restaurants')
plt.grid()
plt.show()
restaurants
City_dtl
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==1]

City_dtl = {}
for i in range(len(df)):
    curCity = df.City.iloc[i]
    if curCity not in City_dtl:
        City_dtl[curCity] = [0,0,0]
    City_dtl[curCity][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    City_dtl[curCity][1] += df.Votes.iloc[i]
    City_dtl[curCity][2] += 1


cities    = list(City_dtl.keys())
wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
restaurants = [City_dtl[city][2] for city in City_dtl]

colors = range(len(cities))
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.ylabel('Number of restaurants')
plt.grid()
plt.show()
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.xticks(rotation=90)
plt.ylabel('Number of restaurants')
plt.grid()
plt.show()
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.xticks(rotation=270)
plt.ylabel('Number of restaurants')
plt.grid()
plt.show()
colors = range(len(cities))
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.xticks(rotation=900)
plt.ylabel('Number of restaurants')
plt.grid()
plt.show()
colors = range(len(cities))
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.xticks(rotation=900)
plt.ylabel('Number of restaurants')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


City_dtl = {}
for i in range(len(df_ROI)):
    curCity = df.City.iloc[i]
    if curCity not in City_dtl:
        City_dtl[curCity] = [0,0,0]
    City_dtl[curCity][0] += df_ROI.Votes.iloc[i]*df_ROI['Aggregate rating'].iloc[i]
    City_dtl[curCity][1] += df_ROI.Votes.iloc[i]
    City_dtl[curCity][2] += 1


cities    = list(City_dtl.keys())
wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
restaurants = [City_dtl[city][2] for city in City_dtl]

colors = range(len(cities))
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.xticks(rotation=900)
plt.ylabel('Number of restaurants')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


City_dtl = {}
for i in range(len(df_ROI)):
    curCity = df.City.iloc[i]
    if curCity not in City_dtl:
        City_dtl[curCity] = [0,0,0]
    City_dtl[curCity][0] += df_ROI.Votes.iloc[i]*df_ROI['Aggregate rating'].iloc[i]
    City_dtl[curCity][1] += df_ROI.Votes.iloc[i]
    City_dtl[curCity][2] += 1


cities    = list(City_dtl.keys())
wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
restaurants = [City_dtl[city][2] for city in City_dtl]

colors = range(len(cities))
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in City')
plt.xlabel('City')
plt.xticks(rotation=90)
plt.ylabel('Number of restaurants')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


City_dtl = {}
for i in range(len(df_ROI)):
    curCity = df.City.iloc[i]
    if curCity not in City_dtl:
        City_dtl[curCity] = [0,0,0]
    City_dtl[curCity][0] += df_ROI.Votes.iloc[i]*df_ROI['Aggregate rating'].iloc[i]
    City_dtl[curCity][1] += df_ROI.Votes.iloc[i]
    City_dtl[curCity][2] += 1


cities    = list(City_dtl.keys())
wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
restaurants = [City_dtl[city][2] for city in City_dtl]

colors = range(len(cities))
plt.scatter(cities,restaurants,s=wt_rating,c=colors)
plt.title('Bubble Graph Restaurants in ROI')
plt.xlabel('City')
plt.xticks(rotation=90)
plt.ylabel('Number of restaurants')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(df):  
    City_dtl = {}
    for i in range(len(df)):
        curCity = df.City.iloc[i]
        if curCity not in City_dtl:
            City_dtl[curCity] = [0,0,0]
        City_dtl[curCity][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
        City_dtl[curCity][1] += df.Votes.iloc[i]
        City_dtl[curCity][2] += 1
    
    
    cities    = list(City_dtl.keys())
    wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
    restaurants = [City_dtl[city][2] for city in City_dtl]
    
    colors = range(len(cities))
    plt.scatter(cities,restaurants,s=wt_rating,c=colors)
    plt.title('Bubble Graph Restaurants in ROI')
    plt.xlabel('City')
    plt.xticks(rotation=90)
    plt.ylabel('Number of restaurants')
    plt.show()


data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]
plot_graph(df_ROI)
plot_graph(df_NCR)
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(df,region):  
    City_dtl = {}
    for i in range(len(df)):
        curCity = df.City.iloc[i]
        if curCity not in City_dtl:
            City_dtl[curCity] = [0,0,0]
        City_dtl[curCity][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
        City_dtl[curCity][1] += df.Votes.iloc[i]
        City_dtl[curCity][2] += 1
    
    
    cities    = list(City_dtl.keys())
    wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
    restaurants = [City_dtl[city][2] for city in City_dtl]
    
    colors = range(len(cities))
    plt.scatter(cities,restaurants,s=wt_rating,c=colors)
    plt.title('Bubble Graph Restaurants in '+region)
    plt.xlabel('City')
    plt.xticks(rotation=90)
    plt.ylabel('Number of restaurants')
    plt.show()


data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]
plot_graph(df_ROI,'ROI')
plot_graph(df_NCR,'NCR')
out    = sorted(Locality_dtl.items(),key=lambda x:x[0]/x[1])
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)]

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]
    Locality_dtl[curLocality][2] += 1


out    = sorted(Locality_dtl.items(),key=lambda x:x[0]/x[1])
Locality_dtl.items()
out    = sorted(Locality_dtl.items(),key=lambda x:x[0])
out    = sorted(Locality_dtl.items(),key=lambda x:(x[0]/x[1]))
out    = sorted(Locality_dtl.items(),key=lambda x:x[1][0]/x[1][1])
out
for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    res_count = Locality_dtl[locality][2]
    Locality_dtl[locality] = [wt_rating_val,res_count]
Locality_dtl
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]
    Locality_dtl[curLocality][2] += 1


for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    res_count = Locality_dtl[locality][2]
    Locality_dtl[locality] = [wt_rating_val,res_count]
Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1][0])
Top_dtl
Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1][0],ascending=False)
Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1][0])[:-11:-1]
Top_dtl
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]



for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    Locality_dtl[locality] = wt_rating_val
Locality_dtl
Locality_dtl.items()
Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])
Top_dtl
Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11]
Top_dtl
Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11:-1]
Top_dtl
Localities    = [x[0] for x in Top_dtl]
wt_rating = [x[1] for x in Top_dtl]
localities
Localities
wt_rating
Top_dtl
for loc_info in Top_dtl: 
    print(*loc_info)
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]



for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    Locality_dtl[locality] = wt_rating_val


Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11:-1]
for loc_info in Top_dtl: 
    print(*loc_info)


Localities    = [x[0] for x in Top_dtl]
wt_rating = [x[1] for x in Top_dtl]

plt.bar(Localities,wt_rating)
plt.title('Weighted Rating in each Locality')
plt.xlabel('Locality')
plt.xticks(rotation=90)
plt.ylabel('Weighted Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]



for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    Locality_dtl[locality] = wt_rating_val


Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11:-1]
for loc_info in Top_dtl: 
    print(*loc_info)


Localities    = [x[0] for x in Top_dtl]
wt_rating = [x[1] for x in Top_dtl]

plt.bar(Localities,wt_rating)
plt.title('Weighted Rating in each Locality')
plt.xlabel('Locality')
plt.xticks(rotation=40)
plt.ylabel('Weighted Rating')
plt.show()
plt.bar(Localities,wt_rating)
plt.title('Weighted Rating in each Locality')
plt.xlabel('Locality')
plt.xticks(rotation=60)
plt.ylabel('Weighted Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]



for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    Locality_dtl[locality] = wt_rating_val


Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11:-1]
for loc_info in Top_dtl: 
    print(*loc_info)


Localities    = [x[0] for x in Top_dtl]
wt_rating = [x[1] for x in Top_dtl]

plt.bar(Localities,wt_rating)
plt.title('Weighted Rating in each Locality')
plt.xlabel('Locality')
plt.xticks(rotation=80)
plt.ylabel('Weighted Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]



for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    Locality_dtl[locality] = wt_rating_val


Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11:-1]
for loc_info in Top_dtl: 
    print(*loc_info)


Localities    = [x[0] for x in Top_dtl]
wt_rating = [x[1] for x in Top_dtl]

plt.bar(Localities,wt_rating)
plt.title('Weighted Rating in each Locality')
plt.xlabel('Locality')
plt.xticks(rotation=75)
plt.ylabel('Weighted Rating')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1) & df['Rating text'] != 'Not rated'].dropna()
df= df[(df['Country Code'] == 1) & (df['Rating text'] != 'Not rated')].dropna()
df= df[(df['Country Code'] == 1) & (df['Rating text'] != 'Not rated') & (df['Aggregate rating'] != 0)].dropna()
rating = df['Aggregate rating'].tolist()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1) & (df['Rating text'] != 'Not rated') & (df['Aggregate rating'] != 0)].dropna()
rating = df['Aggregate rating'].tolist()

ratingmin = int(min(rating))
ratingmax = int(max(rating))
rdelta = (ratingmax - ratingmin) /10 
print(rdelta)
print(ratingmin)
print(ratingmax)
a = [x for x in range(ratingmin,ratingmax,int(rdelta))]
print(a)
ratingmax
ratingmin
rating
ratingmin = min(rating)
ratingmax = max(rating)
rdelta = (ratingmax - ratingmin) /10 
print(rdelta)
print(ratingmin)
print(ratingmax)
a = [x for x in range(ratingmin,ratingmax,int(rdelta))]
print(a)
ratingmin
ratingmax
rdelta = round((ratingmax - ratingmin) /10,2)
rdelta
rdelta = round((ratingmax - ratingmin) /10,1)
rdelta
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1) & (df['Rating text'] != 'Not rated') & (df['Aggregate rating'] != 0)].dropna()
rating = df['Aggregate rating'].tolist()

ratingmin = min(rating)
ratingmax = max(rating)
rdelta = round((ratingmax - ratingmin) /10,1) 
a = [x for x in range(ratingmin,ratingmax,int(rdelta))]
print(a)
a = [x for x in range(ratingmin,ratingmax,rdelta)]
print(a)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1) & (df['Rating text'] != 'Not rated') & (df['Aggregate rating'] != 0)].dropna()
rating = df['Aggregate rating'].tolist()

ratingmin = min(rating)
ratingmax = max(rating)
rdelta = round((ratingmax - ratingmin) /10,1) 
a = np.arange(ratingmin,ratingmax,rdelta)
print(a)
plt_dtl = np.arange(ratingmin,ratingmax,rdelta)
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1) & (df['Rating text'] != 'Not rated') & (df['Aggregate rating'] != 0)].dropna()
rating = df['Aggregate rating'].tolist()
plt.hist(rating,bins=10,edgecolor='black')
plt.grid()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]



for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    Locality_dtl[locality] = wt_rating_val


Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11:-1]
for loc_info in Top_dtl: 
    print(*loc_info)


Localities    = [x[0] for x in Top_dtl]
wt_rating = [x[1] for x in Top_dtl]

plt.bar(Localities,wt_rating)
plt.title('Weighted Rating in each Locality')
plt.xlabel('Locality')
plt.xticks(rotation=75)
plt.ylabel('Weighted Rating')
plt.show()
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 2.5.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
runfile('C:/Data Backup/E Drive/Learning/Python/api/API-Project 2/Problem 3.2.py', wdir='C:/Data Backup/E Drive/Learning/Python/api/API-Project 2')
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data  = BeautifulSoup(html,'html.parser')
data.body
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data = BeautifulSoup(html,'html.parser')
print(data.div.attrs)
## Print the required output in given format
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/AttributesOfDivTag.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data = BeautifulSoup(html,'html.parser')
attributes = data.div.attrs
for attribute in attributes: 
    print(attribute)

## Print the required output in given format
import bs4 from BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data = BeautifulSoup()
arr    = data.find_all('li')
print(arr)
from BS4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data = BeautifulSoup()
arr    = data.find_all('li')
print(arr)
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data = BeautifulSoup()
arr    = data.find_all('li')
print(arr)
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data = BeautifulSoup(html,'html.parser')
arr    = data.find_all('li')
print(arr)
for ele in arr: 
    print(ele)
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'
data = BeautifulSoup(html,'html.parser')
arr    = data.find_all('li')
print(arr)
for ele in arr: 
    print(ele.li)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/StringsOfLi.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/hrefOfATag.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
data = BeautifulSoup(html,'html.parser')
print(arr)
arr = data.find_all('a')
p
print(arr)
for ele in arr: 
    print(ele.get_text())
for ele in arr: 
    print(ele.a)
for ele in arr: 
    print(ele.a['href'])
for ele in arr: 
    print(ele['href'])
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data= BeautifulSoup(html,'html.parser')
print(data.html.children)
## Print the required output in given format
print(len(data.html.children))
print(len(data.html.contents))
print(len(data.html.descendants))
print(len(list(data.html.descendants)))
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data= BeautifulSoup(html,'html.parser')
difference = len(list(data.html.descendants)) - len(data.html.contents)
print(difference)
## Print the required output in given format
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
## Print the required output in given format

data.find_all(id)
data.find_all('id')
data.find_all(id=*)
data.find_all(id)
data.find_all(id="li2")
data.li
data.a
data.a.attrs()
data.a.attrs
data.find_all({"id"})
data.select("id")
data.select(lambda tag:tag.name =='id')
data.select(li[id])
data.select(li['id'])
data.find_all['id']
data.find_all(attrs={"id":True})
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
arr = data.find_all(attrs={"id":True})
for ele in arr: 
    print(ele)


## Print the required output in given format
for ele in arr: 
    print(ele.tag)
print(ele.name)
for ele in arr: 
    print(ele.name)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/NextSibling.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'hmtl.parser')
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/NextSibling.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
data = BeautifulSoup(html,'html.parser')
arr = data.find_all(id="li2")
print(arr)
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
arr = data.find_all(id="li2")
for ele in arr: 
    print(ele)

## Print the required output in given format
ele.next_sibling
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
arr = data.find_all(id="li2")
for ele in arr: 
    print(ele)
    ele1 = ele.next_sibling
    print(ele)
    ele2 = ele1.next_sibling
    print(ele2)

## Print the required output in given format
print(ele2.next_sibling)
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
arr = data.find_all(id="li2")
for ele in arr: 
    print(ele)
    while ele is not None: 
        ele = ele.next_sibling
        print(ele)

## Print the required output in given format
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
arr = data.find_all(id="li2")
for ele in arr: 
    ele = ele.next_sibling    
    while ele is not None: 
        print(ele)
        ele = ele.next_sibling

## Print the required output in given format
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data  = BeautifulSoup(html,'html.parser')
title_tag = data.find('title')
title_tag
title_tag.parents
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data  = BeautifulSoup(html,'html.parser')
title_tag = data.find('title')
for i in title_tag.parents: 
    print(i)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/NextElement.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
print(tag.next_element.String)
tag.next_element
print(tag.next_element.next_element)
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
tags = data.find('a')
tags
## Print the required output in given format
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
tags = data.find_all('a')
tags
## Print the required output in given format
from bs4 import BeautifulSoup
html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'
data = BeautifulSoup(html,'html.parser')
tags = data.find_all('a')
print(tags[1].next_element)
## Print the required output in given format

## ---(Wed Jan 22 08:59:40 2020)---
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
print(response.status_code)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BooksToScrape.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
response
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BooksToScrape.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
response
response.text
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
print(data.prettify())
print(data.title())
print(data.title)
print(data.a)
print(data.a.string)
print(data.a.get_text())
print(data.article(class='product_pod'))
b1 = data.find(class_='product_pod')
b1
b1.a
b1.find_all('a')
b1.find_all('a')[1]
b1.find_all('a')[1]['title']
b1
b1.find_all('a')[1]['href']
for book in books:
    print(book.h3.a)
books = data.find_all(class_='product_pod')
for book in books:
    print(book.h3.a)
for book in books:
    print(book.h3.a['href'])
base_url = 'http://books.toscrape.com/'
for book in books:
    print(base_url + book.h3.a['href'])

## ---(Thu Jan 23 02:09:38 2020)---
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BooksToScrape.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
books = data.find_all(class_='product_pod')
books
books[0]
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
books = data.find_all(class_='product_pod')
for book in books:
    print(book.h3.a.string)
books[0].h3.a
books[0
]
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
books = data.find_all(class_='product_pod')
for book in books:
    print(book.h3.a['title'])
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
categories = data.find_all(class='side_categories')
categories
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
categories = data.find_all(class_='side_categories')
categories
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find_all(class_='side_categories')
categories = cat_list.find_all('a')
categories
categories = cat_list.find('a')
categories
cat_list
cat_list[0]
cat_list[1]
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
categories
categories
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    print(category)
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    print(category.a.string)
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    print(category.a)
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    print(category.a['href'])
for category in categories: 
    print(category)
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    print(category['href'])
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    print(category.string)
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    print(category['href'].strip(),category.string.strip())
import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
cat_list = data.find(class_='side_categories')

categories = cat_list.find_all('a')
for category in categories: 
    category_name = category['href'].split('/')[3]
    print(category_name,category.string.strip())
categories[0]

runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/AllCategories.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
categories
cat_list
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/AllCategories.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BookNamesFromFirstPage.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/AllBookNames.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
import requests
from bs4 import BeautifulSoup

## Print the required output in given format
## You are given page links in variable allPages, use this

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
            'http://books.toscrape.com/catalogue/page-6.html',
            'http://books.toscrape.com/catalogue/page-7.html',
            'http://books.toscrape.com/catalogue/page-8.html',
            'http://books.toscrape.com/catalogue/page-9.html',
            'http://books.toscrape.com/catalogue/page-10.html']
all_books = []

for url in allPages: 
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    books = data.find_all(class_='product_pod')
    for book in books:
        all_books.append(book.h3.a['title'])


print(len(all_books))
import requests
from bs4 import BeautifulSoup

## Print the required output in given format
## You are given page links in variable allPages, use this

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
            'http://books.toscrape.com/catalogue/page-6.html',
            'http://books.toscrape.com/catalogue/page-7.html',
            'http://books.toscrape.com/catalogue/page-8.html',
            'http://books.toscrape.com/catalogue/page-9.html',
            'http://books.toscrape.com/catalogue/page-10.html']
all_books = []

for url in allPages: 
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    books = data.find_all(class_='product_pod')
    for book in books:
        all_books.append(book.h3.a['title'])


all_books
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/AllBookNames.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BookDetails.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
import requests
from bs4 import BeautifulSoup
import re 

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html']

column_names = ['Title', 'Link', 'Price', 'Quantity in Stock']

base_url = 'http://books.toscrape.com//catalogue/'
for url in allPages: 
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    books = data.find_all(class_='product_pod')
    for book in books:
        name = book.h3.a['title']
        link = base_url + book.h3.a['href']
        response = requests.get(link)
        bhtml    = response.text 
        bdata  = BeautifulSoup(bhtml,'html.parser')
        price_str = bdata.find(class_='price_color').string
        price  = re.search('%d+',price_str)
        stock = bdata.find(class_='instock availability').string
        ele   = [name,link,price_str,stock]
        print(ele)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BookDetails.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
book
name
link
response = requests.get(link)
bhtml    = response.text 
bdata  = BeautifulSoup(bhtml,'html.parser')
price_str = bdata.find(class_='price_color').string
price  = re.search('/d+',price_str)
stock = bdata.find(class_='instock availability').string
ele   = [name,link,price,stock]
print(ele)
price_str
price  = re.search('\d+',price_str)
price
print(price)
price  = re.search('/d+',price_str).group()
print(ele)
price_str = bdata.find(class_='price_color').string
price  = re.search('/d+',price_str).group()
price  = re.search('\d+',price_str).group()
price
price  = re.search('\d.+',price_str).group()
price
stock = bdata.find(class_='instock availability')
stock
stock = bdata.find(class_='instock availability').contents()
stock = bdata.find(class_='instock availability').contents
stock
stock = bdata.find(class_='instock availability').contents[-1].strip()
stock
stock = re.search('\d+',stock_str).group()
stock_str = bdata.find(class_='instock availability').contents[-1].strip()
stock = re.search('\d+',stock_str).group()
stock
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BookDetails.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html']

column_names = ['Title', 'Link', 'Price', 'Quantity in Stock']

base_url = 'http://books.toscrape.com//catalogue/'
csv_arr = []
for url in allPages: 
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    books = data.find_all(class_='product_pod')
    for book in books:
        name = book.h3.a['title']
        link = base_url + book.h3.a['href']
        response = requests.get(link)
        bhtml    = response.text 
        bdata  = BeautifulSoup(bhtml,'html.parser')
        price_str = bdata.find(class_='price_color').string
        price  = re.search('\d.+',price_str).group()
        stock_str = bdata.find(class_='instock availability').contents[-1].strip()
        stock = re.search('\d+',stock_str).group()
        ele   = [name,link,price,stock]
        csv_arr.append(ele)


df = pd.DataFrame(csv_arr,columns=column_names)
df
df.head()
for i in range(len(df)):
    print(df['Title'].iloc(i))
for i in range(len(df)):
    print(df.iloc(i))
for i in range(len(df)):
    print(df['Title'])
print(df.iloc(1,1))
print(df.iloc(1))
for ele in df:
    print(ele)
for ele in df.rows:
    print(ele)
for ele in df.rows():
    print(ele)
for index, row in df.iterrows():
    print(row['Title'])
df = pd.DataFrame(csv_arr,columns=column_names)
for index, row in df.iterrows():
    for column in df: 
        print(row[column],end=' ')
    print()
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BookDetails.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

url = 'https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
out = data.find_all(class_='lister-item mode-advanced')
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

url1 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start='
url2 = '&ref_=adv_prv'
maxRunTime = 0 
title = ' ' 
for page in range(5):
    page_start = (page*5) + 1
    url = url1 + str(page_start) + url2
    print(url)
"""
Created on Sat Jan 25 05:16:47 2020

@author: GGR0
"""

import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

url1 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start='
url2 = '&ref_=adv_prv'
maxRunTime = 0 
title = ' ' 
for page in range(5):
    page_start = (page*50) + 1
    url = url1 + str(page_start) + url2
    print(url)
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/QuoteswithTagHumor.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
quotes = data.find_all(class_='quote')
quotes
for quote_str in quotes: 
    tags  = find_tags(quote_str)
    print(tags)
for quote_str in quotes: 
    tags  = find_tags(quote_str)
    if 'humor' in tags: 
        print(tags)
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

def find_tags(quote):
    tag_strs = quote.find_all(class_='tag')
    tags = []
    for tag_str in tag_strs:
        tags.append(tag_str.string)
    return tags


url = 'http://quotes.toscrape.com/'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
quotes = data.find_all(class_='quote')
for quote_str in quotes: 
    tags  = find_tags(quote_str)
    if 'humor' in tags: 
        quote = quote_str.find(class_='text')
        print(quote)
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

def find_tags(quote):
    tag_strs = quote.find_all(class_='tag')
    tags = []
    for tag_str in tag_strs:
        tags.append(tag_str.string)
    return tags


url = 'http://quotes.toscrape.com/'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
quotes = data.find_all(class_='quote')
for quote_str in quotes: 
    tags  = find_tags(quote_str)
    if 'humor' in tags: 
        quote = quote_str.find(class_='text').string
        print(quote)
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

def find_tags(quote):
    tag_strs = quote.find_all(class_='tag')
    tags = []
    for tag_str in tag_strs:
        tags.append(tag_str.string)
    return tags


base_url = 'http://quotes.toscrape.com/'

for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    quotes = data.find_all(class_='quote')
    for quote_str in quotes: 
        tags  = find_tags(quote_str)
        if 'humor' in tags: 
            quote = quote_str.find(class_='text').string
            print(quote)
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

def find_tags(quote):
    tag_strs = quote.find_all(class_='tag')
    tags = []
    for tag_str in tag_strs:
        tags.append(tag_str.string)
    return tags


base_url = 'http://quotes.toscrape.com/'

authors = set()
for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    auths = data.find_all(class_='author')
    for auth_str in auths: 
        authors.add(auth_str.string.strip())

print(authors)
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

base_url = 'http://quotes.toscrape.com/'

authors = set()
for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    auths = data.find_all(class_='author')
    for auth_str in auths: 
        authors.add(auth_str.string.strip())

print(sorted(authors))
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

base_url = 'http://quotes.toscrape.com/'

authors = set()
for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    auths = data.find_all(class_='author')
    for auth_str in auths: 
        authors.add(auth_str.string.strip())

for author in sorted(authors):
    print(author)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BirthDateOfAuthors.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
for author in sorted(authors):
    if author[0:1] == 'J':
        print(author)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/BirthDateOfAuthors.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
for author in sorted(authors):
    if author[0:1] == 'J':
        url = base_url + 'author/'+author.strip()+'/'
        print(url)
url = base_url + 'author/'+author.strip()+'/'
print(url)
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
print(data)
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace('.',' ')
        print(author_mod)
        url = base_url + 'author/'+author_mod.strip()+'/'
DoB = {}
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace('.','')
        print(author_mod)
        url = base_url + 'author/'+author_mod.strip()+'/'
DoB = {}
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace(' ','-')
        print(author_mod)
        url = base_url + 'author/'+author_mod.strip()+'/'
DoB = {}
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace(' ','-').replace('.-','-')
        print(author_mod)
        url = base_url + 'author/'+author_mod.strip()+'/'
DoB = {}
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace(' ','-').replace('.-','-').replace('.','-')
        print(author_mod)
        url = base_url + 'author/'+author_mod.strip()+'/'
DoB = {}
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace(' ','-').replace('.-','-').replace('.','-')
        print(author_mod)
        url = base_url + 'author/'+author_mod.strip()+'/'
        response = requests.get(url)
        html_data = response.text
        data = BeautifulSoup(html_data,'html.parser')
        date_of_birth = data.find(class_='author-born-date').string.strip()
        DoB[author] = date_of_birth

print(DoB)
DoB = {}
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace(' ','-').replace('.-','-').replace('.','-')
        print(author_mod)
        url = base_url + 'author/'+author_mod.strip()+'/'
        response = requests.get(url)
        html_data = response.text
        data = BeautifulSoup(html_data,'html.parser')
        date_of_birth = data.find(class_='author-born-date').string.strip()
        DoB[author] = date_of_birth
print(DoB)
import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com/'

for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    quotes = data.find_all(class_='quote')
    for quote_str in quotes: 
        author = quote_str.find(class_='author').string
        if author == 'Albert Einstein': 
            quote = quote_str.find(class_='text').string
            print(quote)
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/ApplicationsOfAI.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping')
import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
response = requests.get(url,verify=False)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
print(data)
from selenium import webdriver 
driver = webdriver.Chrome(executable_path='/Driver')
driver
from selenium import webdriver 
driver = webdriver.Chrome(executable_path='/Driver/chromedriver.exe')
driver
from selenium import webdriver 
driver = webdriver.Chrome(executable_path='\Driver\chromedriver.exe')
driver
from selenium import webdriver 
driver = webdriver.Chrome(executable_path='C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe')
driver
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-extensions")
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, chrome_options=options)
driver
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-extensions")
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.chrome(driverpath,chrome_options=options)
driver.get('https://codingninjas.in/')
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-extensions")
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(driverpath,chrome_options=options)
driver.get('https://codingninjas.in/')
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-extensions")
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(driverpath,chrome_options=options)
driver
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-extensions")
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, chrome_options=options)
driver
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbod")
options.add_argument("--disable-infobars")
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, chrome_options=options)
driver
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-infobars")
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, chrome_options=options)
driver
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def setOptions():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    return options


options = setOptions()
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, options=options)
driver
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def setOptions():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    return options


options = setOptions()
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, options=options)
driver.get('https://codingninjas.in')
driver.title()
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def setOptions():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    return options


options = setOptions()
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, options=options)
driver.get('https://codingninjas.in')
driver.title()

## ---(Tue Jan 28 15:56:26 2020)---
runfile('C:/Data Backup/E Drive/Learning/Python/WebScraping/Selenium/SeleniumFirst.py', wdir='C:/Data Backup/E Drive/Learning/Python/WebScraping/Selenium')
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def setOptions():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    return options


options = setOptions()
driverpath = 'C:\Data Backup\E Drive\Learning\Python\WebScraping\Selenium\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath, options=options)
driver.get('https://codingninjas.in')
driver.title()
driver.title