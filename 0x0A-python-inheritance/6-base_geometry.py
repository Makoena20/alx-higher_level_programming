#!/usr/bin/python3
"""BaseGeometry class."""

class BaseGeometry:
    """Represents the base geometry."""

    def area(self):
        raise NotImplementedError("area() is not implemented")

    def __str__(self):
        return f"[BaseGeometry]"
