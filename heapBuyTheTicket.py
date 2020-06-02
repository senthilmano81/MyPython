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
