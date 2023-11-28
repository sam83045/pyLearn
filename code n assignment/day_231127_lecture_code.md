# 27<sup>th</sup> Nov 2023

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Set
>>> # syntax: set()
>>> d = set()
>>> d
set()
>>> # if we use empty {} then its dictionary
>>> s = {}
>>> s
{}
>>> type(s)
<class 'dict'>
>>> a = {10,20,30,40}
>>> a
{40, 10, 20, 30}
>>> type(a)
<class 'set'>
>>> # Features of set
>>> # - Background data structure is Hash table
>>> # - set wont preserve sequence order
>>> # - duplicates are not allowed
>>> {1,2,3,1,2,3,1,2,3}
{1, 2, 3}
>>> {'A','B',1,2,1,2,'B'}
{1, 2, 'B', 'A'}
>>> # - Homo./Hetro data allowed
>>> # - No indexing No slicing as No array
>>> a
{40, 10, 20, 30}
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a[0]
TypeError: 'set' object does not support indexing
>>> a[::-1]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[::-1]
TypeError: 'set' object is not subscriptable
>>> #-------------------------------
>>> # Set is Mutable in nature
>>> a
{40, 10, 20, 30}
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a
{40, 10, 20, 30}
>>> id(a)
2035683698952
>>> # add element
>>> a.add(100)
>>> a
{100, 40, 10, 20, 30}
>>> help(a.pop)
Help on built-in function pop:

pop(...) method of builtins.set instance
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> a.pop()
100
>>> a
{40, 10, 20, 30}
>>> # check id now after changing the things
>>> id(a)
2035683698952
>>> # as changes get performed in the same object in same id
>>> # hence Set is Mutable in nature
>>> #---------------------------------------------
>>> # Methods of Set
>>> # Additing content/object
>>> # add() update()
>>> # add is used to add one object at a time
>>> a
{40, 10, 20, 30}
>>> a.add('java')
>>> a
{'java', 40, 10, 20, 30}
>>> a.add('java','.net')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.add('java','.net')
TypeError: add() takes exactly one argument (2 given)
>>> a.add(('java','.net'))
>>> a
{'java', 40, 10, ('java', '.net'), 20, 30}
>>> a.add([230,450])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.add([230,450])
TypeError: unhashable type: 'list'
>>> a.add(tuple([230,450]))
>>> a
{'java', 40, 10, ('java', '.net'), (230, 450), 20, 30}
>>> # using update we can add n number of objects
>>> b = set()
>>> b
set()
>>> b.update({20,30,40,50})
>>> b
{40, 50, 20, 30}
>>> b.update([1,2,3])
>>> b
{1, 2, 3, 40, 50, 20, 30}
>>> # Update adds elements from an iterable/collection
>>> # union()
>>> # Combine 2 sets
>>> s1 = {1,2,3}
>>> s1
{1, 2, 3}
>>> s2 = {2,3,4}
>>> s2
{2, 3, 4}
>>> s1.union(s2)
{1, 2, 3, 4}
>>> # intersection()
>>> # Common elements between 2 sets
>>> s1.intersection(s2)
{2, 3}
>>> # difference()
>>> # Uncommon elements from set 1
>>> s1.difference(s2)
{1}
>>> s2.difference(s1)
{4}
>>> # symmetric_difference()
>>> # Uncommon elements from set1 and set2
>>> s1.symmetric_difference(s2)
{1, 4}
>>> # all above operations are temp.
>>> s1
{1, 2, 3}
>>> s2
{2, 3, 4}
>>> s1.symmetric_difference(s2)
{1, 4}
>>> s1.symmetric_difference_update(s2)
>>> s1
{1, 4}
>>> # Assignment: difference_update(),intersection_update()
>>> #---------------------------------------------
>>> # Removal of an elements from set
>>> a
{'java', 40, 10, ('java', '.net'), (230, 450), 20, 30}
>>> # pop(), remove(), discard()
>>> help(set.pop)
Help on method_descriptor:

pop(...)
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> a
{'java', 40, 10, ('java', '.net'), (230, 450), 20, 30}
>>> a.pop()
40
>>> help(set.remove)
Help on method_descriptor:

remove(...)
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.

>>> a
{'java', 10, ('java', '.net'), (230, 450), 20, 30}
>>> a.remove('java')
>>> a
{10, ('java', '.net'), (230, 450), 20, 30}
>>> a.remove('java')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.remove('java')
KeyError: 'java'
>>> help(set.discard)
Help on method_descriptor:

discard(...)
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.

>>> a
{10, ('java', '.net'), (230, 450), 20, 30}
>>> a.discard(20)
>>> a
{10, ('java', '.net'), (230, 450), 30}
>>> a.discard(2000)
>>> a
{10, ('java', '.net'), (230, 450), 30}
>>> #---------------------------------------
>>> s1
{1, 4}
>>> s2 = {1,2,3,4}
>>> s2
{1, 2, 3, 4}
>>> s1.issubset(s2) # return boolean output
True
>>> s1.issubset({100,200,300})
False
>>> # Assignment: issuperset, isdisjoint
>>> #------------------------------------------
>>> 
```
