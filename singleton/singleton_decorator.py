"""
This module is to demonstrate how could we solve the double-initialization issue
in ./singleton.py
"""


def singleton(_class):
    # Hold all instances in a dict
    _instances = {}

    def create_instance(*args, **kwargs):
        if _class not in _instances:
            _instances[_class] = _class(*args, **kwargs)
        return _instances[_class]

    return create_instance


@singleton
class Database:
    def __init__(self):
        print("Init DB")


db_instance_1 = Database()
db_instance_2 = Database()
# print(db_instance_1 == db_instance_2) # True
