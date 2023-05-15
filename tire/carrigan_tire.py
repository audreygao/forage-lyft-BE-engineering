from tire import Tire 

class CarriganTire(Tire):
    def __init__(self, wearness):
        super().__init__(wearness)
    
    def needs_service(self):
        for tire in self.wearness:
            if tire >= 0.9: return True
        return False