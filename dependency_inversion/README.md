# Dependency inversion principle
> High-level modules should not depend on low-level modules. Both should depend on *abstractions*

> Abstractions should not depend on implementation details. Details should depend on abstraction.

## No deps inversion example
Consider example in [no dependency inversion](./no_dep_inversion.py), there are several problems with this implementation:
* `SizeCalculation` depends on `Formatter` in `calculate` method. This make it impossible to e.g. use a different type of formatter.
```python
# TODO (?) Make `SizeCalculation` use this formatter
class AnotherFormatter:
    def format(self, rectangle: Rectangle):
        return (rectangle.width * 2, rectangle.width * 2)
```

* `Formatter` also depends on on `Rectangle`. We cannot format another shape e.g. a square.
```python
class Square:
    def __init__(self, size) -> None:
        self.size = size

class Formatter:
    ...
    def format_square(self, size):
        """
        Its akward to have another method to do the same thing with existing `format` method 
        """
        return int(size)
```

## Deps inversion example
Example: [width dependency inversion](./with_dep_inversion.py)
The implementation of `SizeCalculation` is now based on the abstraction of both `FormatterProtocol` and `ShapeProtocol`. 
We don't need to care about the implementation details of either `formatter` or `shape`. As long as they conform to the corresponding protocol, it should be fine:
* In case we want to use a new formatter in the size calculation logic, we just need to specify a brand new formatter conforms to `FormatterProtocol`.
* If we want to calculate size for a different shape, let's create a new shape class conform to `ShapeProtocol`

## Linkage to Open and Close principle
IMO, dependency inversion principle connects to "Open and Close" principle to some extents:
* `SizeCalculation` is open for extension because we could just inject new types of formatters and shapes.
* `SizeCalculation` is also closed for modification. Because we don't need to modify its `calculate` method to support a new kind of formatter or shape. Just injecting new formatters and shapes and leave `calculate` untouched.

## Resources
[Python Protocols](https://www.python.org/dev/peps/pep-0544/#defining-a-protocol)

https://codingwithjohan.com/blog/solid-python-dependency-inversion-principle/

https://levelup.gitconnected.com/tenet-of-inversion-with-python-9759ef73dbcf
