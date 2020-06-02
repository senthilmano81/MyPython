class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    #  Given a sorted linked list (elements are sorted in ascending order).
    #  Eliminate duplicates from the given LL, such that output LL contains only
    #  unique elements.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    curr = head.next  
    prev = head 
    while curr is not None: 
        if curr.data == prev.data: 
            curr = curr.next 
        else: 
            prev.next = curr 
            prev = curr 
            curr = curr.next 
            prev.next = None  
    return head 

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
l = eliminate_duplicate(l)
printll(l)
