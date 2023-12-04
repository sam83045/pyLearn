# 01<sup>st</sup> Dec Lecture code

```
""""""
"""
Elif ladder: when we need to test more than 2 conditions
then go with multiple use of elif
---------------------------
per =  float(input('Enter your percentage: '))
if per >= 80:
    print('You got Distinction')
elif per >= 75:
    print('You got first class')
elif per>= 65:
    print('You got second class')
elif per>= 55:
    print('You got Pass class')
else:
    print('You are Fail. Try Again')
-----------------------------
Nested if: if inside if

nationality = input('Enter your Nationality:')
if nationality == 'IND':
    age = int(input('Enter your age:'))
    if age>=18:
        print('You are Eligible for Voting')
    else:
        print('Age must be>=18')
else:
    print('You are from Other Country')
------------------------
make it simple using combining


nationality = input('Enter your Nationality:')
age = int(input('Enter your age:'))

if (nationality =='IND') and (age>=18):
    print('You are eligible for Vote')
else:
    print('Both conditions required to be satisfied')
------------------------------------------------
num = 30
# Write a code to test num is divisible by
# 5 & 7
if (num%5==0) and (num%7==0):
    print(num,'is divisible by both 5 & 7')
----------------------------------------------
Assignment: Solve at least 5 examples on each  
==========================================
Iterative statement:
We have iterables in python, from those iterables
when we want to fetch one element at a time this process
is called as iterations.

Ex. p = [10,20,30]
# we can fetch individual element from p using for loop

for loop syntax:

for var_name in iterable_name:
    process
-----------------------------
p = [100,200,300]
for value in p:
    print(value)
--------------------------
s = 'python'
for i in s:
    #print(i,end='\n\n')
    print(i,end='')
-----------------------
# lets use if else inside for loop

k = [10,4,22,98,45,6,10,37]

# print even numbers
#num%2==0
for num in k:
    if num%2==0:
        print(num,'is even number')
----------------------------
k = [10,4,22,98,45,6,10,37]

# Create a list of even numbers
#num%2==0
e = []
for num in k:
    if num%2==0:
        #print(num,'is even number')
        e.append(num)
print('Even list:',e)
-----------------------------------
k = [10,4,22,98,45,6,10,37]
e = []
for num in k:
    if num%2==0:
        #print(num,'is even number')
        e.append(num)
print('Even list:',e)
-----------------------------------
"""
```