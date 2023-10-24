#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a class square."""

    def __init__(self, size=0):
        """Initialize a new class square.

        Args:
            size (int): The size of new class square.
        """
        self.size = size

    @property
    def size(self):
        """Returns the current size of the class square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
