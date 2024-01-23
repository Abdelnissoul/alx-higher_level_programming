class Square:
    """A class Square that defines a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size : The size of the square.
            position: The position of the square.

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gives back the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting up the size of the square.

        Args:
            value : The new size value.

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
        """gives back the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set up the position of the square.

        Args:
            value: The new position value.

        Raises:
            TypeError: if isnt tuple.

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using hash sign '#' characters.

        if size equal to 0 print new line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """class as a String of the square."""
        res = ""
        for _ in range(self.__position[1]):
            res += "\n"
        for _ in range(self.__size):
            res += " " * self.__position[0] + "#" * self.__size + "\n"
        return res.rstrip()