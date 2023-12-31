#!/usr/bin/python3
"""Function defines a base geometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """"Raises exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """"Checks that value is greater than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
