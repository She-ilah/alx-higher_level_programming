#!/usr/bin/python3
"""Defines a square module class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Function defines the class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of a class square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string serialization of a square"""
        r = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        c = "{}/{} - {}".format(self.x, self.y, self.width)
        return r + c

    @property
    def size(self):
        """Obtains the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Function re-assigns attributes to args"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(
                                self.width, self.width, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.width, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "size":
                        self.width = value
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns dict representation of square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
