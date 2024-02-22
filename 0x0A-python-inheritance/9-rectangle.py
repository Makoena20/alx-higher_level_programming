#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class BaseGeometry:
    """
    This is an empty class
    """
    def area(self):
        """
        This method raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This class defines a rectangle
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle instance
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Computes the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of a rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
