# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:57:50 2019

@author: GGR0
"""
class Node: 
    def __init__(self,data): 
        self.data = data
        self.next = None

a = Node(13)
b = Node(15)
a.next = b 
print(a.data)
print(b.data)
print(a.next.data)
