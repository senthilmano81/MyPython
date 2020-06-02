class Node:
    def __init__(self,data): 
        self.data = data
        self.next = None
        
def mergeSort(root): 
    if root is None: 
        return root     
    
    length = lengthLL(root)
    if length == 1: 
        return root
    
    mid    = (length // 2)
    root1  = root
    root2  = root 
    i      = 0
    while root2 is not None and i <= mid: 
        temp  = root2 
        root2 = root2.next 
        if i == mid: 
            temp.next = None 
        i = i + 1
        
    root1 = mergeSort(root1)
    root2 = mergeSort(root2)
    root = merge(root1,root2)
    
    return root 

def merge(root1,root2): 
    root = None
    curr = None 
    while root1 is not None and root2 is not None: 
        if root1.data < root2.data: 
            curr = root1
            root1= root1.next 
            curr.next = None
        else: 
            curr = root2
            root2 = root2.next
            curr.next = None 
        if root is None: 
            root = curr 
    
    while root1 is not None: 
        curr = root1
        root1=root1.next
        curr.next = None
        if root is None: 
            root = curr
            
    while root2 is not None: 
        curr = root2 
        root2 = root2.next 
        curr.next = None
        if root is None: 
            root = curr 
            
    return root 
        

def lengthLL(root): 
    length= 0 
    while root is not None: 
        length += 1
        root = root.next
    return length     

def array2LL(arr): 
    root = None
    curr = None
    for ele in arr: 
        newNode = Node(ele)
        if curr is None: 
            root = newNode
        else: 
            curr.next = newNode
        curr = newNode
    return root 

def printLL(root): 
    while root is not None: 
        print(root.data,end=' ')
        root = root.next 
    return 
    
arr = [int(x) for x in input().split()]
root = array2LL(arr)
printLL(mergeSort(root))


