"""
# access sample.py present root dir
# access will be direct

import sample
sample.show('shivani',23)
print(sample.c)

# Assignment:
# import sample as s
# from sample import *
# from sample import show,a,b,c
-----------------------------------------
If module is present in sub directory

#import shop # direct access wont be possible
# because it is present in another directory
# present in DMart
# we have specify hierarchy

from DMart import shop

print(shop.articles)
--------------------------------
Assignment:
from DMart.shop import *
from DMart.shop import bal.cloths
from DMart import shop as s
---------------------------------------
=====================================
"""
"""
Package:-
A folder contains multiple modules
with one file named __init__.py
then that folder is a Package

Means Entry point of execution for
that package is __init__.py file
------------------------
# lets import bank_sbi package

import bank_sbi
------------------------
# import account.py, info.py and online.py
# module--> Package--> Library

import bank_sbi 

# importing bank info will call __init__.py
# we have to provide logic inside this init file
# to reduce complexity of writing multiple loc
# in main  project file
# hence Package gives flexibility in terms of writing code and accessing
==============================================
"""































