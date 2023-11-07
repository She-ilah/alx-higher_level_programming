#!/usr/bin/python3
"""Function writes a class Student"""


class Student:
    """Representation of the class student"""
    def __init__(self, first_name, last_name, age):
        """Initialization the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict

    def reload_from_json(self, json):
        """All attributes from student instance are replaced"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
