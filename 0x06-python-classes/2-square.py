#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize instance
        Args:
            size: lgth of a side of the square
        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__self = size
