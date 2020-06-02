# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:11:57 2019

@author: GGR0
"""

class Node: 
    def __init__(self,data): 
        self.data = data
        self.next = None
        
def printLL(head): 
    curr = head 
    while curr is not None: 
        print(str(curr.data) + '-->',end=' ')
        curr = curr.next    
    print('None')
    
def takeInput(): 
    li = [int(x) for x in input().split()]
    head = None 
    for ele in li:
        if ele == -1: 
            break 
        newNode = Node(ele)        
        if head is None: 
            head = newNode 
        else: 
            prevNode.next = newNode 
        prevNode = newNode 
    return head 

head = takeInput()
printLL(head)
