import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printNodeswithoutSibling(root):
    # Given a Binary Tree and an integer x, check if node with data x is present
    # in the input binary tree or not. Return True or False.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None: 
        return 
    
    if root.left is not None and root.right is None: 
        print(root.left.data,end=' ')
        printNodeswithoutSibling(root.left)
    elif root.left is None and root.right is not None: 
        print(root.right.data,end=' ')
        printNodeswithoutSibling(root.right)
    else: 
        printNodeswithoutSibling(root.left)
        printNodeswithoutSibling(root.right)
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
printNodeswithoutSibling(root)