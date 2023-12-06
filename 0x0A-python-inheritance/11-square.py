#!/usr/bin/python3
"""
Module to write an empty class
"""


class BaseGeometry:
    """
    Geometry class
    """
    def area(self, width, height):
        """
        check area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """
        Method to calculate area of a rectangle
        """
        return self.__width * self.__height
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    Inherits from a rectangle
    """
    def __init__(self, size):
        width = size
        height = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(width, height)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
