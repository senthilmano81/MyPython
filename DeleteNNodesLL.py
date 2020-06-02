# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteList(head,retain,delete):
    #  Even after Odd LinkedList: Arrange elements in a given Linked List such
    #  that, all even numbers are placed after odd numbers. Respective order of
    #  elements should remain same.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if retain==0: 
        return None

    if delete==0: 
        return head 
        
    curr = head
    m    = 0
    n    = 0 
    deleteFlg  = False 
    while curr is not None: 
        if deleteFlg: 
            n = n + 1 
            if n <= delete:
                curr = curr.next 
            else: 
                n = 0 
                deleteFlg = False
                prev.next = curr
        else:
            m = m + 1 
            if m <= retain: 
                prev = curr 
                curr = curr.next
            else: 
                prev.next = None
                m = 0
                deleteFlg = True                
        
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
m = int(input())
n = int(input())
l =  deleteList(l,m,n)
printll(l)
