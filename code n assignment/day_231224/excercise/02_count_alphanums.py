# str = input("Enter your string:")
str = "P@#yn26at^&i5ve"
d = {"digit": 0, "alpha": 0, "symbols": 0}

for char in str:
    if char.isalpha():
        d["alpha"] += 1
    elif char.isdigit():
        d["digit"] += 1
    else:
        d["symbols"] += 1
print(d)
