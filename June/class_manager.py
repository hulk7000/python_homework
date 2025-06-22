from class2 import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def getfirstname(self):
        return self.name.split(' ')[0]

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person("Bob Smith", 42, 50000, "software")
    qin = Manager('QIN KE', 43, 50000)

    print(bob)
    print(qin)

    print(qin.job)
    # print(qin.name)
    # print(qin.pay)
    # print(qin.getlastname())
    # print(qin.getfirstname())
    #
    # # bob.giveraise(0.1)
    # # qin.giveraise(0.1)
    # # print(bob.pay)
    # # print(qin.pay)
    #
    # for p in [bob, qin]:
    #     p.giveraise(0.1)
    #     print(p.name, p.pay)