#!/usr/bin/python3
"""Function is a class-checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class

    Args:
        obj: Object to be checked
        a_class: Class to match to the checked object

    Returns:
        True upon success or False upon failure
    """
    if type(obj) == a_class:
        return True
    return False
