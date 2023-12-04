# lets use if else inside loop

# print only even numbers
"""
k = [10, 4, 22, 98, 45, 6, 10, 37]

for num in k:
    if num % 2 == 0:
        print(num)
"""


# Create separate list of even and odd numbers and print both
k = [10, 4, 22, 98, 45, 6, 10, 37]
even = []
odd = []

for num in k:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even number list:", even)
print("Odd number list:", odd)
