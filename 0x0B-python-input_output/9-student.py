#!/usr/bin/python3
"""Function Write a class Student"""


class Student:
    """Representation of the class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialization of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a Student instance"""
        return self.__dict__
