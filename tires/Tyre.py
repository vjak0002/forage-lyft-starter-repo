from abc import abstractmethod


class Tyre:

    @abstractmethod
    def needs_service(self, wornStatus) -> bool:
        pass
