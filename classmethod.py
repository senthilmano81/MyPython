# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:13:30 2019

@author: GGR0
"""
from datetime import date

class  Person: 
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    @classmethod
    def createPerson(cls,name,birthyear): 
        return cls(name,date.today().year - birthyear)
    
    @staticmethod
    def calcAge(birthyear): 
        age = date.today().year - birthyear
        return age
    
    def printV(self): 
        print("today's date is :", date.today())
        print("name of the person is : ", self.__name)
        print("age of the person is : ", self.__age)
    

p1 = Person("senthil",37)
p1.printV()

p2 = Person.createPerson("Eswari",34)
p2.printV()

print(Person.calcAge(1981))