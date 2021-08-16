class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

    def set_width(self, val):
        self._width = val

    def set_height(self, val):
        self._height = val

    def __repr__(self) -> str:
        return f"Width is {self._width}. Height is {self._height}"


class Square(Rectangle):
    """
    It probably does not make sense to have 2 separate set_with and set_height for this class
    since a square should always have width = height.
    This fails the Liskov Substitution Test. Square should better be a separate class.
    """
    def __init__(self, size) -> None:
        super().__init__(width=size, height=size)

    def set_width(self, val):
        super().set_width(val)
        self._width = self._height = val

    def set_height(self, val):
        super().set_height(val)
        self._height = self._width = val


def calculate_area(rect: Rectangle):
    width = rect.width
    rect.set_height(10)
    expected = int(width * 10)

    print(f"Expected an area of {expected}, got {rect.area}")
    # Expected an area of 150, got 150
    # This is unexpected because rect.set_height had a side effect of changing
    # both width and height of the rect
    # Expected an area of 50, got 100


my_rect = Rectangle(15, 5)
my_sq = Square(5)

calculate_area(my_rect)
calculate_area(my_sq)
