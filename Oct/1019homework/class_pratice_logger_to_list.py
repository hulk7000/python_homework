class Messagerloggor:
    def __init__(self,message,lst=None):
        self.message = message
        self.lst = lst

    def __str__(self):
        return f'{self.__class__.__name__} : message : {self.message}'

    def log(self):
        self.lst.append(self.message)

    def showlog(self):
        if self.message in self.lst:
            return f'log : {self.message}'
        else:
            return f'{self.message} not found in log.'

if __name__ == '__main__':
    lst41 = []
    hi1 = Messagerloggor('hello world1',lst41)
    hi2 = Messagerloggor('hello world2',lst41)
    hi3 = Messagerloggor('hello world3',lst41)
    hi4 = Messagerloggor('hello world4',lst41)
    hi5 = Messagerloggor('hello world5',lst41)
    hi6 = Messagerloggor('hello world6',lst41)
    hi7 = Messagerloggor('hello world7',lst41)
    hi8 = Messagerloggor('hello world8',lst41)

    hi1.log()
    hi2.log()
    hi8.log()

    print(hi4.showlog())