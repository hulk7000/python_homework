class Laptop:
    def __init__(self,name , brand, size, cpu, memory, price, os = 'Windows'):
        self.name = name
        self.brand = brand
        self.size = size
        self.cpu = cpu
        self.memory = memory
        self.price = price
        self.os = os

    def promotionprice(self):
        price = self.price*0.8
        return price

def print_prom(a):
    output = '''Name:             {:<20}\nOriginal Price:   {:<20}\nPromotion Price:  {:<20}'''.format(a.name, a.price, a.promotionprice())
    return output

# from class3list import laptops

