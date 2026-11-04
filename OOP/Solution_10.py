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
    
    @staticmethod #decorator
    def general_description():
        return "Cars are good"
        
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
            return "EV"
        
my_tesla = ElectricCar("Tesla", "Model S" , "85Kwh")
my_new_car = Car("FORD", "RAPTOR")

class battery:
    def battery_info(self):
        return "100KwH"

class engine:
    def engine_info(self):
        return "V8 NA"
    
class ElectricCarTwo(battery, engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

