# -*- coding: utf-8 -*- python
"""
Created on Wed Sep  4 09:28:48 2019

@author: GGR0
"""
class Node: 
    def __init__(self,data): 
        self.data = data
        self.next = None 


def createll(arr): 
    head = Node(arr[0])
    prev = head 
    for ele in arr[1:]: 
        curr = Node(ele)
        prev.next = curr 
        prev = curr 
    return head

def printll(head): 
    while head is not None: 
        print(str(head.data) + '-->',end='' )
        head = head.next
    print('None')
    
def reversell1(head): 
    if head is None or head.next is None: 
        tail    = head
        newhead = head 
        return tail, newhead 
    
    tail, newhead = reversell1(head.next)
    tail.next = head 
    tail      = head 
    head.next = None 
    return tail, newhead 
    
def reversell(head,prev=None): 
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
            tail.next = head    
            tail      = head 
        if prev is None: 
             # recursion returned to first call 
             tail.next = None
             return newhead
        else:
            # return newly formed tail and newhead 
             return tail,newhead 

arr = [int(x) for x in input().split()]
head = createll(arr)
printll(head)
head = reversell(head)
printll(head)
tail, head = reversell1(head)
printll(head)
tail, head = reversell1(head)
printll(head)

