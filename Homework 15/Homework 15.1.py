class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        self.display()
        print("Section:", self.section)


# Creating a student object and testing the displayStudent method
student = Student("John Doe", 20, "A")
student.displayStudent()
