#!/usr/bin/python3
"""Function defines a rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represenattion of a square"""

    def __init__(self, size):
        """Initializes a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
