def checkRedundant(string):
#### Implement Your Code Here
    s = stack()
    for char in string: 
        if char in '{[(':
            s.push(char,True)            
        elif char == '}': 
            prevchar, flag = s.pop()
            if prevchar != '{':
                return True
            else: 
                if flag: 
                    return True
        elif char == ')':
            prevchar, flag = s.pop()
            if prevchar != '(':
                return True
            else: 
                if flag: 
                    return True 
        elif char == ']':
            prevchar, flag = s.pop()
            if prevchar != '[':
                return True
            else: 
                if flag: 
                    return True
        else: 
            if not s.isEmpty(): 
                s.updateFlag(False)
    return False
            
    
class stack: 
    def __init__(self): 
        self.__size = 0 
        self.__arr  = []
        self.__flag = []
    
    def push(self,data,flag):
        self.__arr.append(data)
        self.__flag.append(flag)
        self.__size = self.__size + 1
    
    def updateFlag(self,flag): 
        if flag: 
            self.__flag[-1] = True
        else: 
            self.__flag[-1] = False 
    
    def pop(self):
        if self.isEmpty():
            return None 
        popdata = self.__arr[-1]
        popflag = self.__flag[-1]
        self.__arr = self.__arr[:-1]
        self.__flag = self.__flag[:-1]
        self.__size = self.__size - 1
        
        return popdata, popflag  
        
    def top(self): 
        if self.isEmpty(): 
            return None 
        else: 
            return self.__arr[-1], self.__flag[-1]
        
    def isEmpty(self): 
        return self.__size == 0 
    
    def getsize(self): 
        return self.__size

    
    
string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')




