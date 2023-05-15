import unittest
from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def testNeedsServiceTrue(self):
        wearness = [0.9, 0.9, 0, 0]
        
        tires = CarriganTire(wearness)
        self.assertTrue(tires.needs_service())
        
    def testNeedsServiceFalse(self):
        wearness = [0, 0, 0.89, 0]
        
        tires = CarriganTire(wearness)
        self.assertFalse(tires.needs_service())