#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """class of the rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Giving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting up the width of the Rectangle with error checking."""
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
        """Setting up the height with error checking."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string of the Rectangle object """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """a message when a Rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
