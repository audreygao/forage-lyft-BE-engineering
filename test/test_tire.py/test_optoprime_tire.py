import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def testNeedsServiceTrue(self):
        wearness = [1, 1, 1, 0]
        
        tires = OctoprimeTire(wearness)
        self.assertTrue(tires.needs_service())
        
    def testNeedsServiceFalse(self):
        wearness = [1, 1, 0.99, 0]
        
        tires = OctoprimeTire(wearness)
        self.assertFalse(tires.needs_service())