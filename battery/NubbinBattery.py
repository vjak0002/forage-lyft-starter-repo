from datetime import date
from battery.Battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_date = self.last_service_date.replace(
            year=self.last_service_date + 2)
        return service_date < self.current_date
