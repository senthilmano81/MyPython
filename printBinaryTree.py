class BinaryTree: 
    def __init__(self,data): 
        self.data = data 
        self.left = None
        self.right = None 
        
def printbt(root):
    if root is None: 
        return 
    print(root.data,end=' ')
    if root.left is not None: 
        print(' L: ', root.left.data,end=' ')
    else: 
        print(' L: None',end=' ')
    if root.right is not None: 
        print(' R: ',root.right.data)
    else:
        print(' R: None')
    
    printbt(root.left)
    printbt(root.right)
    return 

def NumberOfNodes(root): 
    if root is None: 
        return 0 
    return 1 + NumberOfNodes(root.left) + NumberOfNodes(root.right)

def treeInput(): 
    rootData = int(input())
    if rootData == -1: 
        return None 
    root     = BinaryTree(rootData)
    rootLeft = treeInput()
    rootRight= treeInput()
    root.left = rootLeft
    root.right = rootRight 
    return root
        
root = treeInput()
printbt(root)
print('number of nodes : ', NumberOfNodes(root))
