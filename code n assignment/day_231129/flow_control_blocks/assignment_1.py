"""
Write if else code
- to check +ve -ve number
- to check even odd number
- to check num divisible by 5
- to check num divisible by 5 and 7 (use operators)
- to check num divisible by 5 or 7 (use operators)
"""
num = int(input('Enter number:'))

if num % 2 == 0:
    print(num, 'is even number')
else:
    print(num, 'is odd number')

if num % 5 == 0:
    print(num, 'is divisible by 5')
else:
    print(num, 'is not divisible by 5')

if num % 5 == 0 and num % 7 == 0:
    print(num, 'is divisible by 5 and 7')
else:
    print(num, 'is not divisible by 5 and 7')

if num % 5 == 0 or num % 7 == 0:
    print(num, 'is divisible by 5 or 7')
else:
    print(num, 'is not divisible by 5 or 7')
