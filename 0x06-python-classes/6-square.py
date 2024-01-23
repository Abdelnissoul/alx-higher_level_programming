#!/usr/bin/python3
""" a class Square with privaes and public instance."""


class Square:
    """A class Square with two methbutes and public instance"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a tuple of 2 positive integers.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If position contains non-positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using hash sign '#' characters.

        If size is equal to 0, print an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
