class TreeNode: 
    def __init__(self,data): 
        self.data = data 
        self.children = list()
        
def printGT(root): 
    if root is None: 
        return 
    
    print(root.data,end=' ')
    for child in root.children: 
        printGT(child)

def printTreeDetails(root): 
    if root is None: 
        return 
    print(root.data,end=':')
    for child in root.children: 
        print(child.data,end=',')
    print()    
    for child in root.children: 
        printTreeDetails(child)
    
                
root = TreeNode(5)
li   = [2,9,8,7]
for ele in li: 
    newNode = TreeNode(ele)
    root.children.append(newNode)
    if ele == 9: 
        n1 = TreeNode(15)
        n2 = TreeNode(1)
        newNode.children.append(n1)
        newNode.children.append(n2)

printGT(root)
print()
printTreeDetails(root)
min(1,2)