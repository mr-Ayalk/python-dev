class Car:
    def __init__(self,brand:str,fuel_type:str)->None:
        self.brand=brand
        self.fuel_type=fuel_type
        
    def drive(self,distance:float)->None:
        print(f"Driving {self.brand} for {distance}km [{self.fuel_type}]")
        
        
        
volvo:Car=Car(brand="Volvo",fuel_type="Diesel")
bmw:Car=Car(brand="BMW",fuel_type="Electric")



print(volvo.brand)
print(volvo.fuel_type)
volvo.drive(distance=10)