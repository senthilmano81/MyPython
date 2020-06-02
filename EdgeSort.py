class Edge:
    def __init__(self,source,dest,weight):
        self.source = source
        self.dest   = dest
        self.weight = weight 
    
    def __gt__(self,other): 
        return True if self.weight > other.weight else False 
    
    def __lt__(self,other): 
        return True if self.weight < other.weight else False 
    
    def __eq__(self,other): 
        return True if self.weight == other.weight else False
    
    def __ge__(self,other): 
        return True if self.weight >= other.weight else False
    
    def __le__(self,other):
        return True if self.weight <= other.weight else False
    
    def __ne__(self,other):
        return True if self.weight != other.weight else False 
    
    def __str__(self): 
        return str(self.source) + ' ' + str(self.dest) + ' '+ str(self.weight)

e1 = Edge(0,1,3)
e2 = Edge(0,3,5)
e3 = Edge(1,2,1)
e4 = Edge(2,3,8)

if e1 > e2: 
    print(e1,'is greater than ',e2)
elif e1 < e2: 
    print(e2,'is greater than ',e1)
else: 
    print(e1,' is equal to ',e2)
    
arr = [e1,e2,e3,e4]
for ele in arr: 
    print(ele,end=' ')
print()
arr.sort()
for ele in arr: 
    print(ele,end=' ')
print()
    


    
    
        


