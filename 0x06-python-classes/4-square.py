#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square with a given size.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square.

        Args:
            value (int): The new size of the Square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2

