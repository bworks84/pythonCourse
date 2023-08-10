# Object Oriented Programming in Python

# OOP aims to implement real-world entities like inheritance, polymorphism, abstraction, and encapsulation
# Main benefit is to bind the data and functions that work on within OOP together to more easily create/debug objects
# Classes are exportable

class Dog:

    def __init__(self, color, name, age):
        self.color = color              # attribute of the class dog
        self.name = name
        self.age = age

    def walk(self):
        print("walking the dog")

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


# mowglie = Dog()  # creating an instance of the class dog
# mowglie.bark()  # calls the method within the class using the new instance
# bowser = Dog("brown", "Bowser", 4)
# print(bowser.get_name())   # can get/return information about the instance
# print(bowser.get_age())
# bowser.set_age(6)       # can modify age now with method
# print(bowser.get_age())


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def __str__(self):
        print(f"{self.students} are enrolled in {self.name}")

    def add_student(self, student):
        if len(self.students) < self.max_students:
            # prints list of students referencing the name of student
            self.students.append(student.name)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Tim", 17, 92)
s2 = Student("Sarah", 18, 74)
s3 = Student("Bill", 18, 86)

course = Course("History", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))  # False
print(course.students)  # ["Tim", "Sarah"]

# returns the first student in the list of students
# print(course.students[0].name)
# print(course.get_average_grade())  # 83


# Inheritance

class Animal:
    number_of_animals = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.add_animal()

    @classmethod
    # class methods act on the class itself, not the instance
    def num_of_animals(cls):
        return cls.number_of_animals

    @classmethod
    def add_animal(cls):
        cls.number_of_animals += 1

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Dog(Animal):
    def __init__(self, name, age, color):
        # add super().__init__() to pull parent attributes into child
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Ruff")

    def show(self):
        print(
            f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Cat(Animal):
    def speak(self):
        print("Meow")


# print(Animal.number_of_animals)  # 0
whiskers = Cat("Whiskers", 3)
whiskers.show()
print(Animal.number_of_animals)
# print(Animal.number_of_animals)  # 1
goose = Dog("Goose", 7, "red")
goose.show()
# print(goose.number_of_animals)  # 2
print(Animal.number_of_animals)

# Static methods


class Math:

    @staticmethod           # static methods are used for organization and specific case use
    def add5(x):
        return x + 5


print(Math.add5(1))         # 6
