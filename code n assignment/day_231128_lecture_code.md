# 28<sup>th</sup> Nov 2023

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Dict: Dictionary
>>> # syntax: {}
>>> {}
{}
>>> type({})
<class 'dict'>
>>> # {key:value} pair
>>> {1:100}
{1: 100}
>>> #-----------------------------
>>> # Features
>>> # Background data structure is Hash table
>>> # Duplicate keys are not allowed
>>> {1:100,2:200,1:'python'}
{1: 'python', 2: 200}
>>> {'A':10,'A':20,'A':30}
{'A': 30}
>>> # it takes last recent pair in a sequenc
>>> # duplicate values are allowed
>>> {'A':20,'B':20,'C':20}
{'A': 20, 'B': 20, 'C': 20}
>>> # multiple values are also ok
>>> {'A':20,'B':20,'C':[20,40,50]}
{'A': 20, 'B': 20, 'C': [20, 40, 50]}
>>> # Sequence order gets preserved
>>> # Homo.Hetro. keys values are allowed
>>> # Mutable in nature
>>> #-------------------
>>> # mthods of dict
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d = {}
>>> d
{}
>>> help(dict.update)
Help on method_descriptor:

update(...)
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

>>> d
{}
>>> d.update({1:10,2:20,3:30})
>>> d
{1: 10, 2: 20, 3: 30}
>>> # we can also update already exist value
>>> # change 20
>>> d.update({2:'c++'})
>>> d
{1: 10, 2: 'c++', 3: 30}
>>> # We cant change key which is already available
>>> id(d)
1970816697616
>>> # lets change 10 to 100
>>> d.update({1:100})
>>> d
{1: 100, 2: 'c++', 3: 30}
>>> id(d)
1970816697616
>>> #----------------------
>>> help(dict.setdefault)
Help on method_descriptor:

setdefault(self, key, default=None, /)
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> d
{1: 100, 2: 'c++', 3: 30}
>>> d.setdefault(4)
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None}
>>> d.setdefault(2) # key 2 is already present
'c++'
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None}
>>> d.setdefault(5) # new pair of 5:None will get added
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None, 5: None}
>>> d.setdefault(1) # will return 100
100
>>> # instead of None if we want other value yes we can assign
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None, 5: None}
>>> d.setdefault('python',1989) # python is key and 1989 is value
1989
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None, 5: None, 'python': 1989}
>>> #--------------------------
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None, 5: None, 'python': 1989}
>>> # fetch all values
>>> d.values()
dict_values([100, 'c++', 30, None, None, 1989])
>>> # fetch all keys
>>> d.keys()
dict_keys([1, 2, 3, 4, 5, 'python'])
>>> # fetch [(key,value)]
>>> d.items()
dict_items([(1, 100), (2, 'c++'), (3, 30), (4, None), (5, None), ('python', 1989)])
>>> #--------------------------
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None, 5: None, 'python': 1989}
>>> # get(): to fetch value using key
>>> d.get(2)
'c++'
>>> # if key is present then return its value
>>> d.get('python')
1989
>>> # if key is not present retrun default= None--> Nothing
>>> None
>>> d.get('Kantara')
>>> # instead of None if we want to return the value
>>> d.get('Kantara',-1)
-1
>>> d.get('Animal','missing')
'missing'
>>> d
{1: 100, 2: 'c++', 3: 30, 4: None, 5: None, 'python': 1989}
>>> d.get(3,'missing')
30
>>> # delete key (means key:value)
>>> # pop()
>>> d.pop(2)
'c++'
>>> d
{1: 100, 3: 30, 4: None, 5: None, 'python': 1989}
>>> # if key is wrong
>>> d.pop('A')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    d.pop('A')
KeyError: 'A'
>>> # if we dont want any error if the key is nt present
>>> d.pop('A','NP')
'NP'
>>> # using del built in function
>>> del d[5]
>>> d
{1: 100, 3: 30, 4: None, 'python': 1989}
>>> # we dont have indexing support bt same context we can use
>>> # in which [key] key can be supplied to fetch values
>>> d[1]
100
>>> d['python']
1989
>>> # d[key] ==> value
>>> #-----------------
>>> # popitem()
>>> help(dict.popitem)
Help on method_descriptor:

popitem(...)
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.

>>> d
{1: 100, 3: 30, 4: None, 'python': 1989}
>>> d.popitem()
('python', 1989)
>>> d
{1: 100, 3: 30, 4: None}
>>> d.popitem()
(4, None)
>>> d
{1: 100, 3: 30}
>>> #-----------------------
>>> help(dict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> dict.fromkeys([10,20,30,40])
{10: None, 20: None, 30: None, 40: None}
>>> # instead on None we want some different value
>>> dict.fromkeys([10,20,30,40],-100)
{10: -100, 20: -100, 30: -100, 40: -100}
>>> dict.fromkeys([10,20,30,40],[1,2,3,4])
{10: [1, 2, 3, 4], 20: [1, 2, 3, 4], 30: [1, 2, 3, 4], 40: [1, 2, 3, 4]}
>>> #----------------------
>>> a1 = [10,20,30,40]
>>> a2 = [1,2,3,4]
>>> # Create a dict from a1 and a2
>>> # expected output is
>>> {10:1,20:2,30:3,40:4}
{10: 1, 20: 2, 30: 3, 40: 4}
>>> #---------------------------
>>> #===============================================
>>> # range(): used to create sequential numbers
>>> # range(N) --> start generating numbers from 0 and stop at N
>>> range(11)
range(0, 11)
>>> # start from 0 stop at 11
>>> # As range output is an object, in order to see actual value we need to typecast
>>> # typecast means conversion
>>> # if we want sequence in a list()
>>> list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> tuple(range(5))
(0, 1, 2, 3, 4)
>>> set(range(15))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
>>> #----------
>>> # range(star,stop)
>>> list(range(5,11))
[5, 6, 7, 8, 9, 10]
>>> list(range(101,111))
[101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
>>> #----------------
>>> # range(start,stop,step)
>>> # default step is 1
>>> list(range(101,111,1))
[101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
>>> list(range(1,20,1))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(1,21,1))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # odd numbers list 1-20
>>> list(range(1,21,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> # can we put -ve stepping --> YES
>>> list(range(1,21,-1))
[]
>>> list(range(20,0,-1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> # Assigments:
>>> # Generate 1-100 even numbers
>>> # -10 to +10
>>> # generate table of 5 -->5,10,15,.....
>>> #===============================================
```
