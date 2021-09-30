# open file - requires file path
# r - read
# w - write
# a - append
# r+ - read/write
employeeFile = open("./Beginner/readingFiles/employees.txt", "r")

# checks if file is readable
print(employeeFile.readable())

# read the file
print(employeeFile.read())

# reads single line
print(employeeFile.readline())

# read all lines and put them in a list
# specify with line you want with brackets
print(employeeFile.readlines()[1])

# for loop for reading
for employee in employeeFile.readlines():
    print(employee)

# make sure to close the file
employeeFile.close()