#!/usr/bin/python3
"""Locked class is defined"""


class LockedClass:
    """
    Prevents user from creating new LockedClass
    attributes for anything but attributes called
    'first_name'.
    """

    __slots__ = ["first_name"]
