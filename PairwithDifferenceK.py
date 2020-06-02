
def printPairDiffK(l, k):
#Implement Your Code Here
    map = dict.fromkeys(l,0)
    for ele in l: 
        map[ele] += 1
    
    k = abs(k)
    if k==0: 
        for ele in map: 
            count = int(map[ele] * (map[ele] - 1) / 2) 
            for i in range(count): 
                print(ele, ele)
    else: 
        for ele in l: 
            count = map.get(ele,'NF')
            if count == 'NF':
                continue 
            
            lcount = map.get(ele-k,'NF')
            if lcount != 'NF': 
                for i in range(count*lcount): 
                    print(ele-k,ele)
                    
            ucount = map.get(ele  + k, 'NF')
            if ucount != 'NF': 
                for i in range(count*ucount): 
                    print(ele, ele+k)
            map.pop(ele)
                

    return 


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)