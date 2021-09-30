def cube(num):
    complete = num*num*num

    # using the return keyword breaks you out of the function (ends the function)
    return complete

cubed = input("Type in a number: ")

cubed2 = int(cubed)
print(cube(cubed2))