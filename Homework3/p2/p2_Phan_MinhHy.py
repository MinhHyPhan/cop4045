class ParkingPermit:
    def __init__(self, owner: str, months: int, fees: dict[str, float]) -> None:
        self.owner = owner
        self.months = months
        self.fees = fees.copy()

    def cost(self) -> float:
        raise NotImplementedError("Use StudentPermit or FacultyPermit")

    def __str__(self) -> str:
        return f"{self.owner}: {self.months} months, cost ${self.cost():.2f}"

    def __repr__(self) -> str:
        return f"ParkingPermit({self.owner!r}, {self.months!r}, {self.fees!r})"

class StudentPermit(ParkingPermit):
    def __init__(self, owner: str, months: int, fees: dict[str, float], vehicles: int) -> None:
        super().__init__(owner, months, fees)
        self.vehicles = vehicles

    def cost(self) -> float:
        return self.months * self.fees["student_monthly"] + max(0, self.vehicles - 1) * self.fees["extra_vehicle"]

    def __str__(self) -> str:
        return f"Student - {self.owner}: {self.months} months, {self.vehicles} vehicles, cost ${self.cost():.2f}"

    def __repr__(self) -> str:
        return f"StudentPermit({self.owner!r}, {self.months!r}, {self.fees!r}, {self.vehicles!r})"

class FacultyPermit(ParkingPermit):
    def __init__(self, owner: str, months: int, fees: dict[str, float], garage: bool) -> None:
        super().__init__(owner, months, fees)
        self.garage = garage

    def cost(self) -> float:
        return self.months * (self.fees["faculty_monthly"] + (self.fees["garage_monthly"] if self.garage else 0))

    def __str__(self) -> str:
        return f"Faculty - {self.owner}: {self.months} months, garage={self.garage}, cost ${self.cost():.2f}"

    def __repr__(self) -> str:
        return f"FacultyPermit({self.owner!r}, {self.months!r}, {self.fees!r}, {self.garage!r})"

def summarize_list(permits: list[ParkingPermit]) -> float:
    total = 0.0
    for permit in permits:
        print(f"{permit.owner}: ${permit.cost():.2f}")
        total += permit.cost()
    return total

def main() -> None:
    fees = {
        "student_monthly": 25.0,
        "extra_vehicle": 10.0,
        "faculty_monthly": 40.0,
        "garage_monthly": 15.0,
    }

    p1 = StudentPermit("Alex", 4, fees, 2)
    p2 = StudentPermit("Taylor", 3, fees, 1)
    p3 = FacultyPermit("Jordan", 4, fees, True)
    p4 = FacultyPermit("Morgan", 2, fees, False)
    permits = [p1, p2, p3, p4]

    print("Permit objects:")
    for permit in permits:
        print(permit)
        print(repr(permit))

    print("\nHere are the revenue summary:")
    total = summarize_list(permits)
    print(f"Total revenue: ${total:.2f}")

    print("Name: Minh Hy Phan")
    print("ID: Z23766758")

if __name__ == "__main__":
    main()