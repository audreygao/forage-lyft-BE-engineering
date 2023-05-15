import unittest
from engine.sternman_engine import SternmanEngine

class TestWilloughbyEngine(unittest.TestCase):
    def testNeedsServiceTrue(self):
        warning_light_is_on = True
        
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())
        
    def testNeedsServiceFalse(self):
        warning_light_is_on = False
        
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())