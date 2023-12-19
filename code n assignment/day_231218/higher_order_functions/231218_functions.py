"""
check = lambda num: ("Positive") if num > 0 else "Negative"

print(check(2))
"""

"""
Higher order function
- map   : 
- filter:
- reduce: import it from funtools package
"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda n: n * 2, num)))

print(list(filter(lambda num: num % 2 == 0, num)))


from functools import reduce

print(reduce(lambda x, y: x + y, num, 5))
