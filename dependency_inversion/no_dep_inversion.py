class Rectangle:
    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length


class Formatter:
    def format(self, rectangle: Rectangle):
        return (int(rectangle.width), int(rectangle.length))


class SizeCalculation:
    def calculate(self, rectangle: Rectangle):
        formatter = Formatter()
        width, length = formatter.format(rectangle)
        return width * length


rectangle = Rectangle(5, 10)
formatter = Formatter()
total_mass = SizeCalculation().calculate(rectangle)