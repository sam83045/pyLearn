# 26<sup>th</sup> Dec Lecture code


```
""""""
"""
   P1
C1   C2
   P2
   
# Hybrid Inheritance
   P    Q
X    Y    Z
  A     B
     C
-------------------------
class P:
    pass
class Q:
    pass

class X(P):
    pass
class Y(P,Q):
    pass
class Z(Q):
    pass

class A(X,Y):
    pass
class B(Y,Z):
    pass

class C(A,B):
    pass

print(C.mro())
---------------------------------   
- Encapsulation: data hiding
Ex. class

class Sample:
    x = 10
    y = 20

print(x,y)

----------------
Like other programming languages we dont  have
access modifiers: public,private and protected
            public  private protected
        
class       Yes      Yes     Yes
outside     Yes      No      Yes
Subclass    Yes      No      Yes   
Package     Yes      No      Yes
   
So we can implement encapsulation using
_ underscore convention
--------------------
Case 1:

class Sample:
    x = 10
    y = 20
    z = 30
    
s =  Sample()
# we can access x,y,z using object bcz they are public
# so variables or methods declared by a user without underscore in prefix
# are public one
-------------------------------------
# for protected use single _
# for private use double __ underscore in prefix
class Sample:
    x = 10 #public var.
    _y = 20 #protected var.
    __z = 30 #private


s = Sample()
print(dir(s))
# access x,_y
print(s.x,s._y)
# access private __z: direct access usig object wont be possible
#print(s.__z)

# Name Mangling: make the private var/method accessible
print(s._Sample__z)
-------------------------------------
class Sample:
    def m1(self):
        print('Public Method')

    def _m2(self):
        print('Protected Method')

    def __m3(self):
        print('Private Method')

s = Sample()
s.m1()
s._m2()
#s.__m3()
s._Sample__m3()
----------------------------------
Can we modify public,protected and private values

class Sample:
    x = 10 #public var.
    _y = 20 #protected var.
    __z = 30 #private

    def m1(self):
        return  1


s = Sample()
s.x = 11
s._y = 21
s.m1()
s._Sample__z = 31
print(s.__dict__)
print(Sample.__dict__)
--------------------------------------
Polymorphism:
Poly(many) + morphs(forms)

One Norm has multiple forms called as Polymorphism

Operators are best examples of it

print(10+10) #addition
print('10'+'10') # concatenation

print(3*4) #multiply
print('3'*4) # repetition
-----------------------------
Types:
- Operator level Polymorphism
- Method level polymorphism
- Constructor level polymorphism

Method Overloading
when we have a method with same name and different arguments

def m1(int a, int b)
def m1(float a, float b)
def m1(int a)
m1(1.,2.)
--------------------------------
class Test:

    def show(self,name):
        pass

    def show(self, name,age):
        pass

    def show(self, name,age,salary):
        print(name,age,salary)

t = Test()
#t.show('Yogesh')
# it takes last recent.latest call of method
# we can only call 
t.show('Yogesh',22,45500)
--------------------------------------------------

"""
class Test:

    def show(self,*n):
        print(n)


t = Test()
#t.show('Yogesh')
# it takes last recent.latest call of method
# we can only call
t.show('Yogesh',22,45500)
t.show()
t.show('Amit',27)
```