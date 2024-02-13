#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Rectangle class

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))
