strList = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

filteredList = filter(lambda str: str != "", strList)

print(list(filteredList))
