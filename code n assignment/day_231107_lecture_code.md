# 7<sup>th</sup> Lecture code

```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Operators in Python
>>> # Arithmatic operators
>>> # + - * / % // **
>>> 2+4
6
>>> 5-2
3
>>> 3*4
12
>>> 4/2
2.0
>>> # % mod: returns remainder
>>> 4%3
1
>>> 20%4
0
>>> # // floor division
>>> 10/3
3.3333333333333335
>>> # it gives floor part
>>> 10//3
3
>>> 8/5
1.6
>>> 8//5
1
>>> # ** -> power of
>>> 2**3
8
>>> 3**2 #num**power
9
>>> 11**2
121
>>> # exponential operator
>>> #---------------------------------
>>> # Assignment operators
>>> a = 100
>>> a
100
>>> a + 100
200
>>> # if we check value of a, its unchanged
>>> a
100
>>> a += 10 # a = a + 10
>>> a
110
>>> a += 50
>>> a
160
>>> a -= 20
>>> a
140
>>> # first it will perform an operation n then answer will b stored in the same variable
>>> # Assignment: try remaining operators
>>> a
140
>>> #--------------------------
>>> # Conditional operators
>>> # Used to compare objects
>>> # < > <= >= == !=
>>> # They result boolean output
>>> # Boolean: True, False
>>> 2 > 3
False
>>> 3 == 3
True
>>> 3 == '3'
False
>>> 5 >= 3
True
>>> 'python' != 'Python'
True
>>> #---------------------------
>>> # Membership
>>> # also returns True , False
>>> # based on checking
>>> # it checks given object is a member of a collection or not
>>> # it has 2 options
>>> # in, not int
>>> # not in
>>> 'dil' in 'dil to pagal hai'
True
>>> # if given object is present then True, else False
>>> 'XYZ' in 'dil to pagal hai'
False
>>> 100 not in [1,2,3,4,5]
True
>>> 1 not in [1,2,3,4,5]
False
>>> #------------------------------
>>> #  Identity operators
>>> # also returns boolean values: True, False
>>> # options available: is, is not
>>> # it checks for content equality
>>> # means if the contents are same then u will get True,else False
>>> 'python' is 'python'
True
>>> 'python' is 'Python'
False
>>> 10 is 10
True
>>> 10 is '10'
False
>>> #-------------------
>>> # difference between == , is
>>> 10 == 10
True
>>> 10 == 10.0
True
>>> 10 is 10
True
>>> 10 is 10.0
False
>>> # Content equality and Address equality
>>> # == does content equality
>>> # if contents are same then u wil get True
>>> 10 == 10.0
True
>>> # instead
>>> # is does address equality
>>> 10 is 10.0
False
>>> # if addresses are same then True
>>> id(10)
140733916763456
>>> id(10.0)
2233135512696
>>> #-------------------------------
>>> # Logical operators
>>> # and or not
>>> # Answer is in True False
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> 1==1 and 4>2
True
>>> 1==1 and 4<2
False
>>> # check for other conditions
>>> #--------------------
>>> # or operator
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> #---------------------
>>> # not operator: negation
>>> not False
True
>>> not True
False
>>> not 10>3
False
>>> #-------------------------------------
>>> 
```