#!/usr/bin/python3
"""a class Square with a private instance attribute and public instance."""


class Square:
    """A class Square with a private instance attribute and public instance."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square with a default start with 0.

        Raises:
            TypeError: If size isnt an integer.
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def get_size(self):
        """gives back the size of the square."""
        return self.__size

    @get_size.setter
    def set_size(self, value):
        """Setting up the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def calculate_area(self):
        """calculates the area of the square.
        by calculating the area of the square we will have a new size

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def print_square(self):
        """Print the square with hash sign # """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
