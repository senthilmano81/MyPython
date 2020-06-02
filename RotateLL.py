# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:16:56 2019

@author: GGR0
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n):
    #  Given a linked list and an integer n, append the last n elements of the LL
    #  to front. 
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None: 
        return head 
    
    i = length(head) - n 
    
    tail  = None  
    curr  = head 
    count = 0 
    while curr is not None:        
        count = count + 1
        if count == i: 
            newtail = curr 
        if curr.next is None: 
            tail = curr 
        curr = curr.next 
    
    if i > 0: 
        tail.next    = head 
        head = newtail.next 
        newtail.next = None
        
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

def length(head): 
    count = 0 
    while head is not None: 
        count = count + 1 
        head = head.next 
    return count 

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr)
i=int(input())
l = append_LinkedList(l, i)
printll(l)
