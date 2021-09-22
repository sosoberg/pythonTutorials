# slicing

newList = [1,2,3,4,5,6,7,8,9]

# start and stops at specified indexs
a = newList[1:5]

# step index - goes from beginning to end with one step
b = newList[::1]
# goes through list in steps of two
c = newList[::2]
# reverses list
d = newList[::-1]

print("\nList Slicing: ")
print(a)
print(b)
print(c)
print(d)


# list comprehension

x = [1,2,3,4,5,6]

# square all of the elements
# fast for loop over the list
y = [i*i for i in x]

print("\nList Comprehension: ")
print(x)
print(y)


# Lists: ordered, mutable, allows duplicate elements
print("\nOther Methods of List Manipulation: ")

myList = ["banana", "cherry", "apple"]

print(myList)

# created empty list with list function
myList2 = list()

print(myList2)

if "banana" in myList:
    print("yes")

else:
    print("no")

print(len(myList))

myList.append("lemon")

print(myList)

# specify index spot
myList.insert(1, "blueberry")

print(myList)

myList.pop()
