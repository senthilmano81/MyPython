import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None: 
        return 
    
    if root.left is None and root.right is None:
        if sumOfArray(lst) + root.data == k: 
            print(*lst,end=' ')
            print(root.data)
        return 
    
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left, k, lst)
    rootToLeafPathsSumToK(root.right, k, lst)
    lst.pop()
    
    return         

def sumOfArray(arr): 
    if len(arr) == 0: 
        return 0 
    else: 
        sum = 0 
        for ele in arr: 
            sum = sum + ele
        return sum 
    
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
k=int(input())
rootToLeafPathsSumToK(root, k, [])
