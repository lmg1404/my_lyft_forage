from abc import ABC

from battery import Battery

class NubbinBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        if self.current_date.year - self.last_service_date.year > 4:
            return True
        else:
            return False