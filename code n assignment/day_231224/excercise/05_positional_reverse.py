# str = input("Enter your string:")
str = "Ajit Pawar"

revStr = str[::-1]
strArr = revStr.split(" ")
strArr.reverse()
positionalRev = " ".join(strArr)


print("Entered string is", str)
print("Reversed string is", positionalRev)
