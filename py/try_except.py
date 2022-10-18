while True:
    try:
        x = int(input("Please enter a first number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    try:
        y = int(input("Please enter a second number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    try:
        result = x / y
    except ZeroDivisionError:
        print("It is not necessary to divide by zero xD")
        result = 0