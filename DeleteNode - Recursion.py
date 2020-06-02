# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:04:28 2019

@author: GGR0
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i,n=0):
    #  a linked list and a position i, delete the node of ith position from
    # Linked List recursively. If position i is greater than length of LL,
    # then:
    # you should return the same LL without any change.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    print(head.data,',',i,n)       
    if n == i and n==0: 
        return head.next 
    
    if n==i: 
        b = head.next 
        if b is None: 
            head.next = None
        else: 
            head.next = b.next 
    else: 
        head.next = deleteRec(head.next,i,n+1)    
        
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
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = deleteRec(l, i)
printll(l)
