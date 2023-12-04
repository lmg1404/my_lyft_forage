from abc import ABC, abstractmethod
from serviceable import Serviceable

class Car(Serviceable, ABC):
    def __init__(self, Engine, Battery, Tire):
        self.engine = Engine
        self.battery = Battery
        self.tires = Tire
        
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service():
            return True
        else:
            return False