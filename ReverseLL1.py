class Node: 
    def __init__(self,data): 
        self.data = data
        self.next = None 
        
def ll(arr):
    if len(arr) == 0 : 
        return None
    head = Node(arr[0])
    last = head 
    for data in arr[1:]: 
        last.next = Node(data)
        last      = last.next 
    return head

def printll(head):
    while head: 
        print(head.data,end=' ')
        head = head.next 
    print()

def splitll(head): 
    if head is None: 
        return None 
    
    length = lengthll(head)
    if length < 2: 
        return None 
    
    length = length // 2 
    for i in range(length): 
        prev = head 
        head = head.next
    prev.next = None
    return head

        
def lengthll(head): 
    length = 0 
    while head: 
        length += 1
        head = head.next 
    return length 
    
def reversell(head): 
    if head is None or head.next is None: 
        return head
    
    newhead = reversell(head.next)
    tail      = head.next
    tail.next = head 
    head.next = None 
    
    return newhead

def mergell(head1,head2): 
    head = head1
    head1 = head.next
    head.next = None     
    H1flag = False
    while head1 is not None or head2 is not None:  
        if H1flag: 
            if head1 is not None: 
                head.next = head1
                head1 = head1.next 
                head = head.next 
                if head is not None: 
                    head.next = None
            H1flag = False 
        else: 
            if head2 is not None: 
                head.next= head2
                head2 = head2.next 
                head = head.next 
                if head is not None: 
                    head.next = None
            H1flag = True 
         
arr = [int(x) for x in input().strip().split()]
head = ll(arr[:-1])
head2 = reversell(splitll(head))
mergell(head,head2)
printll(head)