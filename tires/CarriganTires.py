class CarriganTires:
    def __init__(self, wornStatus) -> None:
        self.wornStatus = wornStatus

    def needs_service(self) -> bool:
        return min(self.wornStatus) >= 0.9
