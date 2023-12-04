# Print following pattern
# *****
# ****
# ***
# **
# *

n = 5

for row in range(n):
    for col in range(n - row):
        print(
            "*",
            end="",
        )
    print("")


# print following pattern
# ABCDE
# ABCD
# ABC
# AB
# A
ascii_val = ord("A")
for row in range(n):
    for col in range(n - row):
        print(chr(ascii_val + col), end="", sep="")
    print()
