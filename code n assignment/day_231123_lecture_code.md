# 23<sup>rd</sup> Nov Lecture code

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Data Structure in Python
>>> # List
>>> # syntax: []
>>> []
[]
>>> a = []
>>> a
[]
>>> type(a)
<class 'list'>
>>> b = list()
>>> b
[]
>>> #-------------------------
>>> # Features of list
>>> # Background data structure is an array
>>> d = [10,20,30,40,50]
>>> d
[10, 20, 30, 40, 50]
>>> # Indexing supported
>>> d[0]
10
>>> d[2]
30
>>> # +ve and -ve both indexing forms present
>>> d[-1]
50
>>> d[-3]
30
>>> #--------------------
>>> # slicing
>>> d
[10, 20, 30, 40, 50]
>>> d[0:2]
[10, 20]
>>> d[-2:]
[40, 50]
>>> d[::-1]
[50, 40, 30, 20, 10]
>>> # Q. indexing vs slicing?
>>> #-------------------------------
>>> # Duplicates are allowed
>>> p = [1,2,3,1,2,3,1,2,3]
>>> p
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> # We can create homo./hetro list
>>> # p is homo. list with int data type
>>> q = [10,2.4,4+5j,'python']
>>> q
[10, 2.4, (4+5j), 'python']
>>> # q is hetro. list
>>> #--------------------------------
>>> # It preserves sequence order
>>> # the way we give a data in the same order it get displayed
>>> #--------------------------------
>>> # List is Mutable in nature
>>> # Mutable means we can modify original list directly
>>> d
[10, 20, 30, 40, 50]
>>> # lets change 50 --> 500
>>> # check address before change
>>> id(d)
2711105577288
>>> d[-1]
50
>>> d[-1] = 500
>>> d
[10, 20, 30, 40, 500]
>>> id(d)
2711105577288
>>> # changes persist in the same object
>>> d
[10, 20, 30, 40, 500]
>>> # ashish wants to add name in the list
>>> d.append('ashish')
>>> d
[10, 20, 30, 40, 500, 'ashish']
>>> # add INDIA at 20
>>> d[1] = 'INDIA'
>>> d
[10, 'INDIA', 30, 40, 500, 'ashish']
>>> id(d)
2711105577288
>>> # Check all the methods present in  the list
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # String is not Mutable/Immutable
>>> s = 'venkatesh'
>>> s
'venkatesh'
>>> s.upper()
'VENKATESH'
>>> # bt ur original s is unchanged
>>> s
'venkatesh'
>>> s.capitalize()
'Venkatesh'
>>> s
'venkatesh'
>>> # to see updates we need to use extra variable
>>> s
'venkatesh'
>>> id(s)
2711100725872
>>> s = s.upper()
>>> s
'VENKATESH'
>>> id(s)
2711100726064
>>> # we can replace char/items from a string using indexing/slicing
>>> s
'VENKATESH'
>>> s[0]
'V'
>>> s[0] = 'vv'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s[0] = 'vv'
TypeError: 'str' object does not support item assignment
>>> # list vs str
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> #-------------------------------
>>> # lets start with methods
>>> e = []
>>> e
[]
>>> e.append(100)
>>> e
[100]
>>> e.append('python')
>>> e
[100, 'python']
>>> # extend()
>>> # when we want to add more elements as a separate enetity
>>> e.extend(['A','B'])
>>> e
[100, 'python', 'A', 'B']
>>> # append vs extend
>>> e.append(['A','B'])
>>> e
[100, 'python', 'A', 'B', ['A', 'B']]
>>> help(list.append)
Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.

>>> help(list.extend)
Help on method_descriptor:

extend(self, iterable, /)
    Extend list by appending elements from the iterable.

>>> e
[100, 'python', 'A', 'B', ['A', 'B']]
>>> e.append(100)
>>> e
[100, 'python', 'A', 'B', ['A', 'B'], 100]
>>> e.extend(100)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    e.extend(100)
TypeError: 'int' object is not iterable
>>> e.extend('100')
>>> e
[100, 'python', 'A', 'B', ['A', 'B'], 100, '1', '0', '0']
>>> [100, 'python', 'A', 'B', ['A', 'B'], 100, '1', '0', '0']
[100, 'python', 'A', 'B', ['A', 'B'], 100, '1', '0', '0']
>>> # VVVIMP: append vs extend
>>> # append adds object
>>> # extend adds an iterable
>>> # Assignment
>>> #----------------------------------
>>> e
[100, 'python', 'A', 'B', ['A', 'B'], 100, '1', '0', '0']
>>> # How to remove elements
>>> # we have 2 methods
>>> # pop() and remove()
>>> help(list.pop)
Help on method_descriptor:

pop(self, index=-1, /)
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> e
[100, 'python', 'A', 'B', ['A', 'B'], 100, '1', '0', '0']
>>> e.pop()
'0'
>>> e
[100, 'python', 'A', 'B', ['A', 'B'], 100, '1', '0']
>>> e.pop()
'0'
>>> e
[100, 'python', 'A', 'B', ['A', 'B'], 100, '1']
>>> # default it remove last element bt if we want to remove element present at spcific index
>>> # then supply that index in pop
>>> e.pop(1)
'python'
>>> e
[100, 'A', 'B', ['A', 'B'], 100, '1']
>>> e.pop(100) #index is out of range
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    e.pop(100) #index is out of range
IndexError: pop index out of range
>>> e.pop(-3)
['A', 'B']
>>> e
[100, 'A', 'B', 100, '1']
>>> # remove()
>>> help(list.remove)
Help on method_descriptor:

remove(self, value, /)
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> e
[100, 'A', 'B', 100, '1']
>>> e.remove(100)
>>> e
['A', 'B', 100, '1']
>>> e.remove('java')
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    e.remove('java')
ValueError: list.remove(x): x not in list
>>> #----------------------------------
>>> # insert()
>>> help(list.insert)
Help on method_descriptor:

insert(self, index, object, /)
    Insert object before index.

>>> e
['A', 'B', 100, '1']
>>> e.insert(2,'C')
>>> e
['A', 'B', 'C', 100, '1']
>>> e.insert(-2,'D')
>>> e
['A', 'B', 'C', 'D', 100, '1']
>>> # Assignment:
>>> # 1. Add 30 before A
>>> # 2. Add 450 between C & D
>>> # 3. Add 'C++' after 1
>>> # 4. Remove 100
>>> # 5. Remove '1'
>>> 
```