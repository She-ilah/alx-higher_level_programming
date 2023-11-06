#!/usr/bin/python3
"""Function is a class-checking function"""


def inherits_from(obj, a_class):
    """Returns:
        True upon successs or False upon failure
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
