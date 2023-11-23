Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 'amitabh bachchan'
>>> # amit, amitabh, bachchan, chan,mit,abh,bh ba,chch
>>> a[:4]
'amit'
>>> a[:7]
'amitabh'
>>> a[-8:]
'bachchan'
>>> a[-4:]
'chan'
>>> a[1:4]
'mit'
>>> a[4:7]
'abh'
>>> a[5:7]
'bh'
>>> a[5:4:-1]
'b'
>>> a[5:3:-1]
'ba'
>>> a[6:10]
'h ba'
>>> a[-6:-10]
''
>>> a[-6:-2]
'chch'
>>> 
