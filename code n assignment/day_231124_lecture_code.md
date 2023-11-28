# 24<sup>th</sup> Nov 2023

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List methods
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a = [1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> a.clear() # removes all items from the list
>>> #----------------------------
>>> help(list.copy)
Help on method_descriptor:

copy(self, /)
    Return a shallow copy of the list.

>>> # Shallow copy- means we copy the elements bt address of new object will be diferent
>>> x = [1,2,3]
>>> x
[1, 2, 3]
>>> id(x)
2707074138568
>>> # create y using copy() method
>>> y = x.copy()
>>> y
[1, 2, 3]
>>> id(y)
2707073972040
>>> # Shallow copy means same contents with different address
>>> # Against this we have Deep copy
>>> # it means Copy the contents bt address remains same
>>> # we have multiple reference to the same object
>>> x
[1, 2, 3]
>>> y
[1, 2, 3]
>>> # we have created y using shallow copy
>>> # lets create z using deep copy
>>> z = y
>>> z
[1, 2, 3]
>>> # check id of y and z
>>> id(y)
2707073972040
>>> id(z)
2707073972040
>>> # As we have same address for y and z
>>> # changes in any of th list will persist in both y and z
>>> y.append(100)
>>> y
[1, 2, 3, 100]
>>> z
[1, 2, 3, 100]
>>> # now check x
>>> x
[1, 2, 3]
>>> #---------------------------------------
>>> id(x)
2707074138568
>>> id(y)
2707073972040
>>> id(z)
2707073972040
>>> #----------------------------------------
>>> # Q. Shallow vs deep copy??
>>> #----------------------------------------
>>> help(list.count)
Help on method_descriptor:

count(self, value, /)
    Return number of occurrences of value.

>>> g = [1,2,1,1,1,1,]
>>> g.count(1)
5
>>> g.count('u') # nt present
0
>>> #---------------------------------
>>> help(list.index)
Help on method_descriptor:

index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    
    Raises ValueError if the value is not present.

>>> g
[1, 2, 1, 1, 1, 1]
>>> g.index(1)
0
>>> # returns lowest index of first occurance
>>> g.index(2)
1
>>> g.index(20)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    g.index(20)
ValueError: 20 is not in list
>>> #-----------------------------
>>> help(list.reverse)
Help on method_descriptor:

reverse(self, /)
    Reverse *IN PLACE*.

>>> # inplace means permanent operation
>>> y
[1, 2, 3, 100]
>>> y.reverse()
>>> y
[100, 3, 2, 1]
>>> # Q. y[::-1] and y.reverse()
>>> #--------------------------------
>>> help(list.sort)
Help on method_descriptor:

sort(self, /, *, key=None, reverse=False)
    Stable sort *IN PLACE*.

>>> y
[100, 3, 2, 1]
>>> t = [199,0,4,77,8,9,10,5,44]
>>> t
[199, 0, 4, 77, 8, 9, 10, 5, 44]
>>> t.sort()
>>> t
[0, 4, 5, 8, 9, 10, 44, 77, 199]
>>> # default it sorts in ascending order
>>> t.sort(reverse=True) # in descending order
>>> t
[199, 77, 44, 10, 9, 8, 5, 4, 0]
>>> # sort(key,reverse)
>>> d = ['nikhil','amy','manohar','sham','boby']
>>> d
['nikhil', 'amy', 'manohar', 'sham', 'boby']
>>> # it follows alphabatic order
>>> # a-z
>>> d.sort()
>>> d
['amy', 'boby', 'manohar', 'nikhil', 'sham']
>>> # z-a
>>> d.sort(reverse=True)
>>> d
['sham', 'nikhil', 'manohar', 'boby', 'amy']
>>> #----------------
>>> # lets work on keys
>>> d
['sham', 'nikhil', 'manohar', 'boby', 'amy']
>>> # on the basis of len if we want to sort then use len function
>>> # here constraint is len nt a-z
>>> d
['sham', 'nikhil', 'manohar', 'boby', 'amy']
>>> d.sort(key=len) #low-high
>>> d
['amy', 'sham', 'boby', 'nikhil', 'manohar']
>>> d.sort(key=len,reverse=True) #high to low
>>> d
['manohar', 'nikhil', 'sham', 'boby', 'amy']
>>> # ------------------
>>> # while using sort() list must be homo.
>>> #-------------------------------------------
>>> #======================================
>>> # Tuple
>>> # syntax: ()
>>> ()
()
>>> e1 = ()
>>> e1
()
>>> e2 = tuple()
>>> e2
()
>>> # Tuple has same features as that of list
>>> # Only ine difference
>>> # *one
>>> # Tuple is Immutable
>>> # List is Mutable
>>> r1 = [10,20,30]
>>> # lets change 20--> 200
>>> r1[1] = 200
>>> r1
[10, 200, 30]
>>> # lets add element
>>> r1.append(-1)
>>> r1
[10, 200, 30, -1]
>>> # now create a tuple
>>> r2 = (10,20,30)
>>> r2
(10, 20, 30)
>>> # try to change 30--> kiran
>>> r2[-1] = 'kiran'
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    r2[-1] = 'kiran'
TypeError: 'tuple' object does not support item assignment
>>> # try to append
>>> r2.append(900)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    r2.append(900)
AttributeError: 'tuple' object has no attribute 'append'
>>> # We can create a tuple only ones, No modifications allowed further
>>> # lets check methods present in tuple
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> # Q. List vs tuple
>>> # Q. Why tuple is immutable
>>> # Q. Which one is faster
>>> # Q. Which one is better
>>> #----------------------------------------
>>> # Packing and Unpacking of tuple
>>> 'sham','ram','amol'
('sham', 'ram', 'amol')
>>> v = 'sham','ram','amol' # wrapping--> packing
>>> v
('sham', 'ram', 'amol')
>>> n1,n2,n3 = 100,200,300 # separation is unpacking
>>> n1
100
>>> n2
200
>>> n3
300
>>> #--------------------
>>> v
('sham', 'ram', 'amol')
>>> x,y,z = v # unpacking
>>> x
'sham'
>>> y
'ram'
>>> z
'amol'
>>> x,y = v
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    x,y = v
ValueError: too many values to unpack (expected 2)
>>> x,y = v[:-1]
>>> x
'sham'
>>> y
'ram'
>>> 
```