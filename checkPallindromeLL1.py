class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check_palindrome(head) :
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if lengthll(head) <= 1: 
        return True 
    head1 = head
    head2 = reversell(splitll(head))
    PalFlag = True
    for i in range(lengthll(head1)): 
        if head1.data != head2.data: 
            PalFlag = False
            break
        head1 = head1.next
        head2 = head2.next 
        
    return PalFlag 

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def splitll(head): 
    if head is None: 
        return None 
    
    lenll = lengthll(head)
    if lenll < 2: 
        return None 
    
    length = lenll // 2 
    rem    = lenll % 2 
    for i in range(length): 
        prev = head 
        head = head.next
    prev.next = None
    if rem == 1: 
        head = head.next 
        
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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
