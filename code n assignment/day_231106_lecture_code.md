# 06<sup>th</sup> Nov Lecture code

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # IDLE: Integrated learning environment
>>> # scripting
>>> # is used for commenting in python
>>> # comment: when we want to add some plain text in a program
>>> #---------------------------------------------
>>> # Features of Python
>>> # Simple and easy to use
>>> # its is dynamically typed
>>> a = 100
>>> a
100
>>> type(a)
<class 'int'>
>>> # In python everything is an object
>>> b = 77.88
>>> b
77.88
>>> type(b)
<class 'float'>
>>> # Each object has a memory
>>> # to check memory address use id() function
>>> id(a)
140733983219840
>>> id(b)
2013631198768
>>> # if we check any variable which is nt present in the memory
>>> id(z)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    id(z)
NameError: name 'z' is not defined
>>> # a,b are identifiers
>>> # 100,77.88 are objects
>>> #----------------------------------
>>> # What is an Identifier?
>>> # Identifier is a name given to the object
>>> # Ex. bank = 'SBI' in this bank is an identifier and 'SBI' is an object
>>> # there are certain rules while declaring an identifier
>>> #--------------------------
>>> # Alphabates are valid/allowed
>>> # a-Z A-Z
>>> # identifiers should be in lower case
>>> # _ underscore is also a valid
>>> _a = 'ammit'
>>> _a
'ammit'
>>> type(_a)
<class 'str'>
>>> # space is not allowed
>>> bank ifsc = 'sbi3435'
SyntaxError: invalid syntax
>>> # we can solve this problem of gap using _
>>> bank_ifsc = 'sbi3435'
>>> bank_ifsc
'sbi3435'
>>> # Other special symbols and chars are not valid./allowed
>>> # $%^&*()_<>:"
>>> a$ = 560
SyntaxError: invalid syntax
>>> info@ = 'Pune'
SyntaxError: invalid syntax
>>> #-----------------------------
>>> # In python we have some reserved keywords
>>> # we cant use those keywords as an identifier
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> try = 100
SyntaxError: invalid syntax
>>> with = 'You'
SyntaxError: invalid syntax
>>> #  PYTHON IS CASE SENSITIVE LANGUAGE
>>> Try = 100
>>> Try
100
>>> #-------------------------------------
>>> # Literals in Python
>>> # literals are based on data types
>>> a
100
>>> # of type int
>>> # int literal
>>> 'python' # str literal
'python'
>>> #--------------------------------------
>>> # print(object/s,sep=' ',end='\n' )
>>> print(10,20,30)
10 20 30
>>> print(10,20,30,sep='-')
10-20-30
>>> # sep works between the objects
>>> print() # empty print function \n means goto new line

>>> print(end='\n\n')


>>> # can we use \n as a separator
>>> print(10,20,30,sep='\n')
10
20
30
>>> # \n for new line and \t for tab(4 spaces)
>>> print(10,20,30,sep='\t')
10	20	30
>>> 
```