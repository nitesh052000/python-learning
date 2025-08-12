class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + " !"

    def printname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Electric Charge"
    
    @staricmethod
    def general_description(self):
        return "no car"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("tesla","model5","85")

my_car = Car("toyota","corola")
print(my_car.printname());

