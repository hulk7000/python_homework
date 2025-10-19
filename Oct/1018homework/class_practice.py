class Dog:
    def __init__(self, name, types):
        self.name = name
        self.types = types

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", "Golden Retriever")

my_dog.bark()



class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

my_car = Car("Toyota", "red")

my_car.drive()



class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm in grade {self.grade}.")

student1 = Student("Alice", 7)

student1.introduce()



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def summary(self):
        print(f"'{self.title}' is written by {self.author}.")

book1 = Book("1984", "George Orwell")

book1.summary()

















