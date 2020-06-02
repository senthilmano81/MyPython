## Read input as specified in the question.
## Print output as specified in the question.
def sumOfDigits(num): 
    if num // 10 == 0: 
        return num 
    
    return num % 10 + sumOfDigits(num//10)

def geoSum(num): 
    if num==0: 
        return 1
    return 1/(2**num) + geoSum(num-1)


num = int(input())
print(sumOfDigits(num))
a= geoSum(num)
print('%.5f'%a)
