# Builder design pattern
The builder pattern is a *creational* pattern.
The goal is try to separate the construction of a complex object from its representation.
We can then use the same *construction process* to create different representations.

## When to use?
* Create complex object

## Simple builder example
See example in [simpler builder](./simple_builder.py)

`IBuilder` is a protocol so that we could have concrete implementations e.g. `CarBuilder` to build different parts of a car.
In this example, each part is a `string` and in each build step, we just append a string to the `parts` property of the `Car` object. However, we could come up with a more challenging situation that the builder pattern is more suitable.
Imagine each part of the car is not a `string`, but a `dict` or `list`.

## More complex builder example
See example in [complex builder](./complex_builder.py)

In this example, each car that we want to build is a "complex" one which has specific parts `engine`, `body` and `wheel`. Each part is an object with their own specs.

## Builder inheritance
If we want to separate the car builders smaller, we can do something like [builder inheritance](./builder_inheritance.py).
In this example, we have 1 specific builder for building a particular aspect of a person. If we want to have more builders e.g. `PersonHobbyBuilder`, we could inherit existing builders in a new one like:

```python
# Existing builder
class PersonInfoBuilder:
    def add_name(self, name):
        return self
    
    def add_age(self, age):
        return self

    
# New hobby builder
class PersonHobbyBuilder(PersonInfoBuilder):
    def add_hobby(self, hobby_name):
        self.person.hobbies.append(hobby_name)
        return self

pb = PersonHobbyBuilder()
person = pb.add_name("Foo").add_age(20).add_hobby("Gaming")
```

This will make `PersonInfoBuilder` strictly comply with *Open and Close* principle. Because it is open for extension through inheritance. It is also closed for modification because if we want to build new stuffs, we are going to make new builders, thus not modifying existing implementation of the class.
