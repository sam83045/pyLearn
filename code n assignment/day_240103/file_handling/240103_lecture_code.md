# 3<sup>rd</sup> Jan Lecture code

```
""""""
"""
Read Operation

f = open('nov3.txt')
# default it has read mode 'r'
print(f.read(5))
print(f.read())
-----------------------
f = open('nov3.txt')
# default it has read mode 'r'
print('1:',f.read())
print('2:',f.read()) # its of no use bcz first read already covered all blocks
--------------------------------
f = open('nov3.txt')

print(f.readline())
print(f.readline())
# it is used to read contents line by line
-------------------------------------
f = open('nov3.txt')

print(f.readlines())
# it is used to read all the lines as a list of str
------------------------
PS: Access numbers from nov2

f = open('nov2.txt')
data = f.read()
for chr in data:
    #print(chr)
    if chr.isdigit():
        print(chr,end='')
----------------------------
f = open('nov2.txt')
data = f.readlines()
for chr in data:
    #print(chr)
    for i in chr.split():
        #print(i)
        if i.isdigit():
            print(i)
----------------------------

n = int(input('How many lines:'))
f = open('nov2.txt')
data = f.readlines() #list of str
for line in range(n):
    print(data[line])
-----------------------
#alternate solution


n = int(input('How many lines:'))
f = open('nov2.txt')
#data = f.readlines( #list of str
for line in range(n):
    print(f.readline())
--------------------------------
seek(): bring a cursor to particular position
Ex.
f = open('nov2.txt')
f.seek(6)
print(f.read(4))
----------------------------------
tell(): tell current cursor position
Ex.
f = open('nov2.txt')
print(f.read(4))
print(f.tell())
----------------------------
# Auto closing
with open('nov2.txt') as f:
    print(f.read(7))
    print('inside:',f.closed)
print('Outside:',f.closed)
-------------------------------
Assignment: Create a.txt write some contents + create b.txt
and paste the contents from a.txt
--------------------------------
CSV[Comma Separated value] Operations: read write
import csv
with open('sample.csv','w',newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['Name','Age','Salary'])
    wr.writerow(['Ashish',27,78000.00])
---------------
read

import csv
with open('sample.csv','r',newline='') as f:
    print(f.readlines())
---------------------------
#f = open('C:\\Users\hakim\PycharmProjects\CNS_AUG\\Nov_batch\OOP\\test.txt','w')

# file on desktop

f = open('C:\\Users\hakim\OneDrive\Desktop\\test.txt','w')
f.write('123456')
-----------------------------------
Assignment:
Read a txt file from project directory and copy the contents
to the file present on desktop
-------------------------------------
# Read an image file
f = open('1_a.jpg','r+b')
# r+b: read binary
# rb
#print(f.read()) 
#  it gives byte stream
# conversion of an image into bytes
--------------------------
# Read an image file
f = open('bro.png','r+b')
data = f.read()

# write the data in function folder
f2 = open('C:\\Users\hakim\PycharmProjects\CNS_AUG\\Nov_batch\\function\\new.png','w+b')
# w+b: write binary
f2.write(data)
------------------------------
Point to be prepared on ur own
functions:
- decorator
- iterator
- generator

modules:
- itertools
- collection
- array
"""
```