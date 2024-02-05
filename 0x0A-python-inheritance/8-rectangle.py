#!/usr/bin/python3
"""a class of Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """child class of a rectangle inherited by BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new rectangle
        with self(str) and width and height(int)"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
