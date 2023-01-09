from car import Car
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery
from tires.OctoprimeTires import OctoprimeTires
from tires.CarriganTires import CarriganTires


class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, wornStatus) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tyres = OctoprimeTires(wornStatus)
        return Car(engine, battery, tyres)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, wornStatus) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tyres = CarriganTires(wornStatus)
        return Car(engine, battery, tyres)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool, wornStatus) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(current_date, last_service_date)
        tyres = CarriganTires(wornStatus)
        return Car(engine, battery, tyres)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileag: int, wornStatus) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileag)
        battery = NubbinBattery(current_date, last_service_date)
        tyres = OctoprimeTires(wornStatus)
        return Car(engine, battery, tyres)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, wornStatus) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tyres = CarriganTires(wornStatus)
        return Car(engine, battery, tyres)
