from __future__ import annotations
from typing import Protocol


class Engine:
    horse_power: int
    version: int

    def __init__(self, horse_power: int, version: int):
        self.horse_power = horse_power
        self.version = version


class Body:
    shape: str
    material: str

    def __init__(self, shape: str, material: str):
        self.shape = shape
        self.material = material


class Wheel:
    size: str
    type: str
    has_booster: bool

    def __init__(self, size: str, type: str, has_booster: bool):
        self.size = size
        self.type = type
        self.has_booster = has_booster


class ComplexCarBuilder(Protocol):
    def build_engine(self, engine: Engine) -> ComplexCarBuilder:
        ...

    def build_body(self, body: Body) -> ComplexCarBuilder:
        ...

    def build_wheels(self, wheel: Wheel) -> ComplexCarBuilder:
        ...

    def get_specs(self) -> str:
        ...


class SportCarBuilder(ComplexCarBuilder):
    engine: Engine
    body: Body
    wheel: Wheel

    def build_engine(self, engine: Engine) -> SportCarBuilder:
        self.engine = engine
        return self

    def build_body(self, body: Body) -> SportCarBuilder:
        self.body = body
        return self

    def build_wheels(self, wheel: Wheel) -> SportCarBuilder:
        self.wheel = wheel
        return self

    def get_specs(self) -> str:
        return f"The car has engine {self.engine.version} {self.engine.horse_power} \n" \
               f"Body specs are {self.body.shape} {self.body.material} \n" \
               f"Wheels specs are {self.wheel.size} {self.wheel.type}"


class Director:
    @staticmethod
    def construct(engine: Engine, body: Body, wheels: Wheel):
        return SportCarBuilder().build_engine(engine).build_body(body).build_wheels(wheels)


director = Director()
porsche_911 = director.construct(Engine(1000, 8), Body('sedan', 'carbon'), Wheel('large', 'sport', True))
print(porsche_911.get_specs())

