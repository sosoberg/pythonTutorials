# Tuple: ordered, immutable

myTuple = ("Max", 28, "Boston")
print(myTuple)

myTuple1 = (1,2,2,2,3,3,3,3,4,4,5,5,5,6,6,7,7,7,7,8,8,8)

# counts instances of specified element
print(myTuple1.count(2))

# returns first occurence of specified element
print(myTuple1.index(3))

# converts to list
myList = list(myTuple)
print(myList)

# converts back to tuple
myTuple = tuple(myList)
print(myTuple)

# set elements equal to tuple values
myTuple2 = "Max", 28, "Boston"

name, age, city = myTuple2
print(name)
print(age)
print(city)

import sys

newList = [0, 1, 2, "hello", True]
newTuple = (0, 1, 2, "hello", True)

# return the number of bytes in them -- tuple is smaller and more efficient to iterate over
print(sys.getsizeof(newList), "bytes")
print(sys.getsizeof(newTuple), "bytes")

import timeit

# another example of tuples being faster - timing creation of one million tuples vs lists
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))