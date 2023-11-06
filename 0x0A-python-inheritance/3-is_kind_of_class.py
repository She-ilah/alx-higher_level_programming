#!/usr/bin/python3
"""Function is a class checking function"""


def is_kind_of_class(obj, a_class):
    """Returns:
        True upon success or False upon Failure
    """
    if isinstance(obj, a_class):
        return True
    return False
