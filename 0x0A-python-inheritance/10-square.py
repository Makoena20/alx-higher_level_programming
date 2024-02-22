#!/usr/bin/python3
"""
Module documentation
"""


class BaseGeometry:
    """
    Class documentation
    """
    def area(self):
        """
        Method documentation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method documentation
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class documentation
    """
    def __init__(self, width, height):
        """
        Method documentation
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        Method documentation
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Method documentation
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Class documentation
    """
    def __init__(self, size):
        """
        Method documentation
        """
        super().__init__(size, size)
