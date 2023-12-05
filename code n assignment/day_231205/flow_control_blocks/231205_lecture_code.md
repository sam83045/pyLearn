# 05<sup>th</sup> Dec Lecture code

```
""""""
"""
Iterative statement
while loop: conditionally infinite
if condition is True then it runs for infinite time

syntax:

while condition:
    process
    
-----------
Ex.
while 2==2:
    print(100)
    
----------------------
num = 5
while num >1:
    print(num)
    num -= 1

-------------------
print 1-10 numbers using while loop

num = 1
while num <=10:
    print(num)
    num += 1 #num = num+1
----------------------------
k = [100,200,300,400,500,800,900]
# print numbers present in k using while loop
print('last index:',len(k)-1)
index = 0
while index <= len(k)-1:
    #print(index)
    print(k[index])
    index += 1
------------------------------
# Assignment:
print 1-20 even numbers using while loop
print python 10 times using while loop
print index of a given string using while loop
Ex. 'python'
Ans: p is present at index 0 
-----------------------------------
Transfer statements
- break 
- continue
- pass
----------------------------------
break: is a keyword which is used to break current 
execution based on condition
we can write break only inside the loop

fruits = ['mango','apple','orange','mango','kiwi','apple']
# if we get orange then stop current execution
for i in fruits:
    if i == 'orange':
        break
    else:
        print('I like:',i)

-----------------------
continue: skips the conditional object, and continues the loop

Ex.
fruits = ['mango','apple','orange','mango','kiwi','orange','apple']
# if we get orange then stop current execution
for i in fruits:
    if i == 'orange':
        continue
    else:
        print('I like:',i)
--------------------------------
amazon_cart = [1200,499,9999,1978,599,999,1000,99]
# Select items>=500, and give Free delivery
for item in amazon_cart:
    if item>=500:
        print('Item price is Rs.',item,',eligible for Free delivery')
    else:
        #break
        continue
-------------------------------------
pass:- empty stub/acts like a null statement
It is used to create empty blocks
i mean empty functions or loops

ex.


if 10 > 0:
   pass
print('hello')

--------------------------
def sample_function():
    pass
---------------------------
what is enumerate()?

a = [40,50,60,70]
# i want list of tuple
#[(index,element)]
print(enumerate(a))
print(list(enumerate(a)))
--------------------------------------
g = [34,76,88,99,12,9,23]
# print index and element in the form tuple
for i in enumerate(g):
    #print(i[1])
    print(i)
-------------------
unpack the result

Ex.
g = [34,76,88,99,12,9,23]
# print (index and element) in the form tuple
for index,value in enumerate(g):
    print(value)
---------------------------------
Q. what is the similarity between break and continue
- it skips the elemnt at given condition
Ex.

for i in range(9):
    if i == 7:
        break
        #continue
    else:
        print(i)
------------------------------
"""
```