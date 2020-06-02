class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)    
    
    def search(self, data):
    #Implement this function here
        return self.searchTree(self.root,data)
    
    def searchTree(self, root,data): 
        if root is None: 
            return False 
        
        if root.data == data: 
            return True
        
        if root.data < data: 
            return self.searchTree(root.right,data)
        else: 
            return self.searchTree(root.left,data)        
        
        
    def insert(self, data):
    #Implement this function here
        self.numNodes = self.numNodes + 1
        self.root = self.insertTreeHelper(self.root,data)
        
    def insertTreeHelper(self, root, data): 
        if root is None: 
            return BinaryTreeNode(data)
        
        if root.data <= data: 
            root.right = self.insertTreeHelper(root.right,data)
            return root 
        else: 
            root.left = self.insertTreeHelper(root.left,data)
            return root 
        
    def delete(self, data):
    #Implement this function here
        self.root,deleted = self.deleteTreeHelper(self.root,data)
        if deleted: 
            self.numNodes = self.numNodes - 1 
    
    def deleteTreeHelper(self, root, data): 
        if root is None: 
            return None, False 
        
        if root.data < data: 
            root.right, deleted = self.deleteTreeHelper(root.right,data)
            return root,deleted
        elif root.data > data: 
            root.left, deleted = self.deleteTreeHelper(root.left,data)
            return root,deleted
        elif root.data == data: 
            if root.left is None and root.right is None: 
                return None, True
            elif root.left is None and root.right is not None: 
                return root.right, True
            elif root.left is not None and root.right is None: 
                return root.left, True
            else: 
                right_Min_Val = self.min_val(root.right)
                newNode = BinaryTreeNode(right_Min_Val)
                newNode.left = root.left
                newNode.right = root.right
                self.delete_node(root.right,right_Min_Val) 
                return newNode, True 
            
    def delete_node(self,root,del_value): 
        if root is None: 
            return None 
        
        if root.data == del_value: 
            return None 
        
        root.left  = self.delete_node(root.left,del_value)
        root.right = self.delete_node(root.right,del_value)
        
        return root 
    
    def min_val(self,root): 
        if root is None: 
            return 9999999999999
        
        return min(root.data,self.min_val(root.right),self.min_val(root.left))
    
    def count(self):
        return self.numNodes
    
b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1
        
    