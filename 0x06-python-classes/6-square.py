#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int, optional): The size of the square.
            position (tuple, optional): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square.

        Args:
            value (int): The size value to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of square.

        Args:
            value (tuple): The position value to set.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square with '#' character."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

