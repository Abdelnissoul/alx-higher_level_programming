
#!/usr/bin/python3
"""Module that defines the MagicClass class"""

import math

class MagicClass:
    """Represents a magic circle"""

    def __init__(self, radius=0):
        """the MagicClass instance

        Args:
            radius: the radius of the magic circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
            TypeError: If radius is not an int or float.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Computes the area of the magic circle

        Returns:
            float: The area of the magic circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference of the magic circle

        Returns:
            float: The circumference of the magic circle
        """
        return 2 * math.pi * self.__radius
