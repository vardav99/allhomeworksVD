Number1 = int(input("Input your number\t:"))
Number2 = int(input("Input your number\t:"))

try:
    division = Number1 // Number2
    print(division)
except ZeroDivisionError:
    print("Can't divide by zero")
    division = None
