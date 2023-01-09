from abc import abstractmethod
from engine.Engine import Engine
from battery.Battery import Battery
from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
