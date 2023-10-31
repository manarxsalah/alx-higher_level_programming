#!/usr/bin/python3
"""
Def a class rectangle
"""


class Rectangle:
    """Representation of the rectangle"""

    number_of_instances = 0
    """int: the no. of active instances"""

    print_symbol = '#'
    """type: Print symbol, can be any type"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle

        Args:
        width: the width of the rectangle
        height: the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """gets the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable str representation of the rectangle"""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """returns a str representation for reproduction"""
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    def __del__(self):
        """prints a msg for every deletion of a rectangle"""
        print("Bye rectangle...")
