# 21<sup>st</sup> Dec Lecture code

```
op_1.py
"""
class: it is a template,structure,blueprint, plan which we use
to create an object
ex. class "list"

class =  properties + behaviour

properties== variables
behaviours== action--> methods
Ex.

class RowHouse:

    # varibles
    room = 4
    size= 200
    p1 = 'parking'

    def construct(self): #self is a reference var
        print('Start construction')

    def footing(self):
        print('Start footing')
# object is an instance of a class
# When we create an object then memory gets allocated
# automatically
# because object gives an access to all the members of a class
# to create an object we need to call a class
r1 = RowHouse()
# r1 is an object
print(r1.p1,r1.room,r1.size)
r1.footing()
r1.construct()
--------------------------------------------
Q. How many objects we can create?
We can create N number of objects
-------------------------------------------
Constructor: Constructor allocates a memory
if i have a class Sample

Sample()--> Constructor

Constructor calls a default method which
def __init__():
    pass

------------------------
class Sample:
    def __init__(self):
        print('Constructor called')

# Class calling means constructor calling
Sample()
Sample()
------------------------
We can supply values to the constructor

class Sample:
    def __init__(self,x,y):
        print('Constructor called:',x,y)

# Class calling means constructor calling
Sample(10,20)
# Constructor can be empty or parameterized
-----------------------------------------
Can we have arguments for normal method
--> YES
----------------------------------
class Sample:
    def m1(self,a,b,c):
        print(a+b+c)

    def m2(self):
        print('Empty method')

    def m3(self):
        print('m3 method')

# init method gets called default when we call a constructor
# but m1 is a normal method
# hence we need an object to access it
s1 = Sample()
s1.m1(2,3,4)
#-----------------------------------
s2 = Sample()
s2.m3()
s2.m1(4,5,6)
---------------------------------------
IMP Q.
what is class
what is an object
what is constructor
what is def __init__(self):
wht is self
types of constructor
difference between function and method
difference between constructor and method
----------------------------------------
self: is a reference variable
it gives u an access to all the member of a class inside the method

self is an integral part of method only

class Bank:

    def __init__(self,balance):
        self.balance = balance
        # balance is local var.
        # self.balance is an instance var.

    # print balance in display method
    def display(self):
        print('Initial balance is:', self.balance)

b = Bank(4500)
b.display()
-------------------------------
class Sample:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def m1(self):
        print(self.name,self.age)

    def m2(self):
        # change values
        self.name = 'amol'
        self.age = 44
        print(self.name, self.age)
s = Sample('Shital',40)
s.m1()
s.m2()
# value of an instance var. changes from object to object method to method
# if required
-----------------------------------------------
# a Default method is an instance method
# means we can call instance the method in any other method

class Sample:
    def m1(self):
        print('m1 called')
    # call m1 in m2
    def m2(self):
        self.m1()
        print('m2 called')

s = Sample()
s.m2()
-----------------------------------
# nested classes
class Sample1:

    def m1(self):
        print('Sample1 m1')
    class Sample2:
        def m2(self):
            print('Sample2 m2')


s = Sample1()
s.m1()

s2 = s.Sample2()
s2.m2()
--------------------------------------
Assignment:
Create a class for Car
add some variables and methods

Create a class and call init method

Create a class Math_Calc with 3 methods
add(x,y)
sub(x,y)
multi(x,y)
and perform operations

Create a method with return statement

"""
```