#!/usr/bin/python3
"""File defines a base model class."""
import json
import os


class Base:
    """Base model of all classes in project 0x0C"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Initializes a new base.
            Args:
                _id (int): A integer/new base.
        """
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string serialization of list dicts"""
        if list_dictionaries is None:
            list_dictionaries = []
        elif type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")

        for d in list_dictionaries:
            if type(d) is not dict:
                msg = "list_dictionaries must be a list of dictionaries"
                raise TypeError(msg)

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string serialization"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string serialization  of list_obj"""
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Function returns a list of specified instances"""
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        ret = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
            ret = [cls.create(**d) for d in list_dicts]
        return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Returns list of classes."""
        if list_objs is None:
            list_objs = []

        filename = "{}.csv".format(cls.__name__)
        attrs = ('id', 'size', 'width', 'height', 'x', 'y')
        with open(filename, "w", encoding="utf-8") as f:
            for o in list_objs:
                d = o.to_dictionary()
                t = []
                for attr in attrs:
                    if attr not in d:
                        continue
                    t.append(str(d.get(attr)))
                f.write(",".join(t))
                f.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes"""
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                arguments = line[:-1].split(",")
                o = cls(1, 1)
                o.update(*[int(x) for x in arguments])
                list_objs.append(o)
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance
