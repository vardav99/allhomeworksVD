number = int(input("Input your number:\t "))
#even or odd
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
#multiple of 3
if number % 3 == 0:
    print("number is multiple of 3")
else:
    print("number is not multiple of 3")
#divides to 2 and 3
if number % 2 == 0 and number % 3 == 0:
    print("number divides to 2 and 3")
else:
    print("number does not divide to 2 and 3")