import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def testNeedsServiceTrue(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())
        
    def testNeedsServiceFalse(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())