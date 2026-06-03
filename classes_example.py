class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    def __repr__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    def name(self):
        return f"{self.year} {self.make} {self.model}"

    def topspeed(self):
        (self.speed) = self.speed * 2

#inheritance class
class BMW(Car):
    pass
    def turbo(self):
        self.speed =  self.speed * 3
        return self.speed

class Mazda(Car):
    pass

class Mercedes(Car):
    pass
    def turbo(self):
        self.speed =  self.speed * 4
        return self.speed

class Tesla(Car):
    pass
    def superturbo(self):
        self.speed = self.speed * 5

    def smart(self):
        print("this is a smart car")

BMW = BMW("BMW", "M3", 2020,180 )
Mazda = Mazda("Mazda", "Mazda3", 2020, 160)
Mercedes = Mercedes("Mercedes", "Coup", 2025, 200)
Tesla = Tesla("Tesla", "Tesla3", 2020,230)

myCars = [BMW, Mazda, Mercedes, Tesla]


for car in myCars:
    print(car)
    print(f"{car.make} speed is: {car.speed} MPH")
    car.topspeed()
    print(f"{car.make} top speed is: {car.speed} MPH")
    print("-" * 56)

print(f"({BMW.name()}) with turbo the top speed is: {BMW.turbo()} MPH")
print(f"({Mercedes.name()}) with turbo the top speed is: {Mercedes.turbo()} MPH")
Tesla.smart()
