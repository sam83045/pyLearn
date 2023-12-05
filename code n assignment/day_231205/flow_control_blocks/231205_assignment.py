# Assignment:
# print 1-20 even numbers using while loop
# print python 10 times using while loop
# print index of a given string using while loop
# Ex. 'python'
# Ans: p is present at index 0

# print 1-20 even numbers using while loop
n = 20
i = 1
while i <= n:
    print(i)
    i += 1

# print python 10 times using while loop
n = 10

while n > 0:
    print("Python")
    n -= 1


# print index of a given string using while loop
# Ex. 'python'
# Ans: p is present at index 0
str = input("Enter string:")
i = 0
while i <= len(str) - 1:
    print("Index of", str[i], "is", i)
    i += 1
