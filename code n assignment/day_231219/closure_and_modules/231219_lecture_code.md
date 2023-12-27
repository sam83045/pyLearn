# 19<sup>th</sup> Dec Lecture code


```
""""""
"""
Call inner function in outside/global scope 
------------
def outer():
    print('Outer Function')

    def inner():
        print('Inner Function')
    #inner()
    return inner

innr = outer()
print(innr)

innr()
innr()
---------------------
def outer():
    print('Outer Function')

    def inner():
        print('Inner Function')
    #inner()
    return inner

innr = outer() # returning inner ref
out = outer #function aliasing
------------------------
def RBI():
    print('RBI Operations')
    def SBI():
        print('SBI Operation')
    SBI()

RBI()
--------------------------
Case 2: return inner reference

def RBI():
    print('RBI Operations')
    def SBI():
        print('SBI Operation')
    return SBI

sb = RBI()
# sb IS A REF FOR SBI FUNCTION
sb()
sb()
sb()
-----------------------------
def University():
    print('University Rule')

    def College():
        print('College Rules')

    def dept():
        print('Dept Rules')

    return College,dept
c1,d1 = University()
c1()
d1()
d1()
------------------------------
Modules in Python:
A module is a file with .py extension
Module contains: variables, functions, classes, methods

Using modular programming one can access members of a module.file
into another file

we have to import the module whose members we want to access

import bank
print(bank.ifsc)
bank.credit()
------------------------------
In python we have 2 types of modules
- Built-in
- User defined modules
-------------------------------
Built-in modules: from Python environment

# math module
import math
print(math.pi)
print(math.factorial(4))
print(math.sin(60))

# using dot operator we are able to access 
# members of a module
------------------------------
Module aliasing: when file has big name or more number of chars
# then we go for short name as an alias

import math as m
print(m.e)
print(m.sqrt(625))
---------------------------------
# To use all options present in a module we can go with
from import option 

from math import *
# * means all
print(e,pi,tau)
print(factorial(7))
-------------------------------------
# Import specific things from module
# from module import member1,2,3...
from math import pi,sqrt
print(pi,sqrt(121))
-------------------------
How to check built-in modules
print(help('modules'))
-----------------------------
Revision:
import math
import math as m
from math import *
from math import pi,factorial
"""
```