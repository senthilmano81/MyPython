# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:12:54 2019

@author: GGR0
"""

def FindUnique(arr):
    # Please add your code here
    mergeSort(arr)
    unique = arr[-1]
    for i in range(0,len(arr)-1,2): 
        if arr[i] != arr[i+1]: 
            unique = arr[i]
            break
    
    return unique 
    
def mergeSort(arr): 
    if len(arr) == 0 or len(arr) == 1: 
        pass 
    else: 
        mid = len(arr) // 2 
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        mergeSort(arr1)
        mergeSort(arr2)
        merge(arr1,arr2,arr)

def merge(arr1, arr2, arr): 
    i = 0 
    j = 0 
    k = 0 
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            k = k + 1
            i = i + 1 
        else: 
            arr[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < len(arr1): 
        arr[k] = arr1[i]
        k = k + 1
        i = i + 1 
    while j < len(arr2): 
        arr[k] = arr2[j]
        k = k + 1
        j = j + 1      
    
    
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
