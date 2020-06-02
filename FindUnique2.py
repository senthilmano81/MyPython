# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:12:54 2019

@author: GGR0
"""

def FindUnique(arr):
    # Please add your code here
    unique = 0
    for ele in arr: 
        unique = unique^ele
    
    return unique 
    
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
