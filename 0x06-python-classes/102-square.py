#!/usr/bin/python3
"""Module that defines a square with area comparison"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the square

        Args:
            size (int): . Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value The new size value.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square.

        Returns:
            float: The area of the square.

        """
        return self.__size ** 2

    def __lt__(self, other):
        """Less than comparator based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator based on area."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal comparator based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparator based on area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than o based on area."""
        return self.area() >= other.area()
