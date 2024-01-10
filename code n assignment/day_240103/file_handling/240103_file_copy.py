sourceFileName= input("Enter source file Name:")
destFileName=input("Enter dest filename:")

sourceFile = open(sourceFileName, "r")
destFile = open(destFileName, "w")

buffer = sourceFile.read()
destFile.write(buffer)

sourceFile.close()
destFile.close()