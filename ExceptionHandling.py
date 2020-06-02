# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:35:07 2019

@author: GGR0
"""
class ZeroError(Exception): 
    pass 

while True: 
    try: 
        num = int(input('Enter the numerator: '))
        den = int(input('Enter the denominator: '))
        if num == 0: 
            raise ZeroError
        value = num / den       
    except ValueError: 
        print('numerator and denominator should be integers')
    except ZeroDivisionError: 
        print('denominator should not be zero')
    #except (ValueError, ZeroDivisionError):
        #5print('numerator & denominator should be integers and denominator should not be zero')
    except ZeroError: 
        print('numerator should be greater than Zero')
    except:
        print('something went wrong')
    else: 
        print(value)        
        print('Division is successful')
        break
    finally: 
        print('Iteration is completed')
