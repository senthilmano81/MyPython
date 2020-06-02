    # -*- coding: utf-8 -*-
    """
    Created on Fri Sep  6 10:05:10 2019
    
    @author: GGR0
    """
    
    # Problem ID 331 even after odd in a LL
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def arrange_LinkedList(head):
        #  Even after Odd LinkedList: Arrange elements in a given Linked List such
        #  that, all even numbers are placed after odd numbers. Respective order of
        #  elements should remain same.
        #############################
        # PLEASE ADD YOUR CODE HERE #
        #############################
        if head is None: 
            return head 
        
        odd      = None 
        even     = None 
        evenhead = None 
        curr     = head 
        while curr is not None: 
            if curr.data % 2 == 1: 
                if odd is None: 
                    head = curr
                    odd      = curr
                else: 
                    odd.next = curr
                    odd      = curr
            else: 
                if even is None: 
                    evenhead = curr 
                    even      = curr
                else: 
                    even.next = curr
                    even      = curr            
            curr = curr.next 
        
        if odd is None: 
            head = evenhead
        else: 
            if evenhead is None: 
                odd.next  = None
            else: 
                odd.next  = evenhead
        
        if even is not None: 
            even.next = None
            
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
    l = arrange_LinkedList(l)
    printll(l)
