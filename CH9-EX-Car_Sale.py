# 11.28.23

class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        return f'{self.year} {self.make} {self.model} with {self.miles} '
        'miles at ${self.price}'

cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Cheverolet', 'Camaro', 2017, 30000, 39000))
cars.append(Car('Nissan', 'Altima', 2010, 50000, 20000))
cars.append(Car('Toyota', 'Camry', 2009, 231000, 500))

for car in cars:
    print(car)
