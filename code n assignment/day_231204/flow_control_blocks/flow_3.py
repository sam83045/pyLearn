"""
Iteration break statemenet
"""

# for i in range(5):
#     print(i)


# Pattern programs

# Start pattern
"""
# *
# **
# ***
# ****
# *****

n = 5

for row in range(n):
    for col in range(row):
        print(
            "*",
            end="",
        )
    print("")

"""

"""
# Mutliplication table of 2 to 20

for i in range(2, 21):
    for j in range(1, 11):
        print(str(i * j).rjust(3,'0'), end=" ", sep="")
    print()
"""


# Character patterns
# ord => gives ASCII value of character
# chr => give character of provided ASCII val

# A
# AB
# ABC
# ABCD
# ABCDE

for row in range(0, 6):
    for col in range(row):
        print(chr(65 + col), sep="", end=" ")
    print()
