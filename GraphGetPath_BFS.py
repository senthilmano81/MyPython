import queue
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
    
    def capturePath(self,v1,v2,visited): 
        dic  = {}
        q    = queue.Queue()      
        q.put(v1)
        dic[v1]     = [v1]
        visited[v1] = True 
        found       = False 
        while not q.empty(): 
            curr = q.get()
            for i in range(self.nVertices): 
                if visited[i] is True or self.adjMatrix[curr][i] == 0: 
                    continue
                
                q.put(i)
                visited[i]  = True 
                dic[i]      = [x for x in dic[curr]]
                dic[i].append(i)
                if i == v2: 
                    found = True 
                    path  = dic[i]
                    break 
            if found: 
                break                                         
            
        return path[-1::-1] if found else []
    
    def getPath(self,v1,v2): 
        visited = [False for x in range(self.nVertices)]
        return self.capturePath(v1,v2,visited)
    
    def __str__(self): 
        return str(self.adjMatrix)
    
    
v, e = input().split()
v = int(v)
gr = Graph(v)
e = int(e)
for i in range(e): 
    vert = [int(x) for x in input().split()]
    gr.addEdge(vert[0],vert[1])
vert = [int(x) for x in input().split()]
path = gr.getPath(vert[0],vert[1])
print(*path)


