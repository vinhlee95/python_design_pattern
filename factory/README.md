# Factory method pattern
> Factory method is a *creational design pattern* used to create concrete implementations of a common interface.

The central idea in Factory Method is to provide a *separate component* with the responsibility to decide *which concrete implementation* should be used based on *some specified parameters*.

## Example
In [factory method](./factory_method.py), we have 2 car builders:
* `DummyCarFactory` has only 1 `build` method with `if/else` condition to decide whether we want to build non-ev or ev car.
* `CarFactory` also has `build` method. But instead of having the condition there, it get the specific car builder through `_get_builder` method based on `is_ev` parameter. `_get_builder` is the one holding the responsibility to decide the concrete implementation (car builder).

`CarFactory` is an example of Factory Method pattern.

### Benefits
* Less `if/else` -> more readable and better readability & maintainability.
* Follow *Open and Closed* principle:
  * If we want to have new builder method for a new car type, e.g. flying car, all we need to do is to make a new factory method `build_flying_car` and update `_get_builder` method to accept a new argument `is_flying`. There is no need to touch existing builder methods `build_ev_car` and `build_non_ev_car`.

## When to use
* Where a client depends on an interface to perform a task and there are multiple concrete implementations of that interface.
* Complex logical structure in the format `if/elif/else`
  * We can put the body of each logical path to a separate method and transform arguments inside conditional statements into arguments of a `creator` to decide which concrete implementation should be used.
* Construct related objects from external data
```python
class EmployeeFactory:
    def create_employee(self, employee, role):
        employee_creator = self.get_employee_factory_by_role(role)
        return employee_creator(employee)

    def get_employee_factory_by_role(self, role):
        if role == 'staff':
            return self.staff_creator
        elif role == 'manager':
            return self.manager_creator
        raise ValueError(f'Role {role} is not found.')
```

## Resources
https://realpython.com/factory-method-python/
