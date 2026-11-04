class Car:
    total_car = 0
    def __init__(self, brand,model): 
        self.__brand = brand 
        self.__model = model
        Car.total_car += 1
    def full_name(self):
        return f"{self.brand} {self.model} "
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod #decorator
    def general_description():
        return "Cars are good"
    
    @property
    def model(self):
        return self.__model  
      
class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
            return "EV"
        
my_tesla = ElectricCar("Tesla", "Model S" , "85Kwh")


my_new_car = Car("FORD", "RAPTOR")
my_new_car.model = "SHELBY"



