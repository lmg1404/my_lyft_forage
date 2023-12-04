from abc import ABC
from datetime import datetime

from battery.battery import Battery

class SplindlerBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        if self.current_date.year - self.last_service_date.year > 3: # changed service after 3 years instead of 2
            return True
        else:
            return False