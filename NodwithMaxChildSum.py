class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(tree):
    # Return the node and its sum
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree is None: 
        return None, 0 
    
    cursum = tree.data 
    for child in tree.children: 
        cursum += child.data 
    
    maxnode = tree
    maxsum  = cursum 
    for child in tree.children: 
        childMaxNode, childMaxSum = maxSumNode(child)
        if childMaxSum > maxsum: 
            maxsum = childMaxSum
            maxnode = childMaxNode
    
    return maxnode, maxsum 
            
    

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
temp, tempSum = maxSumNode(tree)
print(temp.data)


a = 1 
b = 2
print(a!=b)