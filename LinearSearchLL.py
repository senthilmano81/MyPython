# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:13:19 2019

@author: GGR0
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linearSearch(head, n):
    #  Given a linked list and an integer n you need to find and return index
    #  where n is present in the LL. Do this iteratively. Return -1 if n is not
    #  present in the LL. Indexing of nodes starts from 0. 
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    count = 0
    while head is not None: 
        if head.data == n: 
            return count 
        head = head.next 
        count = count + 1
    return -1 

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
l = ll(arr[:-1])
data=int(input())
index = linearSearch(l, data)
print(index)
