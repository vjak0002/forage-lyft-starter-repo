from abc import abstractclassmethod
from car import Car


class Serviceable:
    @abstractclassmethod
    def needs_service(self) -> bool:
        pass
