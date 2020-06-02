class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
            
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def __percolatedown(self): 
        parentindex = 0 
        while (parentindex * 2 + 2) <= (self.getSize() - 1): 
            child1index = (parentindex*2) + 1 
            child2index = (parentindex*2) + 2
            if self.pq[child1index].priority < self.pq[child2index].priority: 
                childindex = child1index
            else: 
                childindex = child2index 
            
            if self.pq[childindex].priority < self.pq[parentindex].priority: 
                self.pq[parentindex], self.pq[childindex] = self.pq[childindex], self.pq[parentindex]
                parentindex = childindex
            else: 
                break
        
    def removeMin(self):
        #Implment This Function Here
        if self.isEmpty(): 
            return None
        last = self.getSize() - 1
        self.pq[0],self.pq[last] = self.pq[last], self.pq[0]
        popNode = self.pq.pop()
        self.__percolatedown()
        return popNode.ele 
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    