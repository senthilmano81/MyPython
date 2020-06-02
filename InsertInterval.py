def search(in_range,new_range,st=9999,end=9999):
    if st == 9999: 
        st = 0 
    if end == 9999: 
        end = len(in_range) - 1        
    
    if new_range[0] <= in_range[st][0]: 
        return st 
    
    if new_range[0] >= in_range[end][0]:
        return st + 1
    
    if end < st + 1: 
        return st 
    
    mid = st + (end-st + 1)//2
    if new_range[0] >= in_range[st][0] and new_range[0] <= in_range[mid-1][0]: 
        return search(in_range,new_range,st,mid-1)
    else: 
        return search(in_range,new_range,mid,end)


n = int(input())
in_range = []
for i in range(n): 
    ele = input().split()
    in_range.append(ele)
in_range = [[int(x[y]) for y in range(len(x))] for x in in_range]
new_range = [int(x) for x in input().split()]

st = search(in_range,new_range)
arr = in_range[:st]
out_arr = []
lower   = new_range[0]
upper   = new_range[1]

while st < len(in_range): 
    if lower <= in_range[st][1] and upper >= in_range[st][0]:
        lower = min(lower,in_range[st][0])
        upper = max(upper, in_range[st][1])
    else: 
        break 
    st +=1 
    
arr.append([lower,upper])
arr.extend(in_range[st:])
for i in arr: 
    print(*i)