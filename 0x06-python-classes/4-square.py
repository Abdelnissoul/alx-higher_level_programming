#!/usr/bin/python3
"""class Square that defines private instance attribute and a public instance method"""


class Square:
    """A class Square with a private instance attribute, and public instance method,
    that well set and get the size """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square. starting with 0.

        Raises:
            TypeError: If size isn't an integer.
            ValueError: If size is less than 0.

        """
        self.__size = size

    @property
    def size(self):
        """getting back the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting up the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If size isn't an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
