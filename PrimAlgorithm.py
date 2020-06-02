## Read input as specified in the question.
## Print output as specified in the question.
import sys
class Graph: 
    def __init__(self,nVertices): 
        self.nVertices = nVertices
        self.adj_matrix = [[0 for x in range(nVertices)] for y in range(nVertices)]
    
    def addEdge(self,v1,v2,wt): 
        self.adj_matrix[v1][v2] = wt
        self.adj_matrix[v2][v1]  = wt
    
    def removeEdge(self,v1,v2): 
        if not self.containsEdge(v1,v2): 
            return 
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0 
    
    def containsEdge(self,v1,v2): 
        return True if self.adj_matrix[v1][v2] > 0 else False 
    
    def __str__(self): 
        return str(self.adj_matrix)
        
    def prim(self): 
        visited   = [False for x in range(self.nVertices)]
        parent    = [-1 for x in range(self.nVertices)]
        weight    = [sys.maxsize for x in range(self.nVertices)]
         
        for i in range(self.nVertices-1): 
            minVertex          = self.getMinVertex(visited,weight)
            visited[minVertex] = True 
            for j in range(self.nVertices): 
                if self.adj_matrix[minVertex][j] > 0 and visited[j] is False: 
                    if weight[j] > self.adj_matrix[minVertex][j]: 
                        weight[j] = self.adj_matrix[minVertex][j]
                        parent[j] = minVertex
                
        for i in range(1,self.nVertices): 
            if i > parent[i]: 
                print(str(parent[i]) + ' ' + str(i) + ' '+ str(weight[i]))
            else: 
                print(str(i) + ' ' + str(parent[i]) + ' '+ str(weight[i]))
        return
        
    def getMinVertex(self,visited,weight):
        minVertex = -1
        for i in range(self.nVertices): 
            if visited[i] is False and (minVertex==-1 or weight[minVertex] > weight[i]):
                minVertex = i 
        return minVertex
        
        
v,e = (int(x) for x in input().split())
gr  = Graph(v)
for i in range(e): 
    v1,v2,wt = (int(x) for x in input().split())
    gr.addEdge(v1,v2,wt)

gr.prim()