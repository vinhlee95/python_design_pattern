from dataclasses import dataclass
from typing import Callable


class Car:
    """
    Generic car class
    """
    def __init__(self, name: str, released_year: int, manufacturer: str, is_ev: bool, battery_range: int):
        self.name = name
        self.released_year = released_year
        self.manufacturer = manufacturer
        self.is_ev = is_ev
        self.battery_range = battery_range


@dataclass
class CarSpecs:
    name: str
    released_year: int
    manufacturer: str
    is_ev: bool
    battery_range: int


class DummyCarFactory:
    @staticmethod
    def build(specs: CarSpecs):
        """
        Car builder method. To provide specs for the car and build it.
        🚧 If the car is an EV, we need to have battery range information.

        :return: a car instance
        """
        if specs.is_ev:
            return Car(specs.name, specs.released_year, specs.manufacturer, specs.is_ev, specs.battery_range)
        else:
            return Car(specs.name, specs.released_year, specs.manufacturer, specs.is_ev)


class CarFactory:
    def build(self, specs: CarSpecs, is_ev: bool):
        builder = self._get_builder(is_ev)
        return builder(specs)

    def _get_builder(self, is_ev: bool) -> Callable[[CarSpecs], Car]:
        return self.build_ev_car if is_ev else self.build_non_ev_car

    @staticmethod
    def build_non_ev_car(specs: CarSpecs) -> Car:
        return Car(specs.name, specs.released_year, specs.manufacturer, False, 0)

    @staticmethod
    def build_ev_car(specs: CarSpecs) -> Car:
        return Car(specs.name, specs.released_year, specs.manufacturer, True, specs.battery_range)

