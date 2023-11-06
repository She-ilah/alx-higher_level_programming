#!/usr/bin/python3
"""Function adds attributes to objects"""


def add_attribute(obj, att, value):
    """Adds new attributes to an object.

    Args:
        obj: Object to add an attribute to.
        att: new Attribute to add to oject.
        value: Value of the attribute.
    Raises:
        TypeError: On the account that attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
