# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:07:55 2019

@author: GGR0
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def check_palindrome(head) :
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None: 
        return True 
    head1, head2 = splitll(head)    
    chkflg       = True
    head2        = reversell(head2)
    while head1 is not None and head2 is not None: 
        if head1.data != head2.data: 
            chkflg = False
            break 
        head1  = head1.next
        head2  = head2.next 
    return chkflg    

def splitll(head): 
    len = length(head)
    if len == 1: 
        return head, head 
    i   = (len // 2) + (len%2) 
    head1 = head
    tail1 = None 
    head2 = None
    count = 0
    curr  = head
    while curr is not None:         
        count = count + 1 
        if count == i:
            tail1 = curr 
            head2 = curr.next 
        curr = curr.next    
    
    tail1.next = None 
    
    return head1, head2

def reversell(head): 
    if head is None or head.next is None: 
        return head
    newhead = reversell(head.next)
    tail = head.next 
    tail.next = head 
    head.next = None
    return newhead 

def reversell1(head,prev=None):
     if head.next is None: 
        if prev is not None: 
            # length of linked list is more than 1 
            head.next = prev 
            prev.next = None 
            tail      = prev  
            newhead   = head   
            return tail, newhead
        else: 
            # length of linked list is 1 
           return head
     else: 
        tail,newhead = reversell(head.next,head) 
        if tail != head:
            # Tail is already formed for last but one element 
            tail.next = head    
            tail      = head 
        if prev is None: 
             # recursion returned to first call 
             tail.next = None
             return newhead
        else:
            # return newly formed tail and newhead 
             return tail,newhead 
    
def length(head): 
    count = 0 
    while head is not None: 
        count = count + 1
        head = head.next
    return count 

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr)
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
