from class_person import Person

class Employee(Person):

    def getemployeename(self):
        return self.name


if __name__ == '__main__':
    tom = Employee(name='Tom Doe', age=50, pay=50000)
    bob = Person('Bob Smith',42,30000,'drawing')