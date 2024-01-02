# 1<sup>st</sup> Jan Lecture code


```
""""""
"""
File handling:
What is file: it is a storage medium which collects and stores data as a single unit.
It has an extension ex. .txt .bin .py
 
Operations we can perform over the file
- Open/Create
- Close
- update
- read
- write
- append

Default python works on text files
it can also handle binary files
-----------------------------------------
Creation of a file

We can use open() function to perform all operation

#open(file_name,mode)
# default mode is read mode 'r'

# to create a file first we hae 3 differnt modes
# w: write and truncate
# a: create a file+append
# x: create file+write
f = open('nov1.txt','a')
# f is an handle/file handling object
# to write contnts we can use write() writelines()
f.write('Happy \nNew \nYear \n2024')
f.write('\nPlan some event')
----------------------------------------
f = open('nov2.txt','a')

f.write('100\n') # it accepts only string

f.writelines(['\n2022','\n2023','\n2024'])
f.writelines('\nPallavi')

# if we add list[str] in write
f.write(['1','2'])
--------------------------------------

# x: is used to create a file only ones
f = open('nov3.txt','x')
# We cant execute above line more than ones
# it will throw an error
---------------------------
f  = open('nov3.txt','w')
#f.write(234234) # write only accepts str data
f.write('234234')# this is ok as its in str form
-----------------------------
Check properties of a file

f = open('nov2.txt')
print(f.name)
print(f.mode)
print(f.writable()) # returns boolean output
#f.write('12') # not allowed bcz mode is read 'r'
print(f.readable())
# check files is closed or nt
print('Before:',f.closed)

f.close() #will close the file
print('After:',f.closed)
------------------------
importance of f.close()

f = open('nov3.txt','w')
f.write('12323435')
f.close()
f.write('777777') # wont get executed as file is closed
# this will throw TypeError


Assignment:
Create a sample.txt file and perform
write and writelines

Create 3 files using w a and x mode
"""
```