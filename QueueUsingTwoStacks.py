class QueueUsing2Stacks: 
    def __init__(self): 
        self.__s1=[]
        self.__s2=[]
        self.__size = 0 
        
    def enqueue(self,data): 
        self.__s1.append(data)
        self.__size = self.__size + 1
    
    def dequeue(self): 
        if self.isEmpty(): 
            return - 1 
        
        for i in range(self.__size-1): 
            self.__s2.append(self.__s1.pop())
        
        data = self.__s1.pop()        
        
        for i in range(self.__size-1): 
            self.__s1.append(self.__s2.pop())
        
        self.__size = self.__size  - 1 
        return data 
        
    def front(self): 
        if self.isEmpty():
            return None
        return self.__s1[-1]
    
    def getSize(self): 
        return self.__size
    
    def isEmpty(self): 
        return self.__size == 0 


q = QueueUsing2Stacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while not q.isEmpty(): 
    print(q.dequeue())
