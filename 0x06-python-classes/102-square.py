#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    Square class defines a square by size
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equal method to compare two squares by area
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not equal method to compare two squares by area
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than method to compare two squares by area
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal method to compare two squares by area
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than method to compare two squares by area
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal method to compare two squares by area
        """
        return self.area() <= other.area()


if __name__ == "__main__":
    s1 = Square(3)
    s2 = Square(3)
    print(s1 == s2)
    print(s1 != s2)
    print(s1 > s2)
    print(s1 >= s2)
    print(s1 < s2)
    print(s1 <= s2)
    s1 = Square(4)
    s2 = Square(3)
    print(s1 > s2)
    print(s1 >= s2)
    print(s1 < s2)
    print(s1 <= s2)
    s1 = Square(3)
    s2 = Square(10)
    print(s1 > s2)
    print(s1 >= s2)
    print(s1 < s2)
    print(s1 <= s2)
    s1 = Square(5)
    s2 = Square(3)
    print(s1 > s2)
    print(s1 >= s2)
    print(s1 < s2)
    print(s1 <= s2)

