# 04<sup>th</sup> Dec Lecture code



```
""""""
"""
Flow control blocks

- Iterative statements

for var_name in iterable:
    process/operation

PS: Print ur name 5 times
for i in range(5):
    print('Shivani')

# ask user for the count

n = int(input('Enter the count u require:'))
for i in range(n):
    print('Shivani')
--------------------------------
# Pattern program
Star patterns

*
**
***
****
*****

for n in range(1,6):
    print('*'*n)

Assignment: print above pattern using list comprehension
-------------------------
Assignment:
**
****
******
********
-------------------------------
*****
****
***
**
*

for i in range(5,0,-1):
    print(i*'*')
--------------------------------------
# Nested for loop
for i in range(6): # rows
    for j in range(6): #columns
        print(i,j,sep='',end=' ')
    print()
---------------------------------------
A
AA
AAA
AAAA
AAAAA
---------------------------
A
AB
ABC
ABCD
ABCDE

# We can check Unicode number using ord fucntion
print(ord('A'))
----------
When we need to convert unicode nummber into a char
then use chr(code) built in function

for i in range(1,6): #[1,2,3,4,5]
    for j in range(1,6):
        print(chr(64+i),end=' ')
    print()
-------------------
for i in range(1,6): #[1,2,3,4,5]
    for j in range(i):
        print(chr(64+i),end=' ')
    print()
--------------------
for i in range(1,6): #[1,2,3,4,5]
    for j in range(i):
        print(chr(65+j),end=' ')
    print()
------------------------------
for i in range(1,6): #[1,2,3,4,5]
    for j in range(1,i+1):
        print(chr(64+i),end=' ')
    print()
----------------------------
# Print all the patterns in reverse order(mirror image)
"""
```