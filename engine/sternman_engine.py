from engine.Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool) -> None:
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on
