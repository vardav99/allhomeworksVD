class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.Perimeter())
        print("Area:", self.Area())


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height


rectangle = Rectangle(5, 3)
rectangle.display()

print()

parallelepiped = Parallelepipede(5, 3, 2)
parallelepiped.display()
print("Volume:", parallelepiped.Volume())
