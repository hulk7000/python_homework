class Person:
    def __init__(self,name,age,pay=0,job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getfirstname(self):
        firstname = self.name.split(' ')[0]
        return firstname

    def getlastname(self):
        lastname = self.name.split(' ')[1]
        return lastname

    def giveraise(self,percent):
        new_pay = int(self.pay * (1 + percent))
        # print(new_pay)
        self.pay = new_pay


if __name__ == '__main__':
    # print('this is class person')
    bob = Person('Bob Smith',42,30000,'writing')
    sue = Person('Sue Jones',45,40000,'drawing')
    sam = Person('Sam Wang',46)

    print(bob.name)
