class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if i > j: 
        i,j = j,i 
    curr = head 
    count = 0 
    prev  = None
    while curr is not None: 
        if count == i: 
            previ = prev
            curri = curr
        elif count == j: 
            prevj = prev
            currj = curr 
        count = count + 1
        prev = curr
        curr = curr.next 
    
    if j == i + 1: 
        curri.next = currj.next 
        currj.next = curri 
        if previ is not None: 
            previ.next = currj        
    else: 
        temp = currj.next 
        currj.next = curri.next  
        curri.next = temp      
        if previ is not None: 
            previ.next = currj        
        if prevj is not None: 
            prevj.next = curri 
        
    if i==0: 
        head = currj 
        
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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)
