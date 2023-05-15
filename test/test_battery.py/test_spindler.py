import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def testNeedsServiceTrue(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())
        
    def testNeedsServiceFalse(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())