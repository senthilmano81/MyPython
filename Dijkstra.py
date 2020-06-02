## Read input as specified in the question.
## Print output as specified in the question.
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

    def Dij_helper(self,visited,parent,distance):
        
        for i in range(self.nVertices-1): 
            minVertex          = self.getMinVertex(visited,distance)
            visited[minVertex] = True 
            for vertex in range(self.nVertices): 
                if visited[vertex] is False and self.containsEdge(minVertex,vertex): 
                    newdistance      = distance[minVertex] + self.adj_matrix[minVertex][vertex]
                    if newdistance < distance[vertex]:
                        distance[vertex] = newdistance
                        parent[vertex]   = minVertex
        return 
        
    def Dijkstra(self): 
        visited   = [False for x in range(self.nVertices)]
        parent    = [-1 for x in range(self.nVertices)]
        distance  = [sys.maxsize for x in range(self.nVertices)]
        distance[0] = 0 
        
        self.Dij_helper(visited,parent,distance)
        return distance 
        
    def getMinVertex(self,visited,distance):
        minVertex = -1
        mindistance = sys.maxsize
        print('visited=',visited)
        print('distance=',distance)
        for vertex in range(self.nVertices):
            print('vertex=',vertex)
            if visited[vertex] is False and (minVertex==-1 or distance[vertex] < mindistance):
                mindistance = distance[vertex]
                minVertex   = vertex
        return minVertex
        
        
v,e = (int(x) for x in input().split())
gr  = Graph(v)
for i in range(e): 
    v1,v2,wt = (int(x) for x in input().split())
    gr.addEdge(v1,v2,wt)

distance = gr.Dijkstra()
for vertex in range(len(distance)): 
    print(vertex,distance[vertex])