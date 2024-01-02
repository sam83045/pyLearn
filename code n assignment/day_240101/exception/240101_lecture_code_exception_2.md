# 1<sup>st</sup> Jan Lecture code


```
""""""
"""
Generating an exception:
- raise keyword
- assert keyword
---------------------------
When user wants to generate an exception we can use above 2 optinons

age = int(input('Enter your age:'))
if age < 18:
    raise Exception('Age must be >=18')

# Challenge: Handle above exception
-------------------------
ex. 2
passwrd = input('Enter the password:')
if passwrd != '3434':
    raise Exception('Password did not match')
else:
    print('Login successful..! You can proceed..')
-------------------------------------
Assignment: Create 4 examples on raise exception
---------------------------------------
assert <condition>
If condition is True--> follow the process/complete the steps
bt if Condition is False--> Generate AssertionError

assert True  # normal execution
assert False # AssertionError

age = 15
assert age>=18,'Age must be >=18'
---------------------------------------
Customized Exception

class PinCheck(Exception):
    def __init__(self,msg):
        self.msg = msg

pin = int(input('Enter the pin:'))
if pin != 1234:
    raise PinCheck('Pls give correct pin')
--------------------------------------
"""
```