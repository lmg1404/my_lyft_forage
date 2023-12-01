from abc import ABC, abstractmethod
from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SplindlerBattery

class CarFactory(ABC):
    
    def create_calliope(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_glissade(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_palinedrome(self, current_date, last_service_date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = SplindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_thovex(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)