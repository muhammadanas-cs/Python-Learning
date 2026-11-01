class Car:
    def __init__(self, brand,model): #__init__ is constructor
        self.brand = brand # we use self to access attribues in class
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("BMW","M5") #instance
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


my_new_car = Car("FORD", "RAPTOR")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())