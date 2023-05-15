from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wearness):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tire = OctoprimeTire(wearness)
        car = Car(battery, engine, tire)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wearness):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tire = OctoprimeTire(wearness)
        car = Car(battery, engine, tire)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_is_on, wearness):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(warning_light_is_on)
        tire = CarriganTire(wearness)
        car = Car(battery, engine, tire)
        return car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wearness):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tire = CarriganTire(wearness)
        car = Car(battery, engine, tire)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wearness):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tire = OctoprimeTire(wearness)
        car = Car(battery, engine, tire)
        return car