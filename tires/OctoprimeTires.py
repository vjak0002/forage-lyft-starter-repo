class OctoprimeTires:
    def __init__(self, wornStatus) -> None:
        self.wornStatus = wornStatus

    def needs_service(self) -> bool:
        return sum(self.wornStatus) >= 3
