#!/usr/bin/python3
"""Function writes a class MyList that inherits from list"""


class MyList(list):
    """Implements built-in soted printing."""

    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
