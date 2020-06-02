class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __gt__(self,other): 
        if self.data > other.data: 
            return True
        else: 
            return False 
    def __str__(self):
        return str(self.data)

def maxDataNode(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree is None: 
        return 0 
    
    maxnode = tree
    for child in tree.children: 
        childmax = maxDataNode(child)
        if childmax > maxnode: 
            maxnode = childmax
    return maxnode

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(maxDataNode(tree).data)
