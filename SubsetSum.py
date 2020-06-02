
def subsetSum(l):
#Implement Your Code Here
    map = {0:[-1]}
    sum = 0 
    for i in range(len(l)): 
        sum += l[i]
        if map.get(sum,'NF') == 'NF': 
            map[sum] = [i]
        else: 
            map[sum].append(i)
    
    maxlen = 0 
    for ele in map:             
        li = map[ele]
        if len(li) > 1: 
            for i in range(0,len(li)-1): 
                maxlen = max(maxlen,(li[i+1] - li[i]))
                
    return maxlen 
                
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
finalLen= subsetSum(l)
print(finalLen)