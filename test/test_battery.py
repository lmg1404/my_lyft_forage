import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SplindlerBattery

class TestNubbin(unittest.TestCase):
    def test_battery_get_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        
        nubbin = NubbinBattery(today, last_service_date)
        self.assertTrue(nubbin.needs_service())
    
    def test_battery_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        
        nubbin = NubbinBattery(today, last_service_date)
        self.assertFalse(nubbin.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_get_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        
        splinder = SplindlerBattery(today, last_service_date)
        self.assertTrue(splinder.needs_service())
    
    def test_battery_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        
        splinder = SplindlerBattery(today, last_service_date)
        self.assertFalse(splinder.needs_service())

if __name__ == "__main__":
    unittest.main()