class Car:
    def __init__(self, brand):
        self.brand = brand

    def max_speed(self):
        return 0


class BMW(Car):
    def color(self):
        return "BMW is Black."

    def max_speed(self):
        return 350


class Ferrari(Car):
    def color(self):
        return "Ferarri is Green."

    def max_speed(self):
        return 450


bmw = BMW("BMW")
ferrari = Ferrari("Ferrari")

print(bmw.max_speed())
print(ferrari.max_speed())

print(bmw.color())
print(ferrari.color())

print(type(bmw))
print(type(ferrari))
