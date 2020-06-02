
class Node: 
    def __init__(self,data): 
        self.data = data 
        self.next = None 

class Stackll: 
    
    def __init__(self): 
        self.__head = None 
        self.__size = 0 
        
    def push(self,data):
        if self.isEmpty(): 
            self.__head = Node(data)
        else: 
            curr             = self.__head 
            self.__head      = Node(data)            
            self.__head.next = curr
        
        self.__size = self.__size + 1 
            
    def pop(self): 
        if self.isEmpty(): 
            return None
        else: 
            popele = self.__head
            self.__head = self.__head.next 
            popele.next = None 
            self.__size = self.__size - 1 
            return popele.data
    
    def top(self): 
        if self.isEmpty(): 
            return None
        else: 
            return self.__head.data 
        
    def isEmpty(self): 
        return self.__size == 0 
        
    def getSize(self): 
        return self.__size 


def reversestack(s1,s2): 
    if s1.getSize() <= 1: 
        return s1 
    
    top = s1.pop()
    s1 = reversestack(s1,s2)
    for i in range(s1.getSize()): 
        data = s1.pop()
        s2.push(data)
        
    s1.push(top)
    for i in range(s2.getSize()): 
        data = s2.pop()
        s1.push(data)
        
    return s1
    
    
arr = [int(x) for x in input().split()]
s1  = Stackll()

for ele in arr: 
    s1.push(ele)
s2  = Stackll()

s1 = reversestack(s1,s2)    
for i in range(s1.getSize()): 
    print(s1.pop(),end=' ')

