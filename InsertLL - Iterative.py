# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:46:22 2019

@author: GGR0
"""

class Node: 
    def __init__(self,data): 
        self.data = data
        self.next = None
    
def createLL(arr): 
    head = None
    for ele in arr: 
        newNode = Node(ele)
        if head is None: 
            head = newNode
        else:
            prevNode.next = newNode
        prevNode = newNode 
    return head 

def insertLL(head,data,i): 
    count = 0 
    prev = None
    curr = head 
    while curr is not None and count < i: 
        prev = curr 
        curr = curr.next         
        count = count + 1 
    
    newNode = Node(data)
    if prev == None: 
        head = newNode 
    else: 
        prev.next = newNode 
    if curr is not None: 
        newNode.next = curr 
        
    return head 
    
def printLL(head): 
    while head is not None: 
        print(str(head.data) + '-->',end='')
        head  = head.next 
    print('None')
    return 

arr = [int(x) for x in input().split()]
head = createLL(arr)
printLL(head)
head = insertLL(head,4,2)
printLL(head)
head = insertLL(head,0,0)
printLL(head)

head = insertLL(head,12,8)
printLL(head)

head = insertLL(head,99,25)
printLL(head)