#!/usr/bin/python3
"""this is a class square with a private instance attribute """


class Square:
    """this is our class for the square"""

    def __init__(self, size):
        """this is initializing a new square instance

        Args:
            size: the length of the first side of the square.
        """
        self.__size = size
