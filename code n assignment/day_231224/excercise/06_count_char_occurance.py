# str = input("Enter your string:")
str = "Apple Mango"
d = {}

for char in str:
    if d.get(char):
        d[char] += 1
    else:
        d[char] = 1
print(d)
