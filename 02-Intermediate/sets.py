# Sets: unordered, mutable, no duplicates

mySet = {1, 2, 3}

print(mySet)

# does not recognize the duplicates
mySet1 = {1, 1, 2, 2, 3}

print(mySet1)

mySet.add(5)
mySet.add(6)
mySet.add(7)

# removes element
mySet.remove(3)

# removes - but if it doesnt find then no error
mySet.discard(2)

# removes from set and returns as value
mySet.pop()

for i  in mySet:
    print(i)

if 1 in mySet:
    print("yes")
else: 
    print("no")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# combines without dups
u = odds.union(evens)

print(u)

# where the values intersect - returns in a set
i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# returns elements in the first set that are not in the second
diff = setA.difference(setB)
print(diff)

# return set with all elements in setA and setB that do NOT overlap
symDiff = setB.symmetric_difference(setA)
print(symDiff)

# adds the two sets together - no dups
setA.update(setB)
print(setA)