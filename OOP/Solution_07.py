class Car:
    total_car = 0
    def __init__(self, brand,model): 
        self.brand = brand 
        self.model = model
        Car.total_car += 1
    def full_name(self):
        return f"{self.brand} {self.model} "
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are good"
        
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
            return "EV"
        
my_tesla = ElectricCar("Tesla", "Model S" , "85Kwh")
print(my_tesla.fuel_type())

my_new_car = Car("FORD", "RAPTOR")
print(my_new_car.fuel_type())

print(Car.total_car)
print(Car.general_description())
