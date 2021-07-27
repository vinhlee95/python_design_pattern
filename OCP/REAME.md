# Open-Closed Principle

> Objects and entities should be open for extension and closed for modification

**Example**
```python
class Car:
    name: str

    def __init__(self, name: str):
        self.name = name

    def set_horse_power(self, horse_power: int):
        return NotImplemented


class NormalCar(Car):
    def set_horse_power(self, hp: int):
        self.hp = hp

class SuperCar(Car):
    def set_horse_power(self, hp: int):
        hp = min(1000, hp)
        self.hp = hp
```
