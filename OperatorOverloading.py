# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:18:20 2019

@author: GGR0
"""

class point: 
    def __init__(self,x,y): 
        self.__x = x
        self.__y = y
    def __str__(self):
        return "This point is at : "+ str(self.__x) + " , " + str(self.__y) 
    def __add__(self,point_object): 
        return point(self.__x + point_object.__x, self.__y + point_object.__y)
    def printV(self,obj): 
        print("object x: ", obj.__x)


class pen: 
    def printV(self,point_object): 
        print("pen object displaying point :", point_object.__x, point_object.__y)
   

    
p1 = point(1,3)
print(p1)

p2 = point(2,4)
print(p2)

p3 = p1 + p2
print(p3)