#!/usr/bin/python3
""" Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass named square inherited by rectangle class"""

    def __init__(self, size):
        """Initialize a new square wit size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the square"""
        return self.__size ** 2
