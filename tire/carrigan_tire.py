from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array
    
    def needs_service(self):
        return any(tire >= 0.9 for tire in self.tire_array)
        
