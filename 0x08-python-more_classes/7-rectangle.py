#!/usr/bin/python3
"""
Function defines Rectangle class
"""


class Rectangle:
    """Representation of rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of new rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the rectangles width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangles width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the rectangles height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the rectangles height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangles area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangles perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of Rec instance"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + "\n") *
                   self.__height)[:-1]

    def __repr__(self):
        """Returns a string representation of Rec instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletion message """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
