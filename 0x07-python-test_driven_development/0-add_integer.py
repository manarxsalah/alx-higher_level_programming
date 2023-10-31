#!/usr/bin/python3
"""Module for add_integer"""

def add_integer(a, b=98):
    """Adds two ints
    Args:
        a: the first int
        b: the second int
    Raises:
        TypeError: if a, b are not int, float
    Returns:
        the sum of two ints
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
