# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 05:41:24 2019

@author: GGR0
"""

def binarySearch(arr,x,si=0,ei='n'):
    if ei == 'n': 
        ei = len(arr) - 1 
    if si > ei:  
        return False
    elif si == ei: 
        return arr[si] == x 
    else: 
        mi = (si+ei) // 2 
        if arr[mi] == x: 
            return True
        else: 
            if arr[mi] < x: 
                print('binarysearch('+ str(mi+1) + ',' + str(ei) +')')
                return binarySearch(arr,x,mi+1,ei)
            else:
                print('binarysearch('+ str(si) + ',' + str(mi-1) +')')
                return binarySearch(arr,x,si,mi-1)
                
arr = [1, 2, 3, 4, 5, 7, 9, 10]
print(binarySearch(arr,6)) 
    
if binarySearch(arr,7): 
    print('true')
else: 
    print('false')