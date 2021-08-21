from __future__ import annotations
from typing import Protocol


class IBuilder(Protocol):
    def build_part_a(self, part_name) -> IBuilder:
        ...

    def build_part_b(self, part_name) -> IBuilder:
        ...

    def build_part_c(self, part_name) -> IBuilder:
        ...

    def get_specs(self) -> str:
        ...


class CarBuilder(IBuilder):
    """
    A concrete implementation of the builder
    """
    def __init__(self):
        self.car = Car()

    def build_part_a(self, part_name):
        self.car.parts.append(part_name)
        return self

    def build_part_b(self, part_name):
        self.car.parts.append(part_name)
        return self

    def build_part_c(self, part_name):
        self.car.parts.append(part_name)
        return self

    def get_specs(self):
        return ", ".join(self.car.parts)


class Car:
    def __init__(self):
        self.parts = []


class Director:
    """
    Director class to build a complex representation
    """

    @staticmethod
    def construct(part_a: str, part_b: str, part_c: str) -> str:
        return CarBuilder().build_part_a(part_a).build_part_b(part_b).build_part_c(part_c).get_specs()


car_director = Director()
print(car_director.construct("Foo", "Bar", "Baz"))

