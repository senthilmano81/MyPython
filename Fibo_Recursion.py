def Fibo(n): 
    if n==0: 
        return 0 
    if n==1: 
        return 1 
    
    fiboval= Fibo(n-1) + Fibo(n-2)
    
    return fiboval 

n= int(input('Enter number of Elements required in Fibonacci Series: '))
sum  = Fibo(n)
print(sum)



v,e  = (int(x) for x in input().split())
print(v)
print(e)
print(v*e)