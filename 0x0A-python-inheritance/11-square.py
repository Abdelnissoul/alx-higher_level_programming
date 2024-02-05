#!/usr/bin/python3
"""a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass named square inherited by rectangle"""

    def __init__(self, size):
        """Initialize a new square with its size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """function defines area"""
        return self.__size ** 2

    def __str__(self):
        """ defines the string that represent the square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
