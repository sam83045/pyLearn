t1 = (10, 20, 30)
t2 = (100, 200, 300)

# Method 1
print(dict(zip(t1, t2)))

# Method 2
dict = {}
for idx, item in enumerate(t1):
    dict[item] = t2[idx]

print(dict)

# Method 3
print({item: t2[idx] for idx, item in enumerate(t1)})
