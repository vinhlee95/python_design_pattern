from typing import Protocol, Tuple


class ShapeProtocol(Protocol):
    width: int
    length: int


class Rectangle(ShapeProtocol):
    def __init__(self, width: int, length:int) -> None:
        self.width = width
        self.length = length


class Square(ShapeProtocol):
    def __init__(self, size: int) -> None:
        self.size = size


class FormatterProtocol(Protocol):
    """
    Abstraction Formatter class
    Any future formatters should conform to this protocol
    Concrete implementation of how the it want to format the shape depends on the formatter itself
    """
    def format(self, shape: ShapeProtocol) -> Tuple[int, int]:
        ...


class RectangleFormatter(FormatterProtocol):
    """
    Specific formatter for rectangle
    """
    def format(self, rectangle: Rectangle):
        return rectangle.width, rectangle.length


class SquareFormatter(FormatterProtocol):
    """
    Specific formatter for square
    """
    def format(self, square: Square):
        return square.size, square.size


class SizeCalculation:
    def __init__(self, formatter: FormatterProtocol) -> None:
        self.formatter = formatter

    def calculate(self, shape: ShapeProtocol) -> int:
        width, length = self.formatter.format(shape)
        return width * length


rect = Rectangle(5, 10)
sqr = Square(5)

square_calculator = SizeCalculation(SquareFormatter())
square_mass = square_calculator.calculate(sqr)

rectangle_calculator = SizeCalculation(RectangleFormatter())
rectangle_mass = rectangle_calculator.calculate(rect)

print("Square mass is", square_mass)
print("Rectangle mass is", rectangle_mass)