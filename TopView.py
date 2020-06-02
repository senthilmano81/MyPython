import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTopView(root): 
    if root is None: 
        return
    
    print(root.data,end=' ')
    LeftNode = root.left 
    RightNode = root.right 
    while LeftNode is not None or RightNode is not None: 
        if LeftNode is not None: 
            print(LeftNode.data,end=' ')
            LeftNode = LeftNode.left
        
        if RightNode is not None: 
            print(RightNode.data,end=' ')
            RightNode = RightNode.right
    
    
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
printTopView(root)