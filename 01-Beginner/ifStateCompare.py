def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num2 and num3 > num1:
        return num3

print(str(max_num(2, 3, 5)) + " is the biggest bumber")