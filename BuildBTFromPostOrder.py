import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder,po='n'):
    # Given Postorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 8 Nodes with following input:
    # postOrder: 8 4 5 2 6 7 3 1
    # inOrder: 4 8 2 5 1 6 3 7
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if po == 'n': 
        po = len(postorder) - 1 
        
    if len(inorder) == 0: 
        return po+1, None 
    
    if po < 0: 
        return po, None 
    
    root = BinaryTreeNode(postorder[po])
    try: 
        idx = inorder.index(postorder[po])
    except: 
        idx = -1
        
    if idx >= 0:    
        po, root.right = buildTreePostOrder(postorder,inorder[idx+1:],po-1)    
        po, root.left  = buildTreePostOrder(postorder,inorder[:idx],po-1)       
        
    return po, root
    

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
po, root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
