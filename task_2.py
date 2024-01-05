# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.


class Vehicle:
    def __init__(
        self, seats: int, manufacture_year: int, wheels: int, top_speed: int
    ) -> None:
        self.seats = seats
        self.manufacture_year = manufacture_year
        self.wheels = wheels
        self.top_speed = top_speed

    def get_seats(self) -> int:
        return self.seats

    def get_manufacture_year(self) -> int:
        return self.manufacture_year

    def get_wheels(self) -> int:
        return self.wheels

    def get_top_speed(self) -> int:
        return self.top_speed

    def get_fare_charge(self) -> int:
        return self.seats * 100


class Bus(Vehicle):
    def __init__(
        self, seats: int, manufacture_year: int, wheels: int, top_speed: int
    ) -> None:
        super().__init__(seats, manufacture_year, wheels, top_speed)

    def get_fare_charge(self) -> int:
        return self.seats * 110


class Taxi(Vehicle):
    def __init__(
        self, seats: int, manufacture_year: int, wheels: int, top_speed: int
    ) -> None:
        super().__init__(seats, manufacture_year, wheels, top_speed)


class Train(Vehicle):
    def __init__(
        self, seats: int, manufacture_year: int, wheels: int, top_speed: int
    ) -> None:
        super().__init__(seats, manufacture_year, wheels, top_speed)


taxi = Taxi(seats=4, manufacture_year=2022, wheels=4, top_speed=200)
bus = Bus(seats=40, manufacture_year=1999, wheels=6, top_speed=110)

print(f"Taxi price: {taxi.get_fare_charge()}")
print(f"Bus price: {bus.get_fare_charge()}")
