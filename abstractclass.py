# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:06:52 2019

@author: GGR0
"""

from abc import ABC,abstractmethod

class automobile(ABC):
    def __init__(self,name): 
        print('automobile created')
    
    @abstractmethod
    def start(self): 
        print('start of automobile') 
    
    @abstractmethod
    def stop(self): 
        pass
    
    @abstractmethod
    def drive(self): 
        pass 

class car(automobile): 
    def __init__(self,name): 
        print("car created")
        self.name = name 
    def start(self): 
        super().start()
        print('start of car called')
    
    def stop(self): 
        pass
    
    def drive(self): 
        pass 

class bus(automobile): 
    def start(self): 
        pass     
    
    def stop(self): 
        pass
    
    def drive(self): 
        pass 

c1 = car('Honda')
c1.start()
b1 = bus('BMTC')