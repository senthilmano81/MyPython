class stack: 
    def __init__(self): 
        self.__size = 0 
        self.__arr  = []
    
    def addarray(self,arr): 
        self.__size = 0
        self.__arr  = []
        for ele in arr: 
            self.push(ele)
    
    def push(self,data):
        self.__arr.append(data)
        self.__size = self.__size + 1
    
    def pop(self):
        if self.isEmpty():
            return None 
        popdata = self.__arr[-1]
        self.__arr = self.__arr[:-1]
        self.__size = self.__size - 1
        
        return popdata 
        
    def top(self): 
        if self.isEmpty(): 
            return None 
        else: 
            return self.__arr[:-1]
        
    def isEmpty(self): 
        return self.__size == 0 
    
    def getsize(self): 
        return self.__size
    
    
def reversestack(s1,s2): 
    if s1.getsize() <= 1: 
        return s1 
    
    top = s1.pop()
    s1 = reversestack(s1,s2)
    for i in range(s1.getsize()): 
        data = s1.pop()
        s2.push(data)
        
    s1.push(top)
    for i in range(s2.getsize()): 
        data = s2.pop()
        s1.push(data)
        
    return s1
    
    
arr = [int(x) for x in input().split()]
s1  = stack()
s1.addarray(arr)
s2  = stack()

s1 = reversestack(s1,s2)    
for i in range(s1.getsize()): 
    print(s1.pop(),end=' ')
    
    