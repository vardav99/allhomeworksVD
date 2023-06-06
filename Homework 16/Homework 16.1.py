class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Monkey(Animal):
    def sound(self):
        return "Uu aa aaah"


class Donkey(Animal):
    def sound(self):
        return "Iaah"


def make_sound(animal):
    print(animal.sound())


monkey = Monkey("Kapik")
donkey = Donkey("Ishak")

make_sound(monkey)
make_sound(donkey)

print(type(monkey))
print(type(donkey))