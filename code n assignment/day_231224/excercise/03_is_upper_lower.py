# str = input("Enter your string:")
str = "The quick Brow Fox"
d = {"upper": 0, "lower": 0, "symbol": 0}

for char in str:
    if char.isupper():
        d["upper"] += 1
    elif char.islower():
        d["lower"] += 1
    else:
        d["symbol"] += 1
print(d)
