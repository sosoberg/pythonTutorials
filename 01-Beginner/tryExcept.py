try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)

# catches the input error
except ValueError:
    print("Invalid number")

# catches the divide error
except ZeroDivisionError:
    print("Cannot divide by Zero")

