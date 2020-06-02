# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 08:28:07 2019

@author: GGR0
"""

class vehicle: 
    def __init__(self,color="blue",maxSpeed=120): 
        self.color = color
        self.__maxSpeed = maxSpeed
        
    def getmaxSpeed(self): 
        return self.__maxSpeed
    
    def setmaxSpeed(self, maxSpeed):
        self.__maxSpeed = maxSpeed
    
    def print_details(self): 
        print('color in vehicle : ',self.color)
        print('maxSpeed in Vehicle : ', self.__maxSpeed)

class Car(vehicle): 
    def __init__(self,color,maxSpeed,gears,isConvertible): 
        #super().__init__(color,maxSpeed)
        super().__init__(color,maxSpeed)
        self.__gears = gears
        self.__isConvertible = isConvertible
        
    def print_details(self): 
        super().printV()
        self.printV()
        print('Number of Gears : ', self.__gears)
        print('Is Convertible  : ', self.__isConvertible)
        
c = Car("red",150,5,'yes')
c.print_details()
print('****************************************')
c.printV()

