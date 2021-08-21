class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.job = None

    def __repr__(self):
        return f"{self.name} is {self.age} years old and is a {self.job}"


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def add_name(self, name):
        self.person.name = name
        return self

    def add_age(self, age):
        self.person.age = age
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def add_job(self, job):
        self.person.job = job
        return self


pb = PersonJobBuilder()
person = pb.add_name("Foo").add_age(20).add_job("developer").build()
print(person)
