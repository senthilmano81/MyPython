simport queue
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
    
    def dfs(self,sv,visited,connec): 
        visited[sv] = True 
        print('sv = ',sv)
        connec.append(sv)
        for i in range(self.nVertices): 
            if visited[i] is False and self.adjMatrix[sv][i] >0: 
                self.dfs(i,visited,connec)
        return connec
    
    def printConnections(self): 
        visited = [False for x in range(self.nVertices)]
        for sv in range(self.nVertices): 
            print(' ')
            if visited[sv] is False: 
                connec = self.dfs(sv,visited,[])
                print(*connec)
        return 
    
    def __str__(self): 
        return str(self.adjMatrix)
    
    
v, e = input().split()
v = int(v)
gr = Graph(v)
e = int(e)
for i in range(e): 
    vert = [int(x) for x in input().split()]
    gr.addEdge(vert[0],vert[1])
gr.printConnections()


