#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, other):
        """
        Inverts the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.
        """
        return super().__eq__(other)
