#!/usr/bin/python3
""" a class MySquare with private instance attributes and public instance."""


class MySquare:
    """A class MySquare with two methods private instance and attributes and public instance"""

    def __init__(self, my_size=0, my_position=(0, 0)):
        """Initializes a new MySquare instance.

        Args:
            my_size (int): The size of the square. Defaults to 0.
            my_position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If my_size is not an integer or my_position is not a tuple of 2 positive integers.
            ValueError: If my_size is less than 0 or my_position contains non-positive integers.

        """
        self.my_size = my_size
        self.my_position = my_position

    @property
    def my_size(self):
        """Retrieve the size of the square."""
        return self.__my_size

    @my_size.setter
    def my_size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If my_size is not an integer.
            ValueError: If my_size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("my_size must be an integer")
        elif value < 0:
            raise ValueError("my_size must be >= 0")
        self.__my_size = value

    @property
    def my_position(self):
        """Retrieve the position of the square."""
        return self.__my_position

    @my_position.setter
    def my_position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If my_position is not a tuple of 2 positive integers.
            ValueError: If my_position contains non-positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("my_position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError("my_position must be a tuple of 2 positive integers")
        self.__my_position = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__my_size ** 2

    def my_print(self):
        """Print the square using hash sign '#' characters.

        If size is equal to 0, print an empty line.

        """
        if self.__my_size == 0:
            print()
        else:
            for _ in range(self.__my_position[1]):
                print()
            for _ in range(self.__my_size):
                print(" " * self.__my_position[0] + "#" * self.__my_size)
