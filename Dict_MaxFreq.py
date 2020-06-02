def maxFreq(l):
    # Please add your code here
    freq = {}
    for ele in l: 
        if freq.get(ele,'Not Found') == 'Not Found': 
            freq[ele] = 1
        else: 
            freq[ele] += 1
    
    maxFrequency = 0 
    print(freq)
    for ele in freq: 
        if freq[ele] > maxFrequency:
            maxFrequency = freq[ele]
            element      = ele 
    
    return element 

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
