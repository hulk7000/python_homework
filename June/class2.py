class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getlastname(self):
        return self.name.split(" ")[1]

    def giveraise(self, percent):
        new_pay = int(self.pay * (1 + percent))
        print(new_pay)
        self.pay = new_pay


if __name__ == '__main__':
    bob = Person("Bob Smith", 42, 30000, "software")
    sue = Person("Sue Jones", 45, 40000, "hardware")

    print(bob.name)
    print(sue.pay)

    print(bob.getlastname())
    sue.giveraise(0.1)
    print(sue.pay)
