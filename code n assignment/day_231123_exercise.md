# 23<sup>rd</sup> Nov Exercise  

```
Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=['A', 'B', 'C', 'D', 100, '1']
>>> list
['A', 'B', 'C', 'D', 100, '1']
>>> type(list)
<class 'list'>
>>> # Assignment:
>>> # 1. Add 30 before A
>>> # 2. Add 450 between C & D
>>> # 3. Add 'C++' after 1
>>> # 4. Remove 100
>>> # 5. Remove '1'
>>> list.insert(0,30)
>>> list
[30, 'A', 'B', 'C', 'D', 100, '1']
>>> list.insert(-3,450)
>>> list
[30, 'A', 'B', 'C', 450, 'D', 100, '1']
>>> list.append('c++')
>>> list
[30, 'A', 'B', 'C', 450, 'D', 100, '1', 'c++']
>>> list.remove(100)
>>> list
[30, 'A', 'B', 'C', 450, 'D', '1', 'c++']
>>> list.remove('1')
>>> list
[30, 'A', 'B', 'C', 450, 'D', 'c++']
>>> 
```
