#!/usr/bin/python3
"""Module for the Square class"""


class Square:
    """Defines a square by size, which must be an integer greater than zero."""
    
    def __init__(self, size=0):
        """Initialization method with optional size parameter."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

