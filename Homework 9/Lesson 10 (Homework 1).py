def perimeter_of_rectangle():
    Rectangle_L = int(input("Input L of rectangle:\t "))
    Rectangle_W = int(input("Input W of rectangle:\t"))
    return 2 * (Rectangle_L + Rectangle_W)


Rectangle_perimeter = perimeter_of_rectangle()
print(Rectangle_perimeter)
