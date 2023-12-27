# 22<sup>nd</sup> Dec Lecture code

```
""""""
"""
class Sample:
    a = 10

    def m1(self):
        print('m1 process')


s = Sample()
print(s)
print(s.a)
s.m1()
---------------------------------
class Test:
    def __init__(self):
        print('Constructor method')



Test()
Test()
Test()
-------------------------
We can supply values to the constructor

class Test:
    def __init__(self,x,y,z):
        print('Constructor method')
        print(x+y,y*z)

Test(2,3,4)
-------------------------
self is a reference variable
it points to the members of a class

class Test:
    def __init__(self,num1):
        self.num1 = num1
        self.num1 = 'Pallavi'

    def show(self):
        print(self.num1)
    def final(self):
        self.show()
        self.show()
    
t = Test(100)
t.show()
t.final()
-------------------------------------
# Pillars of Object Oriented programming
- Inheritance: To build a Parent child relationship
between classes 
So one class can be a parent and other class can become a child
who can access members of Parent
-----------------------------
Simple Inheritance: one child -one parent
class RBI:# parent/base class
    currency = 'INR'
    def rules(self):
        print('RBI Rules and regulations')

class SBI(RBI): # child/derived
    def new_rules(self):
        print('New rules by SBI')

s = SBI()
print(s.currency)
s.rules()
s.new_rules()
-------------------------------
Multilevel inheritance:

class PM:
    def __init__(self,amt):
        print(amt)
    def funds(self):
        print('PM Care fund')

class CM(PM):
    def state_fund(self):
        print('CM funds')

    def funds(self):
        print('CM Care funds')
        # to access PM funds use super
        super().funds()
        super().__init__(600)

class MLA(CM):
    pass

m = MLA(45)
m.funds()
m.state_fund()

p = PM(70)

# Method overriding:
# When a child and Parent has a method with same name
# n inheritance is there so a method of child can override
# a method in parent
----------------------------------
class Grandfather:
    def m1(self):
        print('m1')
class Father(Grandfather):
    def m2(self):
        print('m2')

class Child(Father):
    def m3(self):
        #self.m1()
        #self.m2()

        #super().m1()
        #super().m2()

        Grandfather.m1(self)
        Father.m2(self)

c = Child()
c.m3()
-----------------------------------
Multiple inheritance:
More than one parent we have in child
---------------------------------
class Brother:
    pass
class Father:
    def car(self):
        print('Father car')
    def money(self):
        print('Father money')
class Mother():
    def money(self):
        print('Mother money')
        
class Child(Mother,Brother,Father):
    pass
c = Child()
c.money()
c.car()
print(Child.mro()) # Method Resolution order
-------------------------
Assignment: 
Solve 3-3 examples on Simple, Multilevel and multiple inheritance
Check Hierarchical and Hybrid Inheritance 
"""

```