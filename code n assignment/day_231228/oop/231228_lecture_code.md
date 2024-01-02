
# 28<sup>th</sup> Dec Lecture code

```
""""""
"""
OOP: Abstraction
Information hiding

-----------------------------------
Rules to create an abstract class

- U have import ABC class from abc module
- Inherit ABC in normal class
- import abstractmethod
- decorate out declared method using @abstractmethod
------------------------------------------
Information hiding is aligned with object creation
We cant create an object of an abstract class
-----------------------------------------
Next step is to create a new class 
Inherit User Created Abstract class
where u can create an object
BUT--> U must have to implement abstract method in new class
----------------------
import BankPins class from bank_secret.py module

from bank_secret import BankPins

class SBI(BankPins):
    def policies(self):
        print('SBI Policies')
s = SBI()
s.policies()
--------------------------------
===================================
# Exception Handling
Exception: error
------------------
# check object level hierarchy of python
print(help('builtins'))

------------------
Why to handle exception

print('Sham')
k = [10,20,30]
print(r)
for i in k:
    print(i)
d = {1:10,2:20}
print(d.keys())

because of print(r) line
rest of the code wont get executed
Execution will stop bcz of error
Hence it is needed to handle
---------------------------
print('Sham')
k = [10,20,30]
#r = 'python'
try:
    print(r)
except:
    r = 10
    print(r)

for i in k:
    print(i)
d = {1:10,2:20}
print(d.keys())
----------------------------------- 
Track exception with msg

try:
    print(10/0)
    #print(10/'0')
    #print(10/t)

except Exception as msg:
    print('Error:',msg)
-----------------------------
Named Exception

try:
    #print(10/0)
    print(10/'0')
    #print(10/t)

except (ZeroDivisionError,TypeError,NameError) as msg:
    print('Error:',msg)
---------------------------
4 blocks present in exception handling
try:
    test_code/error prone_code
except:
    if exception handle it here
else:
    if no exception come here
finally:
    irrespective of exception,this block will be executed
----------------------
# Case1- Exception
try: 
    print(r)
except Exception as msg:
    print(msg)
else:
    print('No error...')
finally:
    print('Process finished')
---------------------------- 
"""
# Case2- No Exception
r = 99
try:
    print(r)
except Exception as msg:
    print(msg)
else:
    print('No error...')
finally:
    print('Process finished')
```