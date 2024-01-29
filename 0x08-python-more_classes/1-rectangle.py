#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """class of rectangle with width and height attributes."""

    def __init__(self, width=0, height=0):
        """start a new Rectangle by default
         
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gives the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting up the width with error checking."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Giving the height of the rectangle."""
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
