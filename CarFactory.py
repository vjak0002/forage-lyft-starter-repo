from car import Car
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery


class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileag: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileag)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)
