# 30<sup>th</sup> Nov Lecture code

```commandline
# single line comment
"""
multi-line comment
-----------------------------
Flow control blocks
Iterables: collection of elements
a = [10,20,30,40,30,50,60,30,10,20]

3 Options we have
- Selective/Conditional statements

if
if else
if elif else
elif ladder
nested if
----------------------------
# when we want to do conditional checking then use if statement
syntax:
if <condition>:
    # indentation
    # process
When if condition is True then process will get executed
--------------------------
Ex.
num =  -10
if num > 0:
    # when cursor goes 4 spaces inside
    # it means Program control is inside a block
    print('Good evening: Process is running')

# As condition is False, we are nt getting an output
----------------------------------
num =  10
if num > 0:
    # when cursor goes 4 spaces inside
    # it means Program control is inside a block
    print('Good evening: Process is running')

# As condition is True, we are getting an output
# print statement will get executed
-------------------------------------------
#pin = '0000'
pin = input('Enter your pin:')
if pin == '0000':
    print('Successful Login')
-------------------------------
# When we need test 2 cases
then use if ....else approach
-----------------------------------
pin = input('Enter your pin:')
if pin == '0000':
    print('Successful Login')
else:
    print('Wrong pin entered')

# else follows if
# if is condition based
# else is condition less
--------------------------------
Assignments:
Write if else code
- to check +ve -ve number
- to check even odd number
- to check num divisible by 5
- to check num divisible by 5 and 7 (use operators)
- to check num divisible by 5 or 7 (use operators)
------------------------------------
# when we want to test 3 cases then use
if condition:
elif condition:
else:
-----------------
Ex.
temp = float(input('Enter temp value:'))
if temp> 35:
    print('Its High Temp')
elif temp>18:
    print('Its Average Temp')
else:
    print('Its Low temp')
--------------------------------
Q. if vs elif vs else
"""




































```