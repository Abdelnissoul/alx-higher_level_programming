#!/usr/bin/python3
""" defines a class square as always """


class Square:
    """initialization of the class square which is private instance attribute"""

    def __init__(self, size=0):
        """initializes a new square instance

        Args:
            size (int): The size of the square. start with 0

        raises:
            TypeError: if size isn't an int
            ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
