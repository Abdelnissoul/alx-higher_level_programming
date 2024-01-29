#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """defining rectangle class"""

    def __init__(self, width=0, height=0):
        """Start a new rectangle with default width and height
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width """
        return self.__width

    @width.setter
    def width(self, value):
        """Set up the width with error checking."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """giving the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with error checking."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculating and returning the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculating and returning the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the Rectangle
        that weill be represented by '#' sign
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string of the Rectangle object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Rectangle instance is deleted."""
        print("Bye rectangle...")