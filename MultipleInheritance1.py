# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:04:11 2019

@author: GGR0
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:43:28 2019

@author: GGR0
"""
class Mother:
    def __init__(self): 
        super().__init__()
    def print(self): 
        print('Print of Mother called')

class Father: 
    def __init__(self):
        self.native = 'Madurai'
    def print(self):
        print('Print of Father called')

class Child(Mother, Father): 
    def __init__(self,name):
        super().__init__()
        self.name = name 
    def printChild(self): 
        print('Child printing name : ',self.name)
        print('Child printing native : ', self.native)

c = Child('Senthil')
c.printChild()
c.print()
print(Child.mro())