class fib_data: 
    def __init__(self): 
        self.fibmap = {1:1,2:1}

    def _lookup(self,n):
        if n in self.fibmap:
            return self.fibmap[n]
        else:
            return -1
    
    def _add_new(self,n,ans): 
        self.fibmap[n] = ans
        
        return   
    
    def fibb(self,n): 
        if n == 1 or n==2: 
            return 1   
        
        fibb1 =  self._lookup(n-1)
        if fibb1 == -1: 
            fibb1 = self.fibb(n-1)
            self._add_new(n-1,fibb1)
            
        fibb2 =  self._lookup(n-2)
        if fibb2 == -1: 
            fibb2 = self.fibb(n-2)
            self._add_new(n-2,fibb2)
        
        return fibb1 + fibb2


n= int(input())
c = fib_data()
for i in range(1,n+1):
    print(i,',',c.fibb(i))