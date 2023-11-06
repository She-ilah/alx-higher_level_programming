#!/usr/bin/python3
"""Function defines a base geometry class"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raises exception when called"""
        raise Exception("area() is not implemented")
