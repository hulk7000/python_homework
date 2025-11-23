from class1 import Person

class Manager(Person):
    def giveraise(self,percent,bonus=0.1):
        self.pay = int(self.pay * (1.0 + percent + bonus))

    def getfullname(self):
        return self.name

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    bob = Person('Bob Smith',42,30000,'drawing')