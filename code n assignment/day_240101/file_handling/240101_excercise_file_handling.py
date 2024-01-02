# Create file using `w` mode
def createFileUsingW():
    f = open("w-file.txt", "w")
    f.write("Hello world from file handling")
    f.write("File created with Write mode")
    f.close()
    print("file created")


createFileUsingW()


# Create file using `a` mode
def createFileUsingA():
    f = open("a-file.txt", "a")
    f.write("Hello world from file handling")
    f.write("File created with Append mode")
    f.close()
    print("file created")


createFileUsingA()


# Create file using `x` - Create once mode
def createFileUsingX():
    f = open("x-file.txt", "x")
    f.write("Hello world from file handling")
    f.write("File created with Create once mode")
    f.close()
    print("file created")


createFileUsingX()
