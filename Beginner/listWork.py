lucky_numbers = [4, 8, 15, 16, 23, 42]

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

# Adds a string to the list

friends.append("Karen")

print(friends)

# add item into middle of list
# index position 1 will have value Kelly - rest of the values are pushed to the right
friends.insert(1, "Kelly")

print(friends)

# remove value
friends.remove("Kevin")

print(friends)

# pop the last element off of the list

friends.pop()

print(friends)

# remove all elements

friends.clear

print(friends)

# see if element is in the list

print(friends.index("Oscar"))

# see how many instances of element are in the list

print(friends.count("Karen"))

# sort the list
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

# adds lucky_numbers list to friends list

friends.extend(lucky_numbers)

print(friends)

# copy a list

friends2 = friends.copy()

