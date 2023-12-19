# 05<sup>th</sup> Dec Lecture code

```
""""""
"""
Lambda Function

syntax: lambda var/s:expression
It has default return

op = lambda  num:num*20
print(op(7))

print(op)
-----------------------
# check number is +ve or -ve
# using ternary operator
# It is condition based operator
#Syntax: return Yes if condition else No
check = lambda num: 'Positive' if num>0 else 'Negative'
print(check(8))
---------------------------
h = [23,45,36,21,34]
# add 100 in each number
def add(n):
    return n + 100

print(list(map(add,h)))

print(list(map(lambda n:n+100,h)))
--------------------
m = lambda m,n:(m.upper(),n+5)
print(m('ashish',33))
------------------
Higher order function:
- map: it takes function and apply over each element
Ex.

# map(func,iterable)
num = [3,4,5,6,7,8]
print(list(map(lambda n:(n**3,n+10),num)))
-----------------------------------------
- filter: it works on condition, wherever condition is True those values will get returned
Ex.
num = [-10,20,30,-22,3,-44]
print(list(filter(lambda n:n<0,num)))

Ex.2

names = ['ramesh','amit','dinesh','alok','swati']
# select names ending with sh
print(tuple(filter(lambda nm:nm.endswith('sh'),names)))

-----------------------------------------------
- reduce: not direct builtin
it is present in another module(file)
we have to import reduce from functools module

- it is used to reduce a sequence into a single number

syntax: reduce(function,sequence) 
-----------------
from functools import reduce

num = [20,90,33,78,45,98,100]
print(reduce(lambda x,y:x+y,num))
---------------------------------------
# Function aliasing: giving a nick name or an alias to the function

def bank_info_data(bname,ifsc,pincode):
    return bname,ifsc,pincode

bi = bank_info_data
# bi is a new ref name/an alias
print(bi('SBI',3454,4565767))
--------------------------------
Nested functions:
function inside function
--------------------------------
def outer():
    print('Outer function')
    def inner():
        print('Inner function')
    inner()
outer()
outer()
# Assignment: I want to call inner function from outside
------------------------------------
# Function recursion:
# Recursive functions: a function calls it again and again

def sample():
    sample()

sample()
# in above case will get RecurssionError
# bcz there is limit of calling function
# when it get exceed , control will throw an error 
-------------------------------
# factorial of number
# 4! = 4*3*2*1
# num-1
# 4*fact(4-1)*fact(3-1)..*fact(1)
# 0! or 1! = 1

def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(10))
"""
```