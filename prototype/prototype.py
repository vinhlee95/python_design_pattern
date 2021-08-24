import copy
from dataclasses import dataclass


class Employee:
    def __init__(self, name, age, headquarter_address):
        self.name = name
        self.age = age
        self.headquarter_address = headquarter_address

    def __str__(self):
        return f"Employee name: {self.name}. Age: {self.age}." \
               f" HQ address is {self.headquarter_address}"


class Address:
    def __init__(self, street_address, postal_code, city):
        self.street_address = street_address
        self.postal_code = postal_code
        self.city = city

    def __str__(self):
        return f"Address is {self.street_address}, {self.postal_code} {self.city}"


@dataclass(frozen=True)
class EmployeeFactory:
    # Employee prototype
    # Future employees will be cloned from this prototype
    employee_helsinki_branch = Employee("", "", Address("Helsinki street 1", "00100", "Helsinki"))
    employee_newyork_branch = Employee("", "", Address("NewYork street 1", "10030", "NewYork"))

    @staticmethod
    def _add_employee(prototype, name, age):
        new_employee = copy.deepcopy(prototype)
        new_employee.name = name
        new_employee.age = age

        return new_employee

    @staticmethod
    def create_new_employee(branch, name, age):
        if branch == "Helsinki":
            creator = EmployeeFactory._create_new_employee_helsinki_branch
        elif branch == "NewYork":
            creator = EmployeeFactory._create_new_employee_newyork_branch
        else:
            raise ValueError(f"Branch {branch} does not exist.")

        return creator(name, age)

    @staticmethod
    def _create_new_employee_helsinki_branch(name, age):
        return EmployeeFactory._add_employee(EmployeeFactory.employee_helsinki_branch, name, age)

    @staticmethod
    def _create_new_employee_newyork_branch(name, age):
        return EmployeeFactory._add_employee(EmployeeFactory.employee_newyork_branch, name, age)


john = EmployeeFactory.create_new_employee("Helsinki", "John", 30)
anne = EmployeeFactory.create_new_employee("NewYork", "Anne", 25)

print(john, "\n", anne)

