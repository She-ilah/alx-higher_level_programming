#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a class square."""

    def __init__(self, size=0):
        """Initialize a new class square.

        Args:
            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the "squares current area"""
        return (self.__size * self.__size)
