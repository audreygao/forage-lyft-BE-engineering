from abc import ABC

class Tire(ABC):
    def __init__(self, wearness):
        self.wearness = wearness
        
    def needs_service(self):
        pass