# Liskov Substitution Principle
> Derived classes must be substitutable for their base classes.

## Example
We have a `Rectangle` class and `Square` inherit `Rectangle`, `Square` should be usable anywhere you expect a `Rectangle`.
```python
class Rectangle:
    width: int
    height: int
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


class Square(Rectangle):
    pass
```
In above case, `Square` is better not inheriting `Rectangle` because a square's width is always equal to its height. Therefore it does not make much sense for a `Square` class to have separate `set_width` and `set_height` method.

This could be considered as violating the Liskov Substitution Principle.

### Resources
* https://stackoverflow.com/questions/56860/what-is-an-example-of-the-liskov-substitution-principle

