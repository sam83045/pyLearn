items = [12, 35, 9, 56, 24]


def interchangeListItems(items: list):
    last = items.pop()
    first = items.pop(0)
    items.insert(0, last)
    items.append(first)


interchangeListItems(items)
print(items)
