list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]


newList = map(lambda item1, item2: item1 + item2, list1, list2)

print(list(newList))
