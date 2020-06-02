def longestConsecutiveSubsequence(l):
#Implement Your Code Here
#You have To Return the list of longestConsecutiveSubsequence\
    final =[]
    map   = dict.fromkeys(l,0)
    first = ''
    last  = ''
    maxlen = 0 
    consmap = {}
    for ele in l: 
        if map.get(ele,-9999) == -9999: 
            continue 
        
        first = ele 
        while map.get(first-1,-9999) != -9999: 
            first = first-1
            map.pop(first)
        last = ele 
        while map.get(last+1,-9999) != -9999: 
            last = last + 1
            map.pop(last)
        map.pop(ele)
        
        newlen = last-first + 1
        if newlen >= maxlen:
            if newlen > maxlen: 
                consmap.clear()
            maxlen= last-first+1
            consmap[first] = maxlen 
    
    for ele in l: 
        if consmap.get(ele,-9999) != -9999: 
            final = range(ele,ele+consmap[ele])
            break
        
    return final 

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
final = longestConsecutiveSubsequence(l)
for num in final:
    print(num)