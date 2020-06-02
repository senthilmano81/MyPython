# Python Program for Beginner
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def isBST(root,in_min=-99999999,in_max=99999999):
    if root is None: 
        return True
    
    if root.data < in_min  or root.data > in_max:
        return False 
    
    return isBST(root.left,in_min,root.data) and isBST(root.right,root.data,in_max) 

def constructBST(lst):
    # Given a sorted integer array A of size n which contains all unique
    # elements. You need to construct a balanced BST from this input array.
    # Return the root of constructed BST. If array size is even, take first mid
    # as root.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if len(lst)==0: 
        return None 
    
    mid = len(lst) // 2 + len(lst) % 2 - 1 
    root       = BinaryTreeNode(lst[mid])
    root.left  = constructBST(lst[:mid])
    root.right = constructBST(lst[mid+1:])
    
    return root 

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

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
lst=[int(i) for i in input().strip().split()]
root = buildLevelTree(lst)
#root=constructBST(lst.sort())
if isBST(root): 
    print('True')
else: 
    print('False')