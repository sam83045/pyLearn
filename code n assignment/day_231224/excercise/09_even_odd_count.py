from functools import reduce

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

evenOdd = {"even": 0, "odd": 0}


def evenOddKey(n):
    if n % 2:
        return "even"
    else:
        return "odd"


evenOdd = reduce(lambda dic,item: dic["event"]=dic["even"]+1 if item%2,numbers,evenOdd )
