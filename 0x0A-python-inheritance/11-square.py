#!/usr/bin/python3
"""Function defines a rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"Representation of the square"""
    def __init__(self, size):
        """Ïnitializes new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
