# 20<sup>th</sup> Nov Lecture code

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Data Types in Python
>>> # 14 data types
>>> # Numeric Data: int, float, complex
>>> a = 5
>>> a
5
>>> type(a)
<class 'int'>
>>> # Python is Dynamically typed laguage
>>> # int a = 2 #static typing
>>> # runtime python interpreter will identify type of data
>>> b = 6.7
>>> b
6.7
>>> type(b)
<class 'float'>
>>> # complex: real+img
>>> c = 4+2j
>>> c
(4+2j)
>>> type(c)
<class 'complex'>
>>> #------------------------------------
>>> # Boolean Data type: True, False
>>> # These are conditional outptuts
>>> # when we are comparing the objects then we ge the result in boolean form
>>> 3 == 4
False
>>> #---------------------------------
>>> # String data type
>>> # syntax: '' or ""
>>> ''
''
>>> ""
''
>>> type('') # empty string
<class 'str'>
>>> type("")
<class 'str'>
>>> # String is a global acceptor
>>> # it accepts all types of data
>>> s = '123ABC_+%#^$   '
>>> s
'123ABC_+%#^$   '
>>> 'Shoaib'+'Pune'
'ShoaibPune'
>>> # does concate operation
>>> #--------------------------
>>> # List
>>> # syntax: []
>>> []
[]
>>> # empty list
>>> type([])
<class 'list'>
>>> r = [10,20,30]
>>> r
[10, 20, 30]
>>> t = ['A','B','C']
>>> t
['A', 'B', 'C']
>>> g = [12,33.33,4+5j,True,'Python']
>>> g
[12, 33.33, (4+5j), True, 'Python']
>>> type(r)
<class 'list'>
>>> type(g)
<class 'list'>
>>> #-----------------------------
>>> # Tuple
>>> # Syntax: ()
>>> u = (2,3,4)
>>> u
(2, 3, 4)
>>> type(u)
<class 'tuple'>
>>> # coma separated values in python are tuple
>>> 'python','java','JS'
('python', 'java', 'JS')
>>> 3,4,5
(3, 4, 5)
>>> #--------------------------
>>> # Set
>>> # syntax: {10,}
>>> # {} this is not a set , its dictionary
>>> a = {22,30}
>>> a
{22, 30}
>>> type(a)
<class 'set'>
>>> d = {1,'2',True,[2,2,3],(8,9)}
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d = {1,'2',True,[2,2,3],(8,9)}
TypeError: unhashable type: 'list'
>>> d = {1,'2',True,(8,9)}
>>> d
{(8, 9), 1, '2'}
>>> {1,1,2,3,4,1,1,1,1,1}
{1, 2, 3, 4}
>>> # duplicates not allowed in set
>>> # Sequence order nt preserved
>>> {987,23,0,'A',0,2,6,'py'}
{0, 2, 987, 6, 'py', 23, 'A'}
>>> # empty curly bracket{} is dict
>>> {}
{}
>>> type({})
<class 'dict'>
>>> #----------------------------------
>>> # dict
>>> # dict contain key:value  pair
>>> # {key:value}
>>> d = {1:100,2:200,3:300}
>>> d
{1: 100, 2: 200, 3: 300}
>>> # keys: 1,2,3
>>> # values:100,200,300
>>> f = {'name':'prakash',101:'rm number'}
>>> f
{'name': 'prakash', 101: 'rm number'}
>>> f = {'name':'prakash',10.1:'rm number'}
>>> f
{'name': 'prakash', 10.1: 'rm number'}
>>> #-----------------------------
>>> # frozenset()
>>> # range()
>>> #---------------------------------
>>> 'virat'.upper()
'VIRAT'
>>> 'virat123'.upper()
'VIRAT123'
>>> #---------------------------
>>> # int,float,comple
>>> # complex
>>> # Boolean
>>> # String
>>> # List
>>> # Tuple
>>> # Set
>>> # Dict
>>> # frozenset
>>> # range
>>> # bytes,bytearray,None
```