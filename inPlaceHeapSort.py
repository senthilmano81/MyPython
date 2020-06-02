
## Read input as specified in the question.
## Print output as specified in the question.
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

arr.sort(reverse=True)
print(arr)
