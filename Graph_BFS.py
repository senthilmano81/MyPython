import queue
class Graph: 
    def __init__(self,nVertices): 
        self.nVertices = nVertices
        self.adjMatrix = [[0 for x in range(nVertices)] for y in range(nVertices)]
    
    def addEdge(self,v1,v2): 
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self,v1,v2): 
        if self.containsEdge(v1,v2) is False: 
            return 
        
        self.adjMatrix[v1][v2] = 0 
        self.adjMatrix[v2][v1] = 0 
    
    def containsEdge(self,v1,v2): 
        return True if self.adjMatrix[v1][v2] > 0 else False 
    
    def bfs(self): 
        visited = [False for x in range(self.nVertices)]
        q       = queue.Queue()
        q.put(0)
        visited[0] = True 
        while not q.empty(): 
            curr = q.get()
            print(curr,end=' ')
            for i in range(self.nVertices):
                if visited[i] is False and self.adjMatrix[curr][i] > 0:                     
                    q.put(i)
                    visited[i] = True         
    
    def __str__(self): 
        return str(self.adjMatrix)
    
    
v, e = input().split()
v = int(v)
gr = Graph(v)
e = int(e)
for i in range(e): 
    vert = [int(x) for x in input().split()]
    gr.addEdge(vert[0],vert[1])
gr.bfs()
        