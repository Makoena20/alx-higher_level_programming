#!/usr/bin/python3
"""
Module 8-rectangle

Defines a rectangle class with private width and height attributes.
"""


class Rectangle:
    """
    Rectangle class

    Defines a rectangle by width and height attributes.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of this Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of this Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of this Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of this Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of this Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of this Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of this Rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """Returns a string representation of this Rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes this Rectangle instance."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the larger area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
