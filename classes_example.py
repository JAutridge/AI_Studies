# --- PARENT CLASS (Superclass) ---
# Car is the base class that all other car classes inherit from
# It contains shared attributes and methods for ALL car types
class Car:

    # Constructor - sets up the car with its basic attributes
    def __init__(self, make, model, year, speed):
        self.make = make    # Car brand (e.g. "BMW")
        self.model = model  # Car model (e.g. "M3")
        self.year = year    # Year of manufacture (e.g. 2020)
        self.speed = speed  # Base speed in MPH (e.g. 180)

    # __str__ controls what shows when you print() the object
    # Used for user-friendly display
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    # __repr__ controls what shows in debugging/logs
    # Usually same as __str__ for simple classes
    def __repr__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    # Returns the full name of the car as a string
    def name(self):
        return f"{self.year} {self.make} {self.model}"

    # Doubles the car's speed to simulate top speed
    def topspeed(self):
        self.speed = self.speed * 2  # Updates speed in place


# --- CHILD CLASSES (Subclasses) ---
# Each class below INHERITS everything from Car
# They can also add their own unique methods on top


# BMW inherits from Car and adds a turbo method
class BMW(Car):
    # pass means no extra attributes needed in __init__
    # BMW uses Car's __init__ directly
    def turbo(self):
        self.speed = self.speed * 3  # Turbo triples the speed
        return self.speed            # Returns the new speed


# Mazda inherits from Car but has no extra methods
# It uses everything from Car as-is
class Mazda(Car):
    pass


# Mercedes inherits from Car and adds its own turbo method
# Mercedes turbo is stronger than BMW turbo
class Mercedes(Car):
    def turbo(self):
        self.speed = self.speed * 4  # Turbo quadruples the speed
        return self.speed            # Returns the new speed


# Tesla inherits from Car and adds two unique methods
# Tesla has superturbo and a smart car feature
class Tesla(Car):
    def superturbo(self):
        self.speed = self.speed * 5  # Superturbo multiplies speed by 5

    def smart(self):
        print("this is a smart car")  # Tesla specific feature


# --- CREATING CAR INSTANCES ---
# Note: variable names match class names here
# Each line creates an object from the subclass
BMW = BMW("BMW", "M3", 2020, 180)
Mazda = Mazda("Mazda", "Mazda3", 2020, 160)
Mercedes = Mercedes("Mercedes", "Coup", 2025, 200)
Tesla = Tesla("Tesla", "Tesla3", 2020, 230)


# --- STORING ALL CARS IN A LIST ---
# Makes it easy to loop through and perform actions on all cars
myCars = [BMW, Mazda, Mercedes, Tesla]


# --- LOOPING THROUGH ALL CARS ---
# For each car: print details, show base speed, apply topspeed, show new speed
for car in myCars:
    print(car)                                          # Calls __str__
    print(f"{car.make} speed is: {car.speed} MPH")     # Print base speed
    car.topspeed()                                      # Double the speed
    print(f"{car.make} top speed is: {car.speed} MPH") # Print doubled speed
    print("-" * 56)                                     # Divider line


# --- SPECIAL METHOD CALLS ---
# BMW turbo: applies on top of already doubled topspeed
print(f"({BMW.name()}) with turbo the top speed is: {BMW.turbo()} MPH")

# Mercedes turbo: applies on top of already doubled topspeed
print(f"({Mercedes.name()}) with turbo the top speed is: {Mercedes.turbo()} MPH")

# Tesla smart: prints Tesla's unique smart car message
Tesla.smart()