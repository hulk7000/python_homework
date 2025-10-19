class Vehicle:
    def __init__(self, name, brand, color,model,is_ev=False, engine=None):
        self.name = name
        self.brand = brand
        self.model = model
        self.color = color
        self.is_ev = is_ev
        if self.is_ev == False:
            self.engine = engine
        else:
            self.engine = None

    def __str__(self):
        return f'{self.__class__.__name__} : name : {self.name}, brand : {self.brand}, model : {self.model}, is_ev : {self.is_ev}, engine : {self.engine}'

    def output_dict(self):
        return {
            self.name:{
                'name': {self.name},
                'brand': {self.brand},
                'model': {self.model},
                'is_ev': {self.is_ev},
                'engine': {self.engine}
            }
        }

if __name__ == '__main__':
    Tom_car = Vehicle('Tom_car', 'Toyota', 'red','rav4', engine='2.0')
    Frank_car = Vehicle('Frank_car', 'Tesla', 'grey','model_y', is_ev=True)
    lily_car = Vehicle('lily_car', 'Mazda', 'black','CX-9', engine='3.7')
    dic = {}
    dic.update(Tom_car.output_dict())
    dic.update(Frank_car.output_dict())
    dic.update(lily_car.output_dict())

    for k,v in dic.items():
        print(k,v.get('brand'),v.get('model'))




