# Dictionary: key-value pairs, unordered, mutable
myDict = {
    "name": "Max", 
    "age": 28,
    "city": "New York"
}

print(myDict)

# create dictionary with dict function
myDict2 = dict(name="Mary", age=27, city="Boston")
print(myDict2)

# select value based on key
value = myDict["name"]
print(value)

# add a key-value - if already exists, the key is overwritten
myDict["email"] = "test@test.com"
print(myDict)

# deletes by key
del myDict["email"]

# pop value off
myDict.pop("age")

# removes last key-value
myDict.popitem()

if "name" in myDict:
    print(myDict["name"])

try:
    print(myDict["name"])
except:
    print("Error")

# for loops can be used
for key in myDict:
    print(key)

# loops over keys
for key in myDict.keys():
    print(key)

# loops over values
for value in myDict.values():
    print(value)

# loops over both
for key, value in myDict.items():
    print(key, value)

# creates copy
dictCopy = myDict.copy()



