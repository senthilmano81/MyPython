class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kReverse(head, n) :
    #  Implement kReverse( k ) in a linked list i.e. you need to reverse
    #  first K elements then reverse next k elements and join the linked list and
    #  so on. Indexing starts from 0. If less than k elements left in the last,
    #  you need to reverse them as well. If k is greater than length of LL,
    #  reverse the complete LL. If n is 4 and LL is:
    #  Input: 1 2 3 4 5 6 7 8 9 10
    #  Output: 4 3 2 1 8 7 6 5 10 9 
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    newhead = None 
    curr    = head 
    tail    = None 
    while curr is not None: 
        head1, head2 = splitll(curr,n)        
        tmphead = reversell(head1)
        if tail is not None: 
            tail.next = tmphead 
        tail = head1 
        if newhead is None: 
            newhead = tmphead  
        curr = head2              
        
    return newhead    

def length(head): 
    count = 0 
    while head is not None: 
        count = count + 1
        head = head.next 
    return count 

def reversell(head): 
    if head is None or head.next is None: 
        return head
    newhead = reversell(head.next)
    tail = head.next 
    tail.next = head 
    head.next = None 
    return newhead 

def splitll(head,k): 
    if length(head) <= k: 
        return head, None  
    head1 = head
    tail1 = None 
    head2 = None
    count = 0
    curr  = head
    while curr is not None:         
        count = count + 1 
        if count == k:
            tail1 = curr 
            head2 = curr.next 
        curr = curr.next    
    
    tail1.next = None 
    
    return head1, head2


def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = kReverse(l, i)
printll(l)
