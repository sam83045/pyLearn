inp = input("Enter marks of three subjects (max=100):")
marks = inp.split()

marks = list(map(int, marks))


# Does marks of three subject provided
if len(marks) != 3:
    raise Exception("Please provide marks of three subjects")

# Marks in one of subject are more than 100
if max(marks) > 100:
    raise Exception("Each subject marks should not be greater than 100")

# Marks in one of subject are more than 100
if min(marks) < 0:
    raise Exception("Marks should not be negative")


# Marks obtained are not sufficient for eligiblity
if min(marks) < 40:
    raise Exception("Marks are not sufficient for eligiblity")
