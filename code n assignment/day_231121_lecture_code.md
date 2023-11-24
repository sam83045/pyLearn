# 21<sup>st</sup> Nov lecture code

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Data Structures
>>> # String
>>> ''
''
>>> ""
''
>>> # Features of a String
>>> # It accepts all types of data
>>> # Sequence order gets preserved
>>> # Background data structure is an array
>>> s = 'viraj'
>>> s
'viraj'
>>> # Array has indexing
>>> # indexing is of 2 types
>>> # +ve indexing
>>> # -ve indexing
>>> #--------------
>>> # +ve index starts with 0 and stop at n-1
>>> s
'viraj'
>>> # n means len(str)
>>> len(s)
5
>>> # we can access single element using an index
>>> #s[index]
>>> s[0]
'v'
>>> s[2]
'r'
>>> s[4]
'j'
>>> #--------------
>>> # -ve indexing
>>> # it starts with -1 from extrem right side
>>> # and it stops at -n
>>> # IT traverse from right to left
>>> s
'viraj'
>>> s[-1]
'j'
>>> s[-3]
'r'
>>> s[-5]
'v'
>>> #--------------------------------
>>> s
'viraj'
>>> # to access multiple blocks we have slicing concepy
>>> # s[star_index:stop_index]
>>> s[:] #empty slicing
'viraj'
>>> # empty slicing fetch all blocks
>>> s[2:]
'raj'
>>> s[2:4]
'ra'
>>> # access vi
>>> s
'viraj'
>>> s[0:2]
'vi'
>>> # access ira
>>> s[1:4]
'ira'
>>> # Assignment:
>>> a = 'amitabh bachchan'
>>> # amit, amitabh, bachchan, chan,mit,abh,bh ba,chch
>>> #------------------------------------
>>> # can we use -ve indexing in slicing
>>> # yes
>>> s
'viraj'
>>> s[-3:]
'raj'
>>> s[-5:-3]
'vi'
>>> a
'amitabh bachchan'
>>> # chan
>>> a[-4:]
'chan'
>>> #----------------------------------
>>> # we can also traverse from right to left in reverse direction
>>> # s[::]
>>> # s[start:stop:step]
>>> # default we have +1 stepping
>>> s[::1]
'viraj'
>>> s[::]
'viraj'
>>> # -1 stepping means in reverse direction
>>> s[::-1]
'jariv'
>>> addr = 'Near Rest house Patan 455677'
>>> addr
'Near Rest house Patan 455677'
>>> addr[-6:]
'455677'
>>> #---------------
>>> s[0::-1]
'v'
>>> s
'viraj'
>>> # if slicing is +ve then progress/reading goes from left to right
>>> # if slicing is -ve then progress/reading goes from right to left
>>> # in slicing if we get empty output then it means wrong indexing
>>> s
'viraj'
>>> s[300:]
''
>>> s[1:3:-1]
''
>>> s
'viraj'
>>> s[1:-5:-1]
'i'
>>> s
'viraj'
>>> s[::2] # step by 2
'vrj'
>>> #------------------------
>>> # Methods of a string
>>> # use dir() to check all the methods of str
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s
'viraj'
>>> v = 'ramesh patil'
>>> v
'ramesh patil'
>>> v.capitalize()
'Ramesh patil'
>>> v.title()
'Ramesh Patil'
>>> #convert from lower to upper case
>>> v.upper()
'RAMESH PATIL'
>>> 
>>> d = 'DiNeSh'
>>> d
'DiNeSh'
>>> d.swapcase()
'dInEsH'
>>> d
'DiNeSh'
>>> d.casefold()
'dinesh'
>>> # to check help from python
>>> help(d.casefold)
Help on built-in function casefold:

casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.

>>> #-----------------------------------
>>> r = '--sumit--'
>>> r
'--sumit--'
>>> r.strip('-')
'sumit'
>>> e = '  elephant            '
>>> e
'  elephant            '
>>> e.strip() #default it strips space
'elephant'
>>> help(e.strip)
Help on built-in function strip:

strip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading and trailing whitespace remove.
    
    If chars is given and not None, remove characters in chars instead.

>>> e = '   ele  phant   '
>>> e
'   ele  phant   '
>>> e.strip() # wont remove spaces in between
'ele  phant'
>>> y = '#  *fanta   #$   '
>>> y
'#  *fanta   #$   '
>>> y.strip('# *$')
'fanta'
>>> #----------------------------------
>>> # rstrip and lstrip
>>> #---------------------------------------
>>> # Convert a string into  a list of string
>>> g = 'hum sath sath hai'
>>> g
'hum sath sath hai'
>>> # use split()
>>> g.split()
['hum', 'sath', 'sath', 'hai']
>>> # split default takes space
>>> ip = '198.162.12.3'
>>> ip
'198.162.12.3'
>>> ip.split('.')
['198', '162', '12', '3']
>>> #--------------------
>>> # Convert list fo string to str
>>> # use join() method
>>> n = ['198', '162', '12', '3']
>>> n
['198', '162', '12', '3']
>>> '-'.join(n)
'198-162-12-3'
>>> '.'.join(n)
'198.162.12.3'
>>> g = ['Ganesh','Ramesh','Pawar']
>>> g
['Ganesh', 'Ramesh', 'Pawar']
>>> ' '.join(g)
'Ganesh Ramesh Pawar'
>>> f = '    198.162.12.3   '
>>> f.strip()
'198.162.12.3'
>>> u = '198.162.12.3'
>>> u
'198.162.12.3'
>>> u.split('.')
['198', '162', '12', '3']
>>> u
'198.162.12.3'
>>> # instead of . we want -
>>> u.replace('.','-')
'198-162-12-3'
>>> '-'.join(u.split('.'))
'198-162-12-3'
>>> #---------------------------
>>> 
```