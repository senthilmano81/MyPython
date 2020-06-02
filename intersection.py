# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 05:18:32 2019

@author: GGR0
"""
def intersection(arr1,arr2): 
    if len(arr1) < len(arr2):
        mergeSort(arr1)
        prevele = ''
        idx = 0 
        for ele in arr2: 
            if ele == prevele: 
                if idx > -1: 
                    idx = binarySearch(arr1,ele,idx+1)
            else:
                idx = binarySearch(arr1,ele)
            prevele = ele 
            if idx > -1: 
                print(ele)
    else: 
        mergeSort(arr2)
        prevele = ''
        for ele in arr1: 
            if ele == prevele: 
                if idx > -1: 
                    idx = binarySearch(arr2,ele,idx+1)
            else:
                idx = binarySearch(arr2,ele)
            prevele = ele 
            if idx > -1: 
                print(ele)
            
def binarySearch(arr,x,si=0,ei='n'):
    if ei == 'n': 
        ei = len(arr) - 1 
    if si > ei:  
        return -1
    elif si == ei: 
        if arr[si] == x: 
            return si 
        else: 
            return -1
    else: 
        mi = (si+ei) // 2 
        if arr[mi] == x: 
            return mi 
        else: 
            if arr[mi] < x: 
                return binarySearch(arr,x,mi+1,ei)
            else:
                return binarySearch(arr,x,si,mi-1)
                
def intersection1(arr1, arr2):
    # Please add your code here
    mergeSort(arr1)
    mergeSort(arr2)
    i = 0 
    j = 0 
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] == arr2[j]:             
            print(arr1[i])
            j = j + 1
            i = i + 1
        elif arr1[i] < arr2[j]: 
            i = i + 1
        else: 
            j = j + 1

def mergeSort(arr): 
    if len(arr) == 0 or len(arr) == 1: 
        pass 
    else: 
        mid = len(arr) // 2 
        arra = arr[:mid]
        arrb = arr[mid:]
        mergeSort(arra)
        mergeSort(arrb)
        merge(arra,arrb,arr)

def merge(arra, arrb, arr): 
    i = 0 
    j = 0 
    k = 0 
    while i < len(arra) and j < len(arrb): 
        if arra[i] <= arrb[j]:
            arr[k] = arra[i]
            k = k + 1
            i = i + 1 
        else: 
            arr[k] = arrb[j]
            k = k + 1
            j = j + 1
    while i < len(arra): 
        arr[k] = arra[i]
        k = k + 1
        i = i + 1 
    while j < len(arrb): 
        arr[k] = arrb[j]
        k = k + 1
        j = j + 1            
        
# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection1(arr1, arr2) 
intersection(arr1, arr2)