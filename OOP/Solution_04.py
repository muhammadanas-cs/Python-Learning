class Car:
    def __init__(self, brand,model): 
        self.brand = brand 
        self.model = model
        
    def get_brand(self):
        return self.brand + "!"
        
    def full_name(self):
        return f"{self.brand} {self.model} "
    
my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())