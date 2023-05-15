from tire import Tire 

class OctoprimeTire(Tire):
    def __init__(self, wearness):
        super().__init__(wearness)
    
    def needs_service(self):
        if sum(self.wearness) >= 3:
            return True
        else:
            return False