class Employee:
    """
    A singleton class based on Borg Singleton pattern,
    where instances could share state
    """
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Employee, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


bob = Employee()
bob.company_name = "Apple"
bob.company_sector = "Tech"


class EmployeeBenefit(Employee):
    """
    This class will share variables created by parent's class
    """
    pass


benefit = EmployeeBenefit()
print(benefit.company_name, benefit.company_sector)  # Apple


class EmployeeWage(Employee):
    """
    This class reset the sharable state
    """
    _shared_state = {}


wage = EmployeeWage()
print(wage.company_name)  # AttributeError: 'EmployeeWage' object has no attribute 'company_name'
