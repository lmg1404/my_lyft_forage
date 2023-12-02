import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_engine_get_service(self):
        current_mileage = 60000
        last_service_mileage = current_mileage - 40000
        
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_engine_no_service(self):
        current_mileage = 60000
        
        engine = CapuletEngine(current_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_get_service(self):
        warning_light = True
        
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())
    
    def test_engine_no_service(self):
        warning_light = False
        
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_get_service(self):
        current_mileage = 100000
        last_service_mileage = current_mileage - 70000
        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_engine_no_service(self):
        current_mileage = 60000
        
        engine = WilloughbyEngine(current_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == "__main__":
    unittest.main()