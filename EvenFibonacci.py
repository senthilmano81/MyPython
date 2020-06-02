n = int(input())

n1 = 0 
n2 = 1
sum  = 0
n3  = 1 
while n3 < n: 
    n3 = n1 + n2 
    n1 = n2
    n2 = n3 
    print(n3)
    if n3 % 2 == 0: 
        sum = sum + n3
        
print('sum=',sum)

arr = [1,2,3,4,5,0]
print(all(i>0 for i in arr))