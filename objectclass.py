# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:34:42 2019

@author: GGR0
"""

"""
 Three classes are provdied by Object namely __init__, __str__, __new__
"""
class Circle:
    def __init__(self,radius): 
        self.radius = radius
        
class Square: 
    def __init__(self,side): 
        self.side = side 
    def __str__(self): 
        return "This is a Square Class" 

c = Circle(4)
print(c)

s = Square(4)
print(s)