import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBalancedTree(root): 
    if root is None: 
        return True 
    
    heightdiff = height(root.left) - height(root.right)
    if heightdiff < 0: 
        heightdiff = 0 - heightdiff
    
    if heightdiff <=1: 
        if checkBalancedTree(root.left): 
            if checkBalancedTree(root.right): 
                return True 
            else: 
                return False 
        else: 
            return False 
    else: 
        return False 
    

def height(root): 
    if root is None: 
        return 0 
    
    return 1 + max(height(root.left),height(root.right))

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

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printbt(root)
if checkBalancedTree(root): 
    print('Yes it is a Balanced Tree')
else: 
    print('No it is not a Balanced Tree')
